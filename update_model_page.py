# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_model_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from components.handle_error_message import HandleErrorMessage
from components.top_bar import TopBar
from utils.common_utils import fetch_data


class UpdateModelPage(QtWidgets.QDialog, HandleErrorMessage):

    def __init__(self, parent, user):
        super().__init__()
        self.parent = parent
        self.user = user
        self.selected_model_id = None
        self.active_model_id = None
        self.inactive_models = {}
        self.setupUi()

    def setupUi(self):
        try:
            self.setObjectName("updateModelPage")
            self.setEnabled(True)
            self.resize(1058, 735)
            self.topBar = TopBar(self, is_menu_visible=True, logout_visible=True, user=self.user)
            self.label = QtWidgets.QLabel(self)
            self.label.setGeometry(QtCore.QRect(40, 130, 231, 31))
            font = QtGui.QFont()
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setStyleSheet("color:rgb(0, 170, 255); font-weight:bold")
            self.label.setObjectName("label")
            self.updateButton = QtWidgets.QPushButton(self)
            self.updateButton.setGeometry(QtCore.QRect(40, 610, 111, 41))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.updateButton.setFont(font)
            self.updateButton.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 170, 255)")
            self.updateButton.setObjectName("updateButton")
            self.gridLayoutWidget = QtWidgets.QWidget(self)
            self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 160, 991, 441))
            self.gridLayoutWidget.setObjectName("gridLayoutWidget")
            self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setHorizontalSpacing(17)
            self.gridLayout.setVerticalSpacing(6)
            self.gridLayout.setObjectName("gridLayout")
            self.selectModelLabel = QtWidgets.QLabel(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.selectModelLabel.sizePolicy().hasHeightForWidth())
            self.selectModelLabel.setSizePolicy(sizePolicy)
            self.selectModelLabel.setMinimumSize(QtCore.QSize(115, 0))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.selectModelLabel.setFont(font)
            self.selectModelLabel.setStyleSheet("color:#757575")
            self.selectModelLabel.setObjectName("selectModelLabel")
            self.gridLayout.addWidget(self.selectModelLabel, 3, 0, 1, 1)
            self.activeModelLabel = QtWidgets.QLabel(self.gridLayoutWidget)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.activeModelLabel.setFont(font)
            self.activeModelLabel.setStyleSheet("color:#757575")
            self.activeModelLabel.setObjectName("activeModelLabel")
            self.gridLayout.addWidget(self.activeModelLabel, 0, 0, 1, 1)
            self.selectModelComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.selectModelComboBox.sizePolicy().hasHeightForWidth())
            self.selectModelComboBox.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.selectModelComboBox.setFont(font)
            self.selectModelComboBox.setStyleSheet("color:#757575")
            self.selectModelComboBox.setObjectName("selectModelComboBox")
            self.selectModelComboBox.currentIndexChanged.connect(self.selection_changed)
            self.gridLayout.addWidget(self.selectModelComboBox, 3, 1, 1, 1)
            self.activeModelLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
            self.activeModelLineEdit.setEnabled(False)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.activeModelLineEdit.sizePolicy().hasHeightForWidth())
            self.activeModelLineEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.activeModelLineEdit.setFont(font)
            self.activeModelLineEdit.setStyleSheet("color:#757575")
            self.activeModelLineEdit.setObjectName("activeModelLineEdit")
            self.gridLayout.addWidget(self.activeModelLineEdit, 0, 1, 1, 1)
            self.activeModelDetailsLabel = QtWidgets.QLabel(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.activeModelDetailsLabel.sizePolicy().hasHeightForWidth())
            self.activeModelDetailsLabel.setSizePolicy(sizePolicy)
            self.activeModelDetailsLabel.setMinimumSize(QtCore.QSize(115, 0))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.activeModelDetailsLabel.setFont(font)
            self.activeModelDetailsLabel.setStyleSheet("color:#757575")
            self.activeModelDetailsLabel.setObjectName("activeModelDetailsLabel")
            self.gridLayout.addWidget(self.activeModelDetailsLabel, 1, 1, 1, 1)
            self.activeModelTextEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
            self.activeModelTextEdit.setObjectName("activeModelTextEdit")
            self.activeModelTextEdit.setStyleSheet("color:#757575")
            self.activeModelTextEdit.setFont(font)
            self.activeModelTextEdit.setReadOnly(True)
            self.gridLayout.addWidget(self.activeModelTextEdit, 2, 1, 1, 1)
            self.selectModelDetailLabel = QtWidgets.QLabel(self.gridLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.selectModelDetailLabel.sizePolicy().hasHeightForWidth())
            self.selectModelDetailLabel.setSizePolicy(sizePolicy)
            self.selectModelDetailLabel.setMinimumSize(QtCore.QSize(115, 0))
            font = QtGui.QFont()
            font.setPointSize(12)
            self.selectModelDetailLabel.setFont(font)
            self.selectModelDetailLabel.setStyleSheet("color:#757575")
            self.selectModelDetailLabel.setObjectName("selectModelDetailLabel")
            self.gridLayout.addWidget(self.selectModelDetailLabel, 4, 1, 1, 1)
            self.selectModelTextEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
            self.selectModelTextEdit.setObjectName("selectModelTextEdit")
            self.selectModelTextEdit.setStyleSheet("color:#757575")
            self.selectModelTextEdit.setFont(font)
            self.selectModelTextEdit.setReadOnly(True)
            self.gridLayout.addWidget(self.selectModelTextEdit, 5, 1, 1, 1)

            self.addErrorLabel(QtCore.QRect(40, 170, 201, 21), self)

            self.topBar.loginButton.clicked.connect(self.gotoHome)
            self.topBar.menuButton.clicked.connect(self.goToMenu)

            self.retranslateUi()
            QtCore.QMetaObject.connectSlotsByName(self)

            self.setValues()
            self.updateButton.clicked.connect(self.updateModel)

        except Exception as e:
            print(e)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("updateModelPage", "Update Model"))
        self.updateButton.setText(_translate("updateModelPage", "Update"))
        self.selectModelLabel.setText(_translate("updateModelPage", "Select Model to Activate"))
        self.activeModelLabel.setText(_translate("updateModelPage", "Current Active Model"))
        self.activeModelDetailsLabel.setText(_translate("updateModelPage", "Details of the Current Active Model"))
        self.selectModelDetailLabel.setText(_translate("updateModelPage", "Details of the Selected Model"))

    def setValues(self):
        data = fetch_data("model_loader/")
        print(data)
        if len(data) > 0:
            for model in data:
                if model["status"] == "Active":
                    details = """<style>
                                    li {
                                        margin-bottom: 10px;
                                    }
                                </style>
                                <ul>"""
                    for key in model:
                        if key == "model_name":
                            self.activeModelLineEdit.setText("[" + model["_id"] + "] " + model[key])
                        elif key != "status":
                            details += "<li>" + str(key) + " : " + str(model[key]) + "</li>"
                    details += "</ul>"
                    self.activeModelTextEdit.setHtml(details)
                    self.active_model_id = model["_id"]
                else:
                    details = """<style>
                                    li {
                                        margin-bottom: 10px;
                                    }
                                </style>
                                <ul>"""
                    for key in model:
                        if key not in ["model_name", "status"]:
                            details += "<li>" + str(key) + " : " + str(model[key]) + "</li>"
                    details += "</ul>"
                    self.inactive_models[model["_id"]] = details
                    self.selectModelComboBox.addItem("[" + model["_id"] + "] " + model["model_name"])

    def selection_changed(self, i):
        self.selected_model_id = self.selectModelComboBox.itemText(i).split("]")[0][1:]
        self.selectModelTextEdit.setHtml(self.inactive_models[self.selected_model_id])

    def updateModel(self):
        if self.selected_model_id and self.active_model_id:
            data = {
                "activate_id" : self.selected_model_id,
                "deactivate_id" : self.active_model_id,
            }
            self.handlePutRequest("model_loader/update_model", data)
        else:
            self.displayErrorMessage(True, "Model(s) are not selected")
