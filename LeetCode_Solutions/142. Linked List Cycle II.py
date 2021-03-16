# Source : https://leetcode.com/problems/linked-list-cycle-ii/
# Author : foxfromworld
# Date  : 16/03/2021
# First attempt

class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    seen = set()
    while head:
      if head in seen:
        return head
      seen.add(head)
      head = head.next
    return None
