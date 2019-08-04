import sys
from PyQt5.QtWidgets import *
from finalDesign import *
from reddit import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_init_data()
        self.ui.subreddit.returnPressed.connect(self.load_subreddit)

    def set_init_data(self):
        self.load_popular_sub()

    def load_popular_sub(self):
        for post in Reddit.call_posts("popular"):
            self.ui.redditList.addItem(post)

    def load_subreddit(self):
        self.ui.redditList.clear()
        if not self.ui.subreddit.text() == "":
            for post in Reddit.call_posts(self.ui.subreddit.text()):
                self.ui.redditList.addItem(post)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setFixedSize(w.size())
    w.show()
    sys.exit(app.exec_())