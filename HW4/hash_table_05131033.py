from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def encrypt(self,key):
        h=MD5.new()
        h.update(key.encode("utf-8"))
        x=h.hexdigest()
        x=int(h.hexdigest(),16)
        return x
    
    def add(self, key):
        x=self.encrypt(key)
        y=x%self.capacity
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
            
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
    def contains(self, key):
        x=self.encrypt(key)
        y=x%self.capacity
        node=self.data[y]
        while node:
            if node.val==key:
                return True
            node=node.next
        return False

