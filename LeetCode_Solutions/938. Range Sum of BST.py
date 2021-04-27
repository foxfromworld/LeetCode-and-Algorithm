# Source : https://leetcode.com/problems/range-sum-of-bst/
# Author : foxfromworld
# Date  : 27/04/2021
# Second attempt (recursive)

class Solution:
  def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    self.retV = 0
    def sub_rangeSumBST(root):
      if root:
        if low <= root.val <= high:
          self.retV += root.val
        if low < root.val:
          sub_rangeSumBST(root.left)
        if root.val < high:
          sub_rangeSumBST(root.right)          
    sub_rangeSumBST(root)
    return self.retV  

# Date  : 26/04/2021
# First attempt (iterative)

class Solution:
  def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    returnV = 0
    stack = [root]
    while stack:
      current = stack.pop()
      if current:
        if low <= current.val <= high:
          returnV += current.val
        if low < current.val:
          stack.append(current.left)
        if current.val < high:
          stack.append(current.right)
    return returnV
