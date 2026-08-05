class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # O(1)
    def __len__(self):
        return self.size

    # O(n)
    def __repr__(self):
        if self.size == 0:
            return []
        current = self.top
        return_list = []
        while current:
            return_list.append(current.data)
            current = current.next
        return ",". join(map(str,return_list))

    # O(1)
    def push(self, data):
        self.new_node = Node(data)
        self.new_node.next = self.top
        self.top = self.new_node
        self.size += 1

    # O(1)
    def pop(self):
        if self.size == 0:
            raise ValueError("pop from empty stack")
        pop_value = self.top
        self.top = self.top.next
        self.size -= 1
        return pop_value.data

    # O(1)
    def peek(self):
        if self.size == 0:
            raise ValueError("peek from empty stack")
        return self.top.data

    # O(1)
    def is_empty(self):
        return self.size == 0

if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(len(stack))
    print(stack)
    stack.peek()
    stack.pop()
    print(len(stack))
    print(stack.is_empty())
