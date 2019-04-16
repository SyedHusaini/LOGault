# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A:\SEMESTER_6\Software_Engineering\logault\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QWidget


class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 400)
        Dialog.setMinimumSize(QtCore.QSize(200, 400))
        Dialog.setMaximumSize(QtCore.QSize(200, 400))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Assign Labels"))

    def making(self):
        data = ['first_row', 'second_row', 'third_row']
        nb_row = len(data)
        nb_col = 2

        qTable = self.dockwidget.tableWidget
        qTable.setRowCount(nb_row)
        qTable.setColumnCount(nb_col)
        chkBoxItem = QTableWidgetItem()

        for row in range(nb_row):
            for col in [0]:
                item = QTableWidgetItem(str(data[row]))
                qTable.setItem(row, col, item)
            for col in [1]:
                chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                qTable.setItem(row, col, chkBoxItem)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

