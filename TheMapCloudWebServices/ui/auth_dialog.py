# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from ..config_parser import parse_config_from_file

try:
    _fromUtf8 = str.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AuthDialog(object):

    def setupUi(self, AuthDialog):

        self.config = parse_config_from_file()
        AuthDialog.setObjectName(_fromUtf8("AuthDialog"))
        AuthDialog.resize(300, 147)
        AuthDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtGui.QVBoxLayout(AuthDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.usernameLabel = QtGui.QLabel(AuthDialog)
        self.usernameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.horizontalLayout_3.addWidget(self.usernameLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.usernameLineEdit = QtGui.QLineEdit(AuthDialog)
        self.usernameLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.usernameLineEdit.setObjectName(_fromUtf8("usernameLineEdit"))
        self.horizontalLayout_3.addWidget(self.usernameLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.passwordLabel = QtGui.QLabel(AuthDialog)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.horizontalLayout_2.addWidget(self.passwordLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.passwordLineEdit = QtGui.QLineEdit(AuthDialog)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.horizontalLayout_2.addWidget(self.passwordLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancelPushButton = QtGui.QPushButton(AuthDialog)
        self.cancelPushButton.setObjectName(_fromUtf8("cancelPushButton"))
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.loginPushButton = QtGui.QPushButton(AuthDialog)
        self.loginPushButton.setObjectName(_fromUtf8("loginPushButton"))
        self.horizontalLayout.addWidget(self.loginPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(AuthDialog)
        QtCore.QMetaObject.connectSlotsByName(AuthDialog)
        AuthDialog.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        AuthDialog.setTabOrder(self.passwordLineEdit, self.loginPushButton)
        AuthDialog.setTabOrder(self.loginPushButton, self.cancelPushButton)

    def retranslateUi(self, AuthDialog):
        AuthDialog.setWindowTitle(_translate("AuthDialog", "{} Login".format(self.config.get('title')), None))
        self.usernameLabel.setText(_translate("AuthDialog", "Username:", None))
        self.passwordLabel.setText(_translate("AuthDialog", "Password:", None))
        self.cancelPushButton.setText(_translate("AuthDialog", "Cancel", None))
        self.loginPushButton.setText(_translate("AuthDialog", "Login", None))

