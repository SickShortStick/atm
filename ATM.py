import sys
from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QPushButton,
    QGridLayout, QVBoxLayout, QApplication,
    QHBoxLayout, QStackedWidget, QMainWindow,
    QLabel
)

localization = {
    'فارسی' : {
                    'password_label' : 'رمز خود را وارد کنید',

                },
    'English' : {
                    'password_label' : 'Enter your password',

                }
}


class LanguageSelect(QWidget):

    def __init__(self):
        self.hbox_layout = QHBoxLayout(self)
        self.vbox_layout = QVBoxLayout(self)
        self.label = QLabel('Choose your language' \
        'زبان خود را انتخاب کنید')
        self.persian_btn = QPushButton('فارسی')
        self.english_btn = QPushButton('English')
        self.english_btn.clicked.connect(lambda new_language=self.english_btn.text(): change_language(new_language))
        self.persian_btn.clicked.connect(lambda new_language=self.persian_btn.text(): change_language(new_language))
        self.hbox_layout.addWidget(self.english_btn)
        self.hbox_layout.addWidget(self.persian_btn)
        self.vbox_layout.addWidget(self.label)
        self.vbox_layout.addLayout(self.hbox_layout)
    

class PasswordPage(QWidget):

    def __init__(self):
        self.vbox_layout = QVBoxLayout(self)
        self.


def change_language(new_language):
    pass
        

class MainWindow(QMainWindow):
    def __init__(self):
        self.language = 'English'
        self.setCentralWidget(LanguageSelect)
        


app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.ex)