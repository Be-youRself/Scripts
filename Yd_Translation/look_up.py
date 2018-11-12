# Filename: look_up.py
# Coding: utf8

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from look_up_ui import Ui_Look_up
import sys
import look_up_ui
import translation

class Ui_Look_up_sub(QtWidgets.QMainWindow, Ui_Look_up): # 多态继承界面类来添加逻辑
    def __init__(self, parent = None):
        super(Ui_Look_up_sub, self).__init__(parent = parent)
        self.setupUi(self)
        self.read_word()
        self.setWindowIcon(QIcon('image/ReThink.ico'))
        self.setStyleSheet('''border-image: url(image/bg_img.jpg);''') # 设置自适应背景
        self.Check.clicked.connect(self.look_up)

    def read_word(self):
        file_r = open("words.txt", "r", encoding="UTF-8")
        self.words = file_r.read()
        file_r.close()
        self.Word.setText(self.words)

    def look_up(self):
        self.Explanation.setText(translation.en2chs(self.words))
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Look_up_sub()
    window.show()
    sys.exit(app.exec_())