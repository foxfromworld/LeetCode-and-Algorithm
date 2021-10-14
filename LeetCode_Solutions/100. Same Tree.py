# Source : https://leetcode.com/problems/same-tree/
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p and q: return False
        if not q and p: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

# Date  : 12/04/2021
# Second attempt (iterative)

class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p == q == None: return True
    stack = [[p, q]]
    while stack:
      curr = stack.pop()
      if not curr[0] and not curr[1]:
        continue
      if not curr[0] or not curr[1]:
        return False
      if curr[0].val != curr[1].val:
        return False
      if p: 
       stack.append([curr[0].left, curr[1].left])
       stack.append([curr[0].right, curr[1].right])
    return True

# Date  : 12/04/2021
# First attempt (recursive)

class Solution:
  def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p == q == None: return True
    if p and q and p.val == q.val:
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
      return False
