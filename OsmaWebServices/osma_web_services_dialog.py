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
from osma_web_services_dock import Ui_OsmaDockWidget
from wms_layer_name import Ui_layerNameDialog
from token_dialog import Ui_TokenDialog
from multi_wms_order import Ui_MultiWmsDialog

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


class TokenDialog(QtGui.QDialog, Ui_TokenDialog):
    # Dialog for user to enter osma token
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_TokenDialog()
        self.ui.setupUi(self)


class MultiWmsDialog(QtGui.QDialog, Ui_MultiWmsDialog):
    # Dialog for user to enter osma token
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_MultiWmsDialog()
        self.ui.setupUi(self)