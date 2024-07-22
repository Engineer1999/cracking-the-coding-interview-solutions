class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """
        Insert a new node with the specified data at the end of the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def get_head(self):
        """
        Return the head node of the linked list.
        """
        return self.head


def display(head):
    """
    Display the linked list elements.
    
    Args:
    head (Node): The head node of the linked list.
    """
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()