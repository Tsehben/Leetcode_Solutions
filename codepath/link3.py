class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # pointing to our answer hence extra space being used, and assign this to cur
        dummy = ListNode()
        cur  = dummy

        # we would be iterating through the two linkedlist whiles it doesn't return Null

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            #digit formation

            val = v1 + v2 + carry
            carry = val // 10

            val = val % 10
            
            cur.next = ListNode(val)

            #update pointers 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return dummy.next

# reverse linked lIst

#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head

        while cur:
             nxt = cur.next
             cur.next = prev
             prev = cur
             cur = nxt
        
        return prev
        