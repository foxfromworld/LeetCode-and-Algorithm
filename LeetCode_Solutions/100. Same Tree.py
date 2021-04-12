# Source : https://leetcode.com/problems/same-tree/
# Author : foxfromworld
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
