class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(i + 1):
                if self.isPalindrome(s[j: len(s) - i + j]):
                    return s[j: len(s) - i + j]

    def isPalindrome(self, s):
        return s[:] == s[::-1]