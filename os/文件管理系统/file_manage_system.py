# Coding: utf-8
import sys

global direction,fat,file,content,now_file
direction = {"根目录": {}}  # 限制最多两级
fat = []
file = {}
content = {}
now_file = {}


def file_manage_system():
    # 主函数
    initial_source()
    print_menu()


def initial_source():
    # 初始化一些资源
    for i in range(3):
        fat.append(-1)
    for i in range(3, 128):
        fat.append(0)
    print("初始化资源成功！")
    print_direction()
    print_fat()


def print_menu():
    while 1:
        print('''1.创建文件或目录
2.打开文件
3.删除文件或目录
4.查看信息
0.退出程序''')
        choose = input()
        if choose == "1":
            create_file()
        elif choose == "2":
            open_file()
        elif choose == "3":
            delete_file()
        elif choose == "4":
            print_direction()
            print_fat()
        elif choose == "0":
            sys.exit()
        else:
            print("输入指令有误！\n")


def print_direction():
    print("目录如下：\n>根目录")
    space = "   "
    temp = direction["根目录"]
    for i in temp:
        print(space + ">>" + i)
        temp = direction["根目录"][i]
        for j in temp:
            print(space + space + ">>>" + j)
            temp = direction["根目录"][i][j]
            for k in temp:
                print(space + space + space + ">>>>" + k)
    print()


def print_fat():
    print("FAT如下：")
    for i in fat:
        print(i, end=" ")
    print("\n")


def create_file():
    print("输入绝对路径：")
    path = input()
    path = path.split("/")
    if path[0] == "":
        path[0] = "根目录"
    if path[-1] == "":
        print("输入有误！1")
        return
    if len(path) == 1:
        print("输入有误！2")
        return
    for i in range(len(path) - 1):
        if path[i].find(".") != -1:
            print("输入有误！3")
            return
    if path[-1].find(".") != path[-1].rfind("."):
        print("输入有误！4")
        return
    try:
        temp = direction
        for i in range(len(path) - 1):
            temp = temp[path[i]]
        if path[-1] in temp:
            print("存在重名文件（目录）！")
        else:
            if path[-1].find(".") != -1:
                result_1 = find_fat(0)
                result_2 = find_fat(result_1 + 1)
                if result_2 == -1:
                    print("资源不够，创建失败！")
                else:
                    fat[result_1] = result_2
                    fat[result_2] = -1
                    temp[path[-1]] = {}
                    all_path = ""
                    for i in path:
                        all_path += i + "/"
                    all_path = all_path[0: -1]
                    file[all_path] = {"path": all_path, "start": result_1, "type": path[-1][path[-1].find("."):], "operation": "common", "length": 2, "content":""}
                    print("创建文件成功！")
                    print_direction()
            else:
                result = find_fat(0)
                if result != -1:
                    fat[result] = -1
                    temp[path[-1]] = {}
                    all_path = ""
                    for i in path:
                        all_path += i + "/"
                    all_path = all_path[0: -1]
                    content[all_path] = result
                    print("创建目录成功！")
                    print_direction()
                else:
                    print("资源不够，创建失败！")
        return
    except:
        print("输入有误！5")
        return


def find_fat(n):
    # 查找 fat 中从 n 到最后可分配的区域，若有则返回下标；无则返回-1
    flag = -1
    for i in range(n, 128):
        if fat[i] == 0:
            flag = i
            break
    return flag


def open_file():
    print("输入绝对路径：")
    path = input()
    path = path.split("/")
    if path[0] == "":
        path[0] = "根目录"
    if path[-1] == "":
        print("输入有误！6")
        return
    if len(path) == 1:
        print("输入有误！7")
        return
    for i in range(len(path) - 1):
        if path[i].find(".") != -1:
            print("输入有误！8")
            return
    if path[-1].find(".") != path[-1].rfind("."):
        print("输入有误！9")
        return
    try:
        temp = direction
        for i in range(len(path) - 1):
            temp = temp[path[i]]
        if path[-1] in temp:
            if path[-1].find(".") != -1:
                all_path = ""
                for i in path:
                    all_path += i + "/"
                all_path = all_path[0: -1]
                open_file_operation(all_path)
            else:
                print("输入非文件！")
        else:
            print("欲打开文件不存在！")
            return
    except:
        print("输入有误！10")
        return


