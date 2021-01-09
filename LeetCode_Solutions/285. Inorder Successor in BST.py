# Source : https://leetcode.com/problems/inorder-successor-in-bst/
# Author : foxfromworld
# Date  : 09/01/2020
# Second attempt 

class Solution:
  def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    target = None
    while root:
      if p.val > root.val:
        root = root.right
      else:
        target = root
        root = root.left
    return target

# Date  : 08/01/2020
# First attempt 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
  def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    nodes = []
    target = None
    def inorder(node, nodes, p, target):
      if node:
        nodes = inorder(node.left, nodes, p, target)
        nodes.append([node.val, node])
        nodes = inorder(node.right, nodes, p, target)
      return nodes # Get all the value in the tree using the Inorder Traversal
    inorder(root, nodes, p, target)
    for i in range (len(nodes)-1): # Find the successor
      if nodes[i][0] == p.val:
        target = nodes[i+1][1]
    return target
