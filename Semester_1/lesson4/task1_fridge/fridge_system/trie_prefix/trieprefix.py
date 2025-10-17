from typing import List


class NodeChar:
    def __init__(self, char):
        self.parent = None
        self.char = char
        self.children = dict()
        self.is_end = False


class TriePrefix:
    def __init__(self, words: List[str]):
        self.root = NodeChar(None)
        self._build(words)

    def _build(self, words) -> None:
        for word in words:
            self.insert(word)

    def insert(self, word) -> None:
        curr_root = self.root
        for char in word:
            if char not in curr_root.children:
                curr_root.children[char] = NodeChar(char)
                curr_root.children[char].parent = curr_root
            curr_root = curr_root.children[char]
        curr_root.is_end = True

    def delete(self, word) -> None:
        node = self._startswith(word)
        if node is None:
            raise ValueError()
        if not node.is_end:
            raise ValueError()
        node.is_end = False
        if node.children:
            return

        curr_node = node
        while curr_node.parent is not None:
            parent_node = curr_node.parent
            if len(parent_node.children) > 1 or parent_node.is_end:
                break
            parent_node.children.pop(curr_node.char)
            curr_node = parent_node

    def search(self, prefix) -> List[str]:
        node = self._startswith(prefix)
        if node is None or node.char is None:
            return []
        return self._collect_words(prefix, node)

    def _collect_words(self, prefix, node: NodeChar) -> List[str]:
        words = []
        if node.is_end:
            words.append(prefix)
        if not node.children:
            return words

        stack = []
        stack.extend((prefix + node.char, node) for node in node.children.values())

        while stack:
            curr_prefix, curr_node = stack.pop()
            if curr_node.is_end:
                words.append(curr_prefix)
            for child in curr_node.children.values():
                if child:
                    new_prefix = curr_prefix + child.char
                    stack.append((new_prefix, child))

        return words

    def _startswith(self, prefix) -> NodeChar | None:
        curr_root = self.root
        for char in prefix:
            if char in curr_root.children:
                curr_root = curr_root.children[char]
            else:
                return None

        return curr_root


if __name__ == "__main__":
    trie = TriePrefix([])
    trie.insert("кот")
    trie.insert("кофе")
    trie.insert("кофе с сахаром")
    trie.insert("кофеин")
    print("До удаления:")
    print(trie.search("ко"))
    print(trie.search("коф"))
    print(trie.search("кофе"))
    print(trie.search("кофеи"))
    trie.delete("кофеин")
    print("После удаления:")
    print(trie.search("ко"))
    print(trie.search("коф"))
    print(trie.search("кофе"))
