import sys


def cycle(n):
    if n < 10:
        return (n * 10) + n
    if n >= 10:
        left = n // 10
        right = n % 10
        result = left + right
        return (right * 10) + (result % 10)


n = int(sys.stdin.readline().rstrip())
num = n
cnt = 0
while True:
    cnt += 1
    num = cycle(num)
    if num == n:
        break
print(cnt)