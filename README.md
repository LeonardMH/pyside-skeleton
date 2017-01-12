# pyside-skeleton

A simple example of how to get started with PySide using a UI file
designed in Qt Designer. This is the easiest way to use Qt.

# Core Code

The essential code is show below (and contained in example.py).

```python
from PySide.QtGui import QWidget, QApplication
from PySide.QtUiTools import QUiLoader
from PySide.QtCore import QFile


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
```

# Screenshots

Here's what it looks like on Windows 10:

![pyside-barebones on Windows 10](/screenshots/windows10.png)
