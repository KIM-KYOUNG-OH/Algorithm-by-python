import sys

numbers = sorted(list(map(int, list(sys.stdin.readline().rstrip()))), reverse=True)
if len(numbers) > 1 and 0 in numbers and sum(numbers) % 3 == 0:
    print(int(''.join(map(str, numbers))))
    exit(0)
print(-1)