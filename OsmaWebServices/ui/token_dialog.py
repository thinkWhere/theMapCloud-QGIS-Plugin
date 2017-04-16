# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'token_dialog.ui'
#
# Created: Tue Mar 24 16:08:53 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
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

class Ui_TokenDialog(object):
    def setupUi(self, TokenDialog):
        TokenDialog.setObjectName(_fromUtf8("TokenDialog"))
        TokenDialog.resize(324, 78)
        self.gridLayout = QtGui.QGridLayout(TokenDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tokenHorizontalLayout = QtGui.QHBoxLayout()
        self.tokenHorizontalLayout.setObjectName(_fromUtf8("tokenHorizontalLayout"))
        self.tokenLabel = QtGui.QLabel(TokenDialog)
        self.tokenLabel.setObjectName(_fromUtf8("tokenLabel"))
        self.tokenHorizontalLayout.addWidget(self.tokenLabel)
        self.tokenLineEdit = QtGui.QLineEdit(TokenDialog)
        self.tokenLineEdit.setObjectName(_fromUtf8("tokenLineEdit"))
        self.tokenHorizontalLayout.addWidget(self.tokenLineEdit)
        self.gridLayout.addLayout(self.tokenHorizontalLayout, 2, 0, 1, 1)
        self.goBtnHorizontalLayout = QtGui.QHBoxLayout()
        self.goBtnHorizontalLayout.setObjectName(_fromUtf8("goBtnHorizontalLayout"))
        self.goTokenButton = QtGui.QPushButton(TokenDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goTokenButton.sizePolicy().hasHeightForWidth())
        self.goTokenButton.setSizePolicy(sizePolicy)
        self.goTokenButton.setObjectName(_fromUtf8("goTokenButton"))
        self.goBtnHorizontalLayout.addWidget(self.goTokenButton)
        self.gridLayout.addLayout(self.goBtnHorizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(TokenDialog)
        QtCore.QMetaObject.connectSlotsByName(TokenDialog)

    def retranslateUi(self, TokenDialog):
        TokenDialog.setWindowTitle(_translate("TokenDialog", "OSMA MapCloudAuthentication", None))
        self.tokenLabel.setText(_translate("TokenDialog", "Please enter OSMA organisation mc_auth:", None))
        self.goTokenButton.setText(_translate("TokenDialog", "Go", None))

import OsmaWebServices.resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TokenDialog = QtGui.QDialog()
    ui = Ui_TokenDialog()
    ui.setupUi(TokenDialog)
    TokenDialog.show()
    sys.exit(app.exec_())

