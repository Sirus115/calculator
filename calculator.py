from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from math import sqrt


class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("calculator.ui")

        # 加载 icon
        app.setWindowIcon(QIcon('logo.png'))

        # 信号处理
        # self.ui.text_num.textChanged.connect(self.handleTextChange)
        self.ui.btn_back.clicked.connect(self.backspace)  # 在文本框中按下回车键直接计算
        self.ui.text_num.returnPressed.connect(self.equ)
        self.ui.btn_equ.clicked.connect(self.equ)
        self.ui.btn_double.clicked.connect(self.double)
        self.ui.btn_sqrt.clicked.connect(self.sqrt_num)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_plus.clicked.connect(self.plus)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_min.clicked.connect(self.sub)
        self.ui.btn_dot.clicked.connect(self.dot)
        self.ui.btn_0.clicked.connect(self.num_0)
        self.ui.btn_1.clicked.connect(self.num_1)
        self.ui.btn_2.clicked.connect(self.num_2)
        self.ui.btn_3.clicked.connect(self.num_3)
        self.ui.btn_4.clicked.connect(self.num_4)
        self.ui.btn_5.clicked.connect(self.num_5)
        self.ui.btn_6.clicked.connect(self.num_6)
        self.ui.btn_7.clicked.connect(self.num_7)
        self.ui.btn_8.clicked.connect(self.num_8)
        self.ui.btn_9.clicked.connect(self.num_9)

    # def handleTextChange(self):
    #     text = self.ui.text_num.text()

    def backspace(self):
        text = self.ui.text_num.text()
        text = text[:len(text) - 1]
        self.ui.text_num.setText(text)

    def double(self):
        self.ui.text_num.insert("**")

    def sqrt_num(self):
        # text = self.ui.text_num
        # result = sqrt(int(text))
        # self.ui.text_num.setText(result)
        self.ui.text_num.insert("**0.5")

    def clear(self):
        self.ui.text_num.clear()

    def equ(self):
        text = self.ui.text_num.text()
        try:
            result = str(eval(text))  # Eval 函数计算结果 表达式 字符串或数值的值
        except BaseException:
            result = "ERROR!"

        self.ui.text_num.setText(text + " = " + result)

    def div(self):
        self.ui.text_num.insert("/")

    def mul(self):
        self.ui.text_num.insert("*")

    def sub(self):
        self.ui.text_num.insert("-")

    def plus(self):
        self.ui.text_num.insert("+")

    def dot(self):
        self.ui.text_num.insert(".")

    def num_0(self):
        self.ui.text_num.insert("0")

    def num_1(self):
        self.ui.text_num.insert("1")

    def num_2(self):
        self.ui.text_num.insert("2")

    def num_3(self):
        self.ui.text_num.insert("3")

    def num_4(self):
        self.ui.text_num.insert("4")

    def num_5(self):
        self.ui.text_num.insert("5")

    def num_6(self):
        self.ui.text_num.insert("6")

    def num_7(self):
        self.ui.text_num.insert("7")

    def num_8(self):
        self.ui.text_num.insert("8")

    def num_9(self):
        self.ui.text_num.insert("9")


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
