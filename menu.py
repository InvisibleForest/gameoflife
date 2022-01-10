# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog, run_func=False):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 400)
        Dialog.setMinimumSize(QtCore.QSize(620, 400))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_browser = QtWidgets.QTextBrowser(Dialog)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.text_browser.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Liberation Mono")
        font.setPointSize(14)
        self.text_browser.setFont(font)
        self.text_browser.setObjectName("text_browser")
        self.verticalLayout_3.addWidget(self.text_browser)
        self.ok_button = QtWidgets.QPushButton(Dialog)
        self.ok_button.setObjectName("ok_button")
        self.verticalLayout_3.addWidget(self.ok_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.ok_button_function(run_func, Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Game Of Life"))
        self.text_browser.setHtml(_translate("dialog", rules))
        self.ok_button.setText(_translate("dialog", "ОК"))


    def ok_button_function(self, run_func, Dialog):
        """Закрытие окна меню. Если меню вызывается как модуль,
        то окно завкроется без завершения всей программы.
        """
        if run_func:
            self.ok_button.clicked.connect(Dialog.close)
        else:
            self.ok_button.clicked.connect(quit)


# подгрузка правил игры для меню
with open('rules.html', encoding='utf-8') as inp:
    rules = inp.read()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
