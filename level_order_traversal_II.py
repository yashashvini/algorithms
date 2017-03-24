# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root):
            a = [root]
            op = []
            while(len(a) > 0):
                count = len(a)
                b = []
                while(count>0):
                    if(a[0].left):
                        a.append(a[0].left)
                    if(a[0].right):
                        a.append(a[0].right)
                    b.append(a[0].val)
                    a = a[1:]
                    count -= 1
                op.insert(0,b)
            return op
        else:
            return []