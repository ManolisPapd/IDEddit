import sys
from PyQt5.QtWidgets import *
from finalDesign import *
from reddit import *
from anytree import Node, RenderTree
from anytree.exporter import JsonExporter
import json

def list_item_format(counter, score, title, url, subreddit, number):
    list_item = (format(counter) + " | " +
                 format(score) + "\t" +
                 title + "\t" + subreddit + "\t" + format(number) + " comments" + "\n\n\t" +
                 url + "\n\n")
    return list_item


class MainWindow(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_init_data()
        self.ui.subreddit.returnPressed.connect(self.load_subreddit)
        self.ui.postUrl.setReadOnly(True)
        self.ui.postBody.setReadOnly(True)
        self.ui.postTitle.setReadOnly(True)
        self.ui.redditList.itemDoubleClicked.connect(self.clicked)

    def set_init_data(self):
        self.load_popular_sub()

    def load_popular_sub(self):
        global posts
        posts = Reddit.call_posts("testingground4bots")

        counter = 0
        for post in posts:
            counter = counter + 1
            self.ui.redditList.addItem(
                list_item_format(counter, post.score, post.title, post.url, post.subreddit,post.number_of_comments)
            )

    def load_subreddit(self):
        self.ui.redditList.clear()
        if not self.ui.subreddit.text() == "":
            #flag will be used on whether we need to print the subreddit name
            flag = False
            sub_name = ""
            # /r/all is similar with /r/popular, we need the subreddit name as well
            if self.ui.subreddit.text() == "all":
                flag = 1
            elif self.ui.subreddit.text() == "popular":
                flag = 2
            counter = 0;
            global posts
            posts = Reddit.call_posts(self.ui.subreddit.text())
            # check if given subreddit exists
            if posts:
                self.ui.messageLabel.setText("")
                for post in posts:
                    counter = counter + 1
                    if flag:
                        sub_name = post.subreddit
                    self.ui.redditList.addItem(
                        list_item_format(counter, post.score, post.title, post.url, sub_name, post.number_of_comments)
                    )
                if flag == 1:
                    self.ui.subredditTitle.setText("/All")
                elif flag == 2:
                    self.ui.subredditTitle.setText("/Popular")
                else:
                    self.ui.subredditTitle.setText(post.subreddit)
            else:
                self.ui.messageLabel.setText("Wrong subreddit name!")
                self.ui.subredditTitle.setText("Subreddit not found! ")
            self.ui.subreddit.setText("")

    def clicked(self, item):
        #Getting the index from the counter
        splitted_item_info = item.text().split(" ")
        index = int(splitted_item_info[0]) - 1
        post = posts[index]
        self.ui.postTitle.setText(post.title)
        self.ui.postBody.setText(post.body)
        self.ui.postUrl.setText(post.url)
        self.ui.postSub.setText(post.subreddit)

        #create comments parents and children
        self.ui.treeComments.clear() #clear previous comments
        commentsTree = Reddit.load_comments(post.id)
        for pre, fill, node in RenderTree(commentsTree):
            print("%s%s" % (pre, node.name))
        exporter = JsonExporter(indent=1, sort_keys=False)
        print(exporter.export(commentsTree))

        # Comments = ({
        #     'Comment1': {
        #         'Reply11' : {('Reply111')},
        #         'Reply12': ('Reply121')},
        #     'Comment2': ('Reply21', 'Reply22')
        # })
        # for key, value in Comments.items():
        #     commentItem = QTreeWidgetItem(self.ui.treeComments, [key])
        #     for val in value:
        #         QTreeWidgetItem(commentItem, [val])
        #     self.ui.treeComments.addTopLevelItem(commentItem)

        l = QTreeWidgetItem(["String A"])
        for i in range(3):
            l_child = QTreeWidgetItem(["Child A" + str(i)])
            for j in range(3):
                l_grand = QTreeWidgetItem(["Child B" + str(i)])
                l_child.addChild(l_grand)
            l.addChild(l_child)
        self.ui.treeComments.addTopLevelItem(l)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setFixedSize(w.size())
    w.show()
    sys.exit(app.exec_())
