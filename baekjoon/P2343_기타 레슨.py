import sys


def get_cnt(lectures, max_lecture):
    cnt = 0
    total = 0
    for lecture in lectures:
        if total + lecture > max_lecture:
            total = lecture
            cnt += 1
        else:
            total += lecture
    if total > 0:
        cnt += 1
    return cnt


n, m = map(int, sys.stdin.readline().rstrip().split())
lectures = list(map(int, sys.stdin.readline().rstrip().split()))

min_len_lecture = sys.maxsize
left = 0
right = sum(lectures) + 1
while left < right:
    mid = (left + right) // 2
    # print('left = ', left, ', right = ', right, ', mid = ', mid)
    if mid < max(lectures):
        left = mid + 1
        continue
    cnt = get_cnt(lectures, mid)
    # print('cnt = ', cnt)
    if cnt <= m:
        right = mid
    else:
        left = mid + 1
print(right)
