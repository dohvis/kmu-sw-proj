from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from week10.keypad import numPadList, operatorList, constantList, functionList


# To-do
# ButtonClass의 clicked 이벤트에 모두 buttonClicked를 연결시킬껀데 callback으로 매번 명시해 주어야하나
# DigitButton들 말고 나머지 버튼들도 굳이 하나씩 추가 해야하나?
# DigitButton 0도 예외로 따로 추가하지 않고 나머지 버튼과 마찬가지의 규칙으로 추가할 수 없을까?

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
        self.display = QLineEdit("")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constantLayout = QGridLayout()
        functionLayout = QGridLayout()
        buttonGroups = {
            "num": {"buttons": numPadList, "layout": numLayout, "columns": 3},
            "op": {"buttons": operatorList, "layout": opLayout, "columns": 2},
            "constants": {"buttons": constantList, "layout": constantLayout, "columns": 1},
            "functions": {"buttons": functionList, "layout": functionLayout, "columns": 1},
        }

        for label in buttonGroups.keys():
            r = 0
            c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad["buttons"]:
                button = Button(btnText, self.buttonClicked)
                buttonPad["layout"].addWidget(button, r, c)
                c += 1
                if c >= buttonPad["columns"]:
                    c = 0
                    r += 1

        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constantLayout, 2, 0)
        mainLayout.addLayout(functionLayout, 2, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        error_msg = "Error occurs!"
        if self.display.text() == error_msg:
            self.display.setText("")
        button = self.sender()
        key = button.text()
        if key == "=":
            try:
                result = str(eval(self.display.text()))
            except:
                result = error_msg
            self.display.setText(result)
        elif key == "C":
            self.display.setText("")
        elif key == "pi":
            self.display.setText("3.141592")
        elif key == "빛의 이동 속도 (m/s)":
            self.display.setText("3E+8")
        elif key == "소리의 이동 속도 (m/s)":
            self.display.setText("340")
        elif key == "태양과의 평균 거리 (km)":
            self.display.setText("1.5E+8")
        elif key == "factorial (!)":
            current_num = self.display.text()
            from math import factorial
            try:
                self.display.setText(str(factorial(int(current_num))))
            except:
                self.display.setText(error_msg)
        elif key == "-> binary":
            current_num = self.display.text()
            try:
                self.display.setText(str(bin(int(current_num))))
            except:
                self.display.setText(error_msg)
        elif key == "binary -> dec":
            current_num = self.display.text()
            try:
                self.display.setText(str(eval(current_num)))
            except:
                self.display.setText(error_msg)
        elif key == "-> roman":
            pass
        else:
            self.display.setText(self.display.text() + key)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())