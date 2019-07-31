import random
'''
内存
'''
#帧结构
class Frame:
    def __init__(self,frame_id,start_address):
        self.id=frame_id
        self.start_address=start_address
        self.size=2**11
        self.free=True
        self.clock=0;

    #占用
    #def using(self):
        

#主存模拟,主存字节数        
class Memory:
    def __init__(self,byte):
        #初始化内存空间，分块(帧)
        self.size=byte      #主存大小
        self.phy_space=[0]*byte #存储空间
        self.frame_table=[] #帧表

        #划分帧
        for i in range(int(byte/2048)):
            self.frame_table.append(Frame(i,i*2048))          
            
        self.pointer=-1 #clock策略所用指针
        
    #随机设定若干帧为已分配
 
    def random_fill(self,n):
        for i in range(n):
            index=random.randint(0,len(self.frame_table)-1)
            self.frame_table[index].free=False
            self.frame_table[index].clock=1
            for j in range(2048):
                self.phy_space[index*2048+j]=1
           
                
    #统计可用内存
    def avail_count(self):
        count=0
        for item in self.frame_table:
            if item.free:
                count+=1
        return count
    #占用一帧
    def set_frame(self):
        for frame in self.frame_table:
            if frame.free:
                frame.clock=1
                frame.free=False
                for i in range(2048):
                    self.phy_space[frame.start_address+i]=1                  
                return frame.id
    #释放帧
    def release(self,frame_id):
        for frame in self.frame_table:
            if frame.id==frame_id:
                frame.free=False
                frame.clock=0
                for i in range(2048):
                    self.phy_space[frame.start_address+i]=0
                break

#页表项
class Page_table_entry:
    def __init__(self,page_id,exist_memory=False,frame_id=-1):
        self.page_id=page_id #页号
        self.exist_memory=exist_memory #是否在主存中
        self.frame_id=frame_id #帧号,当页不在主存中时,帧号为-1
        
#页表
class Page_table:
    def __init__(self,name,pages_count):
        self.name=name #页表名
        self.page_items=[] #页表项列表
        self.page_pointer=-1
        self.resident=[] #常驻集
        #初始化页表项列表
        for i in range(pages_count):
            self.page_items.append(Page_table_entry(page_id=i))
            
        
        
