from builtins import print

from PyQt5 import QtGui
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QTreeWidgetItem, QTableWidgetItem, QMessageBox, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from db_handling import connection
import logault
import dialog as label_dialog
from new_reference_DialogBox import Ui_Dialog
import time, subprocess


class Local_Label_Dialog:
    Dialog = None
    checklist = []
    dialog = None
    rsp = 0
    outdate_check = False

    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.dialog = label_dialog.Ui_Dialog()
        self.dialog.setupUi(self.Dialog)

    def reset(self):
        self.outdate_check = False
        self.rsp = 0
        self.checklist.clear()
        while(self.dialog.label_table.rowCount()):
            self.dialog.label_table.removeRow(0)


def initiate():
    ui.reference_table.hideColumn(5)# hiding the path of the file
    ui.category_tree.hideColumn(1)# hiding category id column
    ui.reference_table.hideColumn(4)# hiding reference id column
    ui.label_table.hideColumn(1)# hiding label id column
    ui.category_tree.clicked.connect(populate_reference_table)
    ui.delete_reference_button.clicked.connect(delete_reference)
    ui.delete_category_button.clicked.connect(delete_category)
    ui.new_dir_button.clicked.connect(make_new_category)
    ui.new_reference_button.clicked.connect(make_new_reference)
    ui.reference_table.clicked.connect(display_reference)
    ui.reference_table.doubleClicked.connect(display_referenced_pdf)
    ui.label_table.clicked.connect(populate_reference_table)
    ui.saveButton.clicked.connect(save_a_reference)
    ui.plus_label.clicked.connect(add_label)
    ui.minus_label.clicked.connect(delete_label)
    ui.newReference.setDisabled(True)
    ui.add_label_button.clicked.connect(open_label_dialog)
    populate_tree()
    populate_label_table()

    # getChoice()

def update_labels(ref_id):
    local_label_dialog.outdate_check = True
    if local_label_dialog.rsp == QtWidgets.QDialog.Accepted:
        table = local_label_dialog.dialog.label_table
        rowcount = table.rowCount()
        cursor = connection.cursor()
        for i in range(0, rowcount):
            if(table.item(i,0).checkState()!=local_label_dialog.checklist[i]):#if state changed
                if(local_label_dialog.checklist[i]==QtCore.Qt.Checked):#label deleted
                    sql = "DELETE FROM `logault`.`reference_label` WHERE " \
                          + "(`lab_id` = '"+table.item(i, 1).text()+"') AND (`ref_id` = '"+ ref_id + "')"
                else:#label added
                    sql = "INSERT INTO `logault`.`reference_label` (`ref_id`, `lab_id`) VALUES ('" \
                          + ref_id + "','" \
                          + table.item(i, 1).text() + "')"
                cursor.execute(sql)
                connection.commit()

def open_label_dialog():
    local_label_dialog.reset()
    # code to display the dialog box for label
    ref_id = str(ui.newReference.property("id"))

    cursor = connection.cursor()

    sql = "SELECT `*` FROM `logault`.`label`"
    cursor.execute(sql)
    result = cursor.fetchall()


    sql = "SELECT * FROM `logault`.`label` WHERE `lab_id` IN" \
          "(SELECT `lab_id` FROM `logault`.`reference_label` WHERE `ref_id`="+ref_id+")"
    cursor.execute(sql)
    ref_result = cursor.fetchall()

    local_label_dialog.dialog.label_table
    for i in result:
        chkBoxItem = QTableWidgetItem(i["tag"])
        chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
        local_label_dialog.checklist.append(QtCore.Qt.Unchecked)
        if (ref_result.__contains__(i)):
            chkBoxItem.setCheckState(QtCore.Qt.Checked)
            local_label_dialog.checklist[len(local_label_dialog.checklist)-1] = QtCore.Qt.Checked
        rowposition = local_label_dialog.dialog.label_table.rowCount()
        local_label_dialog.dialog.label_table.insertRow(rowposition)
        local_label_dialog.dialog.label_table.setItem(rowposition, 0, chkBoxItem)
        local_label_dialog.dialog.label_table.setItem(rowposition, 1, QTableWidgetItem(str(i["lab_id"])))


    local_label_dialog.dialog.label_table.hideColumn(1)#hiding id row
    local_label_dialog.Dialog.show()

    local_label_dialog.rsp = local_label_dialog.Dialog.exec_()  # calling exec so dialog window can stay open and rsp stores which button we pressed

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
    sql = "INSERT INTO `logault`.`label` (`tag`) VALUES ('"+newLabel+"')"
    cursor.execute(sql)
    connection.commit()
    populate_label_table()

def delete_label():
    row = ui.label_table.currentRow()
    lab_id = ui.label_table.item(row, 1).text()
    cursor = connection.cursor()
    sql = "DELETE FROM `logault`.`label` WHERE (`lab_id` = '"+lab_id+"')"
    cursor.execute(sql)
    connection.commit()
    ui.label_table.removeRow(ui.label_table.rowAt(row))
    # populate_label_table()

