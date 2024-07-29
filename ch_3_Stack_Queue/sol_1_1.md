### Detailed Description of Methods for Implementing Three Stacks Using a Single Array

#### Method 1: Fixed Division Method

**Description:**
The array is divided into three equal parts, each representing a stack. Separate pointers are maintained to track the top element of each stack.

**Implementation Details:**

1. **Initialization:**
   - Suppose the array size is `N`.
   - Divide the array into three parts:
     - Stack 1: `arr[0]` to `arr[N/3 - 1]`
     - Stack 2: `arr[N/3]` to `arr[2N/3 - 1]`
     - Stack 3: `arr[2N/3]` to `arr[N - 1]`

2. **Pointers:**
   - `top1`, `top2`, `top3` initialized to `-1`, `N/3 - 1`, and `2N/3 - 1`, respectively.

3. **Push Operation:**
   - Stack 1: Increment `top1` and insert at `arr[top1]`.
   - Stack 2: Increment `top2` and insert at `arr[top2]`.
   - Stack 3: Increment `top3` and insert at `arr[top3]`.

4. **Pop Operation:**
   - Stack 1: Return `arr[top1]` and decrement `top1`.
   - Stack 2: Return `arr[top2]` and decrement `top2`.
   - Stack 3: Return `arr[top3]` and decrement `top3`.

**Pros:**
- Simple and straightforward.
- Easy to implement and understand.

**Cons:**
- Inflexible as each stack has a fixed size.
- Inefficient space utilization if one stack is full while others are empty.

**Use Case:**
- Suitable for scenarios where the maximum size of each stack is known and fixed.
- Ideal for basic demonstrations of stack operations and array manipulation in interviews.

**Example Code:**

```python
class ThreeStacks:
    def __init__(self, n):
        self.n = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n // 3 - 1
        self.top3 = 2 * n // 3 - 1

    def push1(self, x):
        if self.top1 + 1 < self.n // 3:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            raise Exception("Stack 1 Overflow")

    def push2(self, x):
        if self.top2 + 1 < 2 * self.n // 3:
            self.top2 += 1
            self.arr[self.top2] = x
        else:
            raise Exception("Stack 2 Overflow")

    def push3(self, x):
        if self.top3 + 1 < self.n:
            self.top3 += 1
            self.arr[self.top3] = x
        else:
            raise Exception("Stack 3 Overflow")

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return x
        else:
            raise Exception("Stack 1 Underflow")

    def pop2(self):
        if self.top2 >= self.n // 3:
            x = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 -= 1
            return x
        else:
            raise Exception("Stack 2 Underflow")

    def pop3(self):
        if self.top3 >= 2 * self.n // 3:
            x = self.arr[self.top3]
            self.arr[self.top3] = None
            self.top3 -= 1
            return x
        else:
            raise Exception("Stack 3 Underflow")

# Example usage:
stacks = ThreeStacks(9)
stacks.push1(10)
stacks.push2(20)
stacks.push3(30)
print(stacks.pop1())  # Output: 10
print(stacks.pop2())  # Output: 20
print(stacks.pop3())  # Output: 30
```

#### Method 2: Dynamic Division Method (Using Auxiliary Arrays)

**Description:**
Use an auxiliary array to keep track of the next free position and a free list to handle dynamic allocation of space.

**Implementation Details:**

1. **Initialization:**
   - Use an array `arr` of size `N`.
   - Maintain three stack pointers `top1`, `top2`, and `top3` initialized to `-1`, `N/3 - 1`, and `2N/3 - 1`, respectively.
   - Use an auxiliary array `next` to keep track of the next free position.
   - Initialize `next` such that `next[i] = i + 1` for `0 <= i < N - 1` and `next[N - 1] = -1`.

2. **Free List:**
   - Maintain an index `free` to keep track of the first free index in `arr`.

3. **Push Operation:**
   - Use `free` index to get the free position.
   - Update `free` index to the next free position using `next` array.
   - Insert the element at the free position and update `next` array and stack pointers accordingly.

4. **Pop Operation:**
   - Use the stack pointer to get the top element.
   - Update the stack pointer to the next element in the stack using `next` array.
   - Update `next` array to include the popped index back into the free list.

**Pros:**
- More flexible than the fixed division method.
- Allows dynamic adjustment of stack sizes based on available space.

**Cons:**
- More complex to implement and maintain.
- Overhead of managing the auxiliary array and free list.

**Use Case:**
- Suitable for scenarios where the stack sizes are highly variable and unpredictable.
- Ideal for demonstrating dynamic memory management and advanced data structures in interviews.

**Example Code:**

