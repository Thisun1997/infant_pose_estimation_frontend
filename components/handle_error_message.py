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
            elif self.objectName() == "poseVisualizationPage":
                self.saveButton.setGeometry(QtCore.QRect(480, 540, 111, 41))
                self.backButton.setGeometry(QtCore.QRect(620, 540, 111, 41))
                self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 210, 941, 41))
                self.imageLabel.setGeometry(QtCore.QRect(40, 309, 400, 361))
                self.lineEdit.setGeometry(QtCore.QRect(480, 310, 501, 211))
                self.remarkLabel.setGeometry(QtCore.QRect(480, 270, 131, 25))
                self.visualizationLabel.setGeometry(QtCore.QRect(40, 270, 131, 25))
                self.feedbackLinkLabel.setGeometry(QtCore.QRect(480, 650, 231, 21))
                self.predictionModelUsedLinkLabel.setGeometry(QtCore.QRect(160, 650, 311, 21))
                self.predictedByLabel.setGeometry(QtCore.QRect(40, 650, 111, 21))
            elif self.objectName() == "feedbackPage":
                self.resize(561, 481)
                self.closeButton.setGeometry(QtCore.QRect(170, 410, 111, 41))
                self.submitButton.setGeometry(QtCore.QRect(30, 410, 111, 41))
                self.feedbackLineEdit.setGeometry(QtCore.QRect(30, 130, 501, 261))
            elif self.objectName() == "viewHistoryPage":
                self.viewButton.setGeometry(QtCore.QRect(40, 290, 81, 31))
                self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 240, 941, 41))
                self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 200, 941, 41))
                self.scrollArea.setGeometry(QtCore.QRect(40, 330, 630, 390))
                self.textArea.setGeometry(QtCore.QRect(40, 330, 630, 390))
                self.widget_2.setGeometry(QtCore.QRect(680, 330, 331, 331))
                self.recordCountLabel.setGeometry(QtCore.QRect(140, 300, 141, 16))
            elif self.objectName() == "EditPatientPage":
                self.closeButton.setGeometry(QtCore.QRect(170, 460, 111, 41))
                self.saveButton.setGeometry(QtCore.QRect(30, 460, 111, 41))
                self.widget_2.setGeometry(QtCore.QRect(30, 100, 511, 341))
            elif self.objectName() == "updateModelPage":
                self.updateButton.setGeometry(QtCore.QRect(40, 650, 111, 41))
                self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 200, 991, 441))
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
            elif self.objectName() == "poseVisualizationPage":
                self.saveButton.setGeometry(QtCore.QRect(480, 500, 111, 41))
                self.backButton.setGeometry(QtCore.QRect(620, 500, 111, 41))
                self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 170, 941, 41))
                self.imageLabel.setGeometry(QtCore.QRect(40, 269, 400, 361))
                self.lineEdit.setGeometry(QtCore.QRect(480, 270, 501, 211))
                self.remarkLabel.setGeometry(QtCore.QRect(480, 230, 131, 25))
                self.visualizationLabel.setGeometry(QtCore.QRect(40, 230, 131, 25))
                self.feedbackLinkLabel.setGeometry(QtCore.QRect(480, 610, 231, 21))
                self.predictionModelUsedLinkLabel.setGeometry(QtCore.QRect(160, 610, 311, 21))
                self.predictedByLabel.setGeometry(QtCore.QRect(40, 610, 111, 21))
            elif self.objectName() == "feedbackPage":
                self.resize(561, 451)
                self.closeButton.setGeometry(QtCore.QRect(170, 380, 111, 41))
                self.submitButton.setGeometry(QtCore.QRect(30, 380, 111, 41))
                self.feedbackLineEdit.setGeometry(QtCore.QRect(30, 100, 501, 261))
            elif self.objectName() == "viewHistoryPage":
                self.viewButton.setGeometry(QtCore.QRect(40, 250, 81, 31))
                self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 200, 941, 41))
                self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 160, 941, 41))
                self.scrollArea.setGeometry(QtCore.QRect(40, 290, 630, 390))
                self.textArea.setGeometry(QtCore.QRect(40, 290, 630, 390))
                self.widget_2.setGeometry(QtCore.QRect(680, 290, 331, 331))
                self.recordCountLabel.setGeometry(QtCore.QRect(140, 260, 141, 16))
            elif self.objectName() == "EditPatientPage":
                self.closeButton.setGeometry(QtCore.QRect(170, 420, 111, 41))
                self.saveButton.setGeometry(QtCore.QRect(30, 420, 111, 41))
                self.widget_2.setGeometry(QtCore.QRect(30, 60, 511, 341))
            elif self.objectName() == "updateModelPage":
                self.updateButton.setGeometry(QtCore.QRect(40, 610, 111, 41))
                self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 160, 991, 441))
    def gotoHome(self):
        try:
            # if self.user:
            #     self.user = None
            i = self.parent.count() - 1
            while self.parent.count() > 1:
                widget = self.parent.widget(i)
                print(widget.objectName())
                self.parent.removeWidget(widget)
                i -= 1
            self.parent.setCurrentIndex(0)
        except Exception as e:
            print(e)

    def goToMenu(self):
        for i in range(self.parent.count()):
            widget = self.parent.widget(i)
            if widget.objectName() == "menuPage":
                self.parent.setCurrentIndex(i)
                break

    def handlePutRequest(self, path, query_data, new_field=None):
        if new_field is None:
            new_field = {}
        if not has_empty_or_null_value(query_data):
            self.displayErrorMessage(False)
            self.error.setHidden(True)
            data = {
                "query": query_data,
                "new_field": new_field
            }
            response = sendPostRequest(path, data, "PUT")
            if response["code"] == 200:
                self.error.setStyleSheet(u"color: rgb(0, 234, 0)")
            self.displayErrorMessage(True, response["message"])
        else:
            self.displayErrorMessage(True, "Inputs marked with * are required")
