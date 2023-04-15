class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1) + 1
        len2 = len(text2) + 1
        dp = [[0 for i in range(len2)] for j in range(len1)]

        for i in range(1, len1):
            for j in range(1, len2):
                dp[i][j] = max(max(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1] + int(text1[i - 1] == text2[j - 1]))

        return dp[len1 - 1][len2 - 1]