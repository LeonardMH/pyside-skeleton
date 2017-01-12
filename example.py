from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import sys


def load_ui_widget(filename, parent):
    loader = QUiLoader()
    uifile = QFile(filename)
    uifile.open(QFile.ReadOnly)
    loader.load(uifile, parent)
    uifile.close()


class ExampleWidget(QWidget):
    def __init__(self, filepath):
        super(ExampleWidget, self).__init__()
        load_ui_widget(filepath, parent=self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ExampleWidget("example.ui")

    sys.exit(app.exec_())
