import sys

line_cnt = int(sys.stdin.readline().rstrip())  # 총 전깃줄 개수
lines = dict()  # 딕셔너리 타입
for _ in range(line_cnt):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    lines[a] = b  # 딕셔너리 타입에 전깃줄 데이터 저장
b_lst = sorted(lines.items(), key=lambda x: x[0])  # A 전봇대 기준 정렬
dp = [1] * (line_cnt + 1)  # dp 초기화
for i in range(line_cnt + 1):  # 가장 긴 증가하는 부분 수열 구하기
    for j in range(1, i):
        if b_lst[j - 1][1] < b_lst[i - 1][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(line_cnt - max(dp))  # 자른 전깃줄의 개수 = (전체 전깃줄 개수) - (가장 긴 증가하는 부분 수열의 길이)
