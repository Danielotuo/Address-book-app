from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
from PyQt5.uic import loadUiType

class AddContact(QtWidgets.QDialog):
    def __init__(self, model):
        super(AddContact, self).__init__()
        self.w = uic.loadUi('add.ui', self)
        print('add.ui')
        self.model = model
        self.w.show()
        self.w.buttonBox.accepted.connect(self.addContact)

    def addContact(self):
        print('add')
        firstname = self.w.lineEditFirstName.text()
        lastname = self.w.lineEditLastName.text()
        email = self.w.lineEditEmail.text()
        
        row = (QStandardItem(firstname), QStandardItem(lastname), QStandardItem(email) )
        self.model.appendRow(row)

class Contact(QtWidgets.QMainWindow):
    def __init__(self):
        super(Contact, self).__init__()
        uic.loadUi('window.ui', self)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['First Name', 'Last Name', 'Email'])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(1)

        row = (QStandardItem('username'), QStandardItem('username'), QStandardItem('username@gamil.com') )
        self.model.appendRow(row)

        self.actionNew.triggered.connect(self.addContact)

    def addContact(self):
        print('add item')
        add = AddContact(self.model)

app = QtWidgets.QApplication([])
win = Contact()
win.show()
sys.exit(app.exec())