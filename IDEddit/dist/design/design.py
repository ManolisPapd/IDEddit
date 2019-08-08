# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(982, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.convertCur = QtWidgets.QPushButton(self.centralwidget)
        self.convertCur.setGeometry(QtCore.QRect(390, 80, 141, 51))
        self.convertCur.setObjectName("convertCur")
        self.euro = QtWidgets.QLineEdit(self.centralwidget)
        self.euro.setGeometry(QtCore.QRect(50, 90, 241, 31))
        self.euro.setObjectName("euro")
        self.dollar = QtWidgets.QLineEdit(self.centralwidget)
        self.dollar.setEnabled(True)
        self.dollar.setGeometry(QtCore.QRect(590, 90, 241, 31))
        self.dollar.setObjectName("dollar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 0, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Analecta")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.newItem = QtWidgets.QLineEdit(self.centralwidget)
        self.newItem.setGeometry(QtCore.QRect(60, 200, 341, 31))
        self.newItem.setObjectName("newItem")
        self.addItem = QtWidgets.QPushButton(self.centralwidget)
        self.addItem.setGeometry(QtCore.QRect(430, 190, 141, 51))
        self.addItem.setObjectName("addItem")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(70, 240, 591, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 581, 471))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 581, 471))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
        self.menubar.setObjectName("menubar")
        self.menudasdas = QtWidgets.QMenu(self.menubar)
        self.menudasdas.setObjectName("menudasdas")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menudasdas.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IDEddit"))
        self.convertCur.setText(_translate("MainWindow", "->"))
        self.label.setText(_translate("MainWindow", "Converter"))
        self.addItem.setText(_translate("MainWindow", "->"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "das asdas \n"
"\n"
"as dasd"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menudasdas.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

