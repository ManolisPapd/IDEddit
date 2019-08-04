# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalDesign.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1298, 897)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("design/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setEnabled(True)
        self.saveBtn.setGeometry(QtCore.QRect(3, 8, 21, 33))
        self.saveBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("design/saveBtn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn.setIcon(icon1)
        self.saveBtn.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn.setFlat(True)
        self.saveBtn.setObjectName("saveBtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 0, 1341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 30, 1341, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 830, 1341, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(350, 37, 20, 800))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 60, 360, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.saveBtn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_4.setEnabled(True)
        self.saveBtn_4.setGeometry(QtCore.QRect(-1, 40, 101, 21))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("iconfinder_folder-green_285644.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_4.setIcon(icon2)
        self.saveBtn_4.setIconSize(QtCore.QSize(20, 20))
        self.saveBtn_4.setFlat(True)
        self.saveBtn_4.setObjectName("saveBtn_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 70, 371, 766))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("design/project.png"))
        self.label.setObjectName("label")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(20, 7, 20, 31))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.saveBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_2.setEnabled(True)
        self.saveBtn_2.setGeometry(QtCore.QRect(40, 8, 21, 33))
        self.saveBtn_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("design/iconfinder_folder_118926.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_2.setIcon(icon3)
        self.saveBtn_2.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_2.setFlat(True)
        self.saveBtn_2.setObjectName("saveBtn_2")
        self.saveBtn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_3.setEnabled(True)
        self.saveBtn_3.setGeometry(QtCore.QRect(74, 8, 21, 33))
        self.saveBtn_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("design/iconfinder_5_-_Refresh_1815572.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_3.setIcon(icon4)
        self.saveBtn_3.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_3.setFlat(True)
        self.saveBtn_3.setObjectName("saveBtn_3")
        self.saveBtn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_5.setEnabled(True)
        self.saveBtn_5.setGeometry(QtCore.QRect(108, 8, 21, 33))
        self.saveBtn_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("design/iconfinder_cardboard-box_307356.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_5.setIcon(icon5)
        self.saveBtn_5.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_5.setFlat(True)
        self.saveBtn_5.setObjectName("saveBtn_5")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(130, 7, 20, 31))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.saveBtn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_6.setEnabled(True)
        self.saveBtn_6.setGeometry(QtCore.QRect(150, 8, 21, 33))
        self.saveBtn_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("design/iconfinder_time_setting_management_clock_4732030.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_6.setIcon(icon6)
        self.saveBtn_6.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_6.setFlat(True)
        self.saveBtn_6.setObjectName("saveBtn_6")
        self.saveBtn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_7.setEnabled(True)
        self.saveBtn_7.setGeometry(QtCore.QRect(178, 8, 31, 33))
        self.saveBtn_7.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("design/iconfinder_Vector-icons_86_1041638.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_7.setIcon(icon7)
        self.saveBtn_7.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_7.setFlat(True)
        self.saveBtn_7.setObjectName("saveBtn_7")
        self.saveBtn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_8.setEnabled(True)
        self.saveBtn_8.setGeometry(QtCore.QRect(218, 8, 21, 33))
        self.saveBtn_8.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("design/iconfinder_bug_383173.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_8.setIcon(icon8)
        self.saveBtn_8.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_8.setFlat(True)
        self.saveBtn_8.setObjectName("saveBtn_8")
        self.saveBtn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_9.setEnabled(True)
        self.saveBtn_9.setGeometry(QtCore.QRect(252, 7, 31, 33))
        self.saveBtn_9.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("design/iconfinder_play_green_controls_61655.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_9.setIcon(icon9)
        self.saveBtn_9.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_9.setFlat(True)
        self.saveBtn_9.setObjectName("saveBtn_9")
        self.saveBtn_10 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_10.setEnabled(True)
        self.saveBtn_10.setGeometry(QtCore.QRect(293, 8, 21, 33))
        self.saveBtn_10.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("design/iconfinder_stop-red_60208.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_10.setIcon(icon10)
        self.saveBtn_10.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_10.setFlat(True)
        self.saveBtn_10.setObjectName("saveBtn_10")
        self.saveBtn_11 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_11.setEnabled(True)
        self.saveBtn_11.setGeometry(QtCore.QRect(326, 8, 21, 33))
        self.saveBtn_11.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("design/iconfinder_icon-pause_211871.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_11.setIcon(icon11)
        self.saveBtn_11.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_11.setFlat(True)
        self.saveBtn_11.setObjectName("saveBtn_11")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(350, 7, 20, 31))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.saveBtn_12 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_12.setEnabled(True)
        self.saveBtn_12.setGeometry(QtCore.QRect(370, 8, 31, 33))
        self.saveBtn_12.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("design/iconfinder_back_126585.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_12.setIcon(icon12)
        self.saveBtn_12.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_12.setFlat(True)
        self.saveBtn_12.setObjectName("saveBtn_12")
        self.saveBtn_13 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_13.setEnabled(True)
        self.saveBtn_13.setGeometry(QtCore.QRect(410, 8, 31, 33))
        self.saveBtn_13.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("design/iconfinder_forward_126569.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_13.setIcon(icon13)
        self.saveBtn_13.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_13.setFlat(True)
        self.saveBtn_13.setObjectName("saveBtn_13")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(440, 7, 20, 31))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.saveBtn_14 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_14.setEnabled(True)
        self.saveBtn_14.setGeometry(QtCore.QRect(460, 8, 31, 33))
        self.saveBtn_14.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("design/iconfinder_52_Cloud_Sync_183465.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_14.setIcon(icon14)
        self.saveBtn_14.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_14.setFlat(True)
        self.saveBtn_14.setObjectName("saveBtn_14")
        self.saveBtn_15 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_15.setEnabled(True)
        self.saveBtn_15.setGeometry(QtCore.QRect(497, 8, 31, 33))
        self.saveBtn_15.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("design/iconfinder_problem-solving_2799202.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_15.setIcon(icon15)
        self.saveBtn_15.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_15.setFlat(True)
        self.saveBtn_15.setObjectName("saveBtn_15")
        self.saveBtn_16 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_16.setEnabled(True)
        self.saveBtn_16.setGeometry(QtCore.QRect(534, 8, 31, 33))
        self.saveBtn_16.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("design/iconfinder_606_Code_edit_editor_language_program_3968803.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_16.setIcon(icon16)
        self.saveBtn_16.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_16.setFlat(True)
        self.saveBtn_16.setObjectName("saveBtn_16")
        self.saveBtn_17 = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn_17.setEnabled(True)
        self.saveBtn_17.setGeometry(QtCore.QRect(1304, 7, 31, 32))
        self.saveBtn_17.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("design/iconfinder_problem_1328787.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn_17.setIcon(icon17)
        self.saveBtn_17.setIconSize(QtCore.QSize(25, 25))
        self.saveBtn_17.setFlat(True)
        self.saveBtn_17.setObjectName("saveBtn_17")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(1290, 7, 20, 31))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 840, 1201, 16))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(1210, 840, 118, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(402, 37, 901, 801))
        self.tabWidget.setObjectName("tabWidget")
        self.dummyTab = QtWidgets.QWidget()
        self.dummyTab.setObjectName("dummyTab")
        self.textEdit = QtWidgets.QTextEdit(self.dummyTab)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 899, 780))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.dummyTab, "")
        self.redditTab = QtWidgets.QWidget()
        self.redditTab.setObjectName("redditTab")
        self.redditList = QtWidgets.QListWidget(self.redditTab)
        self.redditList.setGeometry(QtCore.QRect(0, 19, 896, 757))
        self.redditList.setObjectName("redditList")
        self.subredditTitle = QtWidgets.QLabel(self.redditTab)
        self.subredditTitle.setGeometry(QtCore.QRect(3, 0, 571, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.subredditTitle.setFont(font)
        self.subredditTitle.setObjectName("subredditTitle")
        self.tabWidget.addTab(self.redditTab, "")
        self.postDetails = QtWidgets.QWidget()
        self.postDetails.setObjectName("postDetails")
        self.postTitle = QtWidgets.QTextEdit(self.postDetails)
        self.postTitle.setGeometry(QtCore.QRect(0, 0, 896, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.postTitle.setFont(font)
        self.postTitle.setObjectName("postTitle")
        self.treeWidget = QtWidgets.QTreeWidget(self.postDetails)
        self.treeWidget.setGeometry(QtCore.QRect(0, 210, 901, 571))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.postSub = QtWidgets.QLabel(self.postDetails)
        self.postSub.setGeometry(QtCore.QRect(608, 190, 281, 20))
        self.postSub.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.postSub.setObjectName("postSub")
        self.postUrl = QtWidgets.QLineEdit(self.postDetails)
        self.postUrl.setEnabled(True)
        self.postUrl.setGeometry(QtCore.QRect(0, 190, 571, 20))
        self.postUrl.setMouseTracking(True)
        self.postUrl.setTabletTracking(False)
        self.postUrl.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.postUrl.setObjectName("postUrl")
        self.postBody = QtWidgets.QTextEdit(self.postDetails)
        self.postBody.setGeometry(QtCore.QRect(0, 21, 895, 170))
        self.postBody.setObjectName("postBody")
        self.postBody.raise_()
        self.postTitle.raise_()
        self.treeWidget.raise_()
        self.postSub.raise_()
        self.postUrl.raise_()
        self.tabWidget.addTab(self.postDetails, "")
        self.subreddit = QtWidgets.QLineEdit(self.centralwidget)
        self.subreddit.setGeometry(QtCore.QRect(795, 11, 241, 21))
        self.subreddit.setText("")
        self.subreddit.setObjectName("subreddit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 14, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setGeometry(QtCore.QRect(1060, 10, 131, 21))
        self.messageLabel.setText("")
        self.messageLabel.setObjectName("messageLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1298, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuNaviage = QtWidgets.QMenu(self.menubar)
        self.menuNaviage.setObjectName("menuNaviage")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        self.menuGit = QtWidgets.QMenu(self.menubar)
        self.menuGit.setObjectName("menuGit")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionClose_2 = QtWidgets.QAction(MainWindow)
        self.actionClose_2.setObjectName("actionClose_2")
        self.actionExit_program = QtWidgets.QAction(MainWindow)
        self.actionExit_program.setObjectName("actionExit_program")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionEncode = QtWidgets.QAction(MainWindow)
        self.actionEncode.setObjectName("actionEncode")
        self.actionToggle = QtWidgets.QAction(MainWindow)
        self.actionToggle.setObjectName("actionToggle")
        self.actionMapping = QtWidgets.QAction(MainWindow)
        self.actionMapping.setObjectName("actionMapping")
        self.menuFile.addAction(self.actionTest)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_program)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEncode)
        self.menuEdit.addAction(self.actionToggle)
        self.menuEdit.addAction(self.actionMapping)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuNaviage.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuGit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ObjectMapper - IDEddit 1.0"))
        self.saveBtn_4.setText(_translate("MainWindow", "ObjectMapper"))
        self.label_2.setText(_translate("MainWindow", "Plugins (7) need update: IDEddit ready to update. (21 minutes ago)                                                                                                                                                                                                                                           47:13   CRLF   UTF-8   maven   "))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">package</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.boot.admin;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> java.lang.management.ManagementFactory;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> javax.management.MBeanServer;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> javax.management.MalformedObjectNameException;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> javax.management.ObjectName;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.apache.commons.logging.Log;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.apache.commons.logging.LogFactory;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.beans.BeansException;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.beans.factory.DisposableBean;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.beans.factory.InitializingBean;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.boot.context.event.ApplicationReadyEvent;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.boot.web.context.WebServerInitializedEvent;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.context.ApplicationContext;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.context.ApplicationContextAware;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.context.ApplicationEvent;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.context.ConfigurableApplicationContext;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.context.EnvironmentAware;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.context.event.GenericApplicationListener;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.core.Ordered;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.core.ResolvableType;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.core.env.Environment;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.core.env.StandardEnvironment;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">import</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> org.springframework.util.Assert;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#d1d1d1;\">/**</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#d1d1d1;\"> * Register a {@link SpringApplicationAdminMXBean} implementation to the platform</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#d1d1d1;\"> * {@link MBeanServer}.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#d1d1d1;\"> *</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#d1d1d1;\"> * @author Stephane Nicoll</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#d1d1d1;\"> * @author Andy Wilkinson</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#d1d1d1;\"> * @since 1.3.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#d1d1d1;\"> */</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public class</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> SpringApplicationAdminMXBeanRegistrar </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">implements</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> ApplicationContextAware, GenericApplicationListener,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        EnvironmentAware, InitializingBean, DisposableBean {</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">private</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">static</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">final</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">Log</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> logger = LogFactory.getLog(SpringApplicationAdmin.</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">class</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">);</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">private</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> ConfigurableApplicationContext applicationContext;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">private</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> Environment environment = new StandardEnvironment();</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">private</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">final</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> ObjectName objectName;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">private</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">boolean</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> ready = false;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">private</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">boolean</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> embeddedWebApplication = false;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#ffaa7f;\">private</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> SpringApplicationAdminMXBeanRegistrar(String name) throws MalformedObjectNameException {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        this.objectName = new ObjectName(name);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> void setApplicationContext(ApplicationContext applicationContext) throws BeansException {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        Assert.state(applicationContext instanceof ConfigurableApplicationContext,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">                &quot;ApplicationContext does not implement ConfigurableApplicationContext&quot;);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        this.applicationContext = (ConfigurableApplicationContext) applicationContext;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> void setEnvironment(Environment environment) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        this.environment = environment;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> boolean supportsEventType(ResolvableType eventType) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        Class&lt;?&gt; type = eventType.getRawClass();</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        if (type == null) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            return false;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        return ApplicationReadyEvent.class.isAssignableFrom(type)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">                || WebServerInitializedEvent.class.isAssignableFrom(type);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> boolean supportsSourceType(Class&lt;?&gt; sourceType) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        return true;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> void onApplicationEvent(ApplicationEvent event) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        if (event instanceof ApplicationReadyEvent) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            onApplicationReadyEvent((ApplicationReadyEvent) event);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        if (event instanceof WebServerInitializedEvent) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            onWebServerInitializedEvent((WebServerInitializedEvent) event);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> int getOrder() {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        return Ordered.HIGHEST_PRECEDENCE;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    void onApplicationReadyEvent(ApplicationReadyEvent event) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        if (this.applicationContext.equals(event.getApplicationContext())) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            this.ready = true;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    void onWebServerInitializedEvent(WebServerInitializedEvent event) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        if (this.applicationContext.equals(event.getApplicationContext())) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            this.embeddedWebApplication = true;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> void afterPropertiesSet() throws Exception {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        MBeanServer server = ManagementFactory.getPlatformMBeanServer();</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        server.registerMBean(new SpringApplicationAdmin(), this.objectName);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        if (logger.isDebugEnabled()) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            logger.debug(&quot;Application Admin MBean registered with name \'&quot; + this.objectName + &quot;\'&quot;);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> void destroy() throws Exception {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        ManagementFactory.getPlatformMBeanServer().unregisterMBean(this.objectName);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">private class</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> SpringApplicationAdmin </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">implements</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> SpringApplicationAdminMXBean {</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> boolean isReady() {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            return SpringApplicationAdminMXBeanRegistrar.this.ready;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> boolean isEmbeddedWebApplication() {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            return SpringApplicationAdminMXBeanRegistrar.this.embeddedWebApplication;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> String getProperty(String key) {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            return SpringApplicationAdminMXBeanRegistrar.this.environment.getProperty(key);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#0000ff;\">@Override</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        </span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#00007f;\">public</span><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"> void shutdown() {</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            logger.info(&quot;Application shutdown requested.&quot;);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">            SpringApplicationAdminMXBeanRegistrar.this.applicationContext.close();</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">        }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">    }</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo,Consolas,Liberation Mono,Menlo,Courier,monospace\'; font-size:8pt; color:#000000;\">}</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dummyTab), _translate("MainWindow", "WebSecurityConfig.java"))
        self.subredditTitle.setText(_translate("MainWindow", "/Popular"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.redditTab), _translate("MainWindow", "ObjectController.java"))
        self.postTitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Double click on a submission in the second tab `ObjectController.java` </p></body></html>"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Comments"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Node1"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Node1_1"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(6).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(7).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(8).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(9).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(10).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(11).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(12).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(13).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(14).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(15).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(16).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(17).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(18).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(19).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(20).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(21).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(22).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(23).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(24).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(25).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(26).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(27).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(28).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(29).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(30).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(31).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(32).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(33).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(34).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(35).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(36).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(37).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(38).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(39).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(40).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(41).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(42).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(43).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(44).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(45).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(46).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(47).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(48).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(49).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(50).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(51).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(52).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(53).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(54).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(55).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(56).setText(0, _translate("MainWindow", "Node2"))
        self.treeWidget.topLevelItem(56).child(0).setText(0, _translate("MainWindow", "Node2_1"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.postSub.setText(_translate("MainWindow", "/subreddit"))
        self.postUrl.setText(_translate("MainWindow", "www.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/urlwww.url.com/url/api/url"))
        self.postBody.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">postBody                                                                                                                                                                                                        </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.postDetails), _translate("MainWindow", "ObjectService.java"))
        self.subreddit.setPlaceholderText(_translate("MainWindow", "subreddit"))
        self.label_3.setText(_translate("MainWindow", "Navigate:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuNaviage.setTitle(_translate("MainWindow", "Navigate"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuGit.setTitle(_translate("MainWindow", "Git"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionTest.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionClose_2.setText(_translate("MainWindow", "Close"))
        self.actionExit_program.setText(_translate("MainWindow", "Exit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionPaste.setText(_translate("MainWindow", "Delete"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionEncode.setText(_translate("MainWindow", "Encode"))
        self.actionToggle.setText(_translate("MainWindow", "Toggle"))
        self.actionMapping.setText(_translate("MainWindow", "Mapping"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

