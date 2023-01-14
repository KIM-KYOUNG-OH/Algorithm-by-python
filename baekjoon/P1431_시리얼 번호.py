import sys


class Serial:
    def __init__(self, s):
        self.val = s
        total = 0
        for ch in s:
            number = ord(ch) - ord('0')
            if 0 <= number < 10:
                total += number
        self.total = total


n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    lst.append(Serial(s))
lst = sorted(lst, key=lambda x: [len(x.val), x.total, x.val])
for num in lst:
    print(num.val)