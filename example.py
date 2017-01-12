import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


def load_ui_widget(filename, parent=None):
    loader = QUiLoader()
    uifile = QFile(filename)
    uifile.open(QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()

    return ui


class ExampleWidget(QWidget):
    def __init__(self, filepath):
        super(ExampleWidget, self).__init__()
        self.ui = load_ui_widget(filepath)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = ExampleWidget("example.ui")
    widget.ui.show()

    sys.exit(app.exec_())
