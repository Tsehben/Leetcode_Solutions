# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # using happy case to implement

        dummy = ListNode(0, head)
        cur = head

        lprev = dummy

        for i in range(left - 1):
            lprev = cur
            cur = cur.next
            

        # next step, reverse linked list the usual way

        prev = None 

        for i in range(right - left + 1):
            tempNext = cur.next
            cur.next = prev
            prev = cur
            cur = tempNext

        # now cur is at r + 1, eend prev is at r

        # update pointers
        lprev.next.next = cur
        lprev.next = prev
        

        return dummy.next
