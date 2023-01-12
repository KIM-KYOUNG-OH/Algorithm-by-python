import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    lst_a = sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)
    lst_b = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    right = len(lst_b) - 1
    result = 0
    for a in lst_a:
        while right >= 0:
            if a > lst_b[right]:
                break
            elif a <= lst_b[right]:
                right -= 1
        result += right + 1
    print(result)
