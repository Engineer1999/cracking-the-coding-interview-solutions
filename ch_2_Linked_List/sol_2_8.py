from LList import LinkedList, Node, display

def find_loop(head):
    slow_runner = head
    fast_runner = head
    collision = False
    
    while fast_runner and fast_runner.next:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
        if slow_runner == fast_runner:
            collision = True
            break
        
    if not collision:
        return None
    
    slow_runner = head
    while slow_runner != fast_runner:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next
    
    return fast_runner

def test_find_loop():
    # Test case 1: No loop in the list
    ll1 = LinkedList()
    for i in range(1, 6):
        ll1.insert(i)
    
    assert find_loop(ll1.get_head()) is None, "Test case 1 failed: Expected None, but got a loop."

    # Test case 2: Single node with no loop
    ll2 = LinkedList()
    ll2.insert(1)
    
    assert find_loop(ll2.get_head()) is None, "Test case 2 failed: Expected None, but got a loop."

    # Test case 3: Single node with a loop (node points to itself)
    ll3 = LinkedList()
    ll3.insert(1)
    ll3.get_head().next = ll3.get_head()  # Creating a loop
    
    assert find_loop(ll3.get_head()) == ll3.get_head(), "Test case 3 failed: Expected loop at node with value 1."

    # Test case 4: Multiple nodes with a loop in the middle
    ll4 = LinkedList()
    for i in range(1, 6):
        ll4.insert(i)
    
    loop_start = ll4.get_head().next.next  # Node with value 3
    end = ll4.get_head()
    while end.next:
        end = end.next
    end.next = loop_start  # Creating a loop
    
    assert find_loop(ll4.get_head()) == loop_start, "Test case 4 failed: Expected loop at node with value 3."

    # Test case 5: Multiple nodes with a loop at the end
    ll5 = LinkedList()
    for i in range(1, 6):
        ll5.insert(i)
    
    loop_start = ll5.get_head().next.next.next.next  # Node with value 5
    end = ll5.get_head()
    while end.next:
        end = end.next
    end.next = loop_start  # Creating a loop
    
    assert find_loop(ll5.get_head()) == loop_start, "Test case 5 failed: Expected loop at node with value 5."

    print("All test cases passed!")


# Run the tests
test_find_loop()
