# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OsmaWebServices
                                 A QGIS plugin
 Easy add OSMA WMS and WMTS layers_wms to QGIS
                              -------------------
        begin                : 2014-11-10
        copyright            : (C) 2014 by thinkWhere
        email                : support@thinkwhere.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os.path
import webbrowser

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from osma_web_services_dialog import OsmaWebServicesDock
from layers import PopulateTree, GetOsmaLayers
from mapcloud_authentication import MapCloudAuthentication


__author__ = 'matthew.walsh'


class OsmaWebServices:
    """
    QGIS Plugin Implementation.
    """

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.preview_btn = None
        self.wiki_btn = None
        self.reset_btn = None

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'OsmaWebServices_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dock = OsmaWebServicesDock()

        # Add dock to main window
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&OSMA Web Services')
        # self.toolbar = self.iface.addToolBar(u'OsmaWebServices')
        # self.toolbar.setObjectName(u'OsmaWebServices')

        # Variable for layers_wms and about/info
        self.layers_wms = None
        self.layers_wmts = None
        self.about = None
        self.caches = None

        self.hit_osma = GetOsmaLayers()

        self.mc_auth = MapCloudAuthentication(self.iface)
        self.mc_auth.validate_auth_credentials()

        # Create instance of qtreeview for wms/wmts
        self.pop_wmts = PopulateTree(self.dock.ui, self.iface, self.mc_auth, wms=False)
        self.pop_wms = PopulateTree(self.dock.ui, self.iface, self.mc_auth, wms=True)

    def tr(self, message):
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('OsmaWebServices', message)

    def add_action(
            self,
            icon_path,
            text,
            callback,
            enabled_flag=True,
            add_to_menu=True,
            add_to_toolbar=False,
            status_tip=None,
            whats_this=None,
            parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToWebMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        icon_path = ':/plugins/OsmaWebServices/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'OSMA Web Services'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # Adds 'OSMA Wiki' to the menu
        self.wiki_btn = QAction("Help Wiki", self.iface.mainWindow())
        QObject.connect(self.wiki_btn, SIGNAL("triggered()"), self.wiki_clicked)
        self.iface.addPluginToWebMenu(u"OSMA Web Services", self.wiki_btn)

        # Adds 'Reset plugin' to the menu
        self.reset_btn = QAction("Reset Plugin", self.iface.mainWindow())
        QObject.connect(self.reset_btn, SIGNAL("triggered()"), self.clear_token)
        self.iface.addPluginToWebMenu(u"OSMA Web Services", self.reset_btn)

        # Adds 'Show preview' to the menu
        self.preview_btn = QAction("Preview enabled", self.iface.mainWindow(), checkable=True)
        QObject.connect(self.preview_btn, SIGNAL("triggered()"),
                        lambda: self.change_preview(self.preview_btn.isChecked()))
        self.iface.addPluginToWebMenu(u"OSMA Web Services", self.preview_btn)

        # Get preview preference from registry and set column visibility
        if QSettings().value("OsmaWebServices/Preview") == "False":
            self.change_preview(False)
        else:
            self.change_preview(True)
            self.preview_btn.setChecked(True)

        # hookup TW logo connection to website
        self.dock.ui.twLogoLabel.mousePressEvent = self.tw_logo_clicked

        # Hookup 'Load layers_wms' buttons to mc_auth function
        self.dock.ui.loadLayersWmsButton.pressed.connect(self.token)
        self.dock.ui.loadLayersWmtsButton.pressed.connect(self.token)

        # Hookup search
        self.dock.ui.wmtsSearchLineEdit.textChanged.connect(self.pop_wmts.filter_layers)
        self.dock.ui.wmsSearchLineEdit.textChanged.connect(self.pop_wms.filter_layers)

    def token(self):
        # Runs on first push of 'Load Layers'
        # Prompt for mc_auth if missing
        if not self.mc_auth.username:
            self.mc_auth.prompt_login()

        # If mc_auth is good then change connections and load layers_wms
        if self.mc_auth.username:
            self.load_layers()
            self.populate_about()

            # Break current 'Load Layers' connections ad connect to load_layers function
            self.dock.ui.loadLayersWmsButton.pressed.disconnect()
            self.dock.ui.loadLayersWmsButton.pressed.connect(self.load_layers)
            self.dock.ui.loadLayersWmtsButton.pressed.connect(self.load_layers)
        else:
            pass

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginWebMenu(
                self.tr(u'OSMA Web Services'),
                action)
            self.iface.removeToolBarIcon(action)
            self.iface.removeDockWidget(self.dock)
            self.iface.removePluginWebMenu(u"OSMA Web Services", self.reset_btn)
            self.iface.removePluginWebMenu(u"OSMA Web Services", self.wiki_btn)
            self.iface.removePluginWebMenu(u"OSMA Web Services", self.preview_btn)

    def run(self):
        # Display docked window
        self.dock.show()

    def tw_logo_clicked(self, mouse_event):
        # Open tw website in browsers on logo click
        webbrowser.open('http://www.thinkwhere.com')

    def wiki_clicked(self):
        # Open wiki in web browser
        webbrowser.open('http://wms.locationcentre.co.uk/wiki/index.php/OSMA_Web_Services')

    def change_preview(self, ischecked):
        self.pop_wms.preview_column(ischecked)
        self.pop_wmts.preview_column(ischecked)

    def request_get_capabilities(self, username, password):
        # Hit the GetCapabilities
        self.layers_wms, self.layers_wmts, self.about = self.hit_osma.get_available_layers(self.mc_auth.username,
                                                                                           self.mc_auth.password)

    def load_layers(self):
        """
        Load layers_wms and populate treeviews
        :return:
        """
        # Get layers_wms from ws and populate tree
        if self.layers_wms is None:
            self.request_get_capabilities(self.mc_auth.username, self.mc_auth.password)

        self.pop_wmts.add_layers(self.layers_wmts)
        self.pop_wms.add_layers(self.layers_wms)

    def populate_about(self):
        # Populate the 'about' tab with info from the GetCapabilities
        if self.about is None:
            self.request_get_capabilities(self.mc_auth.username, self.mc_auth.password)

        self.dock.ui.abstractLabel.setText(self.about.get('abstract'))
        self.dock.ui.emailLabel.setText("email: " + self.about.get('email'))
        self.dock.ui.personLabel.setText("Contact: " + self.about.get('person'))
        self.dock.ui.positionLabel.setText("Position: " + self.about.get('position'))
        self.dock.ui.phoneLabel.setText("Phone:" + self.about.get('phone'))
        self.dock.ui.cityLabel.setText(self.about.get('city'))
        # self.dock.ui.faxLabel.setText("Fax: " + self.about.get('fax'))
        self.dock.ui.countryLabel.setText(self.about.get('country'))
        self.dock.ui.postcodeLabel.setText(self.about.get('postcode'))
        self.dock.ui.addrLabel.setText("Address: " + self.about.get('address'))
        self.dock.ui.accessLabel.setText("Access Constraint: " + self.about.get('access'))
        self.dock.ui.orgLabel.setText("organization: " + self.about.get('org'))

    def clear_token(self):
        # Reset plugin to initial state
        self.mc_auth.clear_auth_credentials()
        self.pop_wms.clear_tree()
        self.pop_wmts.clear_tree()
        self.layers_wms = None
        self.about = None
        self.caches = None

        # Break current 'Load Layers' connections ad re-connect to mc_auth function
        self.dock.ui.loadLayersWmsButton.pressed.disconnect()
        self.dock.ui.loadLayersWmsButton.pressed.connect(self.token)
        self.dock.ui.loadLayersWmtsButton.pressed.connect(self.token)

        # Info box
        QMessageBox.information(self.iface.mainWindow(), "Reset Successful", "OSMA Web Services Plugin has been reset")
