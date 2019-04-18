# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hamza/PycharmProjects/logault/dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 400)
        Dialog.setMinimumSize(QtCore.QSize(200, 400))
        Dialog.setMaximumSize(QtCore.QSize(200, 400))
        self.label_table = QtWidgets.QTableWidget(Dialog)
        self.label_table.setGeometry(QtCore.QRect(4, 10, 191, 341))
        self.label_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.label_table.setProperty("showDropIndicator", False)
        self.label_table.setDragDropOverwriteMode(False)
        self.label_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.label_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.label_table.setObjectName("label_table")
        self.label_table.setColumnCount(2)
        self.label_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.label_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.label_table.setHorizontalHeaderItem(1, item)
        self.label_table.horizontalHeader().setVisible(False)
        self.label_table.horizontalHeader().setCascadingSectionResizes(True)
        self.label_table.horizontalHeader().setDefaultSectionSize(100)
        self.label_table.horizontalHeader().setHighlightSections(False)
        self.label_table.horizontalHeader().setMinimumSectionSize(0)
        self.label_table.horizontalHeader().setStretchLastSection(True)
        self.label_table.verticalHeader().setVisible(False)
        self.accept_labels_btn = QtWidgets.QPushButton(Dialog)
        self.accept_labels_btn.setGeometry(QtCore.QRect(70, 363, 61, 25))
        self.accept_labels_btn.setObjectName("accept_labels_btn")

        self.retranslateUi(Dialog)
        self.accept_labels_btn.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Assign Labels"))
        item = self.label_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "label"))
        item = self.label_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "id"))
        self.accept_labels_btn.setText(_translate("Dialog", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
