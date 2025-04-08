from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class InstrumentButton(QPushButton):
    def __init__(self, text="", icon_path=None, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #0d6efd;
                color: white;
                padding: 8px;
                border-radius: 6px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #0b5ed7;
            }
        """)
        if icon_path:
            self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(64, 64))
        self.setMinimumSize(80, 80)
