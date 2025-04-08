from PyQt5 import QtWidgets
from widgets.button_instrument import InstrumentButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Music")

        central = QtWidgets.QWidget()
        main_layout = QtWidgets.QHBoxLayout(central)

        main_layout.addStretch()

        right_container = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout(right_container)

        self.buttons = []

        for i in range(4):
            btn = InstrumentButton(f"", f"icons/{i+1}.png")
            self.buttons.append(btn)
            row = i // 4
            col = i % 4
            grid.addWidget(btn, row, col)

        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addStretch()
        right_layout.addWidget(right_container)
        right_layout.addStretch()

        main_layout.addLayout(right_layout)

        MainWindow.setCentralWidget(central)
