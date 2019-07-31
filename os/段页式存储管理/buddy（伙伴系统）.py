import math
 
achieve = False
achieve2 = False
# 基本节点
class Node(object):
    def __init__(self, size, depth):
        self.ID = ""
        self.status=0  # 初始空闲
        self.size=size # 初始大小为0
        self.left=None
        self.right=None
        self.depth=depth   # 此节点创建的深度
 
 
class Operation(object):
    def __init__(self,maxlen,minlen):
        self.maxlen=int(math.pow(2,maxlen))
        self.minlen=int(math.pow(2, minlen))
        self.result= []
        self.root = Node(self.maxlen, 0)    # 初始化节点
 
    def allocate(self, size, ID):
        global achieve
        global achieve2
        level = 0     # 裂变的层数
        # print('maxlen',self.maxlen,'root',root.size)
 
        # 获取此节点应该在的深度
        for i in range(10):
            if size <= self.maxlen//math.pow(2,i) and size > self.maxlen//math.pow(2,i+1):
                level = i    # 获取裂变的层数或者搜索的深度
                break
        
        print("搜索深度为", level)
        print('将要分配的节点是:', ID)
 
        # 未分配状态下建立二叉树
        if self.root.left is None and self.root.right is None:
            p = self.root
            for i in range(level):
                p.status = 1
                p.left = Node(p.size/2, i+1)
                p.right = Node(p.size/2, i+1)
                p = p.left
            p.status = 1    # 最后一个分配的节点状态变为已分配
            p.ID = ID
            
            print("%8s %5s %5s %2s" % ('size', 'depth', 'status', 'id'))
            self.printMemMap(self.root)
 
        else:    
            # 已建立二叉树情况下的二叉树
            achieve = False
            achieve2 = False
            print('\n 已经有建立的伙伴树')
            self.LRD(self.root, 0, level, 0, ID)
 
            print("%8s %5s %5s %2s" % ('size','depth','status','id'))
            self.printMemMap(self.root)
 
            if achieve == True:
                print('在已经建立的二叉树已找到空闲节点且已分配')
            else:
                print('\n在已建立的二叉树上未找到空闲的节点,尝试分配')
 
                # 找到此节点以上的任意一层的空闲节点
 
                self.LRD2(self.root, 0, level-1, 0, ID)
 
                print("%8s %5s %5s %2s" % ('size','depth','status','id'))
                self.printMemMap(self.root)
 
                if achieve2 == False:
                    print('分配失败，请等待内存释放')
                else:
                    print('分配成功')
 
    # 释放
    def release(self, ID):
        print('\n释放过程。。。', '释放节点为', ID)
        self.searchAll(self.root, ID)
        self.releaseWay(self.root)
        print("%8s %5s %5s %2s" % ('size','depth','status','ID'))
        self.printMemMap(self.root)
 
    def searchAll(self, root, ID):
        if root.ID != ID:
            if root.left is not None:
                self.searchAll(root.left, ID)
            if root.right is not None:
                self.searchAll(root.right, ID)
        else:
            root.status = 0
            root.ID = ''
            print('已成功释放')
    
    def releaseWay(self, root):
        if root.left is not None and root.right is not None:
            if root.left.status == 0 and root.right.status == 0:
                root.left = None
                root.right = None
                root.status = 0
        if root.left is not None:
            self.releaseWay(root.left)
        if root.right is not None:
            self.releaseWay(root.right)
 
 
 
    # 树能满足的情况下
    def LRD(self, node, depth, level, flag, ID):
        global achieve
        if flag == 0:
            # print('depth', depth,' level', level, 'size', node.size)
            if depth < level:
                if node.left is not None:
                    self.LRD(node.left, depth+1, level, flag, ID)
                if node.right is not None:
                    self.LRD(node.right, depth+1, level, flag, ID)
            if depth == level:
                if node.status == 0:
                    node.status = 1
                    flag = 1
                    achieve = True
                    node.ID = ID
 
    # 遍历
    def LRD2(self, node, depth, level, flag, ID):
        global achieve2
        if flag == 0 and achieve2 == False:
            if depth < level:
                if node.left is not None:
                    self.LRD2(node.left, depth+1, level, flag, ID)
                if node.right is not None:
                    self.LRD2(node.right, depth+1, level, flag, ID)
            if depth == level and node.status == 0:
                flag = 1
                node.status = 1
                achieve2 = True
                node.left = Node(node.size/2, depth+1)
                node.right = Node(node.size/2, depth+1)
                node.left.ID = ID
                node.left.status = 1
            # print('Achieve2',achieve2)
 
 
    def printMemMap(self, node):
        print("%8s %5s %5s %2s"%(node.size, node.depth, node.status, node.ID))
        if node.left is not None:
            self.printMemMap(node.left)
        if node.right is not None:
            self.printMemMap(node.right)
            
 
 
test = Operation(10, 1)
 
test.allocate(100, 'ID1')
test.allocate(240, 'ID2')
test.allocate(64, 'ID3')
test.allocate(256, 'ID4')
test.release('ID2')
test.release('ID1')
test.allocate(75, 'ID5')
test.release('ID3')
test.release('ID4')
