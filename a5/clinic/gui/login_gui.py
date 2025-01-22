import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import pyqtSignal

from clinic.controller import Controller



class LoginGUI(QMainWindow):
    login_successful = pyqtSignal()

    def __init__(self, controller):
        super().__init__()
        # Continue here with your code!
        self.controller = controller
        self.setWindowTitle("Login")

        login_layout = QGridLayout()

        label_username = QLabel("Username")
        self.text_username = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()
        self.text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_button = QPushButton("Login")

        login_layout.addWidget(label_username, 0, 0)
        login_layout.addWidget(self.text_username, 0, 1)
        login_layout.addWidget(label_password, 1, 0)
        login_layout.addWidget(self.text_password, 1, 1)
        login_layout.addWidget(self.login_button, 2, 0)

        widget = QWidget()
        widget.setLayout(login_layout)
        self.setCentralWidget(widget)

        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.text_username.text().strip()
        password = self.text_password.text().strip()

        if username == "":
            QMessageBox.warning(self, "Login", "Please enter a username")
        elif password =="":
            QMessageBox.warning(self, "Login", "Please enter a password")
        else:
            if self.controller.login(username, password) == True:
                self.login_successful.emit()
                self.close()
            else:
                QMessageBox.warning(self, "Login failed", "username or password is not correct")



def main():
    app = QApplication(sys.argv)
    window = LoginGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
