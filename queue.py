class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # O(1)
    def __len__(self):
        return self.size

    # O(n)
    def __repr__(self):
        if self.is_empty():
            return "[]"
        else:
            current = self.front
            return_list = []
            while current:
                return_list.append(current.data)
                current = current.next
            return ",".join(map(str, return_list))

    # O(1)
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1


    # O(1)
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self.size -= 1
            return data

    # O(1)
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.front.data

    # O(1)
    def rear(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.rear.data

    # O(1)
    def is_empty(self):
        return self.size == 0


if __name__=='__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.peek())
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    print(queue.dequeue())
    print(queue.peek())
    print(queue)
