import sys

t = int(sys.stdin.readline().rstrip())  # 테스트 횟수
for _ in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())  # 현재 위치: x, 목표 위치: y
    cnt = 0  # 최소한의 공간이동 장치 작동 횟수
    distance = y - x  # 이동 거리
    n = 0  # 등차수열의 항
    while True:
        n += 1
        if distance <= (n * (n + 1)):
            diff = n * (n + 1) - distance
            if diff < n:
                cnt = 2 * n
            else:
                cnt = (2 * n) - 1
            break
    print(cnt)
