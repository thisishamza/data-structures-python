class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # O(n)
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string = f"{last.data}"
            while last.next:
                last = last.next
                return_string += f", {last.data}"
            return return_string

    # o(n) - linear time
    def __contains__(self, data) -> bool:
        last = self.head
        while last:
            if last.data == data:
                return True
            last = last.next
        return False

    # O(n) Linear time
    def __len__(self):
        last = self.head
        count = 0
        while last:
            count += 1
            last = last.next
        return count

    # O(1) constant time
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            last_node = Node(data)
            last_node.prev = self.tail
            self.tail.next = last_node
            self.tail = last_node

    # O(1) constant time
    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            first_node = Node(data)
            first_node.next = self.head
            self.head.prev = first_node
            self.head = first_node

    # O(n) Linear time
    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
        else:
            if self.head is None:
                raise ValueError("Index out of range")
            else:
                last = self.head
                for i in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of range")
                    last = last.next

                new_node = Node(data)
                new_node.next = last.next
                new_node.prev = last
                if last.next is not None:
                    last.next.prev = new_node
                last.next = new_node

    # O(n)
    def delete(self, value):
        last = self.head
        if last.data == value:
            self.head = last.next
        else:
            while last.next:
                if last.next.data == value:
                    if last.next.next is not None:
                        last.next.next.prev = last
                    last.next = last.next.next
                    break
                last = last.next
    # O(n)
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of range")
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of range")
                last = last.next

            if last.next is None:
                raise ValueError("Index out of range")
            else:
                if last.next.next is not None:
                    last.next.next.prev = last
                last.next = last.next.next

    # O(n)
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of range")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of range")
                last = last.next
            return last.data


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.append(10)
    dll.insert(1, 63)
    dll.insert(1, 23)
    dll.append(20)
    dll.append(30)
    dll.prepend(55)
    dll.insert(3, 100)
    print(dll)
    dll.delete(40)
    print(dll)
    dll.pop(4)
    print(dll)

