# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(700, 600)
        menu_window.setMinimumSize(QtCore.QSize(700, 600))
        menu_window.setMaximumSize(QtCore.QSize(700, 600))
        font = QtGui.QFont()
        font.setFamily("Dhurjati")
        menu_window.setFont(font)
        menu_window.setStyleSheet("background-color: #FFFBCE;\n"
"color: #1E6214;\n"
"")
        self.centralwidget = QtWidgets.QWidget(menu_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.exit_game = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.exit_game.setFont(font)
        self.exit_game.setStyleSheet("QPushButton{\n"
"background-color:#1E6214;\n"
"color:#FFFBCE\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#60C04C;\n"
"color:#1E6214;\n"
"border: 4px solid #60C04C;\n"
"}")
        self.exit_game.setObjectName("exit_game")
        self.gridLayout.addWidget(self.exit_game, 0, 0, 1, 1)
        self.rules = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.rules.setFont(font)
        self.rules.setStyleSheet("QPushButton{\n"
"background-color:#1E6214;\n"
"color:#FFFBCE\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#60C04C;\n"
"color:#1E6214;\n"
"border: 4px solid #60C04C;\n"
"}")
        self.rules.setObjectName("rules")
        self.gridLayout.addWidget(self.rules, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dhurjati")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.new_game = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.new_game.setFont(font)
        self.new_game.setStyleSheet("QPushButton{\n"
"background-color:#1E6214;\n"
"color:#FFFBCE\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#60C04C;\n"
"color:#1E6214;\n"
"border: 4px solid #60C04C;\n"
"}")
        self.new_game.setObjectName("new_game")
        self.gridLayout.addWidget(self.new_game, 2, 0, 1, 2)
        menu_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu_window)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "Меню"))
        self.exit_game.setText(_translate("menu_window", "Выход"))
        self.rules.setText(_translate("menu_window", "Правила игры"))
        self.label.setText(_translate("menu_window", "Симулятор учителя"))
        self.new_game.setText(_translate("menu_window", "Начать игру"))
