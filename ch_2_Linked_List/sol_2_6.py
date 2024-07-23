from LList import LinkedList, display, Node

def check_palindrome(head: Node) -> bool:
    """
    Checks if the given linked list is a palindrome.
    
    Args:
    head (Node): The head node of the linked list.

    Returns:
    bool: True if the linked list is a palindrome, False otherwise.
    
    Time Complexity: O(N), where N is the number of nodes in the linked list.
    Space Complexity: O(N), for storing the left half of the list.
    """
    if head is None:
        return False

    # Use two pointers to find the middle of the linked list
    fast = head
    slow = head
    left_half = []

    # Move slow pointer one step and fast pointer two steps at a time
    while fast and fast.next:
        left_half.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # If the length is odd, skip the middle element
    if fast:
        slow = slow.next

    # Compare the second half of the list with the reversed first half
    while slow:
        if slow.data != left_half.pop():
            return False
        slow = slow.next

    return True

def check_palindrome_optimized(head: Node):
    """
    Checks if the given linked list is a palindrome.
    
    Args:
    head (Node): The head node of the linked list.

    Returns:
    bool: True if the linked list is a palindrome, False otherwise.
    
    Time Complexity: O(N), where N is the number of nodes in the linked list.
    Space Complexity: O(1), for storing the left half of the list.
    """
    if head is None:
        return False

    # Use two pointers to find the middle of the linked list
    fast = head
    slow = head
    current = head
    
    # Move slow pointer one step and fast pointer two steps at a time
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # If the length is odd, skip the middle element
    if fast:
        slow = slow.next
    
    while slow:
        if current.data != slow.data:
            return False
        current = current.next
        slow =  slow.next
    
    return True

# Comprehensive test cases
def run_tests():
    # Test case 1: Palindrome list with even number of elements
    items = [3, 5, 8, 8, 5, 3]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 1 - Original linked list:")
    display(head)
    print("Is palindrome?", check_palindrome_optimized(head))
    print("-" * 50)

    # Test case 2: Palindrome list with odd number of elements
    items = [3, 5, 8, 5, 3]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 2 - Original linked list:")
    display(head)
    print("Is palindrome?", check_palindrome_optimized(head))
    print("-" * 50)

    # Test case 3: Non-palindrome list
    items = [3, 5, 8, 7, 5, 3]
    linked_list = LinkedList()
    for item in items:
        linked_list.insert(item)
    head = linked_list.get_head()
    print("Test case 3 - Original linked list:")
    display(head)
    print("Is palindrome?", check_palindrome_optimized(head))
    print("-" * 50)

    # Test case 4: Single element list
    items = [3]
    linked_list = LinkedList()
    linked_list.insert(items[0])
    head = linked_list.get_head()
    print("Test case 4 - Original linked list:")
    display(head)
    print("Is palindrome?", check_palindrome_optimized(head))
    print("-" * 50)

    # Test case 5: Empty list
    linked_list = LinkedList()
    head = linked_list.get_head()
    print("Test case 5 - Original linked list:")
    display(head)
    print("Is palindrome?", check_palindrome_optimized(head))
    print("-" * 50)

run_tests()
