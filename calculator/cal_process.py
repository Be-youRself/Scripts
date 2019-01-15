# Filename: calculator.py
# coding: utf8
# 对于负数的处理：进行数字提取时候采用"@"标记 运算前还原成"-"

import re
import decimal # 运用 decimal 模块来进行精确浮点数运算

def calculator(exp):
    # 字符串形式返回表达式的运算结果
    # 仅仅加减乘除
    # 添加判断是否可以运算
    if re.search(r"[*/+-]", exp) == None:
        # 输出纯数字或者小数或者负数 即无运算符
        return(exp)
    sym = re.search(r"[*/+-]", exp).group()
    fst = exp.split(sym)[0].replace("@", "-") # "@" 用于区别运算符 计算时转化成 "-" 处理
    snd = exp.split(sym)[1].replace("@", "-")
    fst = int(fst) if fst.find(".") == -1 else decimal.Decimal(fst) # 将带有小数点的数字转为浮点型
    if snd == ".": # 防止只有一个小数点
        snd = decimal.Decimal(0.0)
    else:
        snd = int(snd) if snd.find(".") == -1 else decimal.Decimal(snd)
    cal_dict = {"+": fst + snd,
                "-": fst - snd,
                "*": fst * snd,
                "/": "ERROR" if snd == 0 else round(fst / snd, 5)} # 限制五位小数 & 判断是否除0
    result = str(cal_dict[sym]).replace("-", "@") # 表达式中仍然使用 "@" 区分
    if result.find("e") != -1:
        return("0")
    return (result)

if __name__ == "__main__":
    print("这是一个示例!")