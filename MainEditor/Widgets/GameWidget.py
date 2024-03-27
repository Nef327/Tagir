from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem
from PySide6.QtOpenGL import QOpenGLWindow


class GameWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(GameWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout()
        layout.addWidget(QSpacerItem(20, 40))
        #self.GLWindow = QOpenGLWindow()
        #layout.addWidget(self.GLWindow)

        layout.addWidget(QSpacerItem(20, 40))
        self.setLayout(layout)