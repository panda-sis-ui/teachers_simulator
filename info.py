# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_info_window(object):
    def setupUi(self, info_window):
        info_window.setObjectName("info_window")
        info_window.resize(700, 600)
        info_window.setMinimumSize(QtCore.QSize(700, 600))
        info_window.setMaximumSize(QtCore.QSize(3000, 3000))
        info_window.setStyleSheet("background-color: #FFFBCE;\n"
"color: #1E6214;\n"
"")
        info_window.setSizeGripEnabled(False)
        info_window.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(info_window)
        self.gridLayout.setObjectName("gridLayout")
        self.text_situation_2 = QtWidgets.QLabel(info_window)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.text_situation_2.setFont(font)
        self.text_situation_2.setAlignment(QtCore.Qt.AlignCenter)
        self.text_situation_2.setWordWrap(True)
        self.text_situation_2.setObjectName("text_situation_2")
        self.gridLayout.addWidget(self.text_situation_2, 0, 0, 1, 3)
        self.img_label = QtWidgets.QLabel(info_window)
        self.img_label.setMinimumSize(QtCore.QSize(251, 251))
        self.img_label.setMaximumSize(QtCore.QSize(261, 261))
        self.img_label.setText("")
        self.img_label.setWordWrap(True)
        self.img_label.setObjectName("img_label")
        self.gridLayout.addWidget(self.img_label, 1, 0, 1, 1)
        self.back = QtWidgets.QPushButton(info_window)
        self.back.setMaximumSize(QtCore.QSize(290, 45))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton{\n"
"background-color:#1E6214;\n"
"color:#FFFBCE\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#60C04C;\n"
"color:#1E6214;\n"
"border: 4px solid #60C04C;\n"
"}")
        self.back.setObjectName("back")
        self.gridLayout.addWidget(self.back, 2, 0, 1, 1)
        self.text_info = QtWidgets.QLabel(info_window)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.text_info.setFont(font)
        self.text_info.setWordWrap(True)
        self.text_info.setObjectName("text_info")
        self.gridLayout.addWidget(self.text_info, 1, 1, 1, 1)

        self.retranslateUi(info_window)
        QtCore.QMetaObject.connectSlotsByName(info_window)

    def retranslateUi(self, info_window):
        _translate = QtCore.QCoreApplication.translate
        info_window.setWindowTitle(_translate("info_window", "Дополнительная информация"))
        self.text_situation_2.setText(_translate("info_window", "Дополнительная информация"))
        self.back.setText(_translate("info_window", "Назад"))
        self.text_info.setText(_translate("info_window", "Текст, описание ситуации, описание этапа, на котором необходимо сделать выбор"))
