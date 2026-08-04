class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

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

    # O(n) linear time
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(data)

    # O(1) constant time
    def prepend(self, data):
        first_node = Node(data)
        first_node.next = self.head
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
                last.next = new_node

    # O(n)
    def delete(self, value):
        last = self.head
        if last.data == value:
            self.head = last.next
        else:
            while last.next:
                if last.next.data == value:
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
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.append(60)
    ll.prepend(55)
    print(ll)
    ll.insert(3, 100)
    print(ll)
    ll.delete(40)
    print(ll)
    print("gettingL::",ll.get(3))
    print(ll)
    ll.pop(3)
    print(ll)