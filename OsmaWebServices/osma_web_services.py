# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OsmaWebServices
                                 A QGIS plugin
 Easy add OSMA WMS and WMTS layers to QGIS
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
from token import Token

__author__ = 'matthew.walsh'


class OsmaWebServices:
    """QGIS Plugin Implementation."""

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

        # Variable for layers and about/info
        self.layers = None
        self.about = None
        self.caches = None

        self.hit_osma = GetOsmaLayers()

        self.token_config = Token(self.iface)
        self.token_config.check_token()

        # Create instance of qtreeview for wms/wmts
        self.pop_wmts = PopulateTree(self.dock.ui, self.iface, self.token_config, wms=False)
        self.pop_wms = PopulateTree(self.dock.ui, self.iface, self.token_config, wms=True)

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

        # Hookup 'Load layers' buttons to token function
        self.dock.ui.loadLayersWmsButton.pressed.connect(self.token)
        self.dock.ui.loadLayersWmtsButton.pressed.connect(self.token)

        # Hookup search
        self.dock.ui.wmtsSearchLineEdit.textChanged.connect(self.pop_wmts.filter_layers)
        self.dock.ui.wmsSearchLineEdit.textChanged.connect(self.pop_wms.filter_layers)

    def token(self):
        # Runs on first push of 'Load Layers'

        # Prompt for token if missing
        if not self.token_config.token:
            self.token_config.prompt_token()

        # If token is good then change connections and load layers
        if self.token_config.token:
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

    def hit_osma_ws(self, token):
        # Hi the GetCapabilities
        osma = self.hit_osma.get_available_layers(token)
        self.layers = osma.get('layers')
        self.about = osma.get('info')
        self.caches = osma.get('caches')

    def load_layers(self):
        # Load layers and populate treeviews

        # Get layers from ws and populate tree
        if self.layers is None and self.caches is None:
            self.hit_osma_ws(self.token_config.token)
        cache_lst = []
        for cache in self.caches:
            cache_lst.append(str(cache))
        wmts_layers = []

        # Check if is WMTS by matching with cache and adds grid to dict
        for layer in self.layers:
            source = layer.get('sources')[0]
            if source in cache_lst:
                grid = self.caches.get(source).get('grids')[0]
                layer['grid'] = grid
                wmts_layers.append(layer)
            else:
                pass
                # Populate trees
        self.pop_wmts.add_layers(wmts_layers)
        self.pop_wms.add_layers(self.layers)

    def populate_about(self):
        # Populate the 'about' tab with info from the GetCapabilities
        if self.about is None:
            self.hit_osma_ws(self.token_config.token)
        meta = self.about.get('wms').get('md')
        abstract = meta.get('abstract')
        email = meta.get('contact').get('email')
        person = meta.get('contact').get('person')
        position = meta.get('contact').get('position')
        phone = meta.get('contact').get('phone')
        city = meta.get('contact').get('city')
        fax = meta.get('contact').get('fax')
        country = meta.get('contact').get('country')
        postcode = meta.get('contact').get('postcode')
        address = meta.get('contact').get('address')
        access = meta.get('access_constraints')
        org = meta.get('contact').get('organization')
        self.dock.ui.abstractLabel.setText(abstract)
        self.dock.ui.emailLabel.setText("email: " + email)
        self.dock.ui.personLabel.setText("Contact: " + person)
        self.dock.ui.positionLabel.setText("Position: " + position)
        self.dock.ui.phoneLabel.setText("Phone:" + phone)
        self.dock.ui.cityLabel.setText(city)
        self.dock.ui.faxLabel.setText("Fax: " + fax)
        self.dock.ui.countryLabel.setText(country)
        self.dock.ui.postcodeLabel.setText(postcode)
        self.dock.ui.addrLabel.setText("Address: " + address)
        self.dock.ui.accessLabel.setText("Access Constraint: " + access)
        self.dock.ui.orgLabel.setText("organization: " + org)

    def clear_token(self):
        # Reset plugin to initial state
        self.token_config.clear_token()
        self.pop_wms.clear_tree()
        self.pop_wmts.clear_tree()
        self.layers = None
        self.about = None
        self.caches = None

        # Break current 'Load Layers' connections ad re-connect to token function
        self.dock.ui.loadLayersWmsButton.pressed.disconnect()
        self.dock.ui.loadLayersWmsButton.pressed.connect(self.token)
        self.dock.ui.loadLayersWmtsButton.pressed.connect(self.token)

        # Info box
        QMessageBox.information(self.iface.mainWindow(), "Reset Successful", "OSMA Web Services Plugin has been reset")
