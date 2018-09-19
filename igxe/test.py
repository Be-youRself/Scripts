searchList = []
file_r = open("want.txt")
while True:
    line = file_r.readline()
    if len(line) == 0:
        break
    searchList.append(line)

# 消除末尾换行符
for i in range(0, len(searchList)):
    if(searchList[i].rfind("\n") != -1):
        searchList[i] = searchList[i][0: searchList[i].rfind("\n")]


print(searchList)