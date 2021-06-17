import sys


def next_permutation(lst):
    l = len(lst)
    x = -1  # highest index
    for i in range(l - 2, -1, -1):
        if lst[i] < lst[i + 1]:
            x = i
            break
    if x == -1:
        return -1  # 다음 순열이 없다는 것을 의미
    for j in range(l - 1, 0, -1):
        if lst[j] > lst[x]:
            lst[x], lst[j] = lst[j], lst[x]
            break
    return lst[:x + 1] + lst[:x:-1]


n = int(sys.stdin.readline().rstrip())
s = list(map(int, sys.stdin.readline().rstrip().split()))
answer = next_permutation(s)
if answer == -1:
    print(answer)
    exit(0)
print(*answer)  # positional argument
