class Node:
    def __init__(self):
        self.childrens: dict[str, Node] = dict()
        self.is_end: bool = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current: Node = self.root
        for c in word:
            if c in current.childrens:
                current = current.childrens[c]
            else:
                current.childrens[c] = Node()
                current = current.childrens[c]
        current.is_end = True

    def search(self, word: str) -> bool:
        current: Node = self.root
        for c in word:
            if c in current.childrens:
                current = current.childrens[c]
            else:
                return False
        return True if current.is_end else False
        
    def startsWith(self, prefix: str) -> bool:
        current: Node = self.root
        for c in prefix:
            if c in current.childrens:
                current = current.childrens[c]
            else:
                return False
        return True
        
        