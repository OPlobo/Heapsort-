class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    '''
    def insert1(self, val):
        if(self.root is None):
            self.root=TreeNode(val)
        else:
            self.insert(self.root, val)
    '''
    def insert(self, root, val):
        if(val <= root.val):
            if(root.left):
                self.insert(root.left, val)
                return self.insert
            else:
                root.left= TreeNode(val)
                return self.insert
        elif(val > root.val):
            if(root.right):
                self.insert(root.right, val)
                return self.insert
            else:
                root.right= TreeNode(val)
                return self.insert
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
    def delete(self, root, target):
        
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
    '''
    def search1(self,val):
        return self.search(self.root, val)
    '''
    def search(self, root, target):
        if(root is None):
            return False
        elif(target == root.val):
            return True
        elif(target < root.val):
            return self.search(root.left, target)
        else:
            return self.search(root.right, target)
        return self.search
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
n=TreeNode(5)
n.left=TreeNode(3)
n.right=TreeNode(6)

a=Solution()
a.root=n
a.insert(n,4)
#print(n.left.val)
print(Solution().search(n,4)==n.left.right)
