from LList import LinkedList, display, Node

def get_number(head):
    """
    Converts a linked list representing a number into an integer.
    
    Args:
    head (Node): The head node of the linked list.

    Returns:
    int: The integer representation of the number.
    
    Time Complexity: O(N), where N is the number of nodes in the linked list.
    Space Complexity: O(N), due to the additional list used to store digits.
    """
    number = 0
    digit_list = []
    
    current = head
    while current:
        digit_list.append(current.data)
        current = current.next
    
    for i in range(len(digit_list)):
        number += digit_list.pop() * (10 ** i)
    
    return number

def number_to_llist(number):
    """
    Converts an integer to a linked list where each digit is a node.
    
    Args:
    number (int): The integer to be converted.

    Returns:
    Node: The head node of the linked list representing the number.
    
    Time Complexity: O(N), where N is the number of digits in the number.
    Space Complexity: O(N), where N is the number of digits in the number.
    """
    linked_list = LinkedList()
    items = [int(x) for x in str(number)]
    for item in items:
        linked_list.insert(item)
    return linked_list.get_head()

def calculate_sum(head_1, head_2):
    """
    Calculates the sum of two numbers represented by linked lists.
    
    Args:
    head_1 (Node): The head node of the first linked list.
    head_2 (Node): The head node of the second linked list.

    Returns:
    Node: The head node of the linked list representing the sum.
    
    Time Complexity: O(N), where N is the maximum length of the two linked lists.
    Space Complexity: O(N), for storing the result in a new linked list.
    """
    number_1 = get_number(head_1)
    number_2 = get_number(head_2)
    sum_number = number_1 + number_2
    return number_to_llist(sum_number)

# Comprehensive test cases
def run_tests():
    # Test case 1: General case with multiple elements
    items_1 = [3, 5, 8, 5]
    items_2 = [1, 3, 5]
    linked_list_1 = LinkedList()
    for item in items_1:
        linked_list_1.insert(item)
    head_1 = linked_list_1.get_head()
    
    linked_list_2 = LinkedList()
    for item in items_2:
        linked_list_2.insert(item)
    head_2 = linked_list_2.get_head()

    print("Test case 1 - Original linked lists:")
    display(head_1)
    display(head_2)
    
    head_3 = calculate_sum(head_1, head_2)
    print("Resultant linked list after sum:")
    display(head_3)
    print("-" * 50)

    # Test case 2: Single element lists
    items_1 = [9]
    items_2 = [5]
    linked_list_1 = LinkedList()
    linked_list_1.insert(items_1[0])
    head_1 = linked_list_1.get_head()

    linked_list_2 = LinkedList()
    linked_list_2.insert(items_2[0])
    head_2 = linked_list_2.get_head()

    print("Test case 2 - Original linked lists:")
    display(head_1)
    display(head_2)

    head_3 = calculate_sum(head_1, head_2)
    print("Resultant linked list after sum:")
    display(head_3)
    print("-" * 50)

    # Test case 3: One list is empty
    items_1 = [1, 2, 3]
    items_2 = []
    linked_list_1 = LinkedList()
    for item in items_1:
        linked_list_1.insert(item)
    head_1 = linked_list_1.get_head()

    linked_list_2 = LinkedList()
    head_2 = linked_list_2.get_head()

    print("Test case 3 - Original linked lists:")
    display(head_1)
    display(head_2)

    head_3 = calculate_sum(head_1, head_2)
    print("Resultant linked list after sum:")
    display(head_3)
    print("-" * 50)

    # Test case 4: Both lists are empty
    linked_list_1 = LinkedList()
    head_1 = linked_list_1.get_head()

    linked_list_2 = LinkedList()
    head_2 = linked_list_2.get_head()

    print("Test case 4 - Original linked lists:")
    display(head_1)
    display(head_2)

    head_3 = calculate_sum(head_1, head_2)
    print("Resultant linked list after sum:")
    display(head_3)
    print("-" * 50)

run_tests()
