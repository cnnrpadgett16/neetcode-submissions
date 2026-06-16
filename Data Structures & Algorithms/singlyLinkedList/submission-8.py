class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int: 
        if (self.head is None):
            return -1
        else:
            current_node = self.head
            position = 0
            while (current_node and position != index):
                current_node = current_node.next
                position += 1
            if (current_node):
                return current_node.data
            else:
                return -1 
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
            

    def insertTail(self, val: int) -> None:
        if (self.head is None):
            self.insertHead(val)
            return
        else:
            new_node = Node(val)
            current_node = self.head
            while (current_node.next is not None):
                current_node = current_node.next
            current_node.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        current_node = self.head
        position = 0

        if index == 0:
            self.head = self.head.next
            return True
        else:
            while (current_node is not None and position < index - 1):
                current_node = current_node.next
                position += 1
      
        if (current_node is not None and current_node.next is not None):
            current_node.next = current_node.next.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        if self.head is None: 
            return []
        
        val_array = []
        current_node = self.head
        while (current_node):
            val_array.append(current_node.data)
            current_node = current_node.next
        
        return val_array

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
