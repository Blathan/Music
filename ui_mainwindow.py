from PyQt5 import QtWidgets, QtGui, QtCore
from widgets.button_instrument import InstrumentButton
from widgets.instrument_menu import InstrumentMenu
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("\U0001F3B5 Music")
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
        title = QtWidgets.QLabel("\U0001F3B6 Music App")
        title.setStyleSheet(
            "color: white; font-size: 28px; font-weight: bold;")
        settings = QtWidgets.QPushButton("\u2699")
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

        add_button = QtWidgets.QPushButton("\u2795 Add Custom Lib")
        add_button.setMinimumHeight(48)
        add_button.setMaximumWidth(200)
        add_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #5d0cff;
                font-size: 16px;
                font-weight: bold;
                border-radius: 12px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #f0eaff;
            }
        """)
        add_button.clicked.connect(self.show_add_instrument_dialog)
        main_layout.addWidget(add_button, alignment=QtCore.Qt.AlignLeft)

        # Scrollable horizontal instrument bar
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("background: transparent; border: none;")

        scroll_content = QtWidgets.QWidget()
        h_layout = QtWidgets.QHBoxLayout(scroll_content)
        h_layout.setContentsMargins(10, 10, 10, 10)
        h_layout.setSpacing(20)

        self.buttons = []
        self.selected_button = None

        instrument_names = ["Piano", "Drums", "Guitar", "Violin"]

        for i in range(4):
            btn = InstrumentButton("", f"icons/{i+1}.png")
            btn.setMinimumSize(350, 350)
            btn.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                              QtWidgets.QSizePolicy.Preferred)
            btn.clicked.connect(lambda _, b=btn: self.select_instrument(b))
            self.buttons.append(btn)
            h_layout.addWidget(btn)

        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

        instrument_menu = InstrumentMenu(instrument_names)
        main_layout.addWidget(instrument_menu)

        MainWindow.setCentralWidget(central)

    def select_instrument(self, selected_button):
        for btn in self.buttons:
            btn.set_selected(btn == selected_button)

    def show_add_instrument_dialog(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Add Custom Instrument")
        layout = QtWidgets.QVBoxLayout(dialog)

        name_input = QtWidgets.QLineEdit()
        name_input.setPlaceholderText("Instrument Name")

        image_button = QtWidgets.QPushButton("Upload Image")
        image_path_label = QtWidgets.QLabel("No image selected")

        def load_image():
            path, _ = QtWidgets.QFileDialog.getOpenFileName(
                dialog, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
            if path:
                image_path_label.setText(path)

        image_button.clicked.connect(load_image)

        notes = ["До", "Ре", "Ми", "Фа", "Соль", "Ля", "Си", "До"]
        mp3_buttons = []
        mp3_paths = {}

        for note in notes:
            hlayout = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(note)
            btn = QtWidgets.QPushButton("Upload MP3")
            path_label = QtWidgets.QLabel("No file")

            def make_upload_function(note_key):
                def upload():
                    path, _ = QtWidgets.QFileDialog.getOpenFileName(
                        dialog, f"Select MP3 for {note_key}", "", "Audio Files (*.mp3)")
                    if path:
                        path_label.setText(os.path.basename(path))
                        mp3_paths[note_key] = path
                return upload

            btn.clicked.connect(make_upload_function(note))
            hlayout.addWidget(label)
            hlayout.addWidget(btn)
            hlayout.addWidget(path_label)
            layout.addLayout(hlayout)

        layout.addWidget(name_input)
        layout.addWidget(image_button)
        layout.addWidget(image_path_label)

        submit = QtWidgets.QPushButton("Save")
        layout.addWidget(submit)

        dialog.exec_()
