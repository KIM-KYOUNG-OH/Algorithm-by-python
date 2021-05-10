import sys


def is_in_stage(s, w):
    for d in s:
        if d[2] == w:
            return True
    return False


n = int(input())
people = int(input())
whos = list(map(int, sys.stdin.readline().rstrip().split()))
stage = []  # [추천횟수, 게시날짜, 학번]
for release_day, who in enumerate(whos):
    if is_in_stage(stage, who):
        for idx, data in enumerate(stage):
            if data[2] == who:
                stage[idx][0] += 1
                break
    else:
        if len(stage) < n:
            stage.append([1, release_day, who])
        else:
            stage[0] = [1, release_day, who]
    stage.sort(key=lambda x: (x[0], x[1]))
stage.sort(key=lambda x: x[2])
for i in range(len(stage)):
    if i == n-1:
        print(stage[i][2])
        continue
    print(stage[i][2], end=' ')
