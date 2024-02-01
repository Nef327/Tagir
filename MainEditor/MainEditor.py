from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from Widgets.MainWindow import MainWindow
import sys

app = QApplication(sys.argv)


window = MainWindow()
window.resize(1366, 768)
window.setWindowTitle("Tagir")

window.show()
app.exec()