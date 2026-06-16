class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1 
        if index == 0:
            return self.head.data
        
        position = 0
        current_node = self.head
        while(current_node != None and position != index):
            position += 1
            current_node = current_node.next
        if current_node != None:
            return current_node.data
        return -1

        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        if self.head is None: 
            self.insertHead(val)
            return
        new_node = Node(val)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        current_node = self.head
        position = 0
    
        if index == 0:
            current_node = self.head
            self.head = current_node.next
            return True
        else:
            while current_node is not None and position < index - 1:
                position += 1
                current_node = current_node.next
            if current_node is None or current_node.next is None:
                return False
            else:
                current_node.next = current_node.next.next
                return True
        return False
    
    def getValues(self) -> List[int]:
        my_list = list()
        if self.head is None:
            return []
        else:
            current_node = self.head
            while(current_node):
                my_list.append(current_node.data)
                current_node = current_node.next
        return my_list

        
