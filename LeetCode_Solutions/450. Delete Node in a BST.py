# Source : https://leetcode.com/problems/delete-node-in-a-bst/ 
# Author : foxfromworld
# Date  : 12/01/2021
# Second attempt 

class Solution:
  def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    if not root: return
    if root.val == key: # when the node to remove has no sub trees
      if not root.left and not root.right: return
      elif root.left and root.right: # when the node to remove has two sub trees
        current = root.right
        while current.left:
          current = current.left
        new = current.val
        root.val = current.val # change the original value of the node to "delete" the node
        root.right = self.deleteNode(root.right, new) # The recursion to remove the duplicated node 
      else: # when the node to remove has one sub tree
        return root.left or root.right        
    elif key > root.val:
      root.right = self.deleteNode(root.right, key)  # Main recursion (to find the key in the right tree)
    else:
      root.left = self.deleteNode(root.left, key) # Main recursion (to find the key in the left tree)
    return root

# Date  : 12/01/2021
# First attempt 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
    if not root: return
    if root.val == key:
      if not root.left and not root.right: return
      elif root.left==None and not root.right or root.left!=None and not root.right:
        return root.left or root.right
      else:
        current = root.right
        while current.left:
          current = current.left
        new = current.val
        root.val = current.val
        root.right = self.deleteNode(root.right, new)
    elif key > root.val:
      root.right = self.deleteNode(root.right, key)  
    else:
      root.left = self.deleteNode(root.left, key)
    return root
