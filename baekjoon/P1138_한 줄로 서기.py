import sys

n = int(input())

# 왼쪽에 자신보다 키가 큰 사람수 리스트
left_count_list = list(map(int, sys.stdin.readline().rstrip().split()))
# 줄선 결과
line = [0] * n

for i in range(n):  # 작은수부터 배치해서 나머지수는 현재수보다 항상 키가 크다
    left_count = left_count_list[i]  # 왼쪽에 자신보다 키가 큰 사람수
    count = 0  # 빈자리 탐색 횟수
    for j in range(n):
        if left_count == count and line[j] == 0:
            line[j] = i + 1
            break
        if line[j] == 0:
            count += 1
print(*line)