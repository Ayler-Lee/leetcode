
"""
# warning 待优化
"""


# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2:
            return None
        
        def merge(t1, t2):
            if t1 and not t2:
                return t1.val
            elif not t1 and t2:
                return t2.val
            else:
                return t1.val + t2.val
                
        def traverse(t1, t2, node):
            if not t1 and not t2:
                return

            node.val = merge(t1, t2)
            if (t1 and t1.left) or (t2 and t2.left):
                node.left = TreeNode()
            if (t1 and t1.right) or (t2 and t2.right):
                node.right = TreeNode()
            traverse(t1 and t1.left, t2 and t2.left, node.left)
            traverse(t1 and t1.right, t2 and t2.right, node.right)
        
        node = TreeNode()
        traverse(root1, root2, node)
        return node
