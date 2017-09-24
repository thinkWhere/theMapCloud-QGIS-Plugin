# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Colin\work\projects\theMapCloud-QGIS-Plugin\TheMapCloudWebServices\ui\auth_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AuthDialog(object):
    def setupUi(self, AuthDialog):
        AuthDialog.setObjectName("AuthDialog")
        AuthDialog.resize(300, 147)
        AuthDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(AuthDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.usernameLabel = QtWidgets.QLabel(AuthDialog)
        self.usernameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout_3.addWidget(self.usernameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.usernameLineEdit = QtWidgets.QLineEdit(AuthDialog)
        self.usernameLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.horizontalLayout_3.addWidget(self.usernameLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.passwordLabel = QtWidgets.QLabel(AuthDialog)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayout_2.addWidget(self.passwordLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.passwordLineEdit = QtWidgets.QLineEdit(AuthDialog)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout_2.addWidget(self.passwordLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelPushButton = QtWidgets.QPushButton(AuthDialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.loginPushButton = QtWidgets.QPushButton(AuthDialog)
        self.loginPushButton.setObjectName("loginPushButton")
        self.horizontalLayout.addWidget(self.loginPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AuthDialog)
        QtCore.QMetaObject.connectSlotsByName(AuthDialog)
        AuthDialog.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        AuthDialog.setTabOrder(self.passwordLineEdit, self.loginPushButton)
        AuthDialog.setTabOrder(self.loginPushButton, self.cancelPushButton)

    def retranslateUi(self, AuthDialog):
        _translate = QtCore.QCoreApplication.translate
        AuthDialog.setWindowTitle(_translate("AuthDialog", "OSMA Web Services Login"))
        self.usernameLabel.setText(_translate("AuthDialog", "Username:"))
        self.passwordLabel.setText(_translate("AuthDialog", "Password:"))
        self.cancelPushButton.setText(_translate("AuthDialog", "Cancel"))
        self.loginPushButton.setText(_translate("AuthDialog", "Login"))

