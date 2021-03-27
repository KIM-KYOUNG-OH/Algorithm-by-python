class Solution:
    def wordSubsets(self, A: list, B: list) -> list:
        B_alps = [0]*26
        for b in B:
            for alp in b:
                cnt = b.count(alp)
                if cnt > B_alps[ord(alp)-97]:
                    B_alps[ord(alp)-97] = cnt
                    b = b.replace(alp,'')
        answer = list(A)
        for a in A:
            for i in range(len(B_alps)):
                if B_alps[i] >= 1:
                    alp = chr(i+97)
                    if a.count(alp) < B_alps[i]:
                        answer.remove(a)
                        break
        return answer

s = Solution()
print(s.wordSubsets(["amazon","apple","facebook","google","leetcode"],["ec","oc","ceo"]))