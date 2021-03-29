# Source : https://leetcode.com/problems/find-mode-in-binary-search-tree/submissions/
# Author : foxfromworld
# Date  : 29/03/2021
# First attempt

class Solution:
  def findMode(self, root: TreeNode) -> List[int]:
    dictMode = {}
    def traverse(node):
      if not node: return
      if node.val in dictMode:
        dictMode[node.val] += 1
      else:
        dictMode[node.val] = 1
      traverse(node.left)
      traverse(node.right)
    dictMode[root.val] = 1
    traverse(root.left)
    traverse(root.right)
    return [key for key, val in dictMode.items() if val == max(dictMode.values())]
