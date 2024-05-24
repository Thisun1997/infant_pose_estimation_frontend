from PyQt5 import QtWidgets, QtCore, QtGui, Qt

from components.clickable_label import ClickableLabel


class TopBar(QtWidgets.QWidget):
    def __init__(self, parent=None, login_visible=False, logout_visible=False, is_home_accessible=False, is_menu_visible=False):
        super(TopBar,self).__init__(parent)
        self.setupUi(login_visible, logout_visible, is_home_accessible, is_menu_visible)

    def setupUi(self, login_visible=False, logout_visible=False, is_home_accessible=False, is_menu_visible=False):
        self.setGeometry(QtCore.QRect(0, 0, 1061, 101))
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color : rgb(0, 170, 255)")
        self.setObjectName("topBar")

        if is_home_accessible:
            self.mainLabel = ClickableLabel(self)
        else:
            self.mainLabel = QtWidgets.QLabel(self)

        self.mainLabel.setGeometry(QtCore.QRect(40, 40, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mainLabel.setFont(font)
        self.mainLabel.setStyleSheet("font-weight: bold; color: rgb(255, 255, 255)")
        self.mainLabel.setObjectName("mainLabel")

        if login_visible or logout_visible:
            self.loginButton = QtWidgets.QPushButton(self)
            self.loginButton.setGeometry(QtCore.QRect(900, 30, 111, 41))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.loginButton.setFont(font)
            self.loginButton.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 170, 255)")
            self.loginButton.setObjectName("loginButton")

        if is_menu_visible:
            self.menuButton = QtWidgets.QPushButton(self)
            self.menuButton.setGeometry(QtCore.QRect(750, 30, 111, 41))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.menuButton.setFont(font)
            self.menuButton.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 170, 255)")
            self.menuButton.setObjectName("menuButton")

        self.retranslateUi(login_visible, logout_visible, is_menu_visible)


    def retranslateUi(self, login_visible, logout_visible, is_menu_visible):
        _translate = QtCore.QCoreApplication.translate
        if login_visible : self.loginButton.setText(_translate("topBar", "Login"))
        if logout_visible : self.loginButton.setText(_translate("topBar", "Logout"))
        if is_menu_visible : self.menuButton.setText(_translate("topBar", "Menu"))
        self.mainLabel.setText(_translate("topBar", "Infant Pose Visualizer"))
