import sys


def is_available(x):
    for i in range(x):
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x - i:
            return False
    return True


def dfs(current_row):
    global answer
    if current_row == n:
        answer += 1
        return
    for i in range(n):
        queen[current_row] = i
        if is_available(current_row):
            dfs(current_row + 1)


n = int(sys.stdin.readline().rstrip())
answer = 0
queen = [0] * n
dfs(0)
print(answer)
