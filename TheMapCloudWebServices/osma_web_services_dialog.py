# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OsmaWebServicesDialog
                                 A QGIS plugin
 Easy add OSMA WMS and WMTS layers to QGIS
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
from PyQt4 import QtGui

from TheMapCloudWebServices.ui.multi_wms_order import Ui_MultiWmsDialog
from TheMapCloudWebServices.ui.osma_web_services_dock import Ui_OsmaDockWidget
from TheMapCloudWebServices.ui.auth_dialog import Ui_AuthDialog
from TheMapCloudWebServices.ui.wms_layer_name import Ui_layerNameDialog

__author__ = 'matthew.walsh'


class OsmaWebServicesDock(QtGui.QDockWidget, Ui_OsmaDockWidget):
    # Main dock widget
    def __init__(self):
        QtGui.QDockWidget.__init__(self)
        self.ui = Ui_OsmaDockWidget()
        self.ui.setupUi(self)


class LayerNameDialog(QtGui.QDialog, Ui_layerNameDialog):
    # WMS layer name dialog
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_layerNameDialog()
        self.ui.setupUi(self)


class MapcloudAuthDialog(QtGui.QDialog, Ui_AuthDialog):
    """
    Dialog for user to enter MapCloud credentials
    """

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_AuthDialog()
        self.ui.setupUi(self)


class MultiWmsDialog(QtGui.QDialog, Ui_MultiWmsDialog):
    # Dialog for user to enter osma mc_auth
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_MultiWmsDialog()
        self.ui.setupUi(self)
