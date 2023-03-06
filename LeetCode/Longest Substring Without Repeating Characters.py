class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        answer = 0
        while left < len(s):
            history = []
            right = left
            while right < len(s):
                cur = s[right]
                if cur not in history:
                    history.append(cur)
                    right += 1
                else:
                    right = left + history.index(cur) + 1
                    break
            left = right
            answer = max(answer, len(history))
        return answer


print(Solution.lengthOfLongestSubstring('', "dvdf"))