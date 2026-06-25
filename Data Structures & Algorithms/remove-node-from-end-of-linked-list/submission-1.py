# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:


    '''
         l   r
    0 [1,2,3,4] n = 2

    l    r
    0 [2]     n = 2



    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        left = right = dummy

        for _ in range(n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        
        left.next =left.next.next

        return dummy.next     

        