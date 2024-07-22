from LList import LinkedList, display, Node

def delete_middle_node(node: Node):
    """
    Deletes a node in the middle of a singly linked list, given only access to that node.
    
    Args:
    node (Node): The node to be deleted.

    Returns:
    bool: True if the deletion was successful, False if it was not (e.g., node is the last node).

    Time Complexity: O(1), constant time to delete the node.
    Space Complexity: O(1), constant space usage.
    """
    if node is None or node.next is None:
        return False  # Failure, can't delete the node if it's the last one or None
    
    node.data = node.next.data
    node.next = node.next.next
    return True

# Comprehensive test cases
def run_tests():
    # Test case 1: General case with multiple elements
    items = [1, 2, 3, 2, 4, 5, 4, 6, 7, 6]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 1 - Original linked list:")
    display(head)

    # Delete node with value 3 (3rd element)
    node_to_delete = head.next.next  # This should point to the node with value 3
    delete_middle_node(node_to_delete)
    print("After deleting node with value 3:")
    display(head)
    print()

    # Test case 2: Delete node with value 4 (first 4)
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    node_to_delete = head.next.next.next.next  # This should point to the node with value 4
    delete_middle_node(node_to_delete)
    print("Test case 2 - After deleting node with value 4:")
    display(head)
    print()

    # Test case 3: Attempt to delete the last node (should fail)
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    node_to_delete = head
    while node_to_delete.next.next:  # Move to the second-to-last node
        node_to_delete = node_to_delete.next
    print(delete_middle_node(node_to_delete.next))
    print("Test case 3 - After attempting to delete the last node (should fail):")
    display(head)
    print()

    # Test case 4: Single element list (delete should fail)
    linked_list = LinkedList()
    linked_list.insert(1)
    head = linked_list.get_head()
    print("Test case 4 - Single element list before deletion:")
    display(head)
    result = delete_middle_node(head)
    print(result)
    print("Deletion result (should be False):", result)
    display(head)
    print()

    # Test case 5: Empty list (nothing to delete)
    linked_list = LinkedList()
    head = linked_list.get_head()
    print("Test case 5 - Empty list before deletion:")
    display(head)
    result = delete_middle_node(head)
    print(result)
    print("Deletion result (should be False):", result)
    display(head)
    print()

run_tests()
