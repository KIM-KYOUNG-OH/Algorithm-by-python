class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['$'] = word

    def search(self, word: str) -> bool:
        def withDot(node, word):
            if not word:
                return '$' in node
            elif word[0] == '.':
                for n in node:
                    if n is not '$':
                        if withDot(node[n], word[1:]):
                            return True
                return False
            else:
                if word[0] not in node:
                    return False
                else:
                    return withDot(node[word[0]], word[1:])

        return withDot(self.trie, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)