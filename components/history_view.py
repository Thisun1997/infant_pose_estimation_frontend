import base64
import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtGui import QPixmap


class HistoryView(QtWidgets.QWidget):
    def __init__(self, parent, data):
        super(HistoryView, self).__init__(parent)
        self.parent = parent
        self.data = data
        self.setupUi()

    def setupUi(self):
        self.showImageLabel = QtWidgets.QLabel(self.parent)
        self.showImageLabel.setGeometry(QtCore.QRect(10, 10, 250, 235))
        self.showImageLabel.setText("")
        self.showImageLabel.setObjectName("showImageLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.parent)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 10, 311, 235))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy)
        self.timeLabel.setMinimumSize(QtCore.QSize(115, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color:#757575")
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout.addWidget(self.timeLabel)
        self.time = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.time.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time.sizePolicy().hasHeightForWidth())
        self.time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time.setFont(font)
        self.time.setStyleSheet("color:#757575")
        self.time.setObjectName("time")
        self.verticalLayout.addWidget(self.time)
        self.medicalRemarkLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.medicalRemarkLabel.sizePolicy().hasHeightForWidth())
        self.medicalRemarkLabel.setSizePolicy(sizePolicy)
        self.medicalRemarkLabel.setMinimumSize(QtCore.QSize(115, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.medicalRemarkLabel.setFont(font)
        self.medicalRemarkLabel.setStyleSheet("color:#757575")
        self.medicalRemarkLabel.setObjectName("medicalRemarkLabel")
        self.verticalLayout.addWidget(self.medicalRemarkLabel)
        self.medicalRemarkLineEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.medicalRemarkLineEdit.setFont(font)
        self.medicalRemarkLineEdit.setStyleSheet("color:#757575")
        self.medicalRemarkLineEdit.setObjectName("medicalRemarkLineEdit")
        self.medicalRemarkLineEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.medicalRemarkLineEdit.setReadOnly(True)
        self.verticalLayout.addWidget(self.medicalRemarkLineEdit)
        self.feedbackLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feedbackLabel.sizePolicy().hasHeightForWidth())
        self.feedbackLabel.setSizePolicy(sizePolicy)
        self.feedbackLabel.setMinimumSize(QtCore.QSize(115, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.feedbackLabel.setFont(font)
        self.feedbackLabel.setStyleSheet("color:#757575")
        self.feedbackLabel.setObjectName("feedbackLabel")
        self.verticalLayout.addWidget(self.feedbackLabel)
        self.feedbackLineEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.feedbackLineEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.feedbackLineEdit.setFont(font)
        self.feedbackLineEdit.setStyleSheet("color:#757575")
        self.feedbackLineEdit.setObjectName("feedbackLineEdit")
        self.feedbackLineEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.verticalLayout.addWidget(self.feedbackLineEdit)
        self.userLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userLabel.sizePolicy().hasHeightForWidth())
        self.userLabel.setSizePolicy(sizePolicy)
        self.userLabel.setMinimumSize(QtCore.QSize(115, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet("color:#757575")
        self.userLabel.setObjectName("userLabel")
        self.verticalLayout.addWidget(self.userLabel)
        self.userLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.userLineEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userLineEdit.setFont(font)
        self.userLineEdit.setStyleSheet("color:#757575")
        self.userLineEdit.setObjectName("userLineEdit")
        self.verticalLayout.addWidget(self.userLineEdit)
        self.retranslateUi()
        self.setValues()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.timeLabel.setText(_translate("viewHistoryPage", "Time"))
        self.medicalRemarkLabel.setText(_translate("viewHistoryPage", "Medical Remarks"))
        self.feedbackLabel.setText(_translate("viewHistoryPage", "Feedback on Pose Estimation"))
        self.userLabel.setText(_translate("viewHistoryPage", "User"))

    def setValues(self):
        data = self.data
        self.time.setText(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["time"] / 1e9)))
        medical_remark = "-"
        feedback = "-"
        user = "-"
        if "medical_remark" in data:
            medical_remark = data["medical_remark"]
        if "feedback" in data:
            feedback = data["feedback"]
        if "user" in data:
            user = data["user"]
        self.medicalRemarkLineEdit.setPlainText(medical_remark)
        self.feedbackLineEdit.setPlainText(feedback)
        self.userLineEdit.setText(user)

        pixmap = QPixmap()
        print(data["visualization"])
        pixmap.loadFromData(QByteArray(base64.b64decode(data["visualization"]["$binary"]['base64'])))
        scaled_pixmap = pixmap.scaled(self.showImageLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        print(pixmap.size(), self.showImageLabel.size(), scaled_pixmap.size())
        self.showImageLabel.setAlignment(Qt.AlignCenter)
        self.showImageLabel.setPixmap(scaled_pixmap)
