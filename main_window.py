from PyQt5.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from controller import setup_connections


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        setup_connections(self.ui)
