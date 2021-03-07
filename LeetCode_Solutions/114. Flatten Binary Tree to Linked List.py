# Source : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Author : foxfromworld
# Date  : 07/03/2021
# First attempt # Iterative

class Solution:
  def flatten(self, root: TreeNode) -> None:
    if not root: return
    searchleft, searchright = 1, 0
    stack = [(root, searchleft)]    
    tailNode = None
    while stack:
      currentNode, status = stack.pop()
      if not currentNode.left and not currentNode.right:
        tailNode = currentNode
        continue
      if status == searchleft:
        if currentNode.left:
          stack.append((currentNode, searchright))
          stack.append((currentNode.left, searchleft))
        else:
            stack.append((currentNode.right, searchleft))
      else:
        rightNode = currentNode.right
        if tailNode:
          tailNode.right = currentNode.right
          currentNode.right = currentNode.left
          currentNode.left = None
          rightNode = tailNode.right
        if rightNode:
          stack.append((rightNode, searchleft))

# Date  : 05/03/2021
# First attempt # Recursive

class Solution:
  def doFlatten(self, node):
    if not node: return None
    if not node.left and not node.right: return node
    leftend = self.doFlatten(node.left)
    rightend = self.doFlatten(node.right) 
    if leftend:
      leftend.right = node.right
      node.right = node.left
      node.left = None
    return rightend if rightend else leftend
  def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    self.doFlatten(root)
