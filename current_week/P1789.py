import sys

s = int(sys.stdin.readline().rstrip())
num = 0
while True:
    num += 1
    total = num * (num + 1) // 2
    if (s - total) <= num:
        break
print(num)
