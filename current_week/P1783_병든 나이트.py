import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
count = 0  # 방문 횟수
# n < 3 or m < 7 일때 최대 방문횟수는 4를 넘을 수 없다
if n == 1:
    count = 1
elif n == 2:
    count = min(4, (m-1) // 2 + 1)  # 오른쪽으로 두칸씩 이동
elif m < 7:
    count = min(4, m)  # 오른쪽으로 한칸씩 이동
else:  # n >= 3 and m >= 7
    count = 5 + (m - 7)  # 3 X 7 행렬일 때 방문 횟수 + 오른쪽으로 한칸씩 이동하는 횟수
print(count)