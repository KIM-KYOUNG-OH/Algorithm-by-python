def isSafe(place):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(5):
        for j in range(5):
            ch = place[i][j]
            if ch == 'P':
                # 1차 이동
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < 5 and 0 <= nx < 5:
                        next = place[ny][nx]
                        if next == 'X':
                            continue
                        elif next == 'P':
                            return 0
                        elif next == 'O':
                            # 2차 이동
                            for l in range(4):
                                nny = ny + dy[l]
                                nnx = nx + dx[l]
                                if 0 <= nny < 5 and 0 <= nnx < 5:
                                    next = place[nny][nnx]
                                    if nny == i and nnx == j:
                                        continue
                                    elif next == 'X':
                                        continue
                                    elif next == 'P':
                                        return 0
                                    elif next == 'O':
                                        continue
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(isSafe(place))

    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])