# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        ## Reverse the second half
        prev = None
        curr = second

        while curr:
            next_node = curr.next # save off the reference to next
            curr.next = prev # reverse the direction of the original .next
            prev = curr # move previous to the curr position
            curr = next_node # move curr to the next node
        
        ## Merge the two lists together
        first_head = head
        second_head = prev

        while second_head:
            tmp1 = first_head.next
            tmp2 = second_head.next
            first_head.next = second_head
            second_head.next = tmp1
            first_head = tmp1
            second_head = tmp2

        
        
        
