import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTableView
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import pyqtSignal

from clinic.controller import Controller
from clinic.gui.table_model import TableModel

"""This class handles when we click the "add patient" button - a new window pops up"""
class AddpatientWindow(QMainWindow):
    window_closed = pyqtSignal()
    def __init__(self, controller, table_model):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.table_model = table_model


        self.setWindowTitle("add patient")
        label_phn = QLabel("PHN")
        label_name = QLabel("Name")
        label_dob = QLabel("Birthdate")
        label_phone = QLabel("Phone Number")
        label_email = QLabel("Email Address")
        label_address = QLabel("Address")

        self.text_phn = QLineEdit()
        self.text_name = QLineEdit()
        self.text_dob = QLineEdit()
        self.text_phone = QLineEdit()
        self.text_email = QLineEdit()
        self.text_address = QLineEdit()

        self.submit_button = QPushButton("add")
        self.cancel_button = QPushButton("cancel")

        self.submit_button.clicked.connect(self.add_patient)

        main_layout = QGridLayout()
        fields_layout = QGridLayout()
        main_layout.addLayout(fields_layout, 0, 0)
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(main_layout)
        fields_layout.addWidget(label_phn, 0, 0)
        fields_layout.addWidget(label_name, 1, 0)
        fields_layout.addWidget(label_dob, 2, 0)
        fields_layout.addWidget(label_phone, 3, 0)
        fields_layout.addWidget(label_email, 4, 0)
        fields_layout.addWidget(label_address, 5, 0)
        fields_layout.addWidget(self.text_phn, 0, 1)
        fields_layout.addWidget(self.text_name, 1, 1)
        fields_layout.addWidget(self.text_dob, 2, 1)
        fields_layout.addWidget(self.text_phone, 3, 1)
        fields_layout.addWidget(self.text_email, 4, 1)
        fields_layout.addWidget(self.text_address, 5, 1)
        main_layout.addWidget(self.submit_button, 1, 1)

    def add_patient(self):
        phn = self.text_phn.text().strip()
        name = self.text_name.text().strip()
        dob = self.text_dob.text().strip()
        phone = self.text_phone.text().strip()
        email = self.text_email.text().strip()
        address = self.text_address.text().strip()

        continue_checks = True
        if phn != "" and continue_checks:
            if not phn.isnumeric():
                QMessageBox.warning(self, "Add Patient", "phn must be a number")
                continue_checks = False
        else:
            QMessageBox.warning(self, "Add Patient", "PHN cannot be empty")
            continue_checks = False
        if name == "" and continue_checks:
            QMessageBox.warning(self, "Add Patient", "Name cannot be empty")
            continue_checks = False
        if dob == "" and continue_checks:
            QMessageBox.warning(self, "Add Patient", "Brithdate cannot be empty")
            continue_checks = False
        if phone == "" and continue_checks:
            QMessageBox.warning(self, "Add Patient", "Phone number cannot be empty")
            continue_checks = False
        if email != "" and continue_checks:
            if "@" not in email:
                QMessageBox.warning(self, "Add Patient", "Please enter a valid email")
                continue_checks = False
        elif continue_checks == True:
            QMessageBox.warning(self, "Add Patient", "Email cannot be empty")
            continue_checks = False
        if address == "" and continue_checks:
            QMessageBox.warning(self, "Add Patient", "Address cannot be empty")
            continue_checks = False
        if continue_checks == True and self.controller.search_patient(int(phn)) is not None:
            QMessageBox.warning(self, "Add Patient", "Patient already added")
            continue_checks = False
        elif continue_checks == True:
            self.controller.create_patient(phn, name, dob, phone, email, address)
            self.table_model.refresh_data()
        self.window_closed.emit()
        self.close() # close window when done 

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()

    def main():
        app = QApplication(sys.argv)
        window = AddpatientWindow()
        # window.show()
        app.exec()
