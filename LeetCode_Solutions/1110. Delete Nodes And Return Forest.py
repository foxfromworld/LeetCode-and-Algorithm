# Source : https://leetcode.com/problems/delete-nodes-and-return-forest/
# Author : foxfromworld
# Date  : 01/06/2020
# First attempt 

class Solution:
  def delNodes(self, root, to_delete):
    to_delete = set(to_delete)
    tree = []
    def traversal(node, parent_exist):
      if not node: return None
      if node.val in to_delete:
        node.left = traversal(node.left, False)
        node.right = traversal(node.right, False)
        return None
      else:
        if parent_exist == False:
          tree.append(node)
        node.left = traversal(node.left, True)
        node.right = traversal(node.right, True)
        return node
    traversal(root, False)
    return tree
