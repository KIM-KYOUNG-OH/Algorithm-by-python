import sys


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


n, s = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.append(s)
nums.sort()
distances = []
for i in range(1, len(nums)):
    distances.append(nums[i] - nums[i - 1])
while len(distances) > 1:
    a = distances.pop()
    b = distances.pop()
    gcd = GCD(a, b)
    distances.append(gcd)
print(distances[0])
