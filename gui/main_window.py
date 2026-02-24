import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

def Window():
    app=QApplication(sys.argv)
    Win=QMainWindow()
    Win.setGeometry(520,960,400,400)
    Win.setWindowTitle("Linux System Monitor")
    Win.show()
    sys.exit(app.exec_())

Window()