import pickle
import sys
from PyQt5.QtWidgets import (
    QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit, QMainWindow
)


def createQHBoxLayout(widgets):
    layoutBox = QHBoxLayout()
    layoutBox.addStretch(1)
    for widget in widgets:
        layoutBox.addWidget(widget)
    return layoutBox


class ScoreManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.dbFileName = 'assignment6.dat'
        self.scoreDB = []
        self.keys = ('Age', 'Name', 'Score')
        self.initUI()

    @property
    def _infoBoxWidget(self):
        nameLabel = QLabel("Name: ", self)
        self.nameForm = QLineEdit(self)

        ageLabel = QLabel("Age: ", self)
        self.ageForm = QLineEdit(self)

        scoreLabel = QLabel('Score :', self)
        self.scoreForm = QLineEdit(self)

        return (
            nameLabel, self.nameForm,
            ageLabel, self.ageForm,
            scoreLabel, self.scoreForm,
        )

    @property
    def _optionBoxWidget(self):
        amountLabel = QLabel('Amount :', self)
        self.amountForm = QLineEdit(self)

        keyLabel = QLabel('Key: ', self)
        self.keyForm = QComboBox(self)
        self.keyForm.addItems(self.keys)
        return (
            amountLabel, self.amountForm,
            keyLabel, self.keyForm,
        )

    @property
    def _actionBoxWidget(self):
        addButton = QPushButton('Add', self)
        addButton.clicked.connect(self.add)

        delButton = QPushButton('Del', self)
        delButton.clicked.connect(self.del_)

        findButton = QPushButton('Find', self)
        findButton.clicked.connect(self.find)

        incButton = QPushButton('Inc', self)
        incButton.clicked.connect(self.inc)

        showButton = QPushButton('Show', self)
        showButton.clicked.connect(self.show_)

        return (
            addButton, delButton, findButton, incButton, showButton,
        )

    @property
    def _resultBoxWidget(self):
        resultLabel = QLabel('Result')
        self.resultForm = QTextEdit()
        return resultLabel, self.resultForm

    def renderResult(self):
        resultString = ''
        for row in self.scoreDB:
            resultString += '{} {} {}\n'.format(row['name'], row['age'], row['score'])
        self.resultForm.setText(resultString)

    def add(self):
        name, age, score = [form.text() for form in (self.nameForm, self.ageForm, self.scoreForm)]
        self.scoreDB.append({"name": name, "age": age, "score": score})
        self.renderResult()

    def del_(self):
        name = self.nameForm.text()
        index = self.findIndex(name)
        del self.scoreDB[index]
        self.renderResult()

    def find(self):
        name = self.nameForm.text()
        tmp = self.scoreDB
        self.scoreDB = filter(lambda x: x['name'] == name, self.scoreDB)
        self.renderResult()
        self.scoreDB = tmp

    def findIndex(self, name):
        for i, row in enumerate(self.scoreDB):
            if row['name'] == name:
                return i

    def inc(self):
        name = self.nameForm.text()
        amount = int(self.amountForm.text())
        for row in self.scoreDB:
            if row['name'] == name:
                row['score'] = int(row['score']) + amount

        self.renderResult()

    def show_(self):
        key = self.keyForm.currentText()
        newList = sorted(self.scoreDB, key=lambda k: k[key.lower()])
        self.scoreDB = newList
        self.renderResult()

    def closeEvent(self, event):
        self.saveScoreToDB()

    def readDB(self):
        try:
            fH = open(self.dbFileName, 'rb')
        except FileNotFoundError as e:
            self.scoreDB = []
            return

        try:
            self.scoreDB = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    def saveScoreToDB(self):
        with open(self.dbFileName, 'wb') as fH:
            pickle.dump(self.scoreDB, fH)
            fH.close()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        componentWidgets = [
            self._infoBoxWidget,
            self._optionBoxWidget,
            self._actionBoxWidget,
            self._resultBoxWidget,
        ]
        infoBox, optionBox, actionBox, resultBox = [createQHBoxLayout(widgets) for widgets in componentWidgets]

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        for box in (infoBox, optionBox, actionBox, resultBox):
            vbox.addLayout(box)
        self.setLayout(vbox)
        self.readDB()
        self.renderResult()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sm = ScoreManagement()
    sys.exit(app.exec_())