def delete_category():
    if (ui.category_tree.currentItem() == None or ui.category_tree.currentItem().text(1) == "-1" or ui.category_tree.currentItem().text(1) == "1"):
        return
    cursor = connection.cursor()
    sql = "DELETE FROM `logault`.`category` WHERE (`cat_id` = '"+ui.category_tree.currentItem().text(1)+"')"
    cursor.execute(sql)
    connection.commit()
    populate_tree()

def save_a_reference():
    path = ui.newReference.property('path')
    id = ui.newReference.property("id")
    if(len(ui.bodyBar.toPlainText())==0):
        gen_msg_box(QMessageBox.Warning, "Reference must have a body", "Type in text for reference body to proceed","Error 777: Invalid Reference")
        return
    if(id!="0"):#editing a reference
        ui.newReference.setWindowTitle("Reference Editor")
        cursor = connection.cursor()
        sql = "UPDATE `logault`.`reference` SET `title` = '" + ui.titleBar.toPlainText()+\
              "',`body` = '"+ui.bodyBar.toPlainText()+\
              "',`source` = '"+ui.sourceBar.toPlainText()+\
              "',`timestamp` = '"+time.strftime('%Y-%m-%d %H:%M:%S')+\
              "'  WHERE (`ref_id` = '"+ id + "')"
        # sql = "UPDATE `logault`.`reference` SET `body` = 'kiun zayan kar bano sody faramosh rahon fikr-e-farda na karon or hamma tan gosh rahon.', `title` = 'aaa', `timestamp` = '2019-04-31 13:55:28', `source` = 'shikwa' WHERE (`ref_id` = '2')"
        cursor.execute(sql)
        connection.commit()
        if not(local_label_dialog.outdate_check):
            update_labels(id)
        # ui.newReference.setProperty("id", "0")
    elif(id=="0"):
        if(ui.category_tree.currentItem().text(0)=="Recent"):
            gen_msg_box(QMessageBox.Warning, "Invalid Category", "Choose appropriate category","Error 404: Invalid Category")
            return
        cursor = connection.cursor()
        sql = "INSERT INTO `logault`.`reference` (`body`, `title`, `source`, `file_path`, `cat_id`) VALUES ('"\
              +ui.bodyBar.toPlainText()+"','"\
              +ui.titleBar.toPlainText() + "','"\
              +ui.sourceBar.toPlainText() + "','"\
              +path + "','"\
              +ui.category_tree.currentItem().text(1) + "')"
        # sql = "UPDATE `logault`.`reference` SET `body` = 'kiun zayan kar bano sody faramosh rahon fikr-e-farda na karon or hamma tan gosh rahon.', `title` = 'aaa', `timestamp` = '2019-04-31 13:55:28', `source` = 'shikwa' WHERE (`ref_id` = '2')"
        cursor.execute(sql)
        connection.commit()

        sql = "SELECT MAX(ref_id) AS 'id' FROM `logault`.`reference`"
        cursor.execute(sql)
        result = cursor.fetchone()
        if not(local_label_dialog.outdate_check):
            update_labels(str(result['id']))

        ui.titleBar.clear()
        ui.bodyBar.clear()
        ui.sourceBar.clear()
        print('')
        populate_reference_table('me')
        ui.newReference.setDisabled(True)

def display_referenced_pdf():
    s = ui.sender()
    row = s.currentRow()
    path = s.item(row,5).text()
    print(path)
    if(path!=""):
        subprocess.Popen([r'evince '+path], shell=True)

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

def delete_reference():
    if(ui.reference_table.currentRow()<0):
        return
    cursor = connection.cursor()
    sql = "DELETE FROM `logault`.`reference` WHERE (`ref_id` = '"+ui.reference_table.item(ui.reference_table.currentRow(),4).text()+"')"
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
        sql = "INSERT INTO `logault`.`category` (`title`, `parent_cat`) VALUES ('"+newTitle+"', '"+selected_folder.text(1)+"')"
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
        #code to display the dialog box for referencing a file
        Dialog = QtWidgets.QDialog()
        ui_d = Ui_Dialog()
        ui_d.setupUi(Dialog)
        Dialog.show()

        rsp = Dialog.exec_() #calling exec so dialog window can stay open and rsp stores which button we pressed

        if rsp == QtWidgets.QDialog.Accepted:
            path = open_file_name_dialog()
        else:
            path=""

        ui.newReference.setProperty("path", path)
        ui.newReference.setProperty("id","0")
        ui.newReference.setVisible(True)
        ui.newReference.setDisabled(False)
        ui.titleBar.clear()
        ui.bodyBar.clear()
        ui.sourceBar.clear()
        ui.newReference.setWindowTitle("New Reference")

def open_file_name_dialog():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(ui,"Choose Resource", "","PDF (*.pdf)", options=options)
    if fileName:
        return fileName

def populate_tree():
        # read database
        myroot = find_parent(ui.category_tree.invisibleRootItem(), str(1))
        while(myroot.childCount()):
            myroot.removeChild(myroot.child(0))

        cursor = connection.cursor()
        sql = "SELECT `*` FROM `category` ORDER BY `parent_cat`"
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
        ui.reference_table.setItem(rowposition, 5, QTableWidgetItem(str(i["file_path"])))

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
    local_label_dialog = Local_Label_Dialog()
    sys.exit(app.exec_())
