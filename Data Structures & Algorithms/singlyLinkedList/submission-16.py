class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        if index < 0 or not self.head:
            return -1
        if index == 0:
            return self.head.val
        
        i = 0
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1
        return curr.val if curr else -1 
    
    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self, index: int) -> bool:
        if index < 0 or not self.head:
            return False
        
        if index == 0:
            self.head = self.head.next
            return True
        
        i = 0
        curr = self.head
        while curr.next and i < index - 1:
            curr = curr.next
            i += 1
        if curr.next: 
            curr.next = curr.next.next
            return True
        
        return False
        
    def getValues(self) -> List[int]:
        ll_values = []
        curr = self.head
        while curr:
            ll_values.append(curr.val)
            curr = curr.next
        return ll_values
