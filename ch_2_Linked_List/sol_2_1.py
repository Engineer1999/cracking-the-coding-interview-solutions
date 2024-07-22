from LList import LinkedList, display

def remove_dups_using_buffer(linked_list):
    """
    Remove duplicates from an unsorted linked list using a buffer (additional space).

    Args:
    linked_list (Node): The head node of the linked list.

    Returns:
    Node: The head node of the modified linked list without duplicates.

    Time Complexity: O(N), where N is the number of nodes in the linked list.
    Space Complexity: O(N), where N is the number of nodes in the linked list.
    """
    if not linked_list:
        return linked_list
    
    unique_values = set()
    current = linked_list
    unique_values.add(current.data)
    
    while current.next:
        if current.next.data in unique_values:
            current.next = current.next.next
        else:
            unique_values.add(current.next.data)
            current = current.next
    
    return linked_list

def remove_dups_without_buffer(head):
    """
    Remove duplicates from an unsorted linked list without using a buffer.

    Args:
    head (Node): The head node of the linked list.

    Returns:
    Node: The head node of the modified linked list without duplicates.

    Time Complexity: O(N^2), where N is the number of nodes in the linked list.
    Space Complexity: O(1), no additional space is used.
    """
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


def run_tests():
    # Test case 1: General case with duplicates
    items = [1, 2, 3, 2, 4, 5, 4, 6, 7, 6]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 1 - Original linked list:")
    display(head)

    print("Test case 1 - After removing duplicates using buffer:")
    remove_dups_using_buffer(head)
    display(head)

    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 1 - After removing duplicates without buffer:")
    remove_dups_without_buffer(head)
    display(head)
    print()

    # Test case 2: No duplicates
    items = [1, 2, 3, 4, 5, 6]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 2 - Original linked list:")
    display(head)

    print("Test case 2 - After removing duplicates using buffer:")
    remove_dups_using_buffer(head)
    display(head)

    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 2 - After removing duplicates without buffer:")
    remove_dups_without_buffer(head)
    display(head)
    print()

    # Test case 3: All duplicates
    items = [1, 1, 1, 1, 1]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 3 - Original linked list:")
    display(head)

    print("Test case 3 - After removing duplicates using buffer:")
    remove_dups_using_buffer(head)
    display(head)

    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 3 - After removing duplicates without buffer:")
    remove_dups_without_buffer(head)
    display(head)
    print()

    # Test case 4: Single element
    items = [1]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 4 - Original linked list:")
    display(head)

    print("Test case 4 - After removing duplicates using buffer:")
    remove_dups_using_buffer(head)
    display(head)

    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 4 - After removing duplicates without buffer:")
    remove_dups_without_buffer(head)
    display(head)
    print()

    # Test case 5: Empty list
    items = []
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 5 - Original linked list:")
    display(head)

    print("Test case 5 - After removing duplicates using buffer:")
    remove_dups_using_buffer(head)
    display(head)

    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 5 - After removing duplicates without buffer:")
    remove_dups_without_buffer(head)
    display(head)
    print()

    # Test case 6: Multiple types of elements (if allowed)
    items = ['a', 'b', 'a', 'c', 'b']
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 6 - Original linked list:")
    display(head)

    print("Test case 6 - After removing duplicates using buffer:")
    remove_dups_using_buffer(head)
    display(head)

    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 6 - After removing duplicates without buffer:")
    remove_dups_without_buffer(head)
    display(head)
    print()

run_tests()

