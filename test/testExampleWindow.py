from PyQt6.QtWidgets import QApplication, QMainWindow

from extendUI.ExampleWindowExt import ExampleWindowExt

app = QApplication([])
myWindow = ExampleWindowExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()