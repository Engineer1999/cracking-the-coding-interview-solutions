from LList import LinkedList, display, Node

def get_llist_size(head):
    if head is None:
        return (0, None)
    
    current = head
    cnt = 0
    while current:
        temp = current
        current = current.next
        cnt+=1
        
    return (cnt, temp)

def check_intersection(head_1, head_2):
    len_1, ll1_last_node = get_llist_size(head_1)
    len_2, ll2_last_node = get_llist_size(head_2)
    
    if ll1_last_node != ll2_last_node:
        return (False, None)
    
    if len_1 > len_2:
        long_head, short_head = head_1, head_2
    elif len_1 < len_2:
        long_head, short_head = head_2, head_1
    else:
        long_head, short_head = head_1, head_2
    
    for i in range(abs(len_1-len_2)):
        long_head = long_head.next
        
        
    while short_head != long_head:
        short_head = short_head.next
        long_head = long_head.next
        
    if long_head:
        return (True, long_head)
    else:
        return (False, None)

def run_tests():
    # Test case 1: No intersection
    items_1 = [1, 2, 3, 4, 5]
    items_2 = [6, 7, 8, 9, 10]
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    for item in items_1:
        linked_list_1.insert(item)
    for item in items_2:
        linked_list_2.insert(item)
    head_1 = linked_list_1.get_head()
    head_2 = linked_list_2.get_head()
    print("Test case 1 - Original linked lists:")
    display(head_1)
    display(head_2)
    intersection = check_intersection(head_1, head_2)
    print("Intersection:", intersection)
    print("-" * 50)

    # Test case 2: Intersection at a common node
    common_node = Node(8)
    items_1 = [1, 2, 3, 4, 5]
    items_2 = [6, 7]
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    for item in items_1:
        linked_list_1.insert(item)
    for item in items_2:
        linked_list_2.insert(item)
    linked_list_1.head.next.next.next.next.next = common_node  # Linking to common node
    linked_list_2.head.next.next = common_node  # Linking to common node
    linked_list_1.insert(9)
    linked_list_1.insert(10)
    head_1 = linked_list_1.get_head()
    head_2 = linked_list_2.get_head()
    print("Test case 2 - Original linked lists:")
    display(head_1)
    display(head_2)
    intersection = check_intersection(head_1, head_2)
    print("Intersection:", intersection)
    print("-" * 50)

    # Test case 3: Intersection at head node
    common_node = Node(1)
    items_1 = [1, 2, 3, 4, 5]
    items_2 = [1, 6, 7, 8]
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_1.head = common_node
    linked_list_2.head = common_node
    for item in items_1[1:]:
        linked_list_1.insert(item)
    for item in items_2[1:]:
        linked_list_2.insert(item)
    head_1 = linked_list_1.get_head()
    head_2 = linked_list_2.get_head()
    print("Test case 3 - Original linked lists:")
    display(head_1)
    display(head_2)
    intersection = check_intersection(head_1, head_2)
    print("Intersection:", intersection)
    print("-" * 50)

    # Test case 4: One empty list
    items_1 = [1, 2, 3, 4, 5]
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    for item in items_1:
        linked_list_1.insert(item)
    head_1 = linked_list_1.get_head()
    head_2 = linked_list_2.get_head()
    print("Test case 4 - Original linked lists:")
    display(head_1)
    display(head_2)
    intersection = check_intersection(head_1, head_2)
    print("Intersection:", intersection)
    print("-" * 50)

    # Test case 5: Both lists empty
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    head_1 = linked_list_1.get_head()
    head_2 = linked_list_2.get_head()
    print("Test case 5 - Original linked lists:")
    display(head_1)
    display(head_2)
    intersection = check_intersection(head_1, head_2)
    print("Intersection:", intersection)
    print("-" * 50)

run_tests()
