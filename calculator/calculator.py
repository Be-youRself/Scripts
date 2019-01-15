from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui_calculator import Ui_MainWindow
import cal_process
import sys


class Ui_Calculator(QtWidgets.QMainWindow, Ui_MainWindow):  # 多态继承界面类来添加逻辑
    def __init__(self, parent=None):
        super(Ui_Calculator, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('image/icon.ico'))
        self.exp = "0"
        # 绑定按钮信号槽
        self.butt0.clicked.connect(self.b0_process)
        self.butt1.clicked.connect(self.b1_process)
        self.butt2.clicked.connect(self.b2_process)
        self.butt3.clicked.connect(self.b3_process)
        self.butt4.clicked.connect(self.b4_process)
        self.butt5.clicked.connect(self.b5_process)
        self.butt6.clicked.connect(self.b6_process)
        self.butt7.clicked.connect(self.b7_process)
        self.butt8.clicked.connect(self.b8_process)
        self.butt9.clicked.connect(self.b9_process)
        self.butt_plus.clicked.connect(self.b_pl_process)
        self.butt_minus.clicked.connect(self.b_mi_process)
        self.butt_multiple.clicked.connect(self.b_mu_process)
        self.butt_division.clicked.connect(self.b_di_process)
        self.butt_equal.clicked.connect(self.b_eq_process)
        self.butt_back.clicked.connect(self.b_bk_process)
        self.butt_dot.clicked.connect(self.b_dot_process)
        self.butt_per.clicked.connect(self.b_per_process)
        self.butt_restart.clicked.connect(self.b_restart_process)
        self.showResult()

    def showResult(self):
        self.showRe = self.exp.replace("@", "-") # “@”用于标记负数
        self.output.setText(self.showRe)

    def error_process(self):
        if self.exp == "ERROR":
            self.b_restart_process()

    def b0_process(self):
        self.error_process()
        self.exp = "0" if self.exp == "0" else self.exp + "0"
        self.showResult()

    def b1_process(self):
        self.error_process()
        self.exp = "1" if self.exp == "0" else self.exp + "1"
        self.showResult()

    def b2_process(self):
        self.error_process()
        self.exp = "2" if self.exp == "0" else self.exp + "2"
        self.showResult()

    def b3_process(self):
        self.error_process()
        self.exp = "3" if self.exp == "0" else self.exp + "3"
        self.showResult()

    def b4_process(self):
        self.error_process()
        self.exp = "4" if self.exp == "0" else self.exp + "4"
        self.showResult()

    def b5_process(self):
        self.error_process()
        self.exp = "5" if self.exp == "0" else self.exp + "5"
        self.showResult()

    def b6_process(self):
        self.error_process()
        self.exp = "6" if self.exp == "0" else self.exp + "6"
        self.showResult()

    def b7_process(self):
        self.error_process()
        self.exp = "7" if self.exp == "0" else self.exp + "7"
        self.showResult()

    def b8_process(self):
        self.error_process()
        self.exp = "8" if self.exp == "0" else self.exp + "8"
        self.showResult()

    def b9_process(self):
        self.error_process()
        self.exp = "9" if self.exp == "0" else self.exp + "9"
        self.showResult()

    def b_pl_process(self):
        self.error_process()
        if self.exp[len(self.exp) - 1].isdigit():
            self.exp = cal_process.calculator(self.exp)
            if self.exp == "ERROR":
                pass
            else:
                self.exp = self.exp + "+"
        else:
            self.exp = self.exp[0: len(self.exp) - 1] + "+"
        self.showResult()

    def b_mi_process(self):
        self.error_process()
        if self.exp[len(self.exp) - 1].isdigit():
            self.exp = cal_process.calculator(self.exp)
            if self.exp == "ERROR":
                pass
            else:
                self.exp = self.exp + "-"
        else:
            self.exp = self.exp[0: len(self.exp) - 1] + "-"
        self.showResult()

    def b_mu_process(self):
        self.error_process()
        if self.exp[len(self.exp) - 1].isdigit():
            self.exp = cal_process.calculator(self.exp)
            if self.exp == "ERROR":
                pass
            else:
                self.exp = self.exp + "*"
        else:
            self.exp = self.exp[0: len(self.exp) - 1] + "*"
        self.showResult()

    def b_di_process(self):
        self.error_process()
        if self.exp[len(self.exp) - 1].isdigit():
            self.exp = cal_process.calculator(self.exp)
            if self.exp == "ERROR":
                pass
            else:
                self.exp = self.exp + "/"
        else:
            self.exp = self.exp[0: len(self.exp) - 1] + "/"
        self.showResult()

    def b_eq_process(self):
        self.error_process()
        if self.exp[len(self.exp) - 1].isdigit():
            self.exp = cal_process.calculator(self.exp)
        else:
            while not self.exp[len(self.exp) - 1].isdigit():
                self.exp = self.exp[0: len(self.exp) - 1]
            self.exp = cal_process.calculator(self.exp)
        self.showResult()

    def b_bk_process(self):
        self.error_process()
        self.exp = self.exp[0: len(self.exp) - 1]
        if self.exp == "" or self.exp == "-":
            self.exp = "0"
        self.showResult()

    def b_dot_process(self):
        self.error_process()
        # 注意一个数内有小数点则无视这个操作
        if self.exp.rfind(".") == -1:
            self.exp = self.exp + "."
        if self.exp[len(self.exp) - 1] != ".":
            if not self.exp[self.exp.rfind(".") + 1:].isdigit():
                self.exp = self.exp + "."
        self.showResult()

    def b_per_process(self):
        self.error_process()
        self.last_index = max(self.exp.find("+"), self.exp.find("-"), self.exp.find("*"), self.exp.find("/"))
        self.last = self.exp[self.last_index + 1:]
        if self.last == "":
            pass
        else:
            self.exp = self.exp[0: self.last_index + 1] + cal_process.calculator(self.last+"/100")
        self.showResult()

    def b_restart_process(self):
        self.exp = "0"
        self.showResult()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Calculator()
    window.show()
    sys.exit(app.exec_())