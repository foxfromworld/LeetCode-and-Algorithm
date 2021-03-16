# Source : https://leetcode.com/problems/linked-list-cycle/
# Author : foxfromworld
# Date  : 16/03/2021
# First attempt #very slow

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    seen = []
    while head:
      if head in seen:
        return True
      else:
        seen.append(head)
      head = head.next
    return False
