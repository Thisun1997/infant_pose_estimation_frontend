# -*- coding: utf-8 -*-
from datetime import datetime

# Form implementation generated from reading ui file 'view_history_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QSizePolicy

from components.dialog_with_guide import DialogWithGuide
from components.handle_error_message import HandleErrorMessage
from components.history_view import HistoryView
from components.top_bar import TopBar
from utils.common_utils import fetch_data


class ViewHistoryPage(DialogWithGuide, HandleErrorMessage):

    def __init__(self, parent):
        super(ViewHistoryPage, self).__init__(parent)
        self.selected_patient_id = None
        self.setupUi()

    def setupUi(self):
        try:
            self.setObjectName("viewHistoryPage")
            self.resize(1058, 735)
            self.topBar = TopBar(self, is_menu_visible=True, logout_visible=True)
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(40, 130, 231, 31))
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setStyleSheet("color:rgb(0, 170, 255); font-weight:bold")
            self.label.setObjectName("label")
            self.viewButton = QtWidgets.QPushButton(self)
            self.viewButton.setGeometry(QtCore.QRect(40, 250, 81, 31))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.viewButton.setFont(font)
            self.viewButton.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 170, 255)")
            self.viewButton.setObjectName("viewButton")
            self.gridLayoutWidget = QtWidgets.QWidget(self)
            self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 200, 941, 41))
            self.gridLayoutWidget.setObjectName("gridLayoutWidget")
            self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setHorizontalSpacing(17)
            self.gridLayout.setVerticalSpacing(6)
            self.gridLayout.setObjectName("gridLayout")
            self.fromDateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.fromDateEdit.sizePolicy().hasHeightForWidth())
            self.fromDateEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.fromDateEdit.setFont(font)
            self.fromDateEdit.setStyleSheet("color:#757575")
            self.fromDateEdit.setObjectName("fromDateEdit")
            self.fromDateEdit.setCalendarPopup(True)
            self.fromDateEdit.setMaximumDate(QDate.currentDate())
            self.fromDateEdit.setDate(QDate.currentDate())
            self.gridLayout.addWidget(self.fromDateEdit, 0, 1, 1, 1)
            self.fromLabel = QtWidgets.QLabel(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.fromLabel.sizePolicy().hasHeightForWidth())
            self.fromLabel.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.fromLabel.setFont(font)
            self.fromLabel.setStyleSheet("color:#757575")
            self.fromLabel.setObjectName("fromLabel")
            self.gridLayout.addWidget(self.fromLabel, 0, 0, 1, 1)
            self.toLabel = QtWidgets.QLabel(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.toLabel.sizePolicy().hasHeightForWidth())
            self.toLabel.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.toLabel.setFont(font)
            self.toLabel.setStyleSheet("color:#757575")
            self.toLabel.setObjectName("toLabel")
            self.gridLayout.addWidget(self.toLabel, 0, 2, 1, 1)
            self.toDateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.toDateEdit.setFont(font)
            self.toDateEdit.setStyleSheet("color:#757575")
            self.toDateEdit.setObjectName("toDateTEdit")
            self.gridLayout.addWidget(self.toDateEdit, 0, 3, 1, 1)
            self.toDateEdit.setCalendarPopup(True)
            self.toDateEdit.setMaximumDate(QDate.currentDate())
            self.toDateEdit.setDate(QDate.currentDate())
            self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
            self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 160, 941, 41))
            self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
            self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.selectPatientLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.selectPatientLabel.sizePolicy().hasHeightForWidth())
            self.selectPatientLabel.setSizePolicy(sizePolicy)
            self.selectPatientLabel.setMinimumSize(QtCore.QSize(115, 0))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.selectPatientLabel.setFont(font)
            self.selectPatientLabel.setStyleSheet("color:#757575")
            self.selectPatientLabel.setObjectName("selectPatientLabel")
            self.gridLayout_2.addWidget(self.selectPatientLabel, 0, 0, 1, 1)
            self.patientListComboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.patientListComboBox.setFont(font)
            self.patientListComboBox.setObjectName("patientListComboBox")
            self.gridLayout_2.addWidget(self.patientListComboBox, 0, 1, 1, 1)
            self.patientListComboBox.currentIndexChanged.connect(self.selection_changed)
            self.patientListComboBox.setStyleSheet("color:#757575")
            # scroll area
            self.scrollArea = QtWidgets.QScrollArea(self)
            self.scrollArea.setGeometry(QtCore.QRect(40, 290, 630, 390))
            # self.scrollArea.setWidgetResizable(True)
            sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
            sizePolicy2.setHorizontalStretch(0)
            sizePolicy2.setVerticalStretch(0)
            sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
            self.scrollArea.setSizePolicy(sizePolicy2)
            self.scrollArea.setObjectName("scrollArea")
            self.scrollAreaWidgetContents = QtWidgets.QWidget()
            self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
            # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 582, 486))
            self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
            self.gridLayout_4.setObjectName(u"gridLayout_4")
            self.widget_2 = QtWidgets.QWidget(self)
            self.widget_2.setGeometry(QtCore.QRect(680, 290, 331, 331))
            self.widget_2.setAutoFillBackground(True)
            self.widget_2.setObjectName("widget_2")
            self.gridLayoutWidget_3 = QtWidgets.QWidget(self.widget_2)
            self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 331, 281))
            self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
            self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
            self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
            self.gridLayout_3.setObjectName("gridLayout_3")
            self.genderLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.genderLabel.sizePolicy().hasHeightForWidth())
            self.genderLabel.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.genderLabel.setFont(font)
            self.genderLabel.setStyleSheet("color:#757575")
            self.genderLabel.setObjectName("genderLabel")
            self.gridLayout_3.addWidget(self.genderLabel, 1, 0, 1, 1)
            self.nameLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
            self.nameLabel.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.nameLabel.setFont(font)
            self.nameLabel.setStyleSheet("color:#757575")
            self.nameLabel.setObjectName("nameLabel")
            self.gridLayout_3.addWidget(self.nameLabel, 0, 0, 1, 1)
            self.guardianLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.guardianLabel.sizePolicy().hasHeightForWidth())
            self.guardianLabel.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.guardianLabel.setFont(font)
            self.guardianLabel.setStyleSheet("color:#757575")
            self.guardianLabel.setObjectName("guardianLabel")
            self.gridLayout_3.addWidget(self.guardianLabel, 3, 0, 1, 1)
            self.dateOfBirthLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.dateOfBirthLabel.sizePolicy().hasHeightForWidth())
            self.dateOfBirthLabel.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.dateOfBirthLabel.setFont(font)
            self.dateOfBirthLabel.setStyleSheet("color:#757575")
            self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")
            self.gridLayout_3.addWidget(self.dateOfBirthLabel, 2, 0, 1, 1)
            self.nameLineEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.nameLineEdit.setFont(font)
            self.nameLineEdit.setStyleSheet("color:#757575")
            self.nameLineEdit.setObjectName("nameLineEdit")
            self.nameLineEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
            self.nameLineEdit.setReadOnly(True)
            self.gridLayout_3.addWidget(self.nameLineEdit, 0, 1, 1, 1)
            self.addressLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.addressLabel.sizePolicy().hasHeightForWidth())
            self.addressLabel.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.addressLabel.setFont(font)
            self.addressLabel.setStyleSheet("color:#757575")
            self.addressLabel.setObjectName("addressLabel")
            self.gridLayout_3.addWidget(self.addressLabel, 4, 0, 1, 1)
            self.contactNumberLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.contactNumberLabel.sizePolicy().hasHeightForWidth())
            self.contactNumberLabel.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.contactNumberLabel.setFont(font)
            self.contactNumberLabel.setStyleSheet("color:#757575")
            self.contactNumberLabel.setObjectName("contactNumberLabel")
            self.gridLayout_3.addWidget(self.contactNumberLabel, 5, 0, 1, 1)
            self.genderLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
            self.genderLineEdit.setEnabled(False)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.genderLineEdit.setFont(font)
            self.genderLineEdit.setStyleSheet("color:#757575")
            self.genderLineEdit.setObjectName("genderLineEdit")
            self.gridLayout_3.addWidget(self.genderLineEdit, 1, 1, 1, 1)
            self.guardianLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
            self.guardianLineEdit.setEnabled(False)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.guardianLineEdit.setFont(font)
            self.guardianLineEdit.setStyleSheet("color:#757575")
            self.guardianLineEdit.setObjectName("guardianLineEdit")
            self.gridLayout_3.addWidget(self.guardianLineEdit, 3, 1, 1, 1)
            self.addressLineEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.addressLineEdit.setFont(font)
            self.addressLineEdit.setStyleSheet("color:#757575")
            self.addressLineEdit.setObjectName("addressLineEdit")
            self.addressLineEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
            self.addressLineEdit.setReadOnly(True)
            self.gridLayout_3.addWidget(self.addressLineEdit, 4, 1, 1, 1)
            self.contactNumberLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
            self.contactNumberLineEdit.setEnabled(False)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.contactNumberLineEdit.setFont(font)
            self.contactNumberLineEdit.setStyleSheet("color:#757575")
            self.contactNumberLineEdit.setObjectName("contactNumberLineEdit")
            self.gridLayout_3.addWidget(self.contactNumberLineEdit, 5, 1, 1, 1)
            self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_3)
            self.dateEdit.setEnabled(False)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.dateEdit.setFont(font)
            self.dateEdit.setStyleSheet("color:#757575")
            self.dateEdit.setObjectName("dateEdit")
            self.gridLayout_3.addWidget(self.dateEdit, 2, 1, 1, 1)

            self.retranslateUi()
            QtCore.QMetaObject.connectSlotsByName(self)

            self.addErrorLabel(QtCore.QRect(40, 170, 201, 21), self)
            self.topBar.loginButton.clicked.connect(self.gotoHome)
            self.topBar.menuButton.clicked.connect(self.goToMenu)

            self.widget_list = []
            self.fetchPatientList()
            self.viewButton.clicked.connect(self.viewData)
        except Exception as e:
            print(e)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("viewHistoryPage", "Infant Pose Visualizer"))
        self.label.setText(_translate("viewHistoryPage", "View Historical Data"))
        self.viewButton.setText(_translate("viewHistoryPage", "View"))
        self.fromLabel.setText(_translate("viewHistoryPage", "From"))
        self.toLabel.setText(_translate("viewHistoryPage", "To"))
        self.selectPatientLabel.setText(_translate("viewHistoryPage", "Select Patient"))
        self.genderLabel.setText(_translate("viewHistoryPage", "Gender"))
        self.nameLabel.setText(_translate("viewHistoryPage", "Name"))
        self.guardianLabel.setText(_translate("viewHistoryPage", "Guardian"))
        self.dateOfBirthLabel.setText(_translate("viewHistoryPage", "Date of Birth"))
        self.contactNumberLabel.setText(_translate("viewHistoryPage", "Contact Number"))
        self.addressLabel.setText(_translate("viewHistoryPage", "Address"))

    def fetchPatientList(self):
        try:
            data = fetch_data("patients/")
            for patient in data:
                self.patientListComboBox.addItem(str(patient["_id"]) + " - " + patient["patient_name"])
        except Exception as e:
            self.displayErrorMessage(True, "Error fetching data: " + str(e))

    def selection_changed(self, i):
        self.selected_patient_id = int(self.patientListComboBox.itemText(i).split("-")[0])

    def viewData(self):
        try:
            self.displayErrorMessage(False)
            if self.gridLayout_4.count() > 0: self.clearScrollArea()
            self.clearFields()
            fromTime = self.fromDateEdit.date()
            toTime = self.toDateEdit.date()
            if self.selected_patient_id:
                patient_data = fetch_data("patients/data", {"_id": self.selected_patient_id})
                self.nameLineEdit.setPlainText(patient_data["patient_name"])
                self.genderLineEdit.setText(patient_data["gender"])
                self.dateEdit.setDate(datetime.fromisoformat(patient_data["date_of_birth"]['$date'][:-1]).date())
                self.guardianLineEdit.setText(patient_data["guardian"])
                self.addressLineEdit.setPlainText(patient_data["address"])
                self.contactNumberLineEdit.setText(patient_data["contact_number"])

                query_data = {
                    "patient_id": self.selected_patient_id,
                    "from_time": fromTime.toString("yyyy-MM-dd"),
                    "to_time": toTime.toString("yyyy-MM-dd")
                }
                history_data = fetch_data("patients/history_data", query_data)
                if "message" in history_data:
                    self.displayErrorMessage(True, history_data["message"])
                else:
                    for i in range(len(history_data)):
                        print(history_data[i]["_id"])
                        feedback_data = fetch_data("feedback/get", {"vis_insertion_id": history_data[i]["_id"]["$oid"]})
                        history_data[i]["feedback"] = feedback_data["message"]
                        widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
                        # widget.setGeometry(QtCore.QRect(10, 10 + (231 * i) + padding, 581, 231))
                        widget.setAutoFillBackground(False)
                        widget.setStyleSheet("background-color:rgb(255, 255, 255)")
                        widget.setObjectName("widget")
                        widget.setMinimumSize(QtCore.QSize(581, 250))
                        widget.setMaximumSize(QtCore.QSize(581, 250))
                        HistoryView(widget, history_data[i])
                        self.gridLayout_4.addWidget(widget, i + 1, 0, 1, 1)
                        self.widget_list.append(widget)
                    self.scrollAreaWidgetContents.adjustSize()
                    self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        except Exception as e:
            print(e)
            self.displayErrorMessage(True, "Error fetching data: " + str(e))

    def clearScrollArea(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_list.clear()

    def clearFields(self):
        self.nameLineEdit.clear()
        self.genderLineEdit.clear()
        self.dateEdit.clear()
        self.guardianLineEdit.clear()
        self.addressLineEdit.clear()
        self.contactNumberLineEdit.clear()
