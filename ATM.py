import sys
from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QPushButton,
    QGridLayout, QVBoxLayout, QApplication,
    QHBoxLayout, QStackedWidget, QMainWindow,
    QLabel
)

admin_password = 'admin'

localization = {
    'فارسی' : {
                    'password_label' : 'رمز خود را وارد کنید',
                    'password_submit' : 'ثبت',
                    'get_cash_btn' : 'برداشت وجه',
                    'change_password_btn' : 'رمز جدید',
                    'money_transfer' : 'کارت به کارت',
                    'account_balance_label' : 'موجودی',
                    'confirm_btn' : 'تایید',
                    'amount_label' : 'مبلغ را وارد کنید',
                    'card_number_label' : 'شماره کارت مقصد'
                },
    'English' : {
                    'password_label' : 'Enter your password',
                    'password_submit' : 'Submit',
                    'get_cash_btn' : 'Get Cash',
                    'change_password_btn' : 'Change Password',
                    'money_transfer' : 'Money Transfer',
                    'account_balance_label' : 'Account Balance',
                    'confirm_btn' : 'Confirm',
                    'amount_label' : 'Enter the desired amount:',
                    'card_number_label' : 'Enter destination card number:'
                }
}

balance = 1000000000
language = 'English'

class LanguageSelect(QWidget):

    def __init__(self):
        super().__init__()
        self.hbox_layout = QHBoxLayout(self)
        self.vbox_layout = QVBoxLayout(self)
        self.label = QLabel('Choose your language' \
        'زبان خود را انتخاب کنید')
        self.persian_btn = QPushButton('فارسی')
        self.english_btn = QPushButton('English')
        self.english_btn.clicked.connect(lambda _, new_language='English': change_language(new_language))
        self.persian_btn.clicked.connect(lambda _, new_language='فارسی': change_language(new_language))
        self.hbox_layout.addWidget(self.english_btn)
        self.hbox_layout.addWidget(self.persian_btn)
        self.vbox_layout.addWidget(self.label)
        self.vbox_layout.addLayout(self.hbox_layout)
    
def change_language(new_language):
    global language
    language = new_language
    main_window.password_page = PasswordPage()
    main_window.setCentralWidget(main_window.password_page)

class PasswordPage(QWidget):

    def __init__(self):
        super().__init__()
        self.vbox_layout = QVBoxLayout(self)

        self.password_line_edit = QLineEdit()
        self.password_label = QLabel(localization[language]['password_label'])
        self.submit_btn = QPushButton(localization[language]['password_submit'])


        self.vbox_layout.addWidget(self.password_label)
        self.vbox_layout.addWidget(self.password_line_edit)
        self.submit_btn.clicked.connect(lambda _: go_to_features_page())
        self.vbox_layout.addWidget(self.submit_btn)

def go_to_features_page():
    text = main_window.password_page.password_line_edit.text()
    if text == admin_password:
        main_window.setCentralWidget(FeaturesPage())

class FeaturesPage(QWidget):

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout(self)
        
        self.get_cash_btn = QPushButton(localization[language]['get_cash_btn'])
        self.change_password_btn = QPushButton(localization[language]['change_password_btn'])
        self.money_transfer = QPushButton(localization[language]['money_transfer'])
        self.account_balance = QPushButton(localization[language]['account_balance_label'])

        self.grid.addWidget(self.get_cash_btn)
        self.grid.addWidget(self.change_password_btn, 0, 1)
        self.grid.addWidget(self.money_transfer, 1, 0)
        self.grid.addWidget(self.account_balance, 1, 1)
        
        self.account_balance.clicked.connect(lambda _: main_window.setCentralWidget(AccountBalancePage()))
        self.get_cash_btn.clicked.connect(lambda _: main_window.setCentralWidget(GetCashPage()))

class AccountBalancePage(QWidget):

    def __init__(self):
        super().__init__()
        
        self.vbox_layout = QVBoxLayout(self)
        self.account_balance_label = QLabel(f'{localization[language]['account_balance_label']} : {balance}')
        self.confirm_btn = QPushButton(localization[language]['confirm_btn'])

        self.confirm_btn.clicked.connect(lambda _: main_window.setCentralWidget(FeaturesPage()))

        self.vbox_layout.addWidget(self.account_balance_label)
        self.vbox_layout.addWidget(self.confirm_btn)

class ChangePasswordPage(QWidget):

    def __init__(self):
        super().__init__()

        self.new_password_label = QLabel(localization[language]['new_password_label'])
        self.password_line_edit = QLineEdit()
        self.confirm_btn = QPushButton(localization[language]['confirm_btn'])

class GetCashPage(QWidget):

    def __init__(self):
        super().__init__()
        
        self.grid = QGridLayout(self)

        self.cash5_btn = QPushButton('500000')
        self.cash15_btn = QPushButton('1500000')
        self.cash10_btn = QPushButton('1000000')
        self.cash20_btn = QPushButton('2000000')

        self.grid.addWidget(self.cash5_btn)
        self.grid.addWidget(self.cash15_btn, 0, 1)
        self.grid.addWidget(self.cash10_btn, 1, 0)
        self.grid.addWidget(self.cash20_btn, 1, 1)

class MoneyTransferPage(QWidget):

    def __init__(self):
        super().__init__()
        
        self.vbox_layout = QVBoxLayout(self)

        self.amount_label = QLabel(localization[language]['amount_label'])
        self.amount_line_edit = QLineEdit()
        self.card_number_label = QLabel(localization[language]['card_number_label'])
        self.card_number_line_edit = QLineEdit()
        self.confirm_btn = QPushButton(localization[language]['confirm_btn'])

        self.vbox_layout.addWidget(self.amount_label)
        self.vbox_layout.addWidget(self.amount_line_edit)
        self.vbox_layout.addWidget(self.card_number_label)
        self.vbox_layout.addWidget(self.card_number_line_edit)
        self.vbox_layout.addWidget(self.confirm_btn)

        self.confirm_btn.clicked.connect(lambda _: main_window.setCentralWidget(FeaturesPage()))

class FinishedPage(QWidget):

    def __init__(self):
        super().__init__()

        self.vbox_layout = QVBoxLayout(self)
        self.hbox_layout = QHBoxLayout(self)

        self.operation_label = QLabel(localization[language]['operation_label'])
        self.exit_btn = QPushButton(localization[language]['exit_btn'])
        self.new_operation = QPushButton(localization[language]['new_operation'])

        self.vbox_layout.addWidget(self.operation_label)
        self.hbox_layout.addWidget(self.exit_btn)
        self.hbox_layout.addWidget(self.new_operation)
        self.vbox_layout.addLayout(self.hbox_layout)

        self.exit_btn.clicked.connect(lambda _: exit())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.language = 'English'
        self.setCentralWidget(LanguageSelect())


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())