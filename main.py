import sys
import serial_check
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

# =============
# INIT COMS
# =============
serial_check.print_available_ports()

# =============
# WINDOW
# =============
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
