import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello !")
        self.setGeometry(200, 100, 500, 400)

        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: white;")
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel("Centered Text")
        label.setAlignment(Qt.AlignHCenter)
        label.setFixedHeight(100)
        label.setStyleSheet("color: white; background-color: yellow;")
        layout.addWidget(label)

        l = QLabel("Hello")
        l.setAlignment(Qt.AlignHCenter)
        l.setFixedHeight(50)
        l.setStyleSheet("color: white; background-color: red;")
        layout.addWidget(l)

        layout.addStretch()

def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e :
        print(f"Error : {e}")

if __name__ == "__main__":
    main()
