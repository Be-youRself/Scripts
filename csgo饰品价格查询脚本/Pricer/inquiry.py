from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from ui.inquiry import Ui_Inquiry
import menu
import requests
import operator
import time
import os


class Ui_Inquiry_sub(QtWidgets.QMainWindow, Ui_Inquiry):
    def __init__(self, parent = None):
        super(Ui_Inquiry_sub, self).__init__(parent = parent)
        self.setupUi(self) 
        self.setWindowIcon(QIcon('ui/image/PC.ico'))
        self.setStyleSheet('''#Inquiry{border-image: url(ui/image/bg_img.jpg);}''')

        self.inquiry_result = {}
        self.searchMax = 10

        self.Sure.clicked.connect(self.inquiry_price_sure)
        self.Fuzzy.clicked.connect(self.inquiry_price_fuzzy)
        self.More_results.clicked.connect(self.more_results)
        self.Up_sort.clicked.connect(self.up_sort_process)
        self.Down_sort.clicked.connect(self.down_sort_process)
        self.Back.clicked.connect(self.op_menu)


    def inquiry_price_sure(self):
        ## 进行查询
        self.inquiry_result = {}
        self.Warning.setText("")
        self.Warning.repaint()
        self.Result.setText("")
        self.Result.repaint()
        self.Result_sum.setText("")
        self.Result.repaint()
        input_names = self.Names.text()
        input_names = input_names.strip()  # 处理空格
        if input_names == "":
            self.Warning.setText("输入不可为空！")
            self.Warning.repaint()
        else:
            self.Result.setText("正在加载中，请稍等...")
            self.Result.repaint()
            ## 处理输入饰品名称
            input_names = input_names.replace("；", ";")  # 将中文分号转化为英文分号
            searchList = input_names.split(";")
            searchList = self.remove_duplication(searchList)
            self.inquiry_process(searchList)
            self.print_result()
            self.save_results()


    def inquiry_price_fuzzy(self):
        ## 进行查询
        self.inquiry_result = {}
        self.Warning.setText("")
        self.Warning.repaint()
        self.Result.setText("")
        self.Result.repaint()
        self.Result_sum.setText("")
        self.Result.repaint()
        input_names = self.Names.text()
        input_names = input_names.strip()  # 处理空格
        if input_names == "":
            self.Warning.setText("输入不可为空！")
            self.Warning.repaint()
        else:
            self.Result.setText("正在加载中，请稍等...")
            self.Result.repaint()
            ## 处理输入饰品名称

            searchList = self.get_names(input_names)
            if searchList == -1: # 网络连接出错
                return()
            searchList = self.remove_duplication(searchList)
            self.inquiry_process(searchList)
            self.print_result()
            self.save_results()


    def get_names(self, search):
        ## 获取模糊查询的所有结果
        results = []
        # 开始查询
        page = 1
        # 设置循环判断状态码 endPage
        # 0表示循环中
        # 1表示终止循环
        endPage = 0
        searchNum = 0
        while endPage == 0:
            # 从网页源代码获取信息
            # 获取网页源代码
            igxe_website = "https://www.igxe.cn/csgo/730?is_buying=0&is_stattrak%5B%5D=0&is_stattrak%5B%5D=0&keyword=" + search + "&sort=0&ctg_id=0&type_id=0&page_no=" + str(
                page) + "&page_size=20&rarity_id=0&exterior_id=0&quality_id=0&capsule_id=0"
            # 对于网络未连接进行异常处理
            try:
                igxe = requests.get(igxe_website)
            except Exception:
                self.Result.setText("网络出现错误，连接失败！")
                return (-1)
            igxe_source = str(igxe.content, encoding="utf-8")

            # 处理所得网页
            ref_1 = 'title="'
            ref_2 = '">'
            while (searchNum < self.searchMax):
                # 定位到商品名称
                ind_1 = igxe_source.find(ref_1)  # 选定第一标记
                # 遍历完所有标记即退出
                if ind_1 == -1:
                    break
                igxe_source = igxe_source[int(ind_1):]  # 截取第一标记后的网页
                ind_2 = igxe_source.find(ref_2)  # 选定第二标记(注意：第二标记可能有很多 所以一定要选第一标记后的)
                temp_result = igxe_source[7: int(ind_2)]  # 获取两标记间的结果
                if temp_result.find("™") == -1: # 不记录暗金 因为特殊字符
                    results.append(temp_result)
                    searchNum += 1
                igxe_source = igxe_source[int(ind_2):]  # 截取之后的网页

            # 到达最大上限
            if searchNum >= self.searchMax:
                endPage = 1
            # 到达最后一页
            if igxe_source.find("<!--没有数据-->") != -1:
                endPage = 1

            page = page + 1
        # 进行去重处理并排序
        results = self.remove_duplication(results)
        return(results)


    def inquiry_process(self, searchList):
        ## 查询价格
        # 遍历列表进行查询
        for i in range(0, len(searchList)):
            search = searchList[i]
            page = 1
            # 设置循环判断状态码 endPage
            # 0表示循环中
            # 1表示出错
            # 2表示正常获取价格
            endPage = 0
            while endPage != 1 and endPage != 2:
                # 从网页源代码获取信息
                # 获取网页源代码
                igxe_website = "https://www.igxe.cn/csgo/730?is_buying=0&is_stattrak%5B%5D=0&is_stattrak%5B%5D=0&keyword=" + search + "&sort=0&ctg_id=0&type_id=0&page_no=" + str(
                    page) + "&page_size=20&rarity_id=0&exterior_id=0&quality_id=0&capsule_id=0"
                # 对于网络未连接进行异常处理
                try:
                    igxe = requests.get(igxe_website)
                except Exception:
                    self.Result.setText("网络出现错误，连接失败！")
                    return (-1)
                igxe_source = str(igxe.content, encoding="utf-8")

                # 处理所得字符串
                # 定位到商品区域
                ref_1 = 'title="' + search + '"'
                ind_1 = igxe_source.find(ref_1)

                # 判断该页有没有这个商品
                if ind_1 == -1:
                    # 到达最后一页
                    if igxe_source.find("<!--没有数据-->") != -1:
                        endPage = 1
                    page = page + 1
                    continue

                    # 定位到价格区域
                ref_2 = '''<div class="price fl"><sup>￥</sup>
                                                    <span>'''
                ind_2 = igxe_source.find(ref_2, ind_1)
                if ind_2 == -1:
                    # 未能正确查找关键字 网站发生变化
                    endPage = 1
                    continue

                ref_3 = '''</span>
                                                    <sub>'''
                ind_3 = igxe_source.find(ref_3, ind_2, ind_2 + 300)
                if ind_3 == -1:
                    # 未能正确查找关键字 网站发生变化
                    endPage = 1
                    continue
                endPage = 2

            # 获取价格
            if endPage == 2:
                try:
                    price = igxe_source[ind_2 + len(ref_2): ind_3] + igxe_source[
                                                                     ind_3 + len(ref_3): ind_3 + len(ref_3) + 2]
                except ValueError:
                    self.inquiry_result[search] = "查询失败！(网站更新)"
                    continue
                self.inquiry_result[search] = float(price)
            else:
                result = "未查找到该饰品！(名称输入出错/网站更新)"
                self.inquiry_result[search] = result



    def print_result(self):
        ## 打印结果
        inquiry_result = ""
        for i in self.inquiry_result:
            inquiry_result += i
            for j in range(0, 40 - len(list(i.encode('gbk')))):
                inquiry_result += " "
            if type(self.inquiry_result[i]) == float:
                inquiry_result += "￥"
            inquiry_result += str(self.inquiry_result[i]) + "\n"
        self.Result.setText(inquiry_result)
        self.Result_sum.setText("经检索，已显示出" + str(len(self.inquiry_result)) + "条结果")


    def save_results(self):
        for i in self.inquiry_result:
            filename = i.replace("|", "1") # 文件命名时候不能出现“|” 因此进行转码
            # 检查是否有该目录 否则创建目录
            if not os.path.isdir("data"):
                os.mkdir("data")
            # 检查是否有该文件 否则创建文件
            file_w = open("data/" + filename + ".txt", "a", encoding="utf-8")
            now_time = time.strftime("%Y.%m.%d %H:%M:%S")
            file_w.write(now_time + ":" + str(self.inquiry_result[i]) + "\n")
            file_w.close()

    def more_results(self):
        ## 点一次多加载五个
        self.searchMax += 5
        self.inquiry_price_fuzzy()

    def up_sort_process(self):
        ## 对于结果按照价格升序排序
        inquiry_result = ""
        sorted_result = sorted(self.inquiry_result.items(), key=operator.itemgetter(1))
        for i in sorted_result:
            inquiry_result += i[0]
            for j in range(0, 57 - len(list(str(i).encode('gbk')))):
                inquiry_result += " "
            if type(i[1]) == float:
                inquiry_result += "￥"
            inquiry_result += str(i[1]) + "\n"
        self.Result.setText(inquiry_result)
        self.Result_sum.setText("经检索，已显示出" + str(len(self.inquiry_result)) + "条结果")


    def down_sort_process(self):
        ## 对于结果按照价格降序排序
        self.inquiry_result
        inquiry_result = ""
        sorted_result = sorted(self.inquiry_result.items(), key=operator.itemgetter(1), reverse=True)
        for i in sorted_result:
            inquiry_result += i[0]
            for j in range(0, 57 - len(list(str(i).encode('gbk')))):
                inquiry_result += " "
            if type(i[1]) == float:
                inquiry_result += "￥"
            inquiry_result += str(i[1]) + "\n"
        self.Result.setText(inquiry_result)
        self.Result_sum.setText("经检索，已显示出" + str(len(self.inquiry_result)) + "条结果")


    def remove_duplication(self, input: list):
        ## 去除重复元素并重新排序
        temp = set(input)
        result = list(temp)
        result.sort()
        return(result)

    def op_menu(self):
        ## 返回菜单
        self.w_menu = menu.Ui_Menu_sub()
        self.w_menu.show()
        self.close()
