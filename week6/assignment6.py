import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        self.scoredb = []
        self.dbfilename = 'assignment6.dat'
        super().__init__()
        self.initUI()
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()
        h_box4 = QHBoxLayout()
        h_box5 = QHBoxLayout()
        v_box = QVBoxLayout()
        v_box.addItem(h_box1)
        v_box.addItem(h_box2)
        v_box.addItem(h_box3)
        v_box.addItem(h_box4)
        v_box.addItem(h_box5)
        name_label = QLabel("Name: ")
        age_label = QLabel("Age: ")
        score_label = QLabel("Score: ")
        amount_label = QLabel("Amount: ")
        key_label = QLabel("Key: ")
        result_label = QLabel("Result: ")
        self.name_edit = QLineEdit()
        self.age_edit = QLineEdit()
        self.score_edit = QLineEdit()
        self.amount_edit = QLineEdit()
        self.key_combo_box = QComboBox()
        add_button = QPushButton("Add")
        del_button = QPushButton("Del")
        find_button = QPushButton("Find")
        inc_button = QPushButton("Inc")
        show_button = QPushButton("Show")
        self.result_edit = QTextEdit()

        h_box1.addWidget(name_label)
        h_box1.addWidget(self.name_edit)
        h_box1.addWidget(age_label)
        h_box1.addWidget(self.age_edit)
        h_box1.addWidget(score_label)
        h_box1.addWidget(self.score_edit)
        h_box2.addSpacing(100)
        h_box2.addWidget(amount_label)
        h_box2.addWidget(self.amount_edit)
        h_box2.addWidget(key_label)
        h_box2.addWidget(self.key_combo_box)
        h_box3.addSpacing(40)
        h_box3.addWidget(add_button)
        h_box3.addWidget(del_button)
        h_box3.addWidget(find_button)
        h_box3.addWidget(inc_button)
        h_box3.addWidget(show_button)
        h_box4.addWidget(result_label)
        h_box5.addWidget(self.result_edit)
        self.key_combo_box.addItems(["Age", "Name", "Score"])
        add_button.clicked.connect(self.add_button_clicked)
        del_button.clicked.connect(self.del_button_clicked)
        find_button.clicked.connect(self.find_button_clicked)
        inc_button.clicked.connect(self.inc_button_clicked)
        show_button.clicked.connect(self.showScoreDB)



        self.setLayout(v_box)
        self.show()

    def add_button_clicked(self):
        self.scoredb.append({"Age": int(self.age_edit.text()), "Name": self.name_edit.text(), "Score": int(self.score_edit.text())})
        self.showScoreDB()
    def del_button_clicked(self):
        key = self.name_edit.text()
        for idx, i in enumerate(self.scoredb):
            if i["Name"] == key:
                del self.scoredb[idx]
        self.showScoreDB()
    def find_button_clicked(self):
        key = self.name_edit.text()
        return_str = ""
        for i in self.scoredb:
            if i["Name"] == key:
                return_str += "Age=%d   Name=%s         Score=%d\n" % (i["Age"], i["Name"], i["Score"])
        self.result_edit.setText(return_str)
    def inc_button_clicked(self):
        key = self.name_edit.text()
        amount = int(self.amount_edit.text())
        for i in self.scoredb:
            if i["Name"] == key:
                i["Score"] += amount


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
        else:
            self.scoredb = pickle.load(fH)
            fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        key = self.key_combo_box.currentText()
        sorted_scoredb = sorted(self.scoredb, key=lambda x: x[key])
        return_str = ""
        for i in sorted_scoredb:
            return_str += "Age=%-10dName=%-10sScore=%-10d\n" % (i["Age"], i["Name"], i["Score"])
        self.result_edit.setText(return_str)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
