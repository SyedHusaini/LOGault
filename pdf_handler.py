import os
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QAction


class PDFViewer(QtWebEngineWidgets.QWebEngineView):
    pathpdf=""
    pathhtml="A:/SEMESTER_6/Software_Engineering/logault/viewer"
    def __init__(self, pathpdf):
        if os.path.exists(self.pathhtml+"s.html"):
            os.remove(self.pathhtml+"s.html")
            print ("File Deleted")
        else:
            print("The file does not exist")
        self.pathpdf = pathpdf
        super(PDFViewer, self).__init__()
        myCmd = 'pdftohtml \"'+ self.pathpdf+'.pdf\"' + ' ' + self.pathhtml
        os.system(myCmd)
        self.load(QtCore.QUrl('file:///'+self.pathhtml+"s.html"))
        self.setObjectName("viewer")
        os.system("del /f "+self.pathhtml+"s.html ")



            # self.addAction(QAction()).connect(print(self.selectedText()))

