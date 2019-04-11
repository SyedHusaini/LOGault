from builtins import print

from PyQt5 import QtGui
from PyQt5.QtWidgets import QTreeWidgetItem, QTableWidgetItem, QMessageBox, QInputDialog, QLineEdit
from db_handling import connection
import logault
import time



def initiate():
    ui.category_tree.hideColumn(1)  # hiding category id column
    ui.reference_table.hideColumn(4)# hiding reference id column
    ui.label_table.hideColumn(1)# hiding label id column
    ui.category_tree.clicked.connect(populate_reference_table)
    ui.delete_reference_button.clicked.connect(delete_reference)
    ui.delete_category_button.clicked.connect(delete_category)
    ui.new_dir_button.clicked.connect(make_new_category)
    ui.new_reference_button.clicked.connect(make_new_reference)
    ui.reference_table.clicked.connect(display_reference)
    ui.label_table.clicked.connect(populate_reference_table)
    ui.saveButton.clicked.connect(save_a_reference)
    ui.plus_label.clicked.connect(add_label)
    ui.minus_label.clicked.connect(delete_label)
    ui.newReference.setDisabled(True)
    populate_tree()
    populate_label_table()

def add_label():
    newLabel = getText("New Label", "Label name:")
    cursor = connection.cursor()
    sql = "SELECT * FROM `label`"
    cursor.execute(sql)
    result = cursor.fetchall()
    check = False
    while not(check):
        check = True
        for i in result:
            if(i["tag"]==newLabel):
                gen_msg_box(QMessageBox.Warning, "Label Already Exists","Select a unique label name to proceed", "Error 406: Duplicate Label")
                newLabel = getText("New Label", "Label name:")
                check = False
                break;

    cursor = connection.cursor()
    sql = "INSERT INTO `logault_final`.`label` (`tag`) VALUES ('"+newLabel+"')"
    cursor.execute(sql)
    connection.commit()
    populate_label_table()

def delete_label():
    row = ui.label_table.currentRow()
    lab_id = ui.label_table.item(row, 1).text()
    cursor = connection.cursor()
    sql = "DELETE FROM `logault_final`.`label` WHERE (`lab_id` = '"+lab_id+"')"
    cursor.execute(sql)
    connection.commit()
    ui.label_table.removeRow(ui.label_table.rowAt(row))
    # populate_label_table()


def delete_category():
    if (ui.category_tree.currentItem() == None or ui.category_tree.currentItem().text(1) == "-1" or ui.category_tree.currentItem().text(1) == "3"):
        return
    cursor = connection.cursor()
    sql = "DELETE FROM `logault_final`.`category` WHERE (`cat_id` = '"+ui.category_tree.currentItem().text(1)+"')"
    cursor.execute(sql)
    connection.commit()
    populate_tree()

def save_a_reference():
    id = ui.newReference.property("id")
    if(len(ui.bodyBar.toPlainText())==0):
        gen_msg_box(QMessageBox.Warning, "Reference must have a body", "Type in text for reference body to proceed","Error 777: Invalid Reference")
        return;
    if(id!="0"):
        cursor = connection.cursor()
        sql = "UPDATE `logault_final`.`reference` SET `title` = '" + ui.titleBar.toPlainText()+\
              "',`body` = '"+ui.bodyBar.toPlainText()+\
              "',`source` = '"+ui.sourceBar.toPlainText()+\
              "',`timestamp` = '"+time.strftime('%Y-%m-%d %H:%M:%S')+\
              "'  WHERE (`ref_id` = '"+ id + "')"
        # sql = "UPDATE `logault_final`.`reference` SET `body` = 'kiun zayan kar bano sody faramosh rahon fikr-e-farda na karon or hamma tan gosh rahon.', `title` = 'aaa', `timestamp` = '2019-04-31 13:55:28', `source` = 'shikwa' WHERE (`ref_id` = '2')"
        cursor.execute(sql)
        connection.commit()
        ui.newReference.setProperty("id", "0")
        ui.category_tree.clic
    elif(id=="0"):
        if(ui.category_tree.currentItem().text(0)=="Recent"):
            gen_msg_box(QMessageBox.Warning, "Invalid Category", "Choose appropriate category","Error 404: Invalid Category")
            return
        cursor = connection.cursor()
        sql = "INSERT INTO `logault_final`.`reference` (`body`, `title`, `source`, `cat_id`) VALUES ('"\
              +ui.bodyBar.toPlainText()+"','"\
              +ui.titleBar.toPlainText() + "','"\
              +ui.sourceBar.toPlainText() + "','"\
              +ui.category_tree.currentItem().text(1) + "')"
        # sql = "UPDATE `logault_final`.`reference` SET `body` = 'kiun zayan kar bano sody faramosh rahon fikr-e-farda na karon or hamma tan gosh rahon.', `title` = 'aaa', `timestamp` = '2019-04-31 13:55:28', `source` = 'shikwa' WHERE (`ref_id` = '2')"
        cursor.execute(sql)
        connection.commit()
        ui.newReference.setDisabled(True)

def display_reference():
    ui.newReference.setVisible(True)
    ui.newReference.setDisabled(False)
    s = ui.sender()
    row = s.currentRow()
    ui.titleBar.clear()
    ui.bodyBar.clear()
    ui.sourceBar.clear()
    ui.newReference.setProperty("id", s.item(row, 4).text())
    ui.titleBar.insertPlainText(s.item(row, 0).text())
    ui.bodyBar.insertPlainText(s.item(row, 1).text())
    ui.sourceBar.insertPlainText(s.item(row, 2).text())

    cursor = connection.cursor()
    sql = "SELECT `tag` FROM `label` WHERE lab_id IN (SELECT lab_id FROM reference_label WHERE ref_id = " + s.item(row, 4).text() + ")"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        ui.labelBar.addItem(i["tag"])

