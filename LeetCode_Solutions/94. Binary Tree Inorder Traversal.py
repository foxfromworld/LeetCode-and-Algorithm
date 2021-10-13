# Source : https://leetcode.com/problems/binary-tree-inorder-traversal/
# Author : foxfromworld
# Date  : 13/10/2021
# Second attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, ret):
            if node:
                helper(node.left, ret)
                ret.append(node.val)
                helper(node.right, ret)
        ret = []
        helper(root, ret)
        return ret

# Date  : 13/10/2021
# First attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, ret = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            ret.append(root.val)
            root = root.right
        return ret