def delete_file():
    print("输入绝对路径：")
    path = input()
    path = path.split("/")
    if path[0] == "":
        path[0] = "根目录"
    if path[-1] == "":
        print("输入有误！11")
        return
    if len(path) == 1:
        print("输入有误！12")
        return
    for i in range(len(path) - 1):
        if path[i].find(".") != -1:
            print("输入有误！13")
            return
    if path[-1].find(".") != path[-1].rfind("."):
        print("输入有误！14")
        return
    try:
        temp = direction
        for i in range(len(path) - 1):
            temp = temp[path[i]]
        if path[-1] in temp:
            if path[-1].find(".") != -1:
                del temp[path[-1]]
                all_path = ""
                for i in path:
                    all_path += i + "/"
                all_path = all_path[0: -1]
                result_1 = file[all_path]["start"]
                result_2 = fat[result_1]
                fat[result_1] = 0
                fat[result_2] = 0
                del file[all_path]
                print("删除文件成功！")
                print_direction()
            else:
                if temp[path[-1]] == {}:
                    # 空目录
                    del temp[path[-1]]
                    all_path = ""
                    for i in path:
                        all_path += i + "/"
                    all_path = all_path[0: -1]
                    result = content[all_path]
                    fat[result] = 0
                    del content[all_path]
                    print("欲删除目录为空，已成功删除！")
                    print_direction()
                else:
                    print("欲删除目录不为空，删除失败！")
        else:
            print("欲删除文件（目录）不存在！")
        return
    except:
        print("输入有误！15")
        return


def open_file_operation(path):
    print("文件打开成功！")
    global now_file
    now_file = file[path]
    show_file_information(now_file)
    file_menu()

def file_menu():
    while 1:
        print('''1.读文件
2.覆盖写文件
3.追加写文件
4.改变文件属性
0.关闭文件''')
        choose_1 = input()
        if choose_1 == "1":
            read_file()
        elif choose_1 == "2":
            write_file()
        elif choose_1 == "3":
            add_file()
        elif choose_1 == "4":
            change_file_operation()
        elif choose_1 == "0":
            close_file()
            break
        else:
            print("输入指令有误！\n")

def show_file_information(show_file):
    print("文件信息如下：\n文件路径：{0}  文件类型：{1}  文件属性：{2}  起始块号：{3}  文件长度：{4}\n"
          .format(show_file["path"], show_file["type"], show_file["operation"], show_file["start"], show_file["length"]))

def read_file():
    print("文件内容为：\n" + now_file["content"] + "\n")

def write_file():
    if is_write():
        print("输入内容：")
        now_file["content"] = input()
        print("文件写入成功！")
        read_file()
    else:
        print("文件为只读格式，不支持写操作！\n")

def add_file():
    if is_write():
        print("输入内容：")
        now_file["content"] += input()
        print("文件写入成功！")
        read_file()
    else:
        print("文件为只读格式，不支持写操作！\n")

def is_write():
    if(now_file["operation"] == "common"):
        return True
    else:
        return False

def change_file_operation():
    print("当前文件属性为：" + now_file["operation"] + "\n您想要修改为？")
    change = input()
    if change != "common" and change != "only_read":
        print("修改文件属性出错！")
        print()
    else:
        now_file["operation"] = change
        print("修改文件属性成功！当前文件属性为：" + now_file["operation"])
        print()

def close_file():
    global now_file
    now_file = {}
    print("关闭文件成功！\n")



if __name__ == '__main__':
    file_manage_system()
