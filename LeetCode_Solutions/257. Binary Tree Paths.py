# Source : https://leetcode.com/problems/binary-tree-paths/
# Author : foxfromworld
# Date  : 01/05/2021
# First attempt (iteratively)

class Solution:
  def binaryTreePaths(self, root: TreeNode) -> List[str]:
    if not root: return []
    stack = [[root, str(root.val)]]
    paths = []
    while stack:
      curr, path = stack.pop()
      if curr.left == None and curr.right == None:
        paths.append(path)
      if curr.left:
        stack.append([curr.left, path + '->' + str(curr.left.val)])
      if curr.right:
        stack.append([curr.right, path + '->' + str(curr.right.val)])
    return paths
  
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
