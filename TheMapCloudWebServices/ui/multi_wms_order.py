# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multi_wms_order.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MultiWmsDialog(object):
    def setupUi(self, MultiWmsDialog):
        MultiWmsDialog.setObjectName("MultiWmsDialog")
        MultiWmsDialog.resize(335, 266)
        self.gridLayout = QtWidgets.QGridLayout(MultiWmsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.layerOrderPushButton = QtWidgets.QPushButton(MultiWmsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerOrderPushButton.sizePolicy().hasHeightForWidth())
        self.layerOrderPushButton.setSizePolicy(sizePolicy)
        self.layerOrderPushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.layerOrderPushButton.setObjectName("layerOrderPushButton")
        self.horizontalLayout_2.addWidget(self.layerOrderPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(MultiWmsDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.displayNameLineEdit = QtWidgets.QLineEdit(MultiWmsDialog)
        self.displayNameLineEdit.setObjectName("displayNameLineEdit")
        self.horizontalLayout.addWidget(self.displayNameLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(MultiWmsDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.layerOrderListWidget = QtWidgets.QListWidget(MultiWmsDialog)
        self.layerOrderListWidget.setDragEnabled(True)
        self.layerOrderListWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.layerOrderListWidget.setObjectName("layerOrderListWidget")
        self.gridLayout.addWidget(self.layerOrderListWidget, 3, 0, 1, 1)

        self.retranslateUi(MultiWmsDialog)
        QtCore.QMetaObject.connectSlotsByName(MultiWmsDialog)

    def retranslateUi(self, MultiWmsDialog):
        _translate = QtCore.QCoreApplication.translate
        MultiWmsDialog.setWindowTitle(_translate("MultiWmsDialog", "WMS Layer Order"))
        self.layerOrderPushButton.setText(_translate("MultiWmsDialog", "Done"))
        self.label_2.setText(_translate("MultiWmsDialog", "Display Name (optional): "))
        self.label.setText(_translate("MultiWmsDialog", "Adjust the order in which the layers are displayed (drag and drop)"))

# import resources_rc
