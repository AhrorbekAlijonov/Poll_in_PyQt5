import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QApplication,
    QHBoxLayout,
    QVBoxLayout
    )

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__init()
        
        
    def on(self):
        with open('userinformation.txt', 'w') as file:
            file.write(self.name_edit.text() + '|')
            file.write(self.age_edit.text() + '|')
            file.write(self.job_edit.text() + '|')
            file.write(self.hobbies_edit.text() + '|')
            self.close()
        
    def __init(self):    
        self.setWindowTitle("QDialog")
        self.setFixedSize(400, 250)
        
        # vertical and horizontal 
        self.v_box = QVBoxLayout()
        self.hh_box = QHBoxLayout()
        
        #layouts
        self.h_box = QHBoxLayout()
        self.h2_box = QHBoxLayout()
        self.h3_box = QHBoxLayout()
        self.h4_box = QHBoxLayout()
        
        # labels
        self.name = QLabel("Name: ")
        self.age = QLabel("Age: ")
        self.job = QLabel("Job: ")
        self.hobbies = QLabel("Hobbies: ")
        
        self.name.setFixedSize(100, 30)
        self.age.setFixedSize(100, 30)
        self.job.setFixedSize(100, 30)
        self.hobbies.setFixedSize(100, 30)
        
        

        self.name_edit = QLineEdit()
        self.age_edit = QLineEdit()
        self.job_edit = QLineEdit()
        self.hobbies_edit = QLineEdit()
        
        
        self.cancel = QPushButton("❌Cancel")
        self.cancel.clicked.connect(self.close)
        
        self.ok_btn = QPushButton("✅OK")
        self.ok_btn.clicked.connect(self.on)
        
        
        
        self.h_box.addWidget(self.name)
        self.h_box.addWidget(self.name_edit)
        
        self.h2_box.addWidget(self.age)
        self.h2_box.addWidget(self.age_edit)
        
        self.h3_box.addWidget(self.job)
        self.h3_box.addWidget(self.job_edit)
        
        self.h4_box.addWidget(self.hobbies)
        self.h4_box.addWidget(self.hobbies_edit)
        
        self.hh_box.addWidget(self.cancel)
        
        self.hh_box.addWidget(self.ok_btn)
        
        
        self.v_box.addLayout(self.h_box)
        self.v_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.v_box.addLayout(self.h2_box)
        self.v_box.addLayout(self.h3_box)
        self.v_box.addLayout(self.h4_box)
        self.v_box.addLayout(self.hh_box)
        
        
        self.setLayout(self.v_box)
        
        self.show()


app = QApplication([])
win = Window()
app.exec_()