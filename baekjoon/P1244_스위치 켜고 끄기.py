import sys


def change(i):
    if switch[i] == 0:
        switch[i] = 1
    else:
        switch[i] = 0


def boy(index):
    for i in range(index, n + 1, index):
        change(i)


def girl(index):
    left = index
    right = index
    change(index)
    while True:
        left -= 1
        right += 1
        if left < 1 or right > n or switch[left] != switch[right]:
            break
        change(left)
        change(right)


n = int(input())
switch = [-1]
switch.extend(list(map(int, sys.stdin.readline().rstrip().split())))
student_cnt = int(input())
for _ in range(student_cnt):
    gender, index = map(int, sys.stdin.readline().rstrip().split())
    if gender == 1:
        boy(index)
    else:
        girl(index)
answer = ''
for i in range(1, n + 1):
    answer += str(switch[i]) + ' '
    if len(answer) >= 40:
        print(answer)
        answer = ''
if len(answer) == 0:
    exit(0)
print(answer)

