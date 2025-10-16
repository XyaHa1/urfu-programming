from typing import List


class NodeChar:
    def __init__(self, char):
        self.parent = None
        self.char = char
        self.children = dict()
        self.words = set()


class TriePrefix:
    def __init__(self, words: List[str]):
        self.root = NodeChar(None)
        self._build(words)

    def _build(self, words):
        for word in words:
            self.insert(word)

    def insert(self, word):
        curr_root = self.root
        for char in word:
            if char not in curr_root.children:
                curr_root.children[char] = NodeChar(char)
                curr_root.children[char].parent = curr_root
            curr_root = curr_root.children[char]
            curr_root.words.add(word)

    def search(self, prefix):
        node = self._startswith(prefix)
        if node is None:
            return []

        return node.words

    def _startswith(self, prefix) -> NodeChar | None:
        curr_root = self.root
        for char in prefix:
            if char in curr_root.children:
                curr_root = curr_root.children[char]
            else:
                return None

        return curr_root
