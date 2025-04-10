import sys
import service.serial_check as sch
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

# =============
# INIT COMS
# =============
sch.print_available_ports()
# =============
# WINDOW
# =============
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
