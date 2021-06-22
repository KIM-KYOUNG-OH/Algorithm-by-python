import math
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
answer = math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
print(answer)