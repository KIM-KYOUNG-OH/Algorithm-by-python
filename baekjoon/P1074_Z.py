import sys


def dfs(length, startY, startX, y, x, cnt):
    if length == 2:
        if y == startY and x == startX:
            answer[0] = cnt
        elif y == startY and x == startX + 1:
            answer[0] = cnt + 1
        elif y == startY + 1 and x == startX:
            answer[0] = cnt + 2
        else:
            answer[0] = cnt + 3
        return

    nl = length // 2
    if startY <= y < startY + nl and startX <= x < startX + nl:  # 1사분면
        dfs(nl, startY, startX, y, x, cnt)
    elif startY <= y < startY + nl and startX + nl <= x < startX + length:  # 2사분면
        dfs(nl, startY, startX + nl, y, x, cnt + nl ** 2)
    elif startY + nl <= y < startY + length and startX <= x < startX + nl:  # 3사분면
        dfs(nl, startY + nl, startX, y, x, cnt + (nl ** 2) * 2)
    else:  # 4사분면
        dfs(nl, startY + nl, startX + nl, y, x, cnt + (nl ** 2) * 3)


n, r, c = map(int, sys.stdin.readline().rstrip().split())
answer = [0]
dfs(2 ** n, 0, 0, r, c, 0)
print(answer[0])
