# Filename: look_up.py
# Coding: utf8
# 对于单词进行全部小写的处理

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
        self.setWindowIcon(QIcon('image/ReThink.ico'))
        self.setStyleSheet('''border-image: url(image/bg_img.jpg);''') # 设置自适应背景
        self.update_repository()
        self.read_word()
        self.Check.clicked.connect(self.look_up)

    def update_repository(self):
        file_r = open("word_list.txt", "r", encoding="UTF-8")
        wordList = []
        while True:
            line = file_r.readline()
            if len(line) == 0:
                break
            wordList.append(line)
        file_r.close()
        # 末尾换行符
        for i in range(0, len(wordList)):
            # range 包括 begin 不包括 end
            wordList[i].replace("\t", "")  # 处理制表符
            wordList[i].replace("\n", "")  # 处理句末回车
            wordList[i] = wordList[i].strip()  # 处理首尾空格
        # 去除空元素
        j = 0
        for i in range(0, len(wordList)):
            if wordList[j] == "":
                del wordList[j]  # 删除空元素
                j = j - 1
            j = j + 1
        if wordList != [] :
            # 打开 repository.txt 文件 读入元组修改
            file_r = open("word_repository.txt", "r", encoding="UTF-8")
            repo_disc = file_r.read()
            file_r.close()
            file_w = open("word_repository.txt", "w", encoding="UTF-8")
            if repo_disc == "":
                repo_disc = {}
            else:
                repo_disc = eval(repo_disc)
            for word in wordList:
                if word not in repo_disc:
                    repo_disc[word] = ""
            file_w.write(str(repo_disc))
            file_w.close()

    def read_word(self):
        self.words = "amplitude"
        self.Word.setText(self.words)

    def look_up(self):
        # 查找 repository
        file_r = open("word_repository.txt", "r", encoding="UTF-8")
        word_disc = file_r.read()
        file_r.close()
        file_w = open("word_repository.txt", "w", encoding="UTF-8")
        if word_disc == "":
            word_disc = {}
            explannation = translation.en2chs(self.words)
            word_disc[self.words] = explannation
            file_w.write(str(word_disc))
            self.Explanation.setText(explannation)
            file_w.close()
        else:
            word_disc = eval(word_disc)
            if self.words not in word_disc:
                explannation = translation.en2chs(self.words)
                word_disc[self.words] = explannation
                file_w.write(str(word_disc))
                self.Explanation.setText(explannation)
                file_w.close()
            else:
                if word_disc[self.words] != "":
                    explannation = word_disc[self.words]
                    file_w.write(str(word_disc))
                    self.Explanation.setText(explannation)
                    file_w.close()
                else:
                    # repository 无解释则进行单词查询
                    explannation = translation.en2chs(self.words)
                    word_disc[self.words] = explannation
                    file_w.write(str(word_disc))
                    self.Explanation.setText(explannation)
                    file_w.close()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Look_up_sub()
    window.show()
    sys.exit(app.exec_())