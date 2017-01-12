# pyside-skeleton

A simple example of how to get started with PySide using a UI file
designed in Qt Designer. This is the easiest way to use Qt.

# Core Code

The essential code is show below (and contained in example.py).

```python
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
```

# Screenshots

Here's what it looks like on Windows 10:

![pyside-barebones on Windows 10](/screenshots/windows10.png)

