import sys
input = sys.stdin.readline

n = int(input())
talks = []
for _ in range(n):
    start, end = map(int, input().split())
    talks.append((start, end))
talks.sort(key=lambda x:(x[1], x[0]))
cnt = 1
end_time = talks[0][1]
for i in range(1, n):
    if talks[i][0] >= end_time:
        cnt += 1
        end_time = talks[i][1]

print(cnt)