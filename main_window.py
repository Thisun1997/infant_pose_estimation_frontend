import sys

from PyQt5 import QtWidgets

from home_page import HomeWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Infant Pose Visualizer")
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.homeWidget = HomeWindow(parent=self.stacked_widget)
        self.stacked_widget.addWidget(self.homeWidget)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
