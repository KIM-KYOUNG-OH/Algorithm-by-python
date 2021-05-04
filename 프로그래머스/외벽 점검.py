from itertools import permutations


def solution(n, weak, dist):
    min_cnt = len(dist) + 1  # 투입된 친구수 최소값
    length = len(weak)  # weak point 개수
    for i in range(length):  # 원이 아닌 직선으로 변경
        weak.append(weak[i] + n)
    for start in range(length):  # 0 ~ len(weak)-1까지
        for candidate in list(permutations(dist, len(dist))):
            cnt = 1  # 투입된 친구수
            end_point = weak[start] + candidate[cnt - 1]  # 친구의 점검 종료 지점
            for index in range(start, start + length):
                if end_point < weak[index]:  # 점검 범위를 벗어남
                    cnt += 1
                    if cnt > len(dist):
                        break
                    end_point = weak[index] + candidate[cnt - 1]
            min_cnt = min(min_cnt, cnt)
    if min_cnt > len(dist):
        return -1
    return min_cnt
