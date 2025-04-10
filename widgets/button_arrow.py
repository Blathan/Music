from PyQt5.QtWidgets import QPushButton, QStyle, QGraphicsColorizeEffect
from PyQt5 import QtGui
from PyQt5.QtCore import QSize, QPropertyAnimation, QEasingCurve


class ArrowButton(QPushButton):
    def __init__(self, direction="up", parent=None):
        super().__init__(parent)
        icon_type = QStyle.SP_ArrowUp if direction == "up" else QStyle.SP_ArrowDown
        self.setIcon(self.style().standardIcon(icon_type))
        self.setIconSize(QSize(70, 70))
        self.setFixedSize(150, 150)

        self.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(93, 12, 255, 255),
                    stop:1 rgba(155, 0, 250, 255)
                );
                color: white;
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:1, x2:1, y2:0,
                    stop:0 rgba(120, 50, 255, 255),
                    stop:1 rgba(170, 80, 255, 255)
                );
            }
        """)

        self.effect = QGraphicsColorizeEffect(self)
        self.setGraphicsEffect(self.effect)
        self.animation = QPropertyAnimation(self.effect, b"color")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.enterEvent = self._start_hover
        self.leaveEvent = self._end_hover

    def _start_hover(self, event):
        self.animation.stop()
        self.animation.setStartValue(self.effect.color())
        self.animation.setEndValue(QtGui.QColor(100, 100, 255))
        self.animation.start()

    def _end_hover(self, event):
        self.animation.stop()
        self.animation.setStartValue(self.effect.color())
        self.animation.setEndValue(QtGui.QColor(0, 0, 0, 0))
        self.animation.start()
