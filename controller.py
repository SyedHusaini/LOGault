from builtins import print

from PyQt5 import QtGui
from PyQt5.QtWidgets import QTreeWidgetItem
from db_handling import connection
import logault

def bindings():
    ui.category_tree.clicked.connect(Category_tree_click)


def populate_tree():
        # read database
        cursor = connection.cursor()
        sql = "SELECT `*` FROM `category`"
        cursor.execute(sql)
        result = cursor.fetchall()

        ui.category_tree.hideColumn(1)#hiding id column
        for i in result:
            if (i["parent_cat"] != i["cat_id"]):#if not root

                root = ui.category_tree.invisibleRootItem()  # picking tree
                print(root.childCount())
                parent = find_parent(root, str(i["parent_cat"]))

                # print(parent.text(0))
                newitem = QTreeWidgetItem(parent)
                newitem.setText(0,i["title"])
                newitem.setText(1,str(i["cat_id"]))

                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("icons/category.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                newitem.setIcon(0, icon)

                parent.addChild(newitem)

def find_parent(root, id):
    for i in range(0,root.childCount()):
        if (root.child(i).text(1) == id):  # find parent of i
            return root.child(i)
        result = find_parent(root.child(i), id)
        if(result != None):
            return result
    return None


def Category_tree_click(self):

if __name__ == "__main__":
    import sys
    app = logault.QtWidgets.QApplication(sys.argv)
    MainWindow = logault.QtWidgets.QMainWindow()
    ui = logault.Ui_MainWindow()
    ui.setupUi(MainWindow)
    bindings()
    populate_tree()


    MainWindow.show()
    sys.exit(app.exec_())
