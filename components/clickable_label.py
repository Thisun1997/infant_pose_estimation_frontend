from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, Qt


class ClickableLabel(QLabel):
    clicked = pyqtSignal()  # Define a new signal called 'clicked'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()  # Emit the 'clicked' signal when the label is clicked
        super().mouseReleaseEvent(event)
