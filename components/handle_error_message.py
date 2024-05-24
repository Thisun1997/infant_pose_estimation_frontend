from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont

from utils.common_utils import has_empty_or_null_value, sendPostRequest


class HandleErrorMessage:

    def addErrorLabel(self, geometry, widget, wrap_text=False):
        self.error = QtWidgets.QLabel(widget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(geometry)
        font2 = QFont()
        font2.setPointSize(12)
        self.error.setFont(font2)
        self.error.setStyleSheet(u"color: rgb(234, 0, 0)")
        if wrap_text: self.error.setWordWrap(True)
        self.error.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.error.setHidden(True)

    def handlePostRequest(self, path, data, get_message=False):
        if not has_empty_or_null_value(data):
            self.displayErrorMessage(False)
            self.error.setHidden(True)
            response = sendPostRequest(path, data)
            if response['code'] != 200:
                self.displayErrorMessage(True, response["message"])
            else:
                if get_message:
                    return response["message"]
                return True
        else:
            self.displayErrorMessage(True, "Inputs marked with * are required")
        return False

    def displayErrorMessage(self, is_displayed, error_message=None):
        if (is_displayed):
            self.error.setHidden(False)
            self.error.setText(error_message)
            self.error.adjustSize()
            if self.objectName() == "LoginPage":
                self.formLayoutWidget.setGeometry(QtCore.QRect(110, 130, 317, 251))
            elif self.objectName() == "patientRegistrationPage":
                self.formLayoutWidget.setGeometry(QRect(40, 210, 921, 300))
                self.registerButton.setGeometry(QRect(40, 530, 111, 41))
            elif self.objectName() == "patientAdmissionPage":
                self.formLayoutWidget.setGeometry(QRect(40, 210, 921, 271))
                self.addButton.setGeometry(QRect(40, 530, 111, 41))
            elif self.objectName() == "imageUploadPage":
                self.uploadButton.setGeometry(QtCore.QRect(40, 660, 111, 41))
                self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 240, 941, 81))
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 320, 941, 41))
                self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 360, 941, 281))
                self.gridLayoutWidget_2.setGeometry(QRect(40, 200, 941, 41))

        else:
            self.error.setHidden(True)
            if self.objectName() == "LoginPage":
                self.formLayoutWidget.setGeometry(QtCore.QRect(110, 90, 317, 251))
            elif self.objectName() == "patientRegistrationPage":
                self.formLayoutWidget.setGeometry(QtCore.QRect(40, 170, 921, 296))
                self.registerButton.setGeometry(QtCore.QRect(40, 490, 111, 41))
            elif self.objectName() == "patientAdmissionPage":
                self.formLayoutWidget.setGeometry(QRect(40, 170, 921, 271))
                self.addButton.setGeometry(QRect(40, 490, 111, 41))
            elif self.objectName() == "imageUploadPage":
                self.uploadButton.setGeometry(QtCore.QRect(40, 620, 111, 41))
                self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 200, 941, 81))
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 280, 941, 41))
                self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 320, 941, 281))
                self.gridLayoutWidget_2.setGeometry(QRect(40, 160, 941, 41))

    def gotoHome(self):
        self.parent.setCurrentIndex(0)

    def goToMenu(self):
        for i in range(self.parent.count()):
            widget = self.parent.widget(i)
            if widget.objectName() == "menuPage":
                self.parent.setCurrentIndex(i)
                break