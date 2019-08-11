import os
import sys
from PyQt5.QtWidgets import *
from finalDesign import *
from designSmallScreen import *
from reddit import *
from comment_handler import *
import anytree
from anytree.exporter import JsonExporter, DictExporter
import pip

# Used for comment splitting based on resolution
global global_comment_splitter


class MainWindow(QtWidgets.QMainWindow):

    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        # checking screen's dimensions to assign the correct design
        g = QDesktopWidget().availableGeometry()
        if g.width() < 1500 and g.height() < 900:
            global global_comment_splitter
            global_comment_splitter = 40
            self.ui = Ui_MainWindowSmallScreen()
            self.ui.setupUiSmallScreen(self)
        else:
            global_comment_splitter = 90
            self.ui = Ui_MainWindowFinalDesign()
            self.ui.setupUiFinalDesign(self)

        # displaying the /r/popular subreddit by default
        self.set_init_data()
        self.ui.treeComments.setStyleSheet(CommentHandler.get_stylesheet(self))
        # radio button listeners
        self.ui.hotRadioBtn.clicked.connect(self.radio_state)
        self.ui.newRadioBtn.clicked.connect(self.radio_state)
        self.ui.controversialRadioBtn.clicked.connect(self.radio_state)
        self.ui.risingRadioBtn.clicked.connect(self.radio_state)

        self.ui.subreddit.returnPressed.connect(lambda: self.load_subreddit("hot"))
        self.ui.postUrl.setReadOnly(True)
        self.ui.postBody.setReadOnly(True)
        self.ui.postTitle.setReadOnly(True)

        # listener for post from subreddit tab
        self.ui.redditList.itemDoubleClicked.connect(self.clicked)

    # diplaying the /r/popular subreddit by default
    def set_init_data(self):
        global posts
        posts = Reddit.call_posts("popular", "hot")

        counter = 0
        for post in posts:
            counter = counter + 1
            self.ui.redditList.addItem(
                CommentHandler.list_item_format(counter, post.score, post.title, post.url, post.subreddit,
                                                 post.number_of_comments)
            )

    # checking which radio button has been pressed and sort subreddit based on preference
    def radio_state(self):
        if self.ui.hotRadioBtn.isChecked():
            self.load_subreddit("hot")
        elif self.ui.newRadioBtn.isChecked():
            self.load_subreddit("new")
        elif self.ui.controversialRadioBtn.isChecked():
            self.load_subreddit("controversial")
        elif self.ui.risingRadioBtn.isChecked():
            self.load_subreddit("rising")

    def load_subreddit(self, sorting):
        # clear tab with post details and comments
        self.ui.postTitle.setText("Double click on a submission in the second tab `ObjectController.java` ")
        self.ui.postUrl.clear()
        self.ui.postBody.clear()
        self.ui.postSub.clear()
        self.ui.treeComments.clear()
        self.ui.redditList.clear()
        if self.ui.subreddit.text() == "":
            self.ui.subreddit.setText("popular")
        # flag will be used on whether we need to print the subreddit name
        flag = False
        sub_name = ""  # initialized empty because we don't need to print the subreddit name for all cases

        # users seem to type /r/ as well, we need to handle this
        if self.ui.subreddit.text().startswith("/r/") or self.ui.subreddit.text().startswith(
                "r/") or self.ui.subreddit.text().startswith("/"):
            new_name = self.ui.subreddit.text()
            new_name = new_name.replace("/r/", "")
            new_name = new_name.replace("r", "")
            new_name = new_name.replace("/", "")
            self.ui.subreddit.setText(new_name)

        # /r/all is similar with /r/popular, we need the subreddit name as well
        if self.ui.subreddit.text() == "all":
            flag = 1
        elif self.ui.subreddit.text() == "popular":
            flag = 2
        counter = 0;
        global posts
        posts = Reddit.call_posts(self.ui.subreddit.text(), sorting)
        # check if given subreddit exists
        if posts:
            self.ui.messageLabel.setText("")
            # display each post
            for post in posts:
                counter = counter + 1
                # here we determinte if we need to print the subreddit name as well (for popular and all subreddits)
                if flag:
                    sub_name = post.subreddit
                self.ui.redditList.addItem(
                    CommentHandler.list_item_format(counter, post.score, post.title, post.url, sub_name,
                                                     post.number_of_comments)
                )
            if flag == 1:
                self.ui.subredditTitle.setText("/All")
            elif flag == 2:
                self.ui.subredditTitle.setText("/Popular")
            else:
                self.ui.subredditTitle.setText(post.subreddit)
            self.ui.progressBar.setValue(24)
        else:
            self.ui.messageLabel.setText("Wrong subreddit name!")
            self.ui.subredditTitle.setText("Subreddit not found! ")

    # listener for post from subreddit tab
    def clicked(self, item):
        self.ui.progressBar.setValue(24)
        # Getting the index from the counter
        split_item_info = item.text().split(" ")
        index = int(split_item_info[0]) - 1
        post = posts[index]
        self.ui.postTitle.setText(post.title)
        self.ui.postBody.setText(post.body)
        self.ui.postUrl.setText(post.url)
        self.ui.postSub.setText(post.subreddit)
        # create comments parents and children
        self.ui.treeComments.clear()  # clear previous comments
        comments_tree = Reddit.load_comments(post.id)
        # for pre, fill, node in RenderTree(comments_tree):
        #     print("%s%s" % (pre, node.name))
        exporter = JsonExporter(indent=1, sort_keys=False)
        dict_exporter = DictExporter()
        dict_comments = dict_exporter.export(comments_tree)
        self.ui.treeComments.clear()
        self.ui.treeComments.addTopLevelItem(self.iterate_dict(dict_comments, QTreeWidgetItem(["EMPTY"])))
        self.ui.progressBar.setValue(100)

    def iterate_dict(self, dict_comments, list_item):
        for p_id, p_info in dict_comments.items():
            if isinstance(p_info, list):
                l_child = QTreeWidgetItem(["EMPTY_CHILD"])
                # Loop list with children -> dict
                for child_dict in p_info:
                    for child_id, child_info in child_dict.items():
                        if isinstance(child_info, list):
                            # Loop list with children -> dict
                            counter = 5
                            for grand_dict in child_info:
                                if counter > 0:
                                    l_child.addChild(self.iterate_dict(grand_dict, l_child))
                                    counter = counter - 1
                        else:
                            # add new line every 100 characters
                            if len(child_info) > global_comment_splitter:
                                child_info_split = child_info.split()
                                child_final = ""
                                tmp_str = ""
                                counter = 0
                                for inner in child_info_split:
                                    if counter <= global_comment_splitter:
                                        child_final = child_final + " " + inner
                                        tmp_str = tmp_str + " " + inner
                                        counter = len(tmp_str)
                                    else:
                                        counter = 0
                                        child_final = child_final + " " + inner
                                        tmp_str = ""
                                        child_final = child_final + "\n"
                                child_info = child_final
                            # adding new line so the upvotes will be on top
                            child_info = child_info[:child_info.find("|")] + '\n' + child_info[child_info.find("|"):]
                            child_info = child_info.replace("|", "", 1)
                            child_info = child_info.replace("-/u/", "\n\n  -/u/", 1)
                            l_child = QTreeWidgetItem([child_info])
                            list_item.addChild(l_child)

            else:
                if len(p_info) > global_comment_splitter:
                    p_info_split = p_info.split()
                    p_final = ""
                    tmp_str = ""
                    counter = 0
                    for inner in p_info_split:
                        if counter <= global_comment_splitter:
                            p_final = p_final + " " + inner
                            tmp_str = tmp_str + " " + inner
                            counter = len(tmp_str)
                        else:
                            counter = 0
                            p_final = p_final + " " + inner
                            tmp_str = ""
                            p_final = p_final + "\n"
                    p_info = p_final
                # adding new line so the upvotes will be on top
                if p_info is not "Comments":
                    p_info = p_info[:p_info.find("|")] + '\n' + p_info[p_info.find("|"):]
                    p_info = p_info.replace("|", "", 1)
                    p_info = p_info.replace("-/u/", "\n\n  -/u/", 1)
                list_item = QTreeWidgetItem([p_info])

        return list_item


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.setMaximumSize(w.size().width(), w.size().height())
    # w.setFixedSize(w.size())
    print(QDesktopWidget().availableGeometry())
    g = QDesktopWidget().availableGeometry()
    w.move(g.center().x() - w.width() / 2, g.center().y() - w.height() / 2)
    sys.exit(app.exec_())
