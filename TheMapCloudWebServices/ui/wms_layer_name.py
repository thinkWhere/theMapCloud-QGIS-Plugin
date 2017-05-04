# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_lc_layer_name.ui'
#
# Created: Mon May 19 12:24:00 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_layerNameDialog(object):
    def setupUi(self, layerNameDialog):
        layerNameDialog.setObjectName(_fromUtf8("layerNameDialog"))
        layerNameDialog.resize(322, 88)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(layerNameDialog.sizePolicy().hasHeightForWidth())
        layerNameDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(layerNameDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.layerNameLabel = QtGui.QLabel(layerNameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerNameLabel.sizePolicy().hasHeightForWidth())
        self.layerNameLabel.setSizePolicy(sizePolicy)
        self.layerNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layerNameLabel.setObjectName(_fromUtf8("layerNameLabel"))
        self.horizontalLayout_2.addWidget(self.layerNameLabel)
        self.layerNameLineEdit = QtGui.QLineEdit(layerNameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerNameLineEdit.sizePolicy().hasHeightForWidth())
        self.layerNameLineEdit.setSizePolicy(sizePolicy)
        self.layerNameLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layerNameLineEdit.setObjectName(_fromUtf8("layerNameLineEdit"))
        self.horizontalLayout_2.addWidget(self.layerNameLineEdit)
        self.usernameLabel = QtGui.QLabel(layerNameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usernameLabel.sizePolicy().hasHeightForWidth())
        self.usernameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setText(_fromUtf8(""))
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.horizontalLayout_2.addWidget(self.usernameLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.okLayerNameButton = QtGui.QPushButton(layerNameDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okLayerNameButton.sizePolicy().hasHeightForWidth())
        self.okLayerNameButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.okLayerNameButton.setFont(font)
        self.okLayerNameButton.setObjectName(_fromUtf8("okLayerNameButton"))
        self.horizontalLayout.addWidget(self.okLayerNameButton)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.retranslateUi(layerNameDialog)
        QtCore.QMetaObject.connectSlotsByName(layerNameDialog)

    def retranslateUi(self, layerNameDialog):
        layerNameDialog.setWindowTitle(QtGui.QApplication.translate("layerNameDialog", "Enter WMS display name...", None, QtGui.QApplication.UnicodeUTF8))
        self.layerNameLabel.setText(QtGui.QApplication.translate("layerNameDialog", "Enter display name:", None, QtGui.QApplication.UnicodeUTF8))
        self.okLayerNameButton.setText(QtGui.QApplication.translate("layerNameDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    layerNameDialog = QtGui.QDialog()
    ui = Ui_layerNameDialog()
    ui.setupUi(layerNameDialog)
    layerNameDialog.show()
    sys.exit(app.exec_())

