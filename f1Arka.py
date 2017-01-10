# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f1Arka.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from main import sinif

from PyQt5 import QtCore, QtGui, QtWidgets

import f1ArkaInfo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1338, 1080)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(1920, 1080))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1318, 1007))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.orgun_ders = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.orgun_ders.setMaximumSize(QtCore.QSize(1250, 363))
        self.orgun_ders.setObjectName("orgun_ders")
        self.orgun_ders.setColumnCount(19)
        self.orgun_ders.setRowCount(0)
        self.gridLayout_2.addWidget(self.orgun_ders, 0, 1, 1, 4)
        self.ogrenci_ismi = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.ogrenci_ismi.setMaximumSize(QtCore.QSize(800, 300))
        self.ogrenci_ismi.setObjectName("ogrenci_ismi")
        self.ogrenci_ismi.setColumnCount(6)
        self.ogrenci_ismi.setRowCount(0)
        self.gridLayout_2.addWidget(self.ogrenci_ismi, 5, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMaximumSize(QtCore.QSize(400, 16))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 1, 1, 1)
        self.lbl_orgun = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_orgun.setMaximumSize(QtCore.QSize(50, 363))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_orgun.setFont(font)
        self.lbl_orgun.setObjectName("lbl_orgun")
        self.gridLayout_2.addWidget(self.lbl_orgun, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMaximumSize(QtCore.QSize(50, 363))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.sinav_tarihi = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.sinav_tarihi.setMaximumSize(QtCore.QSize(400, 300))
        self.sinav_tarihi.setObjectName("sinav_tarihi")
        self.sinav_tarihi.setColumnCount(6)
        self.sinav_tarihi.setRowCount(0)
        self.gridLayout_2.addWidget(self.sinav_tarihi, 5, 1, 1, 1)
        self.ikinci_ders = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.ikinci_ders.setMaximumSize(QtCore.QSize(1250, 363))
        self.ikinci_ders.setObjectName("ikinci_ders")
        self.ikinci_ders.setColumnCount(19)
        self.ikinci_ders.setRowCount(0)
        self.gridLayout_2.addWidget(self.ikinci_ders, 1, 1, 1, 4)

        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 5, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1338, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename()
        sinifa = sinif()
        htmlList = sinifa.getHtmlList(filename)
        self.setOrgunColoumWidth()
        self.setIkinciColoumWidth()
        self.setOgrenciColoumWidth()
        self.setSinavColoumWidth()
        self.setTitles()
        self.insertRows()
        self.setItems()
        self.fillRows(htmlList)
        MainWindow.setStatusBar(self.statusBar)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sınav Tarihleri"))
        self.lbl_orgun.setText(_translate("MainWindow",
                                          "<html><head/><body><p>ÖR</p><p>GÜN</p><p>ÖĞ</p><p>RE</p><p>TİM</p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p>İKİ</p><p>NCi</p><p>ÖĞ</p><p>RE</p><p>TİM</p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "OKUYUNUZ"))

    def setOrgunColoumWidth(self):
        self.orgun_ders.setColumnWidth(0, 34)
        self.orgun_ders.setColumnWidth(2, 20)
        self.orgun_ders.setColumnWidth(3, 20)
        self.orgun_ders.setColumnWidth(5, 20)
        self.orgun_ders.setColumnWidth(6, 20)
        self.orgun_ders.setColumnWidth(8, 20)
        self.orgun_ders.setColumnWidth(9, 20)
        self.orgun_ders.setColumnWidth(11, 20)
        self.orgun_ders.setColumnWidth(12, 20)
        self.orgun_ders.setColumnWidth(14, 20)
        self.orgun_ders.setColumnWidth(15, 20)
        self.orgun_ders.setColumnWidth(17, 20)
        self.orgun_ders.setColumnWidth(18, 20)
        self.orgun_ders.setColumnWidth(1, 147)
        self.orgun_ders.setColumnWidth(4, 147)
        self.orgun_ders.setColumnWidth(7, 147)
        self.orgun_ders.setColumnWidth(10, 147)
        self.orgun_ders.setColumnWidth(13, 147)
        self.orgun_ders.setColumnWidth(16, 147)

    def setIkinciColoumWidth(self):
        self.ikinci_ders.setColumnWidth(0, 34)
        self.ikinci_ders.setColumnWidth(2, 20)
        self.ikinci_ders.setColumnWidth(3, 20)
        self.ikinci_ders.setColumnWidth(5, 20)
        self.ikinci_ders.setColumnWidth(6, 20)
        self.ikinci_ders.setColumnWidth(8, 20)
        self.ikinci_ders.setColumnWidth(9, 20)
        self.ikinci_ders.setColumnWidth(11, 20)
        self.ikinci_ders.setColumnWidth(12, 20)
        self.ikinci_ders.setColumnWidth(14, 20)
        self.ikinci_ders.setColumnWidth(15, 20)
        self.ikinci_ders.setColumnWidth(17, 20)
        self.ikinci_ders.setColumnWidth(18, 20)
        self.ikinci_ders.setColumnWidth(1, 147)
        self.ikinci_ders.setColumnWidth(4, 147)
        self.ikinci_ders.setColumnWidth(7, 147)
        self.ikinci_ders.setColumnWidth(10, 147)
        self.ikinci_ders.setColumnWidth(13, 147)
        self.ikinci_ders.setColumnWidth(16, 147)

    def setOgrenciColoumWidth(self):
        self.ogrenci_ismi.setColumnWidth(0, 248)
        self.ogrenci_ismi.setColumnWidth(1, 150)
        self.ogrenci_ismi.setColumnWidth(2, 120)
        self.ogrenci_ismi.setColumnWidth(3, 50)
        self.ogrenci_ismi.setColumnWidth(4, 120)
        self.ogrenci_ismi.setColumnWidth(5, 6)

    def setSinavColoumWidth(self):
        self.sinav_tarihi.setColumnCount(6)
        self.sinav_tarihi.setColumnWidth(0, 30)
        self.sinav_tarihi.setColumnWidth(1, 30)
        self.sinav_tarihi.setColumnWidth(2, 160)
        self.sinav_tarihi.setColumnWidth(3, 30)
        self.sinav_tarihi.setColumnWidth(4, 50)
        self.sinav_tarihi.setColumnWidth(5, 50)

    def setTitles(self):
        self.orgun_ders.setHorizontalHeaderLabels(
            ["DER", "PAZARTESİ", "[1]", "[2]", "SALI", "[1]", "[2]", "ÇARŞAMBA", "[1]", "[2]", "PERŞEMBE", "[1]", "[2]",
             "CUMA", "[1]", "[2]", "CUMARTESİ", "[1]", "[2]"])
        self.ikinci_ders.setHorizontalHeaderLabels(
            ["DER", "PAZARTESİ", "[1]", "[2]", "SALI", "[1]", "[2]", "ÇARŞAMBA", "[1]", "[2]", "PERŞEMBE", "[1]", "[2]",
             "CUMA", "[1]", "[2]", "CUMARTESİ", "[1]", "[2]"])
        self.sinav_tarihi.setHorizontalHeaderLabels(["SIRA", "SIRA", "DERSLERİN ADI", "", "1.VİZE", "2.VİZE", "2"])
        self.ogrenci_ismi.setHorizontalHeaderLabels(
            ["ÖĞRENCİNİN ADI SOYADI", "BÖLÜMÜ", "BAŞLAMA YILI", "TEZ", "PROJE", "SEMİNER"])

    def insertRows(self):
        self.orgun_ders.insertRow(0)
        self.orgun_ders.insertRow(1)
        self.orgun_ders.insertRow(2)
        self.orgun_ders.insertRow(3)
        self.orgun_ders.insertRow(4)
        self.orgun_ders.insertRow(5)
        self.orgun_ders.insertRow(6)
        self.orgun_ders.insertRow(7)
        self.orgun_ders.insertRow(8)
        self.orgun_ders.insertRow(9)

        self.ikinci_ders.insertRow(0)
        self.ikinci_ders.insertRow(1)
        self.ikinci_ders.insertRow(2)
        self.ikinci_ders.insertRow(3)
        self.ikinci_ders.insertRow(4)
        self.ikinci_ders.insertRow(5)
        self.ikinci_ders.insertRow(6)
        self.ikinci_ders.insertRow(7)
        self.ikinci_ders.insertRow(8)
        self.ikinci_ders.insertRow(9)

        self.sinav_tarihi.insertRow(0)
        self.sinav_tarihi.insertRow(1)
        self.sinav_tarihi.insertRow(2)
        self.sinav_tarihi.insertRow(3)
        self.sinav_tarihi.insertRow(4)
        self.sinav_tarihi.insertRow(5)
        self.sinav_tarihi.insertRow(6)
        self.sinav_tarihi.insertRow(7)
        self.sinav_tarihi.insertRow(8)
        self.sinav_tarihi.insertRow(9)

        self.ogrenci_ismi.insertRow(0)
        self.ogrenci_ismi.insertRow(1)
        self.ogrenci_ismi.insertRow(2)
        self.ogrenci_ismi.insertRow(3)
        self.ogrenci_ismi.insertRow(4)
        self.ogrenci_ismi.insertRow(5)
        self.ogrenci_ismi.insertRow(6)
        self.ogrenci_ismi.insertRow(7)
        self.ogrenci_ismi.insertRow(8)
        self.ogrenci_ismi.insertRow(9)
        self.ogrenci_ismi.insertRow(10)
        self.ogrenci_ismi.insertRow(11)
        self.ogrenci_ismi.insertRow(12)

    def fillRows(self, htmlList):
        i = 0
        while i < 10:
            j = 1
            while j < 17:
                if j == 1:
                    check = str(htmlList[i + 1][1])[2:-2]
                    if check == '\\n':
                        check = ""
                    self.orgun_ders.setItem(i, j, QtWidgets.QTableWidgetItem(check))
                if j == 4:
                    check = str(htmlList[i + 1][2])[2:-2]
                    if check == '\\n':
                        check = ""
                    self.orgun_ders.setItem(i, j, QtWidgets.QTableWidgetItem(check))
                if j == 7:
                    check = str(htmlList[i + 1][3])[2:-2]
                    if check == '\\n':
                        check = ""
                    self.orgun_ders.setItem(i, j, QtWidgets.QTableWidgetItem(check))
                if j == 10:
                    check = str(htmlList[i + 1][4])[2:-2]
                    if check == '\\n':
                        check = ""
                    self.orgun_ders.setItem(i, j, QtWidgets.QTableWidgetItem(check))
                if j == 13:
                    check = str(htmlList[i + 1][5])[2:-2]
                    if check == '\\n':
                        check = ""
                    self.orgun_ders.setItem(i, j, QtWidgets.QTableWidgetItem(check))
                if j == 16:
                    check = str(htmlList[i + 1][6])[2:-2]
                    if check == '\\n':
                        check = ""
                    self.orgun_ders.setItem(i, j, QtWidgets.QTableWidgetItem(check))
                j += 1

            i += 1

    def setItems(self):
        self.ogrenci_ismi.setItem(1, 2, QtWidgets.QTableWidgetItem('deneme'))

        self.orgun_ders.setItem(0, 0, QtWidgets.QTableWidgetItem('[3]'))
        self.orgun_ders.setItem(1, 0, QtWidgets.QTableWidgetItem('[4]'))
        self.ikinci_ders.setItem(0, 0, QtWidgets.QTableWidgetItem('[3]'))
        self.ikinci_ders.setItem(1, 0, QtWidgets.QTableWidgetItem('[4]'))

    def on_pushButton_clicked(self):
        subprocess.call("python f1ArkaInfo.py 0", shell=True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
