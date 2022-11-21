from copy import deepcopy
from collections import defaultdict


def isSame(startY, startX, row, col):
    global matrix
    for i in range(startY, startY + row):
        for j in range(startX, startX + col):
            if matrix[i][j] != matrix[startY][startX]:
                return False
    return True


def dfs(startY, startX, row, col):
    global matrix, dic
    if isSame(startY, startX, row, col):
        dic[matrix[startY][startX]] += 1
        return

    dfs(startY, startX, row // 2, col // 2)
    dfs(startY + row // 2, startX, row // 2, col // 2)
    dfs(startY, startX + col // 2, row // 2, col // 2)
    dfs(startY + row // 2, startX + col // 2, row // 2, col // 2)


def solution(arr):
    global matrix, dic
    row = len(arr)
    col = len(arr[0])
    matrix = deepcopy(arr)
    dfs(0, 0, row, col)
    answer = [dic[0], dic[1]]
    return answer


dic = defaultdict(int)
matrix = []
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])