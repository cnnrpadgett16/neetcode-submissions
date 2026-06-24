# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_array = []
        # iterate through nodes and add them to the array
        curr = head
        while curr:
            node_array.append(curr)
            curr = curr.next
        
        # Now we have an array of nodes
        left, right = 0, len(node_array) - 1
        while left < right:
            node_array[left].next = node_array[right]
            left +=1
            node_array[right].next = node_array[left]
            right -= 1
        
        node_array[left].next = None
        
        
        
