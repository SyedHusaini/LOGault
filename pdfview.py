# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/hamza/PycharmProjects/logault/pdfview.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.PDFView = QtWebKitWidgets.QWebView(Form)
        self.PDFView.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.PDFView.setUrl(QtCore.QUrl("about:blank"))
        self.PDFView.setObjectName("PDFView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PDF View"))


im


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
