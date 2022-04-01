# import necessary modules and classes
import sys
from tabnanny import check
from PyQt5.QtWidgets import (QWidget,QApplication,QLabel,QTextEdit,QLineEdit,QPushButton,QCheckBox,QGridLayout,QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ToDoListGUI(QWidget):
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
        # Create Grid System Layout:
        main_grid = QGridLayout()
        
        # Create Components
        
        # 1 : Title
        todo_title = QLabel("To Do List")
        todo_title.setFont(QFont("Tahoma",24))
        todo_title.setAlignment(Qt.AlignCenter)
        
        # 2 : Close Button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        
        # 3 : Create labels
        mustdo_lbl = QLabel("Must Dos")
        mustdo_lbl.setFont(QFont("Tahoma",20))
        mustdo_lbl.setAlignment(Qt.AlignCenter)
        
        appoint_lbl = QLabel("Appointments")
        appoint_lbl.setFont(QFont("Tahoma",20))
        appoint_lbl.setAlignment(Qt.AlignCenter)
        
        # 4 : Create must-do section
        mustdo_grid = QGridLayout()
        mustdo_grid.setContentsMargins(5, 5, 5, 5)
        mustdo_grid.addWidget(mustdo_lbl, 0, 0, 1, 2)
        
        #  Create CheckBoxes and LineEdits widgets:
        for position in range(1, 10):
            checkbox = QCheckBox()
            checkbox.setChecked(False)
            linedit = QLineEdit()
            linedit.setMinimumWidth(200)
            mustdo_grid.addWidget(checkbox, position, 0)
            mustdo_grid.addWidget(linedit, position, 1)
        
        # 5: Create labels for appointments section
        morning_lbl = QLabel("Morning")
        morning_lbl.setFont(QFont("Tahoma",16))
        morning_entry = QTextEdit()
        
        noon_lbl = QLabel("Noon")
        noon_lbl.setFont(QFont("Tahoma",16))
        noon_entry = QTextEdit()
        
        evening_lbl = QLabel("Evening")
        evening_lbl.setFont(QFont("Tahoma",16))  
        evening_entry = QTextEdit()
        
        # Create Verical Layout:
        appt_v_box = QVBoxLayout()
        appt_v_box.setContentsMargins(5, 5, 5, 5)
        appt_v_box.addWidget(appoint_lbl)
        
        appt_v_box.addWidget(morning_lbl)
        appt_v_box.addWidget(morning_entry)
        
        appt_v_box.addWidget(noon_lbl)
        appt_v_box.addWidget(noon_entry)
        
        appt_v_box.addWidget(evening_lbl)
        appt_v_box.addWidget(evening_entry)
        
        # Add other layouts to main grid layout:
        main_grid.addWidget(todo_title, 0, 0, 1, 2)
        main_grid.addLayout(mustdo_grid, 1, 1)
        main_grid.addLayout(appt_v_box, 1, 0)
        main_grid.addWidget(close_btn, 2, 0 , 1, 2)
        
        self.setLayout(main_grid)
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    todolist = ToDoListGUI()
    sys.exit(app.exec_())
        
        