```python
class DynamicThreeStacks:
    def __init__(self, n):
        self.n = n
        self.arr = [None] * n
        self.next = list(range(1, n)) + [-1]
        self.free = 0
        self.top1 = -1
        self.top2 = -1
        self.top3 = -1

    def push(self, stack_num, x):
        if self.free == -1:
            raise Exception("Stack Overflow")
        free_index = self.free
        self.free = self.next[free_index]
        if stack_num == 1:
            self.next[free_index] = self.top1
            self.top1 = free_index
        elif stack_num == 2:
            self.next[free_index] = self.top2
            self.top2 = free_index
        elif stack_num == 3:
            self.next[free_index] = self.top3
            self.top3 = free_index
        else:
            raise Exception("Invalid Stack Number")
        self.arr[free_index] = x

    def pop(self, stack_num):
        if stack_num == 1:
            if self.top1 == -1:
                raise Exception("Stack 1 Underflow")
            top_index = self.top1
            self.top1 = self.next[top_index]
        elif stack_num == 2:
            if self.top2 == -1:
                raise Exception("Stack 2 Underflow")
            top_index = self.top2
            self.top2 = self.next[top_index]
        elif stack_num == 3:
            if self.top3 == -1:
                raise Exception("Stack 3 Underflow")
            top_index = self.top3
            self.top3 = self.next[top_index]
        else:
            raise Exception("Invalid Stack Number")
        self.next[top_index] = self.free
        self.free = top_index
        x = self.arr[top_index]
        self.arr[top_index] = None
        return x

# Example usage:
stacks = DynamicThreeStacks(9)
stacks.push(1, 10)
stacks.push(2, 20)
stacks.push(3, 30)
print(stacks.pop(1))  # Output: 10
print(stacks.pop(2))  # Output: 20
print(stacks.pop(3))  # Output: 30
```

#### Method 3: Doubly Linked List Method (Each Node Holds Three Elements)

**Description:**
Use a doubly linked list where each node holds three elements, one for each stack. Maintain separate pointers for each stack.

**Implementation Details:**

1. **Node Structure:**
   - Each node in the doubly linked list will hold three elements and pointers to the previous and next nodes.

2. **Stack Pointers:**
   - Maintain three pointers (`top1`, `top2`, `top3`) to keep track of the top elements of each stack.

3. **Push Operation:**
   - When pushing an element, add it to the corresponding position in the current node. If the current node is full, create a new node and link it.

4. **Pop Operation:**
   - When popping an element, remove it from the corresponding position. If the current node becomes empty, adjust the pointers to remove the node if necessary.

**Pros:**
- Flexible and allows for dynamic growth of each stack.
- Efficient space utilization as nodes are created only when needed.

**Cons:**
- More complex implementation compared to array-based methods.
- Over

head of managing pointers and linked list structure.

**Use Case:**
- Suitable for scenarios where space utilization and dynamic growth are critical.
- Ideal for demonstrating linked list operations and memory management in interviews.

**Example Code:**

```python
class Node:
    def __init__(self):
        self.elements = [None, None, None]
        self.next = None
        self.prev = None

class ThreeStacks:
    def __init__(self):
        self.head = Node()
        self.top1 = self.head
        self.top2 = self.head
        self.top3 = self.head

    def push1(self, x):
        if self.top1.elements[0] is None:
            self.top1.elements[0] = x
        else:
            new_node = Node()
            new_node.elements[0] = x
            new_node.next = self.top1
            self.top1.prev = new_node
            self.top1 = new_node

    def push2(self, x):
        if self.top2.elements[1] is None:
            self.top2.elements[1] = x
        else:
            new_node = Node()
            new_node.elements[1] = x
            new_node.next = self.top2
            self.top2.prev = new_node
            self.top2 = new_node

    def push3(self, x):
        if self.top3.elements[2] is None:
            self.top3.elements[2] = x
        else:
            new_node = Node()
            new_node.elements[2] = x
            new_node.next = self.top3
            self.top3.prev = new_node
            self.top3 = new_node

    def pop1(self):
        if self.top1.elements[0] is not None:
            x = self.top1.elements[0]
            self.top1.elements[0] = None
            if all(e is None for e in self.top1.elements) and self.top1 != self.head:
                self.top1 = self.top1.next
                self.top1.prev = None
            return x
        else:
            raise Exception("Stack 1 Underflow")

    def pop2(self):
        if self.top2.elements[1] is not None:
            x = self.top2.elements[1]
            self.top2.elements[1] = None
            if all(e is None for e in self.top2.elements) and self.top2 != self.head:
                self.top2 = self.top2.next
                self.top2.prev = None
            return x
        else:
            raise Exception("Stack 2 Underflow")

    def pop3(self):
        if self.top3.elements[2] is not None:
            x = self.top3.elements[2]
            self.top3.elements[2] = None
            if all(e is None for e in self.top3.elements) and self.top3 != self.head:
                self.top3 = self.top3.next
                self.top3.prev = None
            return x
        else:
            raise Exception("Stack 3 Underflow")

# Example usage:
stacks = ThreeStacks()
stacks.push1(10)
stacks.push2(20)
stacks.push3(30)
print(stacks.pop1())  # Output: 10
print(stacks.pop2())  # Output: 20
print(stacks.pop3())  # Output: 30
```

