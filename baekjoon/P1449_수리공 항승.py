import sys
from collections import deque

n, l = map(int, sys.stdin.readline().rstrip().split())
holes = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
tape_cnt = 0  # 총 필요한 테이프 개수
queue = deque(holes)  # 구멍의 위치를 저장
prev_tape_end_pos = -1  # 직전 테이프 마지막 위치
while queue:
    hole_pos = queue.popleft()
    if prev_tape_end_pos >= (hole_pos + 0.5):
        continue
    tape_cnt += 1
    prev_tape_end_pos = hole_pos - 0.5 + l

print(tape_cnt)