import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QGroupBox,
      QHBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QRadioButton, 
      QVBoxLayout, QWidget, QGridLayout)

class AreaCalculator(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('CP1890 Final - Jordan Badcock')
        self.main_layout = QVBoxLayout()

        self.title = QLabel('<h1 style="color: black">Area Calculator</h1>')
        self.title.setAlignment(Qt.AlignCenter)
        self.form = QFormLayout()

        self.base = QLineEdit()
        self.height = QLineEdit()

        self.form.addRow('Base:', self.base)
        self.form.addRow('Height:', self.height)

        self.radio_group = QGroupBox("Select Shape:")
        self.radio_layout = QVBoxLayout()
        self.rectangle_btn = QRadioButton("Rectangle")
        self.triangle_btn = QRadioButton("Triangle")
        self.radio_layout.addWidget(self.rectangle_btn)
        self.radio_layout.addWidget(self.triangle_btn)

        self.radio_group.setLayout(self.radio_layout)

        self.btn_layout = QHBoxLayout()
        self.calculate_btn = QPushButton('Calculate area')
        self.btn_layout = QHBoxLayout()
        self.clear_btn = QPushButton('Clear')
        self.btn_layout.addWidget(self.calculate_btn)
        self.btn_layout.addWidget(self.clear_btn)

        self.main_layout.addWidget(self.title)
        self.main_layout.addLayout(self.form)
        self.main_layout.addWidget(self.radio_group)
        self.main_layout.addLayout(self.btn_layout)
        self.setLayout(self.main_layout)

        self.clear_btn.clicked.connect(self.base.clear)
        self.clear_btn.clicked.connect(self.height.clear)

        self.calculate_btn.clicked.connect(self.area_calc)

    def area_calc(self):
        base = int(self.base.text())
        height = int(self.height.text())

        if self.rectangle_btn.isChecked():
            a = Rectangle(base, height)
            print(a)
        
        elif self.triangle_btn.isChecked():
            a = Triangle(base, height)
            print(a)

        else:
            a = Shape(base, height)
            print(a)

class Shape: 
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __str__(self):
        return f'Shape object | {self.base} {self.height}'


class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)
    
    def __str__(self):
        return f'Rectangle object | base = {self.base}, height = {self.height}, area = {self.area()}'

    def area(self):
        area = self.base * self.height
        return format(area, '.1f')
    
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)
    
    def __str__(self):
        return f'Triangle object | base = {self.base}, height = {self.height}, area = {self.area()}'

    def area(self):
        area = (self.base * self.height)/2
        return format(area, '.1f')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = AreaCalculator()
    dlg.show()
    sys.exit(app.exec_())