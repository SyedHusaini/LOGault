# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A:\SEMESTER_6\Software_Engineering\logault\logault.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 603)
        MainWindow.setStyleSheet("background-color: slategray;\n"
"selection-background-color: rgb(186, 189, 182);\n"
"color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cat_and_lab_container = QtWidgets.QVBoxLayout()
        self.cat_and_lab_container.setSpacing(1)
        self.cat_and_lab_container.setObjectName("cat_and_lab_container")
        self.toolbox = QtWidgets.QHBoxLayout()
        self.toolbox.setObjectName("toolbox")
        self.new_reference_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_reference_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_reference_button.setIcon(icon)
        self.new_reference_button.setIconSize(QtCore.QSize(25, 25))
        self.new_reference_button.setObjectName("new_reference_button")
        self.toolbox.addWidget(self.new_reference_button)
        self.delete_reference_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_reference_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_reference_button.setIcon(icon1)
        self.delete_reference_button.setIconSize(QtCore.QSize(25, 25))
        self.delete_reference_button.setObjectName("delete_reference_button")
        self.toolbox.addWidget(self.delete_reference_button)
        self.delete_category_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_category_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/bind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_category_button.setIcon(icon2)
        self.delete_category_button.setIconSize(QtCore.QSize(25, 25))
        self.delete_category_button.setObjectName("delete_category_button")
        self.toolbox.addWidget(self.delete_category_button)
        self.new_dir_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_dir_button.sizePolicy().hasHeightForWidth())
        self.new_dir_button.setSizePolicy(sizePolicy)
        self.new_dir_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/newd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_dir_button.setIcon(icon3)
        self.new_dir_button.setIconSize(QtCore.QSize(25, 25))
        self.new_dir_button.setObjectName("new_dir_button")
        self.toolbox.addWidget(self.new_dir_button)
        self.cat_and_lab_container.addLayout(self.toolbox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("background-color : skyblue")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.cat_and_lab_container.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.cat_and_lab_container.addWidget(self.lineEdit)
        self.category_tree = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category_tree.sizePolicy().hasHeightForWidth())
        self.category_tree.setSizePolicy(sizePolicy)
        self.category_tree.setMouseTracking(True)
        self.category_tree.setObjectName("category_tree")
        item_0 = QtWidgets.QTreeWidgetItem(self.category_tree)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/recent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon4)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_0 = QtWidgets.QTreeWidgetItem(self.category_tree)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon5)
        self.cat_and_lab_container.addWidget(self.category_tree)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.plus_label = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus_label.sizePolicy().hasHeightForWidth())
        self.plus_label.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus_label.setIcon(icon6)
        self.plus_label.setObjectName("plus_label")
        self.horizontalLayout_2.addWidget(self.plus_label)
        self.minus_label = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus_label.sizePolicy().hasHeightForWidth())
        self.minus_label.setSizePolicy(sizePolicy)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minus_label.setIcon(icon7)
        self.minus_label.setIconSize(QtCore.QSize(18, 16))
        self.minus_label.setObjectName("minus_label")
        self.horizontalLayout_2.addWidget(self.minus_label)
        self.cat_and_lab_container.addLayout(self.horizontalLayout_2)
        self.label_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_table.sizePolicy().hasHeightForWidth())
        self.label_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_table.setFont(font)
        self.label_table.setMouseTracking(True)
        self.label_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_table.setLineWidth(0)
        self.label_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.label_table.setProperty("showDropIndicator", False)
        self.label_table.setDragDropOverwriteMode(False)
        self.label_table.setAlternatingRowColors(False)
        self.label_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.label_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.label_table.setShowGrid(False)
        self.label_table.setObjectName("label_table")
        self.label_table.setColumnCount(2)
        self.label_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.label_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.label_table.setHorizontalHeaderItem(1, item)
        self.label_table.horizontalHeader().setVisible(False)
        self.label_table.horizontalHeader().setCascadingSectionResizes(False)
        self.label_table.horizontalHeader().setDefaultSectionSize(100)
        self.label_table.horizontalHeader().setMinimumSectionSize(150)
        self.label_table.horizontalHeader().setStretchLastSection(True)
        self.label_table.verticalHeader().setVisible(False)
        self.label_table.verticalHeader().setDefaultSectionSize(20)
        self.label_table.verticalHeader().setHighlightSections(False)
        self.label_table.verticalHeader().setMinimumSectionSize(20)
        self.cat_and_lab_container.addWidget(self.label_table)
        self.horizontalLayout.addLayout(self.cat_and_lab_container)
        self.ref_table_container = QtWidgets.QVBoxLayout()
        self.ref_table_container.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.ref_table_container.setSpacing(1)
        self.ref_table_container.setObjectName("ref_table_container")
        self.ref_box_title = QtWidgets.QLabel(self.centralwidget)
        self.ref_box_title.setStyleSheet("background-color : tomato")
        self.ref_box_title.setObjectName("ref_box_title")
        self.ref_table_container.addWidget(self.ref_box_title)
        self.reference_table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.reference_table.sizePolicy().hasHeightForWidth())
        self.reference_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(9)
        self.reference_table.setFont(font)
        self.reference_table.setMouseTracking(True)
        self.reference_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.reference_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.reference_table.setDragDropOverwriteMode(False)
        self.reference_table.setAlternatingRowColors(False)
        self.reference_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.reference_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.reference_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.reference_table.setObjectName("reference_table")
        self.reference_table.setColumnCount(6)
        self.reference_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.reference_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reference_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reference_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reference_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.reference_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.reference_table.setHorizontalHeaderItem(5, item)
        self.reference_table.horizontalHeader().setVisible(True)
        self.reference_table.horizontalHeader().setCascadingSectionResizes(False)
        self.reference_table.horizontalHeader().setDefaultSectionSize(100)
        self.reference_table.horizontalHeader().setHighlightSections(False)
        self.reference_table.horizontalHeader().setMinimumSectionSize(15)
        self.reference_table.horizontalHeader().setSortIndicatorShown(True)
        self.reference_table.horizontalHeader().setStretchLastSection(True)
        self.reference_table.verticalHeader().setVisible(False)
        self.reference_table.verticalHeader().setHighlightSections(True)
        self.reference_table.verticalHeader().setMinimumSectionSize(15)
        self.ref_table_container.addWidget(self.reference_table)
        self.horizontalLayout.addLayout(self.ref_table_container)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuThemes = QtWidgets.QMenu(self.menubar)
        self.menuThemes.setObjectName("menuThemes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.newReference = QtWidgets.QDockWidget(MainWindow)
        self.newReference.setMouseTracking(True)
        self.newReference.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable|QtWidgets.QDockWidget.DockWidgetFloatable)
        self.newReference.setProperty("path", "")
        self.newReference.setProperty("id", "")
        self.newReference.setObjectName("newReference")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(4, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBar = QtWidgets.QPlainTextEdit(self.dockWidgetContents)
        self.titleBar.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titleBar.setFont(font)
        self.titleBar.setTabChangesFocus(True)
        self.titleBar.setObjectName("titleBar")
        self.verticalLayout.addWidget(self.titleBar)
        self.bodyBar = QtWidgets.QPlainTextEdit(self.dockWidgetContents)
        self.bodyBar.setTabChangesFocus(True)
        self.bodyBar.setObjectName("bodyBar")
        self.verticalLayout.addWidget(self.bodyBar)
        self.sourceBar = QtWidgets.QPlainTextEdit(self.dockWidgetContents)
        self.sourceBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.sourceBar.setTabChangesFocus(True)
        self.sourceBar.setObjectName("sourceBar")
        self.verticalLayout.addWidget(self.sourceBar)
        self.add_label_button = QtWidgets.QPushButton(self.dockWidgetContents)
        self.add_label_button.setObjectName("add_label_button")
        self.verticalLayout.addWidget(self.add_label_button)
        self.saveButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.newReference.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.newReference)
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionCustom = QtWidgets.QAction(MainWindow)
        self.actionCustom.setObjectName("actionCustom")
        self.actionKhatoni = QtWidgets.QAction(MainWindow)
        self.actionKhatoni.setObjectName("actionKhatoni")
        self.menuHelp.addAction(self.actionAbout_Us)
        self.menuThemes.addAction(self.actionCustom)
        self.menuThemes.addAction(self.actionKhatoni)
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuThemes.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.new_reference_button.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.label.setText(_translate("MainWindow", "LogAult"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search your library..."))
        self.category_tree.headerItem().setText(0, _translate("MainWindow", "My Library"))
        self.category_tree.headerItem().setText(1, _translate("MainWindow", "id"))
        __sortingEnabled = self.category_tree.isSortingEnabled()
        self.category_tree.setSortingEnabled(False)
        self.category_tree.topLevelItem(0).setText(0, _translate("MainWindow", "Recent"))
        self.category_tree.topLevelItem(0).setText(1, _translate("MainWindow", "-1"))
        self.category_tree.topLevelItem(1).setText(0, _translate("MainWindow", "root"))
        self.category_tree.topLevelItem(1).setText(1, _translate("MainWindow", "1"))
        self.category_tree.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "Labels"))
        self.plus_label.setText(_translate("MainWindow", "..."))
        self.minus_label.setText(_translate("MainWindow", "..."))
        item = self.label_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "label"))
        item = self.label_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id"))
        self.ref_box_title.setText(_translate("MainWindow", "<html><head/><body><table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\"><tr><td><p><img src=\"icons/reference.png\" width=\"25\" height=\"25\"/></p></td><td><p><span style=\" font-size:14pt;\">References</span></p></td></tr></table></body></html>"))
        item = self.reference_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.reference_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Body"))
        item = self.reference_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source"))
        item = self.reference_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Last Updated"))
        item = self.reference_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "refid"))
        item = self.reference_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "path"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuThemes.setTitle(_translate("MainWindow", "Themes"))
        self.newReference.setWindowTitle(_translate("MainWindow", "Reference Editor"))
        self.add_label_button.setText(_translate("MainWindow", "Add Labels"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.actionCustom.setText(_translate("MainWindow", "Custom"))
        self.actionKhatoni.setText(_translate("MainWindow", "Khatoni"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

