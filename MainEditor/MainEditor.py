from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)


window = QMainWindow()
window.setWindowTitle("Tagir")

window.show()
app.exec()