# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multi_wms_order.ui'
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

class Ui_MultiWmsDialog(object):
    def setupUi(self, MultiWmsDialog):
        MultiWmsDialog.setObjectName(_fromUtf8("MultiWmsDialog"))
        MultiWmsDialog.resize(335, 266)
        self.gridLayout = QtGui.QGridLayout(MultiWmsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.layerOrderPushButton = QtGui.QPushButton(MultiWmsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layerOrderPushButton.sizePolicy().hasHeightForWidth())
        self.layerOrderPushButton.setSizePolicy(sizePolicy)
        self.layerOrderPushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.layerOrderPushButton.setObjectName(_fromUtf8("layerOrderPushButton"))
        self.horizontalLayout_2.addWidget(self.layerOrderPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(MultiWmsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.displayNameLineEdit = QtGui.QLineEdit(MultiWmsDialog)
        self.displayNameLineEdit.setObjectName(_fromUtf8("displayNameLineEdit"))
        self.horizontalLayout.addWidget(self.displayNameLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.label = QtGui.QLabel(MultiWmsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.layerOrderListWidget = QtGui.QListWidget(MultiWmsDialog)
        self.layerOrderListWidget.setDragEnabled(True)
        self.layerOrderListWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.layerOrderListWidget.setObjectName(_fromUtf8("layerOrderListWidget"))
        self.gridLayout.addWidget(self.layerOrderListWidget, 3, 0, 1, 1)

        self.retranslateUi(MultiWmsDialog)
        QtCore.QMetaObject.connectSlotsByName(MultiWmsDialog)

    def retranslateUi(self, MultiWmsDialog):
        MultiWmsDialog.setWindowTitle(_translate("MultiWmsDialog", "WMS Layer Order", None))
        self.layerOrderPushButton.setText(_translate("MultiWmsDialog", "Done", None))
        self.label_2.setText(_translate("MultiWmsDialog", "Display Name (optional): ", None))
        self.label.setText(_translate("MultiWmsDialog", "Adjust the order in which the layers_wms are displayed (drag and drop)", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MultiWmsDialog = QtGui.QDialog()
    ui = Ui_MultiWmsDialog()
    ui.setupUi(MultiWmsDialog)
    MultiWmsDialog.show()
    sys.exit(app.exec_())

