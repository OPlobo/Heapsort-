from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def encrypt(self,key):                              #加密
        h=MD5.new()
        h.update(key.encode("utf-8"))
        x=h.hexdigest()
        x=int(h.hexdigest(),16)
        return x
    
    def get(self,node,key):                            #增加並確認
        if node.next:
            return self.get(node.next,key)
        else:
            node.next=ListNode(key)
            
    def add(self, key):
        x=self.encrypt(key)
        y=x%self.capacity
        #print(y)                                     #不小心加的print
        if self.data[y]==None:                        #若一開始為空，則直接加入
            newnode=ListNode(key)
            self.data[y]=newnode
        else:
            newnode=self.get(self.data[y],key)
            
    def remove(self, key):
        x=self.encrypt(key)
        y=x%self.capacity
        node=self.data[y]
        if node.val==key:
            self.data[y]=node.next
            return None
        i=None
        while node:
            if node.val==key:
                i.next=node.next
                return None
            else:
                i=node
                node=node.next

    def contains(self, key):                         #是否存在
        x=self.encrypt(key)
        y=x%self.capacity
        #print(y)                                   #不小心加的print
        node=self.data[y]
        while node:
            if node.val==key:                       #如果再，就回傳True
                return True
            else:
                node=node.next                      #如果不再，就往下找
        return False                                #不存在，則回傳False

    #參考資料:老師課堂投影片
