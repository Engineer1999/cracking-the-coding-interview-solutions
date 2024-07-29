class StackX:
    def __init__(self, threashold):
        self.threashold = threashold
        self.stack_list = [[]]
        self.size = 0
        self.idx = 0

    def push(self, data):
        if self.idx < self.threashold:
            self.stack_list[-1].append(data)
            self.size += 1
            self.idx += 1
        elif (self.size)%self.threashold >= 0:
            self.stack_list.append([data])
            self.idx = 1

    def pop(self):
        if self.idx == 0:
            return "Stack Empty"
        else:
            return self.stack_list[-1].pop()
    
    def display(self):
        for stack in self.stack_list:
            print(stack)
        print()
        
    def popAt(self, pop_idx):
        if pop_idx < 0 or pop_idx >= self.size:
            raise IndexError("Index out of range")

        # Determine which sub-stack and the index within that sub-stack
        stack_idx = pop_idx // self.threashold
        idx_within_stack = pop_idx % self.threashold

        # Remove the element at the specified index
        removed_element = self.stack_list[stack_idx].pop(idx_within_stack)
        self.size -= 1

        # Shift elements from subsequent sub-stacks
        for i in range(stack_idx, len(self.stack_list) - 1):
            if len(self.stack_list[i + 1]) > 0:
                # Move the bottom element of the next stack to the top of the current stack
                self.stack_list[i].append(self.stack_list[i + 1].pop(0))
            else:
                break

        # Remove the last sub-stack if it becomes empty
        if len(self.stack_list[-1]) == 0:
            self.stack_list.pop()

        return removed_element
            
            
stackx = StackX(10)
for i in range(55):
    stackx.push(i)

print("--------------------------")
stackx.display()
print(stackx.pop())
stackx.display()
stackx.popAt(18)
stackx.display()