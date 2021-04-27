# Source : https://leetcode.com/problems/binary-tree-paths/
# Author : foxfromworld
# Date  : 27/04/2021
# First attempt (recursive)

class Solution:
  def binaryTreePaths(self, root: TreeNode) -> List[str]:
    def sub_binarTreePaths(root, path):
      if root:
        path += str(root.val)
        if not root.left and not root.right:
          paths.append(path)
        else:
          path += '->'
          sub_binarTreePaths(root.left, path)
          sub_binarTreePaths(root.right, path)
    paths = []
    sub_binarTreePaths(root, '')
    return paths
