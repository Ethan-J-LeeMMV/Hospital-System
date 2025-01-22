import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTableView, QPlainTextEdit
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import Qt, QItemSelectionModel


from clinic.gui.login_gui import LoginGUI
from clinic.controller import Controller
from clinic.gui.table_model import TableModel
from clinic.gui.add_patient_window import AddpatientWindow


class ClinicGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # Continue here with your code!
        self.controller = Controller(True)
        self.login_screen = LoginGUI(self.controller)
        self.table_model = TableModel(self.controller)
        self.add_patient_window = AddpatientWindow(self.controller, self.table_model)


        # add_patient table
        self.table = QTableView()
        self.table.setModel(self.table_model)


        if self.controller.is_logged != True:
            self.show_login()
        else:
            self.show()

        self.login_screen.login_successful.connect(self.show_main_window)
        self.add_patient_window.window_closed.connect(self.enable_main)

        self.text_search = QLineEdit()
        self.search_button = QPushButton("search")
        layout = QGridLayout()
        self.logout_button = QPushButton("logout")
        self.delete_button = QPushButton("delete")
        layout.addWidget(self.text_search, 0, 0)
        layout.addWidget(self.search_button, 0, 1)
        layout.addWidget(self.logout_button, 0, 3)
        layout.addWidget(self.delete_button, 0, 2)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Add the first table
        layout.addWidget(self.table, 1, 0, 1, 3)

        # Add buttons
        self.add_patient_button = QPushButton("add patient")
        layout.addWidget(self.add_patient_button, 3, 0)


        self.logout_button.clicked.connect(self.logout)
        self.add_patient_button.clicked.connect(self.add_patient)
        self.search_button.clicked.connect(self.search)
        self.table.selectionModel().selectionChanged.connect(self.selected_row)
        self.delete_button.clicked.connect(self.delete)

    def show_login(self):
        self.login_screen.show()

    def show_main_window(self):
        self.show()
        self.table_model.refresh_data()

    def logout(self):
        self.controller.logout()
        self.hide()
        self.show_login()

    def add_patient(self):
        self.setEnabled(False)
        self.add_patient_window.show()

    

    def enable_main(self):
        self.setEnabled(True)

    """Handles how we search for patients"""
    def search(self):
        search_string = self.text_search.text().strip()
        if search_string != "":
            if search_string.isnumeric():
                patient = self.controller.search_patient(int(search_string))
                if patient is not None:
                    self.table_model.phn_search_table(patient)
                else:
                    QMessageBox.warning(self, "Search", "Patient not found")
            else:
                patient_list = self.controller.retrieve_patients(search_string)
                if patient_list is not None:
                    self.table_model.string_search_table(patient_list)
                else:
                    QMessageBox.warning(self, "Search", "Patient not found")
        else:
            self.table_model.refresh_data()

    def selected_row(self):
        selected_indices = self.table.selectionModel().selectedRows()
        return selected_indices[0].row()


    def delete(self):
        row_num = self.selected_row()
        if row_num is not None:
            phn = int(self.table_model.get_phn(row_num))
            self.controller.delete_patient(phn)
            self.table_model.refresh_data()


def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    app.exec()


if __name__ == '__main__':
    main()
