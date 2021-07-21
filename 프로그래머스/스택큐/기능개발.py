from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    curr = 0  # 현재 일 수
    release_cnt = 0  # 배포 중첩수
    while progresses:  # 큐가 존재하는 동안
        if (progresses[0] + speeds[0] * curr) >= 100:
            progresses.popleft()
            speeds.popleft()
            release_cnt += 1
        else:
            if release_cnt > 0:
                answer.append(release_cnt)
                release_cnt = 0  # 배포 중첩 수 초기화
            curr += 1  # 현재 일 수 + 1
    # popleft 직후 반복문을 빠져 나오기 때문에 release_cnt 는 항상 1보다 큼
    answer.append(release_cnt)

    return answer


# def solution(progresses, speeds):
#     answer = []
#     curr = 0  # 현재 일수
#     release_cnt = 0  # 배포 중첩수
#     for i in range(len(progresses)):
#         progress, speed = progresses[i], speeds[i]
#         if progress + speed * curr >= 100:
#             release_cnt += 1
#             continue
#         if progress + speed * curr < 100 and release_cnt != 0:
#             answer.append(release_cnt)
#             release_cnt = 0
#         rest = 100 - progress
#         if rest % speed == 0:
#             curr = rest // speed
#         else:
#             curr = (rest // speed) + 1
#         release_cnt += 1
#     if release_cnt != 0:
#         answer.append(release_cnt)
#     return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
