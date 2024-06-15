from PyQt5 import QtWidgets, QtGui


class CustomWidget(QtWidgets.QWidget):
    def __init__(self, label_list, parent=None):
        super().__init__(parent)

        # Create two labels
        font = QtGui.QFont()
        font.setPointSize(12)
        layout = QtWidgets.QVBoxLayout()

        for label_value in label_list:
            self.label1 = QtWidgets.QLabel(label_value)
            self.label1.setFont(font)
            self.label1.setStyleSheet("color:#757575")
            layout.addWidget(self.label1)

        layout.addStretch()

        self.setLayout(layout)