from Crypto.Hash import MD5
'''
h=MD5.new()
h.update("Allen".encode("utf-8"))
print(h.hexdigest())
x=h.hexdigest()
x=int(h.hexdigest(),16)
print(x)
print(x%5)
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """      
        :type capacity: int
        :rtype: None
        """
    def encrypt(self,key):
        #print(key)
        h=MD5.new()
        h.update(key.encode("utf-8"))
        #print(h.hexdigest())
        x=h.hexdigest()
        x=int(h.hexdigest(),16)
        #print(x)
        return x
    def add(self, key):
        x=self.encrypt(key)
        print(key)
        y=x%self.capacity
        print(y)
        node=self.data[y]
        if node:
            if node.val==key:
                return
            node=node.next
            newnode=ListNode(key)
            self.data[y].next=newnode
        else:
            newnode=ListNode(key)
            self.data[y]=newnode
        """
        :type key: str
        :rtype: None
        """
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        x=self.encrypt(key)
        y=x%self.capacity
        #print(y)
        node=self.data[y]
        while node:
            if node.val==key:
                return True
            node=node.next
        return False
        """
        :type key: str
        :rtype: bool(True or False)
        """

a=MyHashSet()
a.add("Allen")
a.add("Bob")
a.contains("Dog")
