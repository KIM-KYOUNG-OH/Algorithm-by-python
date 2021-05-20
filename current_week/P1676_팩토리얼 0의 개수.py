import sys


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


n = int(sys.stdin.readline().rstrip())
fac = factorial(n)
answer = 0
while True:
    if fac % 10 == 0:
        answer += 1
        fac //= 10
        continue
    break
print(answer)
