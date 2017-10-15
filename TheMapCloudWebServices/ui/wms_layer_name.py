# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wms_layer_name.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_layerNameDialog(object):
    def setupUi(self, layerNameDialog):
        layerNameDialog.setObjectName("layerNameDialog")
        layerNameDialog.resize(322, 88)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(layerNameDialog.sizePolicy().hasHeightForWidth())
        layerNameDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(layerNameDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layerNameLabel = QtWidgets.QLabel(layerNameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerNameLabel.sizePolicy().hasHeightForWidth())
        self.layerNameLabel.setSizePolicy(sizePolicy)
        self.layerNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layerNameLabel.setObjectName("layerNameLabel")
        self.horizontalLayout_2.addWidget(self.layerNameLabel)
        self.layerNameLineEdit = QtWidgets.QLineEdit(layerNameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerNameLineEdit.sizePolicy().hasHeightForWidth())
        self.layerNameLineEdit.setSizePolicy(sizePolicy)
        self.layerNameLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layerNameLineEdit.setObjectName("layerNameLineEdit")
        self.horizontalLayout_2.addWidget(self.layerNameLineEdit)
        self.usernameLabel = QtWidgets.QLabel(layerNameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setText("")
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout_2.addWidget(self.usernameLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.okLayerNameButton = QtWidgets.QPushButton(layerNameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okLayerNameButton.sizePolicy().hasHeightForWidth())
        self.okLayerNameButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.okLayerNameButton.setFont(font)
        self.okLayerNameButton.setObjectName("okLayerNameButton")
        self.horizontalLayout.addWidget(self.okLayerNameButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.retranslateUi(layerNameDialog)
        QtCore.QMetaObject.connectSlotsByName(layerNameDialog)

    def retranslateUi(self, layerNameDialog):
        _translate = QtCore.QCoreApplication.translate
        layerNameDialog.setWindowTitle(_translate("layerNameDialog", "Enter your display name..."))
        self.layerNameLabel.setText(_translate("layerNameDialog", "Enter display name:"))
        self.okLayerNameButton.setText(_translate("layerNameDialog", "OK"))

