from LList import LinkedList, display, Node

def partition(head: Node, x: int) -> Node:
    """
    Partitions a linked list around a value x such that all nodes less than x come before all nodes
    greater than or equal to x.

    Args:
    head (Node): The head node of the linked list.
    x (int): The partition value.

    Returns:
    Node: The head node of the partitioned linked list.

    Time Complexity: O(N), where N is the number of nodes in the linked list.
    Space Complexity: O(1), in-place partitioning.
    """
    if head is None:
        return None

    # Create two dummy nodes to start the less and greater lists
    less_head = less = Node(0)
    greater_head = greater = Node(0)

    current = head
    while current:
        if current.data < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next

    # Terminate the greater list
    greater.next = None
    # Connect the less list with the greater list
    less.next = greater_head.next

    return less_head.next

# Comprehensive test cases
def run_tests():
    # Test case 1: General case with multiple elements
    items = [3, 5, 8, 5, 10, 2, 1]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 1 - Original linked list:")
    display(head)

    x = 5
    head = partition(head, x)
    print(f"After partitioning around {x}:")
    display(head)
    print("-" * 50)

    # Test case 2: All elements less than x
    items = [1, 2, 3, 4]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 2 - Original linked list:")
    display(head)

    x = 5
    head = partition(head, x)
    print(f"After partitioning around {x}:")
    display(head)
    print("-" * 50)

    # Test case 3: All elements greater than or equal to x
    items = [6, 7, 8, 9]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 3 - Original linked list:")
    display(head)

    x = 5
    head = partition(head, x)
    print(f"After partitioning around {x}:")
    display(head)
    print("-" * 50)

    # Test case 4: Elements equal to x
    items = [5, 5, 5, 5]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 4 - Original linked list:")
    display(head)

    x = 5
    head = partition(head, x)
    print(f"After partitioning around {x}:")
    display(head)
    print("-" * 50)

    # Test case 5: Single element
    items = [3]
    linked_list = LinkedList()
    linked_list.insert(items[0])
    head = linked_list.get_head()
    print("Test case 5 - Original linked list:")
    display(head)

    x = 5
    head = partition(head, x)
    print(f"After partitioning around {x}:")
    display(head)
    print("-" * 50)

    # Test case 6: Empty list
    linked_list = LinkedList()
    head = linked_list.get_head()
    print("Test case 6 - Original linked list:")
    display(head)

    x = 5
    head = partition(head, x)
    print(f"After partitioning around {x}:")
    display(head)
    print("-" * 50)

run_tests()
