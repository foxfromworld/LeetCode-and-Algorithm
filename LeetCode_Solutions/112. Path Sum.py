# Source : https://leetcode.com/problems/path-sum/
# Author : foxfromworld
# Date  : 19/10/2021
# Second attempt 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = [(root, targetSum - root.val)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right and val == 0:
                return True
            if node.right:
                stack.append((node.right, val - node.right.val))
            if node.left:
                stack.append((node.left, val - node.left.val))
        return False

# Date  : 19/10/2021
# First attempt 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
