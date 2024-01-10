from PySide6.QtWidgets import (
    QMainWindow, QApplication
)

#from PySide6.QtGui import QIcon, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface pra Gabriela se localizar")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()