#### Method 4: Interleaved Index Method

**Description:**
Use a fixed-size array and interleave the elements of the three stacks. Stack 1 elements are stored at indices `0, 3, 6, ...`, Stack 2 at indices `1, 4, 7, ...`, and Stack 3 at indices `2, 5, 8, ...`.

**Implementation Details:**

1. **Array Layout:**
   - Use a single array `arr` of size `N`.
   - Stack 1 elements are stored at indices `0, 3, 6, ...`
   - Stack 2 elements are stored at indices `1, 4, 7, ...`
   - Stack 3 elements are stored at indices `2, 5, 8, ...`

2. **Pointers:**
   - Maintain three pointers `top1`, `top2`, `top3` initialized to `-3`, `-2`, and `-1`, respectively.

3. **Push Operation:**
   - For Stack 1: Increment `top1` by 3 and insert the element at `arr[top1]`.
   - For Stack 2: Increment `top2` by 3 and insert the element at `arr[top2]`.
   - For Stack 3: Increment `top3` by 3 and insert the element at `arr[top3]`.

4. **Pop Operation:**
   - For Stack 1: Return the element at `arr[top1]` and decrement `top1` by 3.
   - For Stack 2: Return the element at `arr[top2]` and decrement `top2` by 3.
   - For Stack 3: Return the element at `arr[top3]` and decrement `top3` by 3.

**Pros:**
- Simple implementation with good space utilization.
- Each stack can grow independently as long as there is space in the array.

**Cons:**
- Less intuitive index calculations.
- Fixed-size array may lead to overflow if not managed properly.

**Use Case:**
- Suitable for scenarios where independent growth of stacks is needed within a fixed-size array.
- Ideal for demonstrating interleaved data storage and efficient use of a single array in interviews.

**Example Code:**

```python
class ThreeStacks:
    def __init__(self, n):
        self.n = n
        self.arr = [None] * n
        self.top1 = -3
        self.top2 = -2
        self.top3 = -1

    def push1(self, x):
        if self.top1 + 3 < self.n:
            self.top1 += 3
            self.arr[self.top1] = x
        else:
            raise Exception("Stack 1 Overflow")

    def push2(self, x):
        if self.top2 + 3 < self.n:
            self.top2 += 3
            self.arr[self.top2] = x
        else:
            raise Exception("Stack 2 Overflow")

    def push3(self, x):
        if self.top3 + 3 < self.n:
            self.top3 += 3
            self.arr[self.top3] = x
        else:
            raise Exception("Stack 3 Overflow")

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 3
            return x
        else:
            raise Exception("Stack 1 Underflow")

    def pop2(self):
        if self.top2 >= 1:
            x = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 -= 3
            return x
        else:
            raise Exception("Stack 2 Underflow")

    def pop3(self):
        if self.top3 >= 2:
            x = self.arr[self.top3]
            self.arr[self.top3] = None
            self.top3 -= 3
            return x
        else:
            raise Exception("Stack 3 Underflow")

# Example usage:
stacks = ThreeStacks(15)
stacks.push1(10)
stacks.push2(20)
stacks.push3(30)
print(stacks.pop1())  # Output: 10
print(stacks.pop2())  # Output: 20
print(stacks.pop3())  # Output: 30
```

### Summary

1. **Fixed Division Method:**
   - **Pros:** Simple, easy to implement.
   - **Cons:** Inflexible, inefficient space utilization.
   - **Use Case:** Basic demonstrations, fixed and known stack sizes.

2. **Dynamic Division Method:**
   - **Pros:** Flexible, dynamic adjustment of stack sizes.
   - **Cons:** Complex implementation, overhead of managing auxiliary structures.
   - **Use Case:** Scenarios with highly variable and unpredictable stack sizes.

3. **Doubly Linked List Method:**
   - **Pros:** Flexible, efficient space utilization.
   - **Cons:** Complex implementation, overhead of managing pointers.
   - **Use Case:** Scenarios requiring dynamic growth and efficient space utilization.

4. **Interleaved Index Method:**
   - **Pros:** Simple, good space utilization, independent stack growth.
   - **Cons:** Less intuitive index calculations, potential for overflow.
   - **Use Case:** Scenarios requiring independent growth within a fixed-size array.