class Trie:

    def __init__(self):
        self.components = list()

    def insert(self, word: str) -> None:
        self.components.append(str)

    def search(self, word: str) -> bool:
        return self.components.find(word)

    def startsWith(self, prefix: str) -> bool:
        for e in self.components:
            if e.startWith(prefix):
                return True
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)