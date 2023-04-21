class Solution:
    def reverseBits(self, n: int) -> int:
        bin_num = bin(n)[2:]
        bin_num = bin_num[::-1].ljust(32, '0')
        return int(bin_num, 2)