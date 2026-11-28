class TrieNode:
    def __init__(self):
        self.childrens: dict = {}
        self.word: bool = False

class WordDictionary:

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def addWord(self, word: str) -> None:
        current: TrieNode = self.root
        for c in word:
            if c not in current.childrens:
                current.childrens[c] = TrieNode()
            current = current.childrens[c]
        current.word = True

    def search(self, word: str) -> bool:
        def dfs(root: TrieNode, j: int) -> bool:
            current = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in current.childrens.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if c not in current.childrens:
                        return False
                    current = current.childrens[c]

            return current.word

        return dfs(self.root, 0)