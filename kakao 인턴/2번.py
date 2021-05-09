from collections import deque


def solution(places):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for room in places:
        breaker = False  # 맨해튼거리 2이하에 P 발견시 반복문 탈출용
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    visited = [[False] * 5 for _ in range(5)]
                    q = deque([(0, i, j)])  # (depth, x, y)
                    visited[i][j] = True
                    while q:
                        depth, x, y = q.popleft()
                        if depth > 2:  # 맨해튼거리 2초과는 탐색할 필요 없다
                            break
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < 5 and 0 <= ny < 5:
                                if room[nx][ny] == 'O' and not visited[nx][ny]:
                                    q.append((depth + 1, nx, ny))
                                if depth < 2 and room[nx][ny] == 'P' and not visited[nx][ny]:
                                    answer.append(0)
                                    breaker = True
                                    break
                        if breaker:
                            break
                    if breaker:
                        break
            if breaker:
                break
        if breaker:
            continue
        answer.append(1)  # 정상
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))