class Solution:
    def spellchecker(self, wordlist, queries):
        vowels = ['a', 'e', 'i', 'o', 'u']
        answer = []
        for query in queries:
            if query in wordlist:
                answer.append(query)
                continue
            else:
                contin = False
                for word in wordlist:
                    if word.lower() == query.lower():
                        answer.append(word)
                        contin = True
                        break
                if contin == True:
                    continue
                for word in wordlist:
                    if len(word) == len(query):
                        query_lower = query.lower()
                        temp = ""
                        for j in range(len(query)):
                            if query_lower[j] == word[j].lower():
                                temp += word[j]
                            elif query_lower[j] in vowels:
                                temp += word[j]
                        if len(temp) == len(word):
                            answer.append(temp)
                            contin = True
                            break
                if contin == True:
                    continue
            answer.append("")
        return answer

s = Solution()
print(s.spellchecker(["wg","uo","as","kv","ra","mw","gi","we","og","zu"],
                             ["AS","in","yc","kv","mw","ov","lc","os","wm","Mw"]))