from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize


class InstrumentButton(QPushButton):
    def __init__(self, text="", icon_path=None, parent=None):
        super().__init__(text, parent)
        if icon_path:
            icon = QIcon(QPixmap(icon_path).scaled(256, 256))
            self.setIcon(icon)
            self.setIconSize(QSize(256, 256))

        self.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                border-radius: 12px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #e0e0ff;
            }
        """)
