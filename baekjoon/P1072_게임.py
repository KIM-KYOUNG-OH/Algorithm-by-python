import sys

x, y = map(int, sys.stdin.readline().rstrip().split())
left, right = 1, x
z = (y * 100) // x
answer = sys.maxsize
while left <= right:
    mid = (left + right) // 2
    temp_x = x + mid
    temp_y = y + mid
    temp_z = (temp_y * 100) // temp_x
    if temp_z == z:
        left = mid + 1
    else:
        answer = min(answer, mid)
        right = mid - 1
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)