from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad import numPadList, operatorList, constantDic, functionDic
import calcFunctions

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout},
            'op': {'buttons': operatorList, 'layout': opLayout},
            'constants': {'buttons': [[x] for x in constantDic.keys()], 'layout': constLayout},
            'functions': {'buttons': [[x] for x in functionDic.keys()], 'layout': funcLayout},
        }

        for label in buttonGroups.keys():
            buttonPad = buttonGroups[label]
            for row, btn_list in enumerate(buttonPad['buttons']):
                for col, btnText in enumerate(btn_list):
                    button = Button(btnText, self.buttonClicked)
                    buttonPad['layout'].addWidget(button, row, col)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):
        except_list = ['Error!', '0']

        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error!'
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('0')
        elif key in constantDic.keys():
            self.display.setText(self.display.text() + constantDic[key])
        elif key in functionDic.keys():
            n = eval(self.display.text())
            value = eval(functionDic[key] + '(n)')
            self.display.setText(str(value))
        else:
            if self.display.text() in except_list:
                self.display.setText('')
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
