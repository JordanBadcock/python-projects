from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class Widgets(QDialog):
    def __init__(self):
        super().__init__()

        # Main layout
        layout = QVBoxLayout()
        title = QLabel("<h1 style=color:purple;>Sweat Society Application</h1>")
        layout.addWidget(title)

        # Combo box
        quantity = QComboBox()
        choices = { "Playstation": 1, "PC": 2, "XBOX": 3, "Nintendo": 4,}
        quantity.addItems(choices.keys())
        quantity_label = QLabel("<h2>Select which console you use.</h2>")
        quantity_label.setBuddy(quantity)

        # Submit button
        button = QPushButton("Submit application")

        self.create_radio_group()
        self.create_checkbox_group()
        self.create_text_edit()

        # Adding widgets to main layout
        layout.addWidget(title)
        layout.addWidget(quantity_label)
        layout.addWidget(quantity)
        layout.addWidget(self.radio_group)
        layout.addWidget(self.checkbox_group)
        layout.addWidget(self.text_group)
        layout.addWidget(button)
        self.setLayout(layout)
    
    def create_checkbox_group(self):
        # Group of checkbox widgets 
        self.checkbox_group = QGroupBox("Select the game(s) you are applying for.")
        checkbox_layout = QHBoxLayout()
        checkbox_1 = QCheckBox("Fortnite")
        checkbox_2 = QCheckBox("Call of Duty")
        checkbox_3 = QCheckBox("Super Smash Bros")
        checkbox_4 = QCheckBox("Rainbow Six: Siege")
        checkbox_5 = QCheckBox("Other")
        checkbox_layout.addWidget(checkbox_1)
        checkbox_layout.addWidget(checkbox_2)
        checkbox_layout.addWidget(checkbox_3)
        checkbox_layout.addWidget(checkbox_4)
        checkbox_layout.addWidget(checkbox_5)

        self.checkbox_group.setLayout(checkbox_layout)

    def create_radio_group(self):
        # Group of Radio buttons
        self.radio_group = QGroupBox("Select your KD.")
        radio_layout = QVBoxLayout()
        radio_1 = QRadioButton(">1")
        radio_2 = QRadioButton("1.00-1.50")
        radio_3 = QRadioButton("1.50-2.00")
        radio_4 = QRadioButton(">2.00")
        radio_layout.addWidget(radio_1)
        radio_layout.addWidget(radio_2)
        radio_layout.addWidget(radio_3)
        radio_layout.addWidget(radio_4)
        
        self.radio_group.setLayout(radio_layout)

    def create_text_edit(self):
        # Text box
        self.text_group = QGroupBox()
        text_layout = QVBoxLayout()
        text_label = QLabel('Add in any additional info we may be interested in.')
        textbox = QTextEdit()
        text_layout.addWidget(text_label)
        text_layout.addWidget(textbox)
        self.text_group.setLayout(text_layout)
    
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    widgets = Widgets()
    widgets.show()
    sys.exit(app.exec_())
