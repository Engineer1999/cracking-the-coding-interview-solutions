class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data):
        self.stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        if self.isEmpty():
            return None
        data = self.stack.pop()
        if data == self.min_stack[-1]:
            self.min_stack.pop()
        return data

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

# Test cases
def test_stack():
    stack = Stack()

    # Test isEmpty on an empty stack
    assert stack.isEmpty() == True, "Test case 1 failed"

    # Test push and peek
    stack.push(10)
    assert stack.peek() == 10, "Test case 2 failed"
    assert stack.isEmpty() == False, "Test case 3 failed"

    # Test push and min
    stack.push(5)
    assert stack.min() == 5, "Test case 4 failed"

    # Test push and min with a larger element
    stack.push(15)
    assert stack.min() == 5, "Test case 5 failed"

    # Test pop
    assert stack.pop() == 15, "Test case 6 failed"
    assert stack.pop() == 5, "Test case 7 failed"
    assert stack.min() == 10, "Test case 8 failed"

    # Test pop to empty the stack
    assert stack.pop() == 10, "Test case 9 failed"
    assert stack.isEmpty() == True, "Test case 10 failed"
    assert stack.pop() == None, "Test case 11 failed"
    assert stack.peek() == None, "Test case 12 failed"
    assert stack.min() == None, "Test case 13 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    test_stack()