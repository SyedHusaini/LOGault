import os
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets


class PDFViewer(QtWebEngineWidgets.QWebEngineView):
    pathpdf="/home/hamza/PycharmProjects/logault/Deliverable3-2019"
    pathhtml="/home/hamza/PycharmProjects/logault/viewer"
    def __init__(self):
        super(PDFViewer, self).__init__()
        myCmd = 'pdftohtml '+ self.pathpdf+'.pdf' + ' ' + self.pathhtml + ''
        os.system(myCmd)
        self.load(QtCore.QUrl('file://'+self.pathhtml+".html"))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = PDFViewer()
    window.setGeometry(600, 50, 800, 600)
    window.show()
    sys.exit(app.exec_())

