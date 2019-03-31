from db_handling import connection
from db_handling import connection
import logault

def initialize():
    cursor = connection.cursor()
    sql = "SELECT `*` FROM `category`"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    for i in result:
        if (i["parent_cat"]!=i["cat_id"]):#for root
            #get item from tree with id == i["parent_cat"]
            #row = item.insert_row()
            #row.id = i["cat_id"], row.text = i["title"]

            print()
    model = ui.category_tree.model()


if __name__ == "__main__":
    import sys
    app = logault.QtWidgets.QApplication(sys.argv)
    MainWindow = logault.QtWidgets.QMainWindow()
    ui = logault.Ui_MainWindow()
    ui.setupUi(MainWindow)
    initialize()
    MainWindow.show()
    sys.exit(app.exec_())
