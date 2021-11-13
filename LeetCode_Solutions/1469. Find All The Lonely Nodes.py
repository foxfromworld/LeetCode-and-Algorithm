# Source : https://leetcode.com/problems/find-all-the-lonely-nodes/
# Author : foxfromworld
# Date  : 13/11/2021
# First attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def help(node, ret):
            if not node:
                return
            if not node.left and node.right:
                ret.append(node.right.val)
            if not node.right and node.left:
                ret.append(node.left.val)
            help(node.left, ret)
            help(node.right, ret)
        ret = []
        help(root, ret)
        return ret