def delete_reference():
    if(ui.reference_table.currentRow()<0):
        return
    cursor = connection.cursor()
    sql = "DELETE FROM `logault_final`.`reference` WHERE (`ref_id` = '"+ui.reference_table.item(ui.reference_table.currentRow(),4).text()+"')"
    cursor.execute(sql)
    connection.commit()
    populate_reference_table('me')

def make_new_category():
    if (ui.category_tree.currentItem() == None or ui.category_tree.currentItem().text(0) == "Recent"):
        gen_msg_box(QMessageBox.Warning, "You have not selected a category","Select an appropriate category to proceed", "Error 404: Invalid Category")
        return
    selected_folder = ui.category_tree.currentItem()
    newTitle = getText("Category Detail", "Title:")
    for i in range(0, selected_folder.childCount()):
        if(selected_folder.child(i).text(0)==newTitle):
            gen_msg_box(QMessageBox.Warning, "Category Already Exists","Select a unique category title to proceed", "Error 405: Duplicate Category")
            newTitle = getText("Category Detail", "Title:")
            i=0
    else:
        cursor = connection.cursor()
        sql = "INSERT INTO `logault_final`.`category` (`title`, `parent_cat`) VALUES ('"+newTitle+"', '"+selected_folder.text(1)+"')"
        cursor.execute(sql)
        connection.commit()
        populate_tree()

def getText(wintitle, label):
    text, okPressed = QInputDialog.getText(ui, wintitle,label, QLineEdit.Normal, "")
    if okPressed and text != '':
        return (text)

def getChoice():
    items = ("Red","Blue","Green")
    item, okPressed = QInputDialog.getItem(ui, "Get item","Color:", items, 0, False)
    if okPressed and item:
        print(item)

def make_new_reference():
    if (ui.category_tree.currentItem()==None or ui.category_tree.currentItem().text(0)=="Recent"):
        gen_msg_box(QMessageBox.Warning,"You have not selected a category","Select an appropriate category to proceed","Error 404: Invalid Category")
        # msg.setDetailedText("The details are as follows:")
    else:
        ui.newReference.setProperty("id","0")
        ui.newReference.setVisible(True)
        ui.newReference.setDisabled(False)
        ui.newReference.setWindowTitle("New Reference")

def populate_tree():
        # read database
        myroot = find_parent(ui.category_tree.invisibleRootItem(), str(3))
        while(myroot.childCount()):
            myroot.removeChild(myroot.child(0))

        cursor = connection.cursor()
        sql = "SELECT `*` FROM `category`"
        cursor.execute(sql)
        result = cursor.fetchall()

        for i in result:
            if (i["parent_cat"] != i["cat_id"]):#if not root

                root = ui.category_tree.invisibleRootItem()  # picking tree
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

def populate_reference_table(caller):
    while (ui.reference_table.rowCount()):#empty reference table
        ui.reference_table.removeRow(ui.reference_table.rowAt(0))
    if(caller=='me'):
        s = ui.category_tree
        sql = "SELECT `*` FROM `reference` WHERE cat_id=" + s.currentItem().text(1)
    else:
        s = ui.sender()
        if(s.objectName()=="label_table"):
            sql = "SELECT `*` FROM `reference` WHERE ref_id IN (SELECT ref_id FROM `reference_label` WHERE lab_id = " + s.item(s.currentRow(), 1).text() + ")"
        elif(s.objectName()=="category_tree"):
            sql = "SELECT `*` FROM `reference` WHERE cat_id=" + s.currentItem().text(1)

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        rowposition = ui.reference_table.rowCount()
        ui.reference_table.insertRow(rowposition)
        ui.reference_table.setItem(rowposition, 0, QTableWidgetItem(i["title"]))
        ui.reference_table.setItem(rowposition, 1, QTableWidgetItem(i["body"]))
        ui.reference_table.setItem(rowposition, 2, QTableWidgetItem(i["source"]))
        ui.reference_table.setItem(rowposition, 3, QTableWidgetItem(str(i["timestamp"])))
        ui.reference_table.setItem(rowposition, 4, QTableWidgetItem(str(i["ref_id"])))

def populate_label_table():
    while(ui.label_table.rowCount()):
        ui.label_table.removeRow(ui.label_table.rowAt(0))
    cursor = connection.cursor()
    sql = "SELECT `*` FROM `label`"
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in result:
        rowposition = ui.reference_table.rowCount()
        ui.label_table.insertRow(rowposition)
        ui.label_table.setItem(rowposition, 0, QTableWidgetItem(i["tag"]))
        ui.label_table.setItem(rowposition, 1, QTableWidgetItem(str(i["lab_id"])))

def gen_msg_box(icon, text, infotext, wintitle):
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setText(text)
    msg.setInformativeText(infotext)
    msg.setWindowTitle(wintitle)
    # msg.setDetailedText("The details are as follows:")
    retval = msg.exec_()


if __name__ == "__main__":
    import sys
    app = logault.QtWidgets.QApplication(sys.argv)
    MainWindow = logault.QtWidgets.QMainWindow()
    ui = logault.Ui_MainWindow()
    ui.setupUi(MainWindow)
    initiate()
    MainWindow.show()
    sys.exit(app.exec_())
