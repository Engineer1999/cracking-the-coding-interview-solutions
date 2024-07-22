from LList import LinkedList, display

def find_kth_last_element(head, k):
    """
    Finds the k-th last element in a linked list.

    Args:
    head (Node): The head node of the linked list.
    k (int): The position from the end (1-based index).

    Returns:
    The data of the k-th last element if it exists, otherwise False.

    Time Complexity: O(N), where N is the number of nodes in the linked list.
    Space Complexity: O(1), constant space usage.
    """
    if head is None or k <= 0:
        return False
    
    current = head
    runner = head
    
    # Move runner k nodes ahead
    for _ in range(k):
        if runner is None:
            return False
        runner = runner.next
    
    # Move both pointers until runner reaches the end
    while runner:
        runner = runner.next
        current = current.next
    
    return current.data

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

    print("Finding 3rd last element:")
    print(find_kth_last_element(head, 3))  # Expected output: 6

    # Test case 2: k is equal to the length of the list
    print("Finding 10th last element:")
    print(find_kth_last_element(head, 10))  # Expected output: 1

    # Test case 3: k is greater than the length of the list
    print("Finding 11th last element:")
    print(find_kth_last_element(head, 11))  # Expected output: False

    # Test case 4: k is 1 (last element)
    print("Finding 1st last element:")
    print(find_kth_last_element(head, 1))  # Expected output: 6

    # Test case 5: Single element in the list
    linked_list = LinkedList()
    linked_list.insert(1)
    head = linked_list.get_head()
    print("Test case 5 - Original linked list:")
    display(head)

    print("Finding 1st last element in single-element list:")
    print(find_kth_last_element(head, 1))  # Expected output: 1

    # Test case 6: Empty list
    linked_list = LinkedList()
    head = linked_list.get_head()
    print("Test case 6 - Original linked list:")
    display(head)

    print("Finding 1st last element in empty list:")
    print(find_kth_last_element(head, 1))  # Expected output: False

run_tests()
