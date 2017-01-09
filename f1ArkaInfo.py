# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f1ArkaInfo.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Info(object):
    def setupUi(self, Info):
        Info.setObjectName("Info")
        Info.resize(585, 397)
        self.gridLayout = QtWidgets.QGridLayout(Info)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Info)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Info)
        QtCore.QMetaObject.connectSlotsByName(Info)

    def retranslateUi(self, Info):
        _translate = QtCore.QCoreApplication.translate
        Info.setWindowTitle(_translate("Info", "Dialog"))
        self.label.setText(_translate("Info",
                                      "<html><head/><body><p><span style=\" font-size:12pt;\">[1] SUNNY:</span></p><p><span style=\" font-size:12pt;\">1-(T-D-L)derslerin teorik,uygulama,labaratuvar uzantılarını yazılacaktır.</span></p><p><span style=\" font-size:12pt;\">[2] SUNNY:</span></p><p><span style=\" font-size:12pt;\">derslerin maaş karşılığı olanlar işaretlenecektir.</span></p><p><span style=\" font-size:12pt;\">(X)maaş karşılıkları X olarak işaretlenecektir.</span></p><p><span style=\" font-size:12pt;\">[3] SUNNY:</span></p><p><span style=\" font-size:12pt;\">sayfa aralıklarını eğer satırlar dar ise genişletebilirsiniz</span></p><p><span style=\" font-size:12pt;\">[4] SUNNY:</span></p><p><span style=\" font-size:12pt;\">Bölüm ders programında ders saatiniz hangi aralıkta ise o saate dersi </span></p><p><span style=\" font-size:12pt;\">yazmalısınız ders programı ve F1 formundaki saat birbiriyle aynı olmalıdır.</span></p><p><span style=\" font-size:12pt;\">Ayrıca bitirme çalışması ve proje dersleri bölüm ders programında hangi saatte</span></p><p><span style=\" font-size:12pt;\"> ise o güne yazılmalıdır.</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Info = QtWidgets.QDialog()
    ui = Ui_Info()
    ui.setupUi(Info)
    Info.show()
    sys.exit(app.exec_())
