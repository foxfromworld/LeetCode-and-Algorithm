# Source : https://leetcode.com/problems/range-sum-of-bst/
# Author : foxfromworld
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
