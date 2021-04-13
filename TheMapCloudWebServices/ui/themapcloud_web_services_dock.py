# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'themapcloud_web_services_dock.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OsmaDockWidget(object):
    def setupUi(self, OsmaDockWidget):
        OsmaDockWidget.setObjectName("OsmaDockWidget")
        OsmaDockWidget.resize(304, 653)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OsmaDockWidget.sizePolicy().hasHeightForWidth())
        OsmaDockWidget.setSizePolicy(sizePolicy)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.wmtsTab = QtWidgets.QWidget()
        self.wmtsTab.setObjectName("wmtsTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wmtsTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.loadLayersWmtsButton = QtWidgets.QPushButton(self.wmtsTab)
        self.loadLayersWmtsButton.setObjectName("loadLayersWmtsButton")
        self.gridLayout_2.addWidget(self.loadLayersWmtsButton, 2, 0, 1, 1)
        self.addWmtsButton = QtWidgets.QPushButton(self.wmtsTab)
        self.addWmtsButton.setObjectName("addWmtsButton")
        self.gridLayout_2.addWidget(self.addWmtsButton, 2, 1, 1, 1)
        self.zoomExtentWmtsBox = QtWidgets.QCheckBox(self.wmtsTab)
        self.zoomExtentWmtsBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.zoomExtentWmtsBox.setChecked(True)
        self.zoomExtentWmtsBox.setObjectName("zoomExtentWmtsBox")
        self.gridLayout_2.addWidget(self.zoomExtentWmtsBox, 2, 2, 1, 1)
        self.wmtsTreeView = QtWidgets.QTreeView(self.wmtsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wmtsTreeView.sizePolicy().hasHeightForWidth())
        self.wmtsTreeView.setSizePolicy(sizePolicy)
        self.wmtsTreeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wmtsTreeView.setDragEnabled(False)
        self.wmtsTreeView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.wmtsTreeView.setObjectName("wmtsTreeView")
        self.wmtsTreeView.header().setDefaultSectionSize(80)
        self.gridLayout_2.addWidget(self.wmtsTreeView, 1, 0, 1, 3)
        self.wmtsSearchLineEdit = QtWidgets.QLineEdit(self.wmtsTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wmtsSearchLineEdit.sizePolicy().hasHeightForWidth())
        self.wmtsSearchLineEdit.setSizePolicy(sizePolicy)
        self.wmtsSearchLineEdit.setInputMask("")
        self.wmtsSearchLineEdit.setText("")
        self.wmtsSearchLineEdit.setObjectName("wmtsSearchLineEdit")
        self.gridLayout_2.addWidget(self.wmtsSearchLineEdit, 0, 0, 1, 3)
        self.tabWidget.addTab(self.wmtsTab, "")
        self.wmsTab = QtWidgets.QWidget()
        self.wmsTab.setObjectName("wmsTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.wmsTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.addWmsButton = QtWidgets.QPushButton(self.wmsTab)
        self.addWmsButton.setObjectName("addWmsButton")
        self.gridLayout_3.addWidget(self.addWmsButton, 2, 1, 1, 1)
        self.loadLayersWmsButton = QtWidgets.QPushButton(self.wmsTab)
        self.loadLayersWmsButton.setObjectName("loadLayersWmsButton")
        self.gridLayout_3.addWidget(self.loadLayersWmsButton, 2, 0, 1, 1)
        self.zoomExtentWmsBox = QtWidgets.QCheckBox(self.wmsTab)
        self.zoomExtentWmsBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.zoomExtentWmsBox.setChecked(False)
        self.zoomExtentWmsBox.setObjectName("zoomExtentWmsBox")
        self.gridLayout_3.addWidget(self.zoomExtentWmsBox, 2, 2, 1, 1)
        self.wmsTreeView = QtWidgets.QTreeView(self.wmsTab)
        self.wmsTreeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wmsTreeView.setProperty("showDropIndicator", False)
        self.wmsTreeView.setDragEnabled(False)
        self.wmsTreeView.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.wmsTreeView.setDefaultDropAction(QtCore.Qt.LinkAction)
        self.wmsTreeView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.wmsTreeView.setObjectName("wmsTreeView")
        self.wmsTreeView.header().setDefaultSectionSize(80)
        self.wmsTreeView.header().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.wmsTreeView, 1, 0, 1, 3)
        self.wmsSearchLineEdit = QtWidgets.QLineEdit(self.wmsTab)
        self.wmsSearchLineEdit.setObjectName("wmsSearchLineEdit")
        self.gridLayout_3.addWidget(self.wmsSearchLineEdit, 0, 0, 1, 3)
        self.tabWidget.addTab(self.wmsTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.accessLabel = QtWidgets.QLabel(self.tab)
        self.accessLabel.setText("")
        self.accessLabel.setWordWrap(True)
        self.accessLabel.setObjectName("accessLabel")
        self.gridLayout_4.addWidget(self.accessLabel, 1, 2, 1, 1)
        self.personLabel = QtWidgets.QLabel(self.tab)
        self.personLabel.setText("")
        self.personLabel.setWordWrap(True)
        self.personLabel.setObjectName("personLabel")
        self.gridLayout_4.addWidget(self.personLabel, 2, 2, 1, 1)
        self.addrLabel = QtWidgets.QLabel(self.tab)
        self.addrLabel.setText("")
        self.addrLabel.setWordWrap(True)
        self.addrLabel.setObjectName("addrLabel")
        self.gridLayout_4.addWidget(self.addrLabel, 6, 2, 1, 1)
        self.phoneLabel = QtWidgets.QLabel(self.tab)
        self.phoneLabel.setText("")
        self.phoneLabel.setWordWrap(True)
        self.phoneLabel.setObjectName("phoneLabel")
        self.gridLayout_4.addWidget(self.phoneLabel, 14, 2, 1, 1)
        self.positionLabel = QtWidgets.QLabel(self.tab)
        self.positionLabel.setText("")
        self.positionLabel.setWordWrap(True)
        self.positionLabel.setObjectName("positionLabel")
        self.gridLayout_4.addWidget(self.positionLabel, 4, 2, 1, 1)
        self.twLogoLabel = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twLogoLabel.sizePolicy().hasHeightForWidth())
        self.twLogoLabel.setSizePolicy(sizePolicy)
        self.twLogoLabel.setMaximumSize(QtCore.QSize(10777215, 10777215))
        self.twLogoLabel.setText("")
        self.twLogoLabel.setPixmap(QtGui.QPixmap(":/plugins/theMapCloud/themapcloud_logo.png"))
        self.twLogoLabel.setScaledContents(False)
        self.twLogoLabel.setOpenExternalLinks(True)
        self.twLogoLabel.setObjectName("twLogoLabel")
        self.gridLayout_4.addWidget(self.twLogoLabel, 19, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 19, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 19, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 16, 2, 1, 1)
        self.abstractLabel = QtWidgets.QLabel(self.tab)
        self.abstractLabel.setText("")
        self.abstractLabel.setScaledContents(False)
        self.abstractLabel.setWordWrap(True)
        self.abstractLabel.setObjectName("abstractLabel")
        self.gridLayout_4.addWidget(self.abstractLabel, 17, 2, 1, 1)
        self.titleLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout_4.addWidget(self.titleLabel, 0, 2, 1, 1)
        self.emailLabel = QtWidgets.QLabel(self.tab)
        self.emailLabel.setText("")
        self.emailLabel.setWordWrap(True)
        self.emailLabel.setObjectName("emailLabel")
        self.gridLayout_4.addWidget(self.emailLabel, 18, 2, 1, 1)
        self.countryLabel = QtWidgets.QLabel(self.tab)
        self.countryLabel.setText("")
        self.countryLabel.setWordWrap(True)
        self.countryLabel.setObjectName("countryLabel")
        self.gridLayout_4.addWidget(self.countryLabel, 10, 2, 1, 1)
        self.cityLabel = QtWidgets.QLabel(self.tab)
        self.cityLabel.setText("")
        self.cityLabel.setWordWrap(True)
        self.cityLabel.setObjectName("cityLabel")
        self.gridLayout_4.addWidget(self.cityLabel, 8, 2, 1, 1)
        self.faxLabel = QtWidgets.QLabel(self.tab)
        self.faxLabel.setText("")
        self.faxLabel.setWordWrap(True)
        self.faxLabel.setObjectName("faxLabel")
        self.gridLayout_4.addWidget(self.faxLabel, 15, 2, 1, 1)
        self.postcodeLabel = QtWidgets.QLabel(self.tab)
        self.postcodeLabel.setText("")
        self.postcodeLabel.setObjectName("postcodeLabel")
        self.gridLayout_4.addWidget(self.postcodeLabel, 13, 2, 1, 1)
        self.orgLabel = QtWidgets.QLabel(self.tab)
        self.orgLabel.setText("")
        self.orgLabel.setWordWrap(True)
        self.orgLabel.setObjectName("orgLabel")
        self.gridLayout_4.addWidget(self.orgLabel, 5, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        OsmaDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(OsmaDockWidget)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(OsmaDockWidget)

    def retranslateUi(self, OsmaDockWidget):
        _translate = QtCore.QCoreApplication.translate
        OsmaDockWidget.setWindowTitle(_translate("OsmaDockWidget", "theMapCloud Web Services"))
        self.loadLayersWmtsButton.setText(_translate("OsmaDockWidget", "Load Layers"))
        self.addWmtsButton.setText(_translate("OsmaDockWidget", "Add Selected"))
        self.zoomExtentWmtsBox.setText(_translate("OsmaDockWidget", "Zoom to extent"))
        self.wmtsSearchLineEdit.setToolTip(_translate("OsmaDockWidget", "Search WMTS Layers..."))
        self.wmtsSearchLineEdit.setPlaceholderText(_translate("OsmaDockWidget", "Search WMTS layers..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wmtsTab), _translate("OsmaDockWidget", "WMTS"))
        self.addWmsButton.setText(_translate("OsmaDockWidget", "Add Selected"))
        self.loadLayersWmsButton.setText(_translate("OsmaDockWidget", "Load Layers"))
        self.zoomExtentWmsBox.setText(_translate("OsmaDockWidget", "Zoom to extent"))
        self.wmsSearchLineEdit.setToolTip(_translate("OsmaDockWidget", "Search WMS Layers"))
        self.wmsSearchLineEdit.setPlaceholderText(_translate("OsmaDockWidget", "Search WMS layers..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wmsTab), _translate("OsmaDockWidget", "WMS"))
        self.titleLabel.setText(_translate("OsmaDockWidget", "theMapCloud Web Services"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("OsmaDockWidget", "About"))


import TheMapCloudWebServices.resources.resources
