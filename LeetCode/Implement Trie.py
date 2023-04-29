class Trie:

    def __init__(self):
        self.components = list()

    def insert(self, word: str) -> None:
        self.components.append(word)

    def search(self, word: str) -> bool:
        for e in self.components:
            if e == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for e in self.components:
            if e.startswith(prefix):
                return True
        return False

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param_2 = obj.search('apple')
param_3 = obj.startsWith('app')