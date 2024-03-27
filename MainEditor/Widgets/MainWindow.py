from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout, QFrame, QSizePolicy

from MainEditor.Widgets.InspectorWidget import InspectorWidget
from MainEditor.Widgets.GameWidget import GameWidget
from MainEditor.Widgets.HierarchyWidget import HierarchyWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        layout = QHBoxLayout()

        line1 = QFrame()
        line1.setFrameStyle(QFrame.VLine | QFrame.Plain)
        line2 = QFrame()
        line2.setFrameStyle(QFrame.VLine | QFrame.Plain)

        self.inspector = InspectorWidget()
        policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        policy.setHorizontalStretch(2)
        policy.setVerticalStretch(1)
        self.inspector.setSizePolicy(policy)

        self.game = GameWidget()
        policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        policy.setHorizontalStretch(5)
        policy.setVerticalStretch(1)
        self.game.setSizePolicy(policy)

        self.hierarchy = HierarchyWidget()
        policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        policy.setHorizontalStretch(2)
        policy.setVerticalStretch(1)
        self.hierarchy.setSizePolicy(policy)

        layout.addWidget(self.inspector)
        layout.addWidget(line1)
        layout.addWidget(self.game)
        layout.addWidget(line2)
        layout.addWidget(self.hierarchy)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
