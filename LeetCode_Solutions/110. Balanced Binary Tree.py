# Source : https://leetcode.com/problems/balanced-binary-tree/
# Author : foxfromworld
# Date  : 06/05/2021
# First attempt

class Solution:
  def isBalanced(self, root: TreeNode) -> bool:
    def checksubtrees(node):
      if not node: return True, 0
      isLeftBalanced, leftHeight = checksubtrees(node.left)
      if not isLeftBalanced:
        return False, 0
      isRightBalanced, rightHeight = checksubtrees(node.right)
      if not isRightBalanced:
        return False, 0
      return abs(leftHeight - rightHeight) < 2, 1 + max(leftHeight, rightHeight)
    return checksubtrees(root)[0]
