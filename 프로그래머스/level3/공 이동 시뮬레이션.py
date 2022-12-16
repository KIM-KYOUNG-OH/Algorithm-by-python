def solution(n, m, y, x, queries):
    top, bottom = y, y
    left, right = x, x
    for command, dx in queries[::-1]:
        if command == 0:  # 좌
            if left != 0:
                left += dx
                if left > m - 1:
                    left = m - 1
            right += dx
            if right > m - 1:
                right = m - 1
        elif command == 1:  # 우
            if right != m - 1:
                right -= dx
                if right < 0:
                    right = 0
            left -= dx
            if left < 0:
                left = 0
        elif command == 2:  # 위
            if top != 0:
                top += dx
                if top > n - 1:
                    top = n - 1
            bottom += dx
            if bottom > n - 1:
                bottom = n - 1
        else:
            if bottom != n - 1:
                bottom -= dx
                if bottom < 0:
                    top = 0  # ???
            top -= dx
            if top < 0:
                top = 0
        if right < 0 or left > m - 1 or top > n - 1 or bottom < 0:
            return 0
    return (bottom - top + 1) * (right - left + 1)


print(solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]))
