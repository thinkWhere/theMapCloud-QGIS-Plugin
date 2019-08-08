# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OsmaWebServicesDialog
                                 A QGIS plugin
 Easy add theMapCloud WMS and WMTS layers to QGIS
                             -------------------
        begin                : 2014-11-10
        git sha              : $Format:%H$
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
from PyQt5 import QtWidgets

from TheMapCloudWebServices.ui.multi_wms_order import Ui_MultiWmsDialog
from TheMapCloudWebServices.ui.themapcloud_web_services_dock import Ui_OsmaDockWidget
from TheMapCloudWebServices.ui.auth_dialog import Ui_AuthDialog
from TheMapCloudWebServices.ui.wms_layer_name import Ui_layerNameDialog

__author__ = 'matthew.walsh'


class MapcloudWebServicesDock(QtWidgets.QDockWidget, Ui_OsmaDockWidget):
    # Main dock widget
    def __init__(self):
        QtWidgets.QDockWidget.__init__(self)
        self.ui = Ui_OsmaDockWidget()
        self.ui.setupUi(self)


class LayerNameDialog(QtWidgets.QDialog, Ui_layerNameDialog):
    # WMS layer name dialog
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_layerNameDialog()
        self.ui.setupUi(self)


class MapcloudAuthDialog(QtWidgets.QDialog, Ui_AuthDialog):
    """
    Dialog for user to enter MapCloud credentials
    """

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_AuthDialog()
        self.ui.setupUi(self)


class MultiWmsDialog(QtWidgets.QDialog, Ui_MultiWmsDialog):
    # Dialog for user to enter theMapCloud mc_auth
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_MultiWmsDialog()
        self.ui.setupUi(self)
