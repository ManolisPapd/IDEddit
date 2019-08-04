import sys
from PyQt5.QtWidgets import *
from design import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_init_data()

    def set_init_data(self):
        self.ui.euro.setPlaceholderText("€")
        self.ui.dollar.setPlaceholderText("$")
        self.ui.convertCur.clicked.connect(self.convert)
        self.ui.euro.returnPressed.connect(self.convert)
        self.ui.dollar.setReadOnly(True)
        self.ui.newItem.setFocus(True)
        self.ui.addItem.clicked.connect(self.add_item_to_list)
        self.ui.listWidget.itemDoubleClicked.connect(self.clicked)

    def convert(self):
        print("mymath called!")
        self.ui.dollar.setText(str(float(self.ui.euro.text()) * 1.23))

    def add_item_to_list(self):
        if not self.ui.newItem.text() == "":
            self.ui.listWidget.addItem(self.ui.newItem.text())
            self.ui.listWidget.addItem("Test\n\t\ttest\n\t\ttest")
            self.ui.newItem.setText("")

    def clicked(self, item):
        print(item.text())

    def loadFile(self):
        print("FILE LOADED");


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setFixedSize(w.size())
    w.show()
    sys.exit(app.exec_())