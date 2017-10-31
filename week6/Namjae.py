import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        incButton = QPushButton("Inc")
        findButton = QPushButton("Find")
        showButton = QPushButton("Show")
        nameLabel = QLabel('Name : ')
        ageLabel = QLabel('Age : ')
        scoreLabel = QLabel('Score : ')
        amountLabel = QLabel('Amount : ')
        keyLabel = QLabel('Key : ')
        resultLabel = QLabel('Result : ')
        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyCombo = QComboBox()
        self.keyCombo.addItem('Name')
        self.keyCombo.addItem('Age')
        self.keyCombo.addItem('Score')
        self.resultText = QTextEdit()
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(nameLabel)
        hbox1.addWidget(self.nameEdit)
        hbox1.addWidget(ageLabel)
        hbox1.addWidget(self.ageEdit)
        hbox1.addWidget(scoreLabel)
        hbox1.addWidget(self.scoreEdit)
        hbox2 = QHBoxLayout()
        hbox2.addStretch()
        hbox2.addWidget(amountLabel)
        hbox2.addWidget(self.amountEdit)
        hbox2.addWidget(keyLabel)
        hbox2.addWidget(self.keyCombo)
        hbox3 = QHBoxLayout()
        hbox3.addStretch()
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)
        hbox4 = QHBoxLayout()
        hbox4.addWidget(resultLabel)
        hbox4.addStretch()
        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.resultText)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        addButton.clicked.connect(self.addDB)
        delButton.clicked.connect(self.delDB)
        findButton.clicked.connect(self.findDB)
        incButton.clicked.connect(self.incDB)
        showButton.clicked.connect(self.showScoreDB)

        self.showScoreDB()
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.setLayout(vbox)
        self.show()

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
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

    def getIndex(self, db, name):
        res = []
        for idx, p in enumerate(db):
            if p['Name'] == name:
                res += [idx]
        return res

    def addDB(self):
        try:
            record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
        except ValueError:
            print("(add)Argument Error(Value Error)")
        else:
            self.scoredb += [record]
        self.showScoreDB()

    def delDB(self):
        idx = self.getIndex(self.scoredb, self.nameEdit.text())
        count = len(idx)
        while count:
            del self.scoredb[idx[count - 1]]
            count -= 1
        self.showScoreDB()

    def findDB(self):
        self.resultText.setText("")
        for idx in self.getIndex(self.scoredb, self.nameEdit.text()):
            for attr in self.scoredb[idx]:
                self.resultText.insertPlainText(attr + "=" + str(self.scoredb[idx][attr]) + "\t")
            self.resultText.append("")

    def incDB(self):
        try:
            val = int(self.amountEdit.text())
        except ValueError:
            print("(inc)Argument Error(Value Error)")
        else:
            for idx in self.getIndex(self.scoredb, self.nameEdit.text()):
                self.scoredb[idx]['Score'] += val
        self.showScoreDB()

    def showScoreDB(self):
        self.resultText.setText("")
        try:
            for p in sorted(self.scoredb, key=lambda person: person[self.keyCombo.currentText()]):
                for attr in sorted(p):
                    self.resultText.insertPlainText(attr + "=" + str(p[attr]) + "\t")
                self.resultText.append("")
        except AttributeError:
            self.resultText.setText("None")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
