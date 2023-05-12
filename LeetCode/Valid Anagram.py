from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        s_alps = sorted(list(s_counter.keys()))
        s_result = ''
        for alp in s_alps:
            s_result += alp + str(s_counter.get(alp))

        t_counter = Counter(t)
        t_alps = sorted(list(t_counter.keys()))
        t_result = ''
        for alp in t_alps:
            t_result += alp + str(t_counter.get(alp))
        if s_result == t_result:
            return True
        else:
            return False


s = Solution()
print(s.isAnagram('anagram', 'nagaram'))
