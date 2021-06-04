import sys


def dfs(cnt, result):
    if cnt == n - 1:
        answer.append(result)
        return
    if operators[0] > 0:
        operators[0] -= 1
        dfs(cnt + 1, result + numbers[cnt + 1])
        operators[0] += 1
    if operators[1] > 0:
        operators[1] -= 1
        dfs(cnt + 1, result - numbers[cnt + 1])
        operators[1] += 1
    if operators[2] > 0:
        operators[2] -= 1
        dfs(cnt + 1, result * numbers[cnt + 1])
        operators[2] += 1
    if operators[3] > 0:
        operators[3] -= 1
        dfs(cnt + 1, result // numbers[cnt + 1] if result >= 0 else -(abs(result) // numbers[cnt + 1]))
        operators[3] += 1


n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
operators = list(map(int, sys.stdin.readline().rstrip().split()))
answer = []
dfs(0, numbers[0])
print(max(answer))
print(min(answer))
