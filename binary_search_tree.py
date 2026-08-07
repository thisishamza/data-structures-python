class Node:
    def __init__(self, key):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f'{self.key} -> {self.value}'


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # O(n) worst case
    # O(log n) average case
    # O(h) always
    def __contains__(self, key):
        current_node = self.root
        while current_node:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return True
        return False

    # O(n)
    def __iter__(self):
        yield from self._in_order_traversal(self.root)

    # O(n)
    def __repr__(self):
        return str(list(self._in_order_traversal(self.root)))

    # O(n) worst case
    # O(log n) average case
    # O(h) always
    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left is None:
                        current_node.left = Node(key)
                        current_node.left.value = value
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif key > current_node.key:
                    if current_node.right is None:
                        current_node.right = Node(key)
                        current_node.right.value = value
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    current_node.value = value
                    break

    # O(n) worst case
    # O(log n) average case
    # O(h) always
    def search(self, key):
        current_node = self.root
        while True:
            if current_node is None or current_node.key == key:
                return current_node
            elif key < current_node.key:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right


    def remove(self, key):
        node_to_remove = self.search(key)
        if node_to_remove is None:
            raise KeyError(f'Key {key} not found')
        else:
            self._delete(node_to_remove)
            return True

    def traverse(self, order='in_order'):
        if order == 'in-order':
            return self._in_order_traversal(self.root)
        elif order == 'pre-order':
            return self._preorder_traversal(self.root)
        elif order == 'post-order':
            return self._postorder_traversal(self.root)
        else:
            raise ValueError(f'Order {order} not supported')

    def _delete(self, node):
        # Node is leaf node
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = node
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent = None

        # Node has one child node
        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right
            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            else:
                if node.parent.left == node:
                    node.parent.left = child_node
                else:
                    node.parent.right = child_node
                child_node.parent = node.parent
            node.parent = node.right = node.left = None
        # Node has two child nodes
        else:
            successor = self._successor(node)
            node.key = successor.key
            node.value = successor.value
            self._delete(successor)

    def _successor(self, node):
        if node is None:
            raise ValueError("cannot find successor of None")
        if node.right is None:
            return node
        else:
            current_node = node.right
            while current_node.left is not None:
                current_node = current_node.left
            return current_node

    def _predecessor(self, node):
        if node is None:
            raise ValueError("cannot find predecessor of None")
        if node.left is None:
            return node
        else:
            current_node = node.left
            while current_node.right is not None:
                current_node = current_node.right
            return current_node

    def _in_order_traversal(self, node):
        # ascending order - left -> root -> right
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield node.key, node.value
            yield from self._in_order_traversal(node.right)


    def _preorder_traversal(self, node):
        # root -> left -> right
        if node is not None:
            yield node.key, node.value
            yield from self._preorder_traversal(node.left)
            yield from self._preorder_traversal(node.right)

    def _postorder_traversal(self, node):
        # left -> right -> root
        if node is not None:
            yield from self._postorder_traversal(node.left)
            yield from self._postorder_traversal(node.right)
            yield node.key, node.value


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10, 'Hello')
    bst.insert(3, 'Hello')
    bst.insert(11, 'world')
    bst.insert(4, 'real')
    bst.insert(7, 'name')
    bst.insert(5, 'word')

    print(bst)
    bst.remove(4)
    bst.insert(8, 'new_word')
    for i in bst.traverse('post-order'):
        print(i)

    print(bst.search(8))




