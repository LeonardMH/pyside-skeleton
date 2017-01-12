from PySide.QtCore import QFile
from PySide.QtGui import QWidget, QApplication
from PySide.QtUiTools import QUiLoader


def load_ui_widget(filename, parent):
    loader = QUiLoader()
    uifile = QFile(filename)
    uifile.open(QFile.ReadOnly)
    loader.load(uifile, parent)
    uifile.close()


class ExampleApplication(QApplication):
    def __init__(self, **kwargs):
        super(ExampleApplication, self).__init__([], **kwargs)

    def start(self):
        self.exec_()


class ExampleWidget(QWidget):
    def __init__(self, filepath):
        super(ExampleWidget, self).__init__()
        load_ui_widget("example.ui", parent=self)
        self.setWindowTitle("PySide Example")
        self.show()


if __name__ == "__main__":
    app = ExampleApplication()
    widget = ExampleWidget("example.ui")
    app.start()
