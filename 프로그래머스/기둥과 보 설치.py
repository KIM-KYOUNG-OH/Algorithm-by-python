def is_possible(frames):
    for frame in frames:
        x, y, stuff = frame
        if stuff == 0:  # 기둥
            if y == 0 or [x, y - 1, 0] in frames or [x, y, 1] in frames or [x - 1, y, 1] in frames:
                continue
            return False
        elif stuff == 1:  # 보
            if [x, y - 1, 0] in frames or [x + 1, y - 1, 0] in frames or (
                    [x - 1, y, 1] in frames and [x + 1, y, 1] in frames):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:  # 삭제
            answer.remove([x, y, stuff])
            if not is_possible(answer):
                answer.append([x, y, stuff])
        elif operate == 1:  # 추가
            answer.append([x, y, stuff])
            if not is_possible(answer):
                answer.remove([x, y, stuff])
    answer.sort()
    return answer


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]))
