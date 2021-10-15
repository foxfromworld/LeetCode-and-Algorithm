# Source : https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Author : foxfromworld
# Date  : 14/10/2021
# Third attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1
            for i in range(len(queue)):
                q = queue.pop(0)
                if q.left:
                    queue.append(q.left)
                if q.right:    
                    queue.append(q.right)
        return depth

# Date  : 14/10/2021
# Second attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if not root.right:
            return 1 + self.maxDepth(root.left)
        elif not root.left:
            return 1 + self.maxDepth(root.right)
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
          
# Date  : 14/10/2021
# First attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
