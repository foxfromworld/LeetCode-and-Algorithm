# Source : https://leetcode.com/problems/swap-nodes-in-pairs/
# Author : foxfromworld
# Date   : 08/03/2022
# First attempt

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        # dummy -> head
        #  　prev ↗
        while head and head.next:
            # 1->2->3->4
            # 1st->2nd ... 1st -> 2nd
            first = head
            second = head.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
            head = first.next
        return dummy.next
