import sys


def prev_permutation(lst):
    l = len(lst)
    x = -1
    for i in range(l - 2, -1, -1):
        if lst[i] > lst[i + 1]:
            x = i
            break
    if x == -1:
        return -1
    for j in range(l - 1, x, -1):
        if lst[x] > lst[j]:
            lst[x], lst[j] = lst[j], lst[x]
    return lst[:x + 1] + lst[:x: -1]


n = int(sys.stdin.readline().rstrip())
case = list(map(int, sys.stdin.readline().rstrip().split()))
answer = prev_permutation(case)
if answer == -1:
    print(-1)
    exit(0)
print(' '.join(map(str, answer)))
