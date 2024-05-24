from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QEvent

from guide_page import GuideDialog


class DialogWithGuide(QtWidgets.QDialog):
    def __init__(self, parent):
        super(DialogWithGuide, self).__init__()
        self.parent = parent
        self.dialog = None
        self.guideButton = QtWidgets.QCommandLinkButton(self)
        self.guideButton.setGeometry(QtCore.QRect(920, 670, 121, 41))
        self.guideButton.setObjectName("guideButton")
        self.guideButton.clicked.connect(self.open_guide_page)
        self.guideButton.setText("Quick Guide")


    def open_guide_page(self):
        if self.dialog is None:
            self.dialog = GuideDialog()
            self.dialog.setAttribute(Qt.WA_DeleteOnClose)
            self.dialog.finished.connect(self.reset_dialog)
        self.dialog.show()

    def closeEvent(self, event):
        if self.dialog is not None:
            self.dialog.close()  # Close the dialog if it is open
        event.accept()

    def reset_dialog(self):
        self.dialog = None
