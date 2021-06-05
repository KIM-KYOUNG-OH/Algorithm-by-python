import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().rstrip().split())
    n = int(sys.stdin.readline().rstrip())
    cnt = 0
    for _ in range(n):
        p_x, p_y, radius = map(int, sys.stdin.readline().rstrip().split())
        start_to_center = (start_x - p_x) ** 2 + (start_y - p_y) ** 2  # 시작점부터 행성계 중심까지 거리(편의상 루트는 생략)
        end_to_center = (end_x - p_x) ** 2 + (end_y - p_y) ** 2  # 도착점부터 행성계 중심까지 거리
        # 행성계안에 시작점이나 도착점이 하나만 존재하면 카운트함
        if start_to_center < (radius ** 2) < end_to_center:
            cnt += 1
            continue
        if end_to_center < (radius ** 2) < start_to_center:
            cnt += 1
            continue
    print(cnt)
