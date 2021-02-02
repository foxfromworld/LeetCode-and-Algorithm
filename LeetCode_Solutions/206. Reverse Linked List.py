# Source : https://leetcode.com/problems/reverse-linked-list/
# Author : foxfromworld
# Date  : 02/02/2021
# First attempt (iterative)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:      
  def reverseList(self, head):  # Recursive
    """
    :type head: ListNode
    :rtype: ListNode
    """    
    #    curr　curr.next
    #     ↓  ↓     
    # prev  1 -> 2 -> None
    #     prev curr　 curr.next
    #      ↓  ↓  ↓     
    # None <- 1 -> 2 -> None    
    prev, curr = None, head
    while curr:
      #curr.next, prev, curr = prev, curr, curr.next
      prev, curr.next, curr = curr, prev, curr.next
    return prev
