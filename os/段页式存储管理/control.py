from memory import *
from math import ceil
class Process:
    def __init__(self,name,size):
        self.name=name
        self.pages_count=ceil(size/2)
        
'''
控制器，管理分配内存
'''

class Control:
    def __init__(self):
        #初始化主存
        self.memory=Memory(2**20)
        self.memory.random_fill(100)       
        self.page_table=None
    
    #检查剩余可用内存是否足够
    def verify(self,needed_count):
        if self.memory.avail_count()>=needed_count:
            return True
        else:
            return False

    #分配常驻集空间
    def alloc(self,pages_count):
        for i in range(min(8,pages_count)):
            self.page_table.page_items[i].exist_memory=True
            frame_id=self.memory.set_frame()
            self.page_table.page_items[i].frame_id=frame_id
            self.page_table.resident.append(frame_id)
            self.page_table.pointer=0
            
    #为进程分配内存,并生成页表(常驻集最大为16k)
    def process_request(self,process):
        if self.verify(min(8,process.pages_count)):
            self.page_table=Page_table(process.name,process.pages_count)
            self.alloc(process.pages_count)
            self.print_page_table()
            self.print_memory()
        else:
            print("可用内存不足!")

    #回收内存
    def release(self):
        for frame_id in self.page_table.resident:
            self.memory.release(frame_id)
        del self.page_table
        self.print_memory()

    #常驻集内的循环指针(存储下标）
    def next_frame(self):
        index=self.page_table.pointer
        if index>=len(self.page_table.resident)-1:
            self.page_table.pointer=0
        else:
            self.page_table.pointer+=1
        return self.page_table.resident[index]
    
    #进程驻留集内的clock算法
    def clock(self):
        while 1:
            frame_id=self.next_frame()
            if self.memory.frame_table[frame_id].clock==1:
                self.memory.frame_table[frame_id].clock=0
            else:
                for entry in self.page_table.page_items:
                    if entry.frame_id==frame_id:
                        entry.frame_id=-1
                        entry.exist_memory=False
                self.memory.frame_table[frame_id].clock=1
                return frame_id
                                       
    #缺页中断
    def page_fault(self,page_id):
        frame_id=self.clock()
        print("出现缺页!")
        print("缺页的页号为:",page_id,"要淘汰的帧号为:",frame_id)
        self.page_table.page_items[page_id].exist_memory=True
        self.page_table.page_items[page_id].frame_id=frame_id
        print("替换成功!")
        self.print_page_table()
    #根据逻辑地址映射物理地址，若缺页，则缺页中断
    #逻辑地址结构[页号,偏移量]
    def mapping(self,log_address):
        if log_address[0]>=len(self.page_table.page_items):
            return "页号越界!"
        elif log_address[1]>=2048:
            return "偏移量越界!"
        for entry in self.page_table.page_items:
            if entry.page_id==log_address[0]:
                if entry.exist_memory:                    
                    return "物理地址为:"+str(self.memory.frame_table[entry.frame_id].start_address+log_address[1])
                else:
                    
                    self.page_fault(log_address[0])
                    return self.mapping(log_address)

                
    #输出
    def print_memory(self):
        string=''
        for i in self.memory.phy_space:
            string+=str(i)
        file_1 = open("save.txt", "w")
        file_1.write(string)
        file_1.close()

    def print_page_table(self):
        print(self.page_table.name,"页表:")
        print("%8s %12s %5s" % ('page_id','exist_memory','frame_id'))
        for i in self.page_table.page_items:
            print("%5s %12s %8s" % (i.page_id,i.exist_memory,i.frame_id))
        



        
