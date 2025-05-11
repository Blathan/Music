from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize


class InstrumentButton(QPushButton):
    def __init__(self, text="", icon_path=None, parent=None):
        super().__init__(text, parent)
        self.selected = False
        self.icon_path = icon_path
        self.set_default_style()
        if icon_path:
            icon = QIcon(QPixmap(icon_path).scaled(256, 256))
            self.setIcon(icon)
            self.setIconSize(QSize(256, 256))

    def set_default_style(self):
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

    def set_selected(self, selected):
        self.selected = selected
        if selected:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #ffe6f0;
                    border: 3px solid hotpink;
                    border-radius: 12px;
                    font-size: 14px;
                }
            """)
        else:
            self.set_default_style()
