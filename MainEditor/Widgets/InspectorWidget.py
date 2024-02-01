from PySide6.QtWidgets import QWidget, QVBoxLayout


class InspectorWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(InspectorWidget, self).__init__(*args, **kwargs)
        self.mainLayout = QVBoxLayout()

