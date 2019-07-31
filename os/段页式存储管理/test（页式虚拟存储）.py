from control import *

control=Control()
pro_name=input("请输入进程名:")
pro_size=int(input("请输入进程大小(k):"))
control.process_request(Process(pro_name,pro_size))

#逻辑地址映射                 
log_address=[]
log_address.append(int(input("请输入页号:")))
log_address.append(int(input("请输入偏移量:")))

print(control.mapping(log_address)) #映射

control.release() #释放内存
