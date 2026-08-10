class Node:

    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = Node()

    # O(m) - where m is the length of the word
    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    # O(m) - where m is the length of the word
    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    # O(m) - where m is the length of the word
    def remove(self, word):
        self._delete(self.root, word, 0)

    # O(m) - where m is the length of the word
    def has_prefix(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

    # O(m + k) - where m is the prefix length and k is total no of characters in all suffixes
    def starts_with(self, prefix):
        words = []
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return words
            current_node = current_node.children[char]

        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(''.join(path))
            for char, child_node in current_node.children.items():
                _dfs(child_node, path + [char])

        _dfs(current_node, list(prefix))
        return words

    # O(n) - n is the no. of nodes in trie
    def list_words(self):
        words = []

        def _dfs(current_node, path):
            if current_node.is_end_of_word:
                words.append(''.join(path))
            for char, child_node in current_node.children.items():
                _dfs(child_node, path + [char])

        _dfs(self.root, [])
        return words


    def _delete(self, current_node, word, index):
        if index == len(word):
            if not current_node.is_end_of_word:
                return False
            current_node.is_end_of_word = False
            return len(current_node.children) == 0

        ch = word[index]
        node = current_node.children.get(ch)
        if not node:
            return False
        delete_current_node = self._delete(node, word, index + 1)
        if delete_current_node:
            del current_node.children[ch]
            return len(current_node.children) == 0 and not current_node.is_end_of_word
        return False


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    trie.insert('banana')
    trie.insert('minimal')
    trie.insert('minimum')
    trie.insert('mini')
    print(trie.list_words())
    print(trie.has_prefix('mi'))
    print(trie.starts_with('mi'))
    trie.remove('mini')
    print(trie.list_words())
