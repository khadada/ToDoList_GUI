# import necessary modules and classes
import sys
from PyQt5.QtWidgets import (QMainWindow,QApplication,QLabel,QTextEdit,QLineEdit,QPushButton,QCheckBox,QGridLayout,QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ToDoListGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initalize_ui()
        self.show()
        
    def initalize_ui(self):
        """
        Initalize the main window to than add its components.
        """
        self.setWindowTitle("ToDoList v- 1.0")
        self.setGeometry(400, 50, 500, 350)
        self.add_components()
    
    def add_components(self):
        """
        Create widgets for to-do list gui in the main window.
        """
        