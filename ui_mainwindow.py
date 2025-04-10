from PyQt5 import QtWidgets, QtGui, QtCore
from widgets.button_instrument import InstrumentButton
from widgets.button_arrow import ArrowButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("🎵 Music")
        MainWindow.resize(1000, 700)

        MainWindow.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(93, 12, 255, 255),
                    stop:1 rgba(155, 0, 250, 255)
                );
            }
        """)

        central = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout(central)

        # AppBar
        appbar = QtWidgets.QHBoxLayout()
        title = QtWidgets.QLabel("🎶 Music App")
        title.setStyleSheet(
            "color: white; font-size: 28px; font-weight: bold;")
        settings = QtWidgets.QPushButton("⚙")
        settings.setFixedSize(36, 36)
        settings.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 20px;
                border: none;
            }
            QPushButton:hover {
                color: #ddddff;
            }
        """)
        appbar.addWidget(title)
        appbar.addStretch()
        appbar.addWidget(settings)
        main_layout.addLayout(appbar)

        # Content
        content = QtWidgets.QHBoxLayout()

        # Arrows (left)
        arrow_layout = QtWidgets.QVBoxLayout()
        arrow_layout.addStretch()
        arrow_up = ArrowButton("up")
        arrow_down = ArrowButton("down")
        arrow_layout.addWidget(arrow_up, alignment=QtCore.Qt.AlignHCenter)
        arrow_layout.addSpacing(40)
        arrow_layout.addWidget(arrow_down, alignment=QtCore.Qt.AlignHCenter)
        arrow_layout.addStretch()
        content.addLayout(arrow_layout, 1)

        # Instruments grid (right)
        grid_container = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout(grid_container)
        grid.setHorizontalSpacing(30)
        grid.setVerticalSpacing(30)

        self.buttons = []
        for i in range(4):
            btn = InstrumentButton("", f"icons/{i+1}.png")
            self.buttons.append(btn)
            grid.addWidget(btn, i // 2, i % 2)

        # Responsive size
        for btn in self.buttons:
            btn.setMinimumSize(100, 100)
            btn.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                              QtWidgets.QSizePolicy.Expanding)

        content.addWidget(grid_container, 3)
        main_layout.addLayout(content)

        MainWindow.setCentralWidget(central)
