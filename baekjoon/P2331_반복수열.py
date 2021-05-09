import sys

a, p = map(int, sys.stdin.readline().rstrip().split())
D = [a]
while True:
    before = D[-1]  # 이전 값
    current = 0   # 현재 값
    while before:
        current += (before % 10) ** p
        before = before // 10
    if current in D:
        D = D[:D.index(current)]
        break
    D.append(current)

sys.stdout.write(str(len(D)))