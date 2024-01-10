from PySide6.QtWidgets import (
    QMainWindow, QApplication, QWidget,
    QGridLayout, QFrame, QPushButton,
    QHBoxLayout, QVBoxLayout, QSpacerItem,
    QSizePolicy
)

#from PySide6.QtGui import QIcon, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Kanban Project")

        
        self.main_widget = QWidget() # Criação de widget principal
        self.main_layout = QGridLayout() # Criação de layout principal do tipo grid
        self.main_widget.setLayout(self.main_layout)

        self.main_widget.setStyleSheet("background-color: #4f94ff;") # Estilização do widget principal
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setCentralWidget(self.main_widget) # Tornano o main.widget em widget central da MainWindow

        ''' 
         Para organizar os widgets e layouts segudários escolhi o GridLayout
        '''

        self.vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Ignored, QSizePolicy.Expanding)

        # QFrame superior
        self.superior_frame = QFrame()
        self.superior_frame_layout = QHBoxLayout()
        self.superior_frame.setLayout(self.superior_frame_layout)
        self.superior_frame.setStyleSheet("QFrame { border-right: 1px solid black; border-bottom: 1px solid black; border-top: 1px solid black; }")
        self.superior_frame.setFixedHeight(80)
        self.main_layout.addWidget(self.superior_frame, 0, 1, 1, 3)

        # QFrame lateral
        self.left_frame = QFrame()
        self.left_frame_layout = QVBoxLayout()
        self.left_frame.setLayout(self.left_frame_layout)
        self.left_frame.setFrameShape(QFrame.Box)
        self.left_frame.setFixedWidth(80)
        self.main_layout.addWidget(self.left_frame, 0, 0, 3, 1)

        self.do_btn = QPushButton("To do")
        self.do_btn.setStyleSheet("background-color: white; border-radius: 10px;  ")
        self.left_frame_layout.addWidget(self.do_btn)

        self.doing_btn = QPushButton("Doing")
        self.doing_btn.setStyleSheet("background-color: white; border-radius: 10px;  ")
        self.left_frame_layout.addWidget(self.doing_btn)

        self.left_frame_layout.addSpacerItem(self.vertical_spacer)

        # QFrame central
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("QFrame { border-top: 0px solid black; border-right: 1px solid black; border-bottom: 1px solid black; }")
        self.central_frame.setFrameShape(QFrame.Box)
        self.main_layout.addWidget(self.central_frame, 1, 1, 2, 3)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()