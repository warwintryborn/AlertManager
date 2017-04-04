# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlertManager_Designer.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(284, 163)
        self.button_login = QtWidgets.QPushButton(Form)
        self.button_login.setGeometry(QtCore.QRect(10, 120, 261, 31))
        self.button_login.setObjectName("button_login")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 261, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.group_login = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.group_login.setContentsMargins(0, 0, 0, 0)
        self.group_login.setObjectName("group_login")
        self.label_username = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_username.setObjectName("label_username")
        self.group_login.addWidget(self.label_username, 1, 0, 1, 1)
        self.text_username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.text_username.setObjectName("text_username")
        self.group_login.addWidget(self.text_username, 1, 1, 1, 1)
        self.label_AlertManager = QtWidgets.QLabel(Form)
        self.label_AlertManager.setGeometry(QtCore.QRect(70, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_AlertManager.setFont(font)
        self.label_AlertManager.setObjectName("label_AlertManager")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alert Manager"))
        self.button_login.setText(_translate("Form", "Login"))
        self.label_username.setText(_translate("Form", "Username"))
        self.label_AlertManager.setText(_translate("Form", "Alert Manager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

