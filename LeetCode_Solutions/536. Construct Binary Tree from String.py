# Source : https://leetcode.com/problems/construct-binary-tree-from-string/
# Author : foxfromworld
# Date  : 19/02/2022
# First attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        num = ''
        stack = []
        for ch in s:
            if ch == '-' or ch.isdigit():
                num += ch
            elif ch == "(":
                if num:
                    stack.append(TreeNode(num))
                    num = ''
            else:
                if num:
                    newNode = TreeNode(num)
                    num = ''
                    if not stack[-1].left:
                        stack[-1].left = newNode
                    elif not stack[-1].right:
                        stack[-1].right = newNode
                else:
                    newNode = stack.pop()
                    if not stack[-1].left:
                        stack[-1].left = newNode
                    elif not stack[-1].right:
                        stack[-1].right = newNode
        return stack[-1] if stack else TreeNode(num) if s else None
                    
                
