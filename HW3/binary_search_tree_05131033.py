class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        if(val < root.val):                             #比root小就加在left
            if(root.left):                              #如果存在root.left，則重新insert
                return self.insert(root.left, val)
            else:
                root.left= TreeNode(val)                #如果root.left不存在，就insert進來
                return root.left                        #並回傳root.left
        elif(val > root.val):
            if(root.right):                             #比root大就加在right
                return self.insert(root.right, val)     #如果存在root.right，則重新insert
            else:
                root.right= TreeNode(val)               #如果root.right不存在，就insert進來
                return root.right                       #並回傳root.right
        elif(val==root.val):
            t=root.left                                 #如果等於也要加在root.left
            if(root.left==None):                        #若root.left==None
                root.left= TreeNode(val)                #就直接insert進來
                return root.left 
            else:
                a=root.left.val                         #若root.left存在則把原始root.left   
                root.left.val=val                       #insert在val的left
                root.left.left=self.insert(root.left, a)
                return root.left
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        
    def delete(self, root, target):
        pass
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
    def search(self, root, target):
        if(root is None):
            return False
        elif(target == root.val):
            if(root.left==None):
                return root
            elif(target==root.left.val):
                return root.left
        elif(target < root.val):
            return self.search(root.left, target)
        else:
            return self.search(root.right, target)
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
    def modify(self, root, target, new_val):
        pass
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
#參考資料:老師課堂投影片
