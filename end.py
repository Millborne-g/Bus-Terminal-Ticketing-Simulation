# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'end.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResultWindow(object):
    def process(self,busTotal_1,busTotal_2,busTotal_3,busTotal_4,busTotal_5,Resultbus_1,Resultbus_2,Resultbus_3,Resultbus_4,Resultbus_5):
        
        #self.setupUi(MainWindow)
        #self.retranslateUi_1()
        self.Totalbus_1= busTotal_1
        
        self.Totalbus_2= busTotal_2
        self.Totalbus_3= busTotal_3
        self.Totalbus_4= busTotal_4
        self.Totalbus_5= busTotal_5
        self.busResult_1 =Resultbus_1
        self.busResult_2 = Resultbus_2
        self.busResult_3 = Resultbus_3
        self.busResult_4 = Resultbus_4
        self.busResult_5 = Resultbus_5
        #self.retranslateUi_1(MainWindow,Resultbus_1,Resultbus_2,Resultbus_3,Resultbus_4,Resultbus_5)
        #
        self.listWidget.addItems(self.busResult_1)
        self.listWidget_2.addItems(self.busResult_2)
        self.listWidget_3.addItems(self.busResult_3)
        self.listWidget_4.addItems(self.busResult_4)
        self.listWidget_5.addItems(self.busResult_5)
        self.BusTot_1.setText('P'+str(self.Totalbus_1))
        self.BusTot_2.setText('P'+str(self.Totalbus_2))
        self.BusTot_3.setText('P'+str(self.Totalbus_3))
        self.BusTot_4.setText('P'+str(self.Totalbus_4))
        self.BusTot_5.setText('P'+str(self.Totalbus_5))
        self.OverAlTotal.setText('P'+str(self.Totalbus_1+self.Totalbus_2+self.Totalbus_3+self.Totalbus_4+self.Totalbus_5))
        
    def setupUi(self, MainWindow):
        self.Totalbus_1= 0
        self.Totalbus_2= 0
        self.Totalbus_3= 0
        self.Totalbus_4= 0
        self.Totalbus_5= 0
        self.busResult_1 = []
        self.busResult_2 = []
        self.busResult_3 = []
        self.busResult_4 = []
        self.busResult_5 = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 151, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(180, 40, 151, 192))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(350, 40, 151, 192))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(520, 40, 151, 192))
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_5 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_5.setGeometry(QtCore.QRect(680, 40, 151, 192))
        self.listWidget_5.setObjectName("listWidget_5")
        self.BusTot_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.BusTot_1.setEnabled(False)
        self.BusTot_1.setGeometry(QtCore.QRect(40, 240, 81, 41))
        self.BusTot_1.setObjectName("BusTot_1")
        self.BusTot_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.BusTot_2.setEnabled(False)
        self.BusTot_2.setGeometry(QtCore.QRect(220, 240, 81, 41))
        self.BusTot_2.setObjectName("BusTot_2")
        self.BusTot_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.BusTot_3.setEnabled(False)
        self.BusTot_3.setGeometry(QtCore.QRect(380, 240, 81, 41))
        self.BusTot_3.setObjectName("BusTot_3")
        self.BusTot_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.BusTot_4.setEnabled(False)
        self.BusTot_4.setGeometry(QtCore.QRect(560, 240, 81, 41))
        self.BusTot_4.setObjectName("BusTot_4")
        self.BusTot_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.BusTot_5.setEnabled(False)
        self.BusTot_5.setGeometry(QtCore.QRect(710, 240, 81, 41))
        self.BusTot_5.setObjectName("BusTot_5")
        self.OverAlTotal = QtWidgets.QTextBrowser(self.centralwidget)
        self.OverAlTotal.setEnabled(False)
        self.OverAlTotal.setGeometry(QtCore.QRect(330, 320, 201, 51))
        self.OverAlTotal.setObjectName("OverAlTotal")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 300, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Try_Again = QtWidgets.QPushButton(self.centralwidget)
        self.Try_Again.setGeometry(QtCore.QRect(400, 380, 75, 23))
        self.Try_Again.setObjectName("Try_Again")
        self.Try_Again.setVisible(False)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 12, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(730, 10, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BusTot_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">A</span></p></body></html>"))
        self.BusTot_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">B</span></p></body></html>"))
        self.BusTot_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">C</span></p></body></html>"))
        self.BusTot_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">D</span></p></body></html>"))
        self.BusTot_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">E</span></p></body></html>"))
        self.OverAlTotal.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">R</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Total Earnings"))
        self.Try_Again.setText(_translate("MainWindow", "Try Again"))
        self.label_2.setText(_translate("MainWindow", "Bus 1"))
        self.label_3.setText(_translate("MainWindow", "Bus 2"))
        self.label_4.setText(_translate("MainWindow", "Bus 3"))
        self.label_5.setText(_translate("MainWindow", "Bus 4"))
        self.label_6.setText(_translate("MainWindow", "Bus 5"))
    def retranslateUi_1(self, MainWindow,A,B,C,D,E):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BusTot_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">A</span></p></body></html>"))
        self.BusTot_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">B</span></p></body></html>"))
        self.BusTot_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">C</span></p></body></html>"))
        self.BusTot_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">D</span></p></body></html>"))
        self.BusTot_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">E</span></p></body></html>"))
        self.OverAlTotal.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">R</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Total Earnings"))
        self.Try_Again.setText(_translate("MainWindow", "Try Again"))
        self.label_2.setText(_translate("MainWindow", "Bus 1"))
        self.label_3.setText(_translate("MainWindow", "Bus 2"))
        self.label_4.setText(_translate("MainWindow", "Bus 3"))
        self.label_5.setText(_translate("MainWindow", "Bus 4"))
        self.label_6.setText(_translate("MainWindow", "Bus 5"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ResultWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
