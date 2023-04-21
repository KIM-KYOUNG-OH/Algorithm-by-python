class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_num = bin(n)[2:]
        cnt = 0
        for ch in bin_num:
            if ch != '0':
                cnt += 1
        return cnt