# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'token_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TokenDialog(object):
    def setupUi(self, TokenDialog):
        TokenDialog.setObjectName("TokenDialog")
        TokenDialog.resize(324, 78)
        self.gridLayout = QtWidgets.QGridLayout(TokenDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tokenHorizontalLayout = QtWidgets.QHBoxLayout()
        self.tokenHorizontalLayout.setObjectName("tokenHorizontalLayout")
        self.tokenLabel = QtWidgets.QLabel(TokenDialog)
        self.tokenLabel.setObjectName("tokenLabel")
        self.tokenHorizontalLayout.addWidget(self.tokenLabel)
        self.tokenLineEdit = QtWidgets.QLineEdit(TokenDialog)
        self.tokenLineEdit.setObjectName("tokenLineEdit")
        self.tokenHorizontalLayout.addWidget(self.tokenLineEdit)
        self.gridLayout.addLayout(self.tokenHorizontalLayout, 2, 0, 1, 1)
        self.goBtnHorizontalLayout = QtWidgets.QHBoxLayout()
        self.goBtnHorizontalLayout.setObjectName("goBtnHorizontalLayout")
        self.goTokenButton = QtWidgets.QPushButton(TokenDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goTokenButton.sizePolicy().hasHeightForWidth())
        self.goTokenButton.setSizePolicy(sizePolicy)
        self.goTokenButton.setObjectName("goTokenButton")
        self.goBtnHorizontalLayout.addWidget(self.goTokenButton)
        self.gridLayout.addLayout(self.goBtnHorizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(TokenDialog)
        QtCore.QMetaObject.connectSlotsByName(TokenDialog)

    def retranslateUi(self, TokenDialog):
        _translate = QtCore.QCoreApplication.translate
        TokenDialog.setWindowTitle(_translate("TokenDialog", "OSMA Token"))
        self.tokenLabel.setText(_translate("TokenDialog", "Please enter OSMA organisation token:"))
        self.goTokenButton.setText(_translate("TokenDialog", "Go"))

# import resources_rc
