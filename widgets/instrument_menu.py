from PyQt5 import QtWidgets, QtCore


class InstrumentMenu(QtWidgets.QWidget):
    def __init__(self, instrument_names):
        super().__init__()

        self.instrument_names = instrument_names
        self.labels = []
        self.is_expanded = False
        self.animation_duration = 300

        self.container = QtWidgets.QWidget()
        self.container.setMaximumHeight(40)  # start collapsed
        self.container.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.container_layout = QtWidgets.QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)

        # Top bar: toggle and close buttons
        top_bar = QtWidgets.QHBoxLayout()
        self.toggle_button = QtWidgets.QPushButton("Instruments")
        self.toggle_button.clicked.connect(self.toggle_menu)
        self.toggle_button.setStyleSheet("""
            QPushButton {
                background-color: #5d0cff;
                color: white;
                padding: 6px 12px;
                border-radius: 15px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover {
                background-color: #7835ff;
            }
        """)
        self.close_button = QtWidgets.QPushButton("❌")
        self.close_button.setFixedSize(24, 24)
        self.close_button.clicked.connect(self.collapse_menu)
        self.close_button.hide()
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 16px;
                border: none;
            }
            QPushButton:hover {
                color: #ddddff;
            }
        """)
        top_bar.addWidget(self.toggle_button)
        top_bar.addStretch()
        top_bar.addWidget(self.close_button)

        self.container_layout.addLayout(top_bar)

        # Search field
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.filter_labels)
        self.search_bar.hide()
        self.search_bar.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: black;
                padding: 6px 12px;
                border-radius: 15px;
                border: 1px solid #ccc;
            }
        """)
        self.container_layout.addWidget(self.search_bar)

        # Bubble-style label row
        self.label_widget = QtWidgets.QWidget()
        self.label_layout = QtWidgets.QHBoxLayout(self.label_widget)
        self.label_layout.setContentsMargins(10, 5, 10, 5)
        self.label_layout.setSpacing(10)

        for name in instrument_names:
            lbl = QtWidgets.QLabel(name)
            lbl.setAlignment(QtCore.Qt.AlignCenter)
            lbl.setStyleSheet("""
                QLabel {
                    background-color: white;
                    color: #5d0cff;
                    padding: 6px 12px;
                    border-radius: 15px;
                    font-weight: bold;
                }
            """)
            self.labels.append(lbl)
            self.label_layout.addWidget(lbl)

        self.label_layout.addStretch()
        self.label_widget.hide()
        self.container_layout.addWidget(self.label_widget)

        # Outer layout
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.container)

    def toggle_menu(self):
        if self.is_expanded:
            self.collapse_menu()
        else:
            self.expand_menu()

    def expand_menu(self):
        self.is_expanded = True
        self.toggle_button.hide()
        self.close_button.show()
        self.search_bar.show()
        self.label_widget.show()

        self.anim = QtCore.QPropertyAnimation(self.container, b"maximumHeight")
        self.anim.setDuration(self.animation_duration)
        self.anim.setStartValue(40)
        self.anim.setEndValue(120)
        self.anim.start()

    def collapse_menu(self):
        self.is_expanded = False
        self.search_bar.hide()
        self.label_widget.hide()
        self.toggle_button.show()
        self.close_button.hide()

        self.anim = QtCore.QPropertyAnimation(self.container, b"maximumHeight")
        self.anim.setDuration(self.animation_duration)
        self.anim.setStartValue(self.container.height())
        self.anim.setEndValue(40)
        self.anim.start()

    def filter_labels(self, text):
        text = text.lower()
        for label in self.labels:
            label.setVisible(text in label.text().lower())
