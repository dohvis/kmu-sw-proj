import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt

# self.score_combo.QComboBox()
# self.score_combo.addItem("Name" ...
# self.score_combo.currentText()

class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

        name = QLabel('Name: ')
        age = QLabel('Age: ')
        score = QLabel('Score: ')
        amount = QLabel('Amount: ')
        key = QLabel('Key: ')
        result = QLabel('Result:')

        self.addButton = QPushButton('Add')
        self.delButton = QPushButton('Del')
        self.findButton = QPushButton('Find')
        self.incButton = QPushButton('Inc')
        self.showButton = QPushButton('Show')

        self.addButton.clicked.connect(self.addScoreDB)
        self.delButton.clicked.connect(self.delScoreDB)
        self.findButton.clicked.connect(self.findScoreDB)
        self.incButton.clicked.connect(self.incScoreDB)
        self.showButton.clicked.connect(self.showScoreDB)

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.resultEdit = QTextEdit()

        self.keyCombo = QComboBox()
        self.keyCombo.addItem('Name')
        self.keyCombo.addItem('Age')
        self.keyCombo.addItem('Score')

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()

        hbox1.addWidget(name)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(age)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoreEdit)

        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keyCombo)

        hbox3.addStretch(1)
        hbox3.addWidget(self.addButton)
        hbox3.addWidget(self.delButton)
        hbox3.addWidget(self.findButton)
        hbox3.addWidget(self.incButton)
        hbox3.addWidget(self.showButton)

        hbox4.addWidget(result)
        hbox5.addWidget(self.resultEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    # add
    def addScoreDB(self):
        try:
            data = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
            self.scoredb += [data]
            self.showButton.click()
        except ValueError:
            ermsg = QMessageBox.critical(self, 'Error', 'You have to input Name, Age and Score !!')

    # delete
    def delScoreDB(self):
        new_list = []
        for p in self.scoredb:
            if p['Name'] != self.nameEdit.text():
                new_list += [p]
        self.scoredb[:] = new_list[:]
        self.showButton.click()

    # find
    def findScoreDB(self):
        result_str = ""
        for p in self.scoredb:
            if p['Name'] == self.nameEdit.text():
                for attr in sorted(p):
                    result_str += attr + " = " + str(p[attr]) + "    "
                self.resultEdit.setText(result_str)
                result_str += "\n"

    # increase
    def incScoreDB(self):
        try:
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    p['Score'] += int(self.amountEdit.text())
            self.showButton.click()
        except ValueError:
            ermsg = QMessageBox.critical(self, 'Error', 'Amount value must be integer !!')

    # show
    def showScoreDB(self):
        keyname = self.keyCombo.currentText()
        result_str = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                result_str += attr + " = " + str(p[attr]) + "    "
            self.resultEdit.setText(result_str)
            result_str += "\n"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())