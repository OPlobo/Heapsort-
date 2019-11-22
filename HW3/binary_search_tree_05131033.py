class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        if(val < root.val):
            if(root.left):
                return self.insert(root.left, val)
            else:
                root.left= TreeNode(val)
                return root.left
        elif(val > root.val):
            if(root.right):
                return self.insert(root.right, val)
            else:
                root.right= TreeNode(val)
                return root.right
        elif(val==root.val):
            t=root.left
            if(root.left==None):
                root.left= TreeNode(val)
                return root.left 
            else:
                a=root.left.val
                root.left.val=val  
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
> 參考資料:
* [Binary Search Tree](https://docs.google.com/presentation/d/e/2PACX-1vQgUh73yvSdxAvMH50DHWJ5lsCX8-daMxtoltU9rYW7xCmqYz2A1wOv0Vcx_F9KO5ZUvZBv3IF1TjGi/pub?start=false&loop=false&delayms=3000&slide=id.g73e451e679_0_18)
