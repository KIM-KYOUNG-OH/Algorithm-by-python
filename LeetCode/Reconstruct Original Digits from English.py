DIGITS = [
            [0, 'z', []],
            [2, 'w', []],
            [4, 'u', []],
            [6, 'x', []],
            [8, 'g', []],
            [3, 'h', [8]],
            [5, 'f', [4]],
            [7, 's', [6]],
            [1, 'o', [0, 2, 4]],
            [9, 'i', [5, 6, 8]]
        ]

class Solution:
    def originalDigits(self, s: str) -> str:
        alps, ans, n = [0]*26, [0]*10, len(s)
        for i in range(10):
            digit, char, rems = DIGITS[i]
            if char in s:
                cnt = s.count(char)
                for rem in rems:
                    cnt -= ans[rem]
                ans[digit] += cnt
        return "".join([str(i) * ans[i] for i in range(10)])

s = Solution()
print(s.originalDigits("owoztneoer"))