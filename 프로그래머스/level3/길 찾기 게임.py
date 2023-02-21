import sys

sys.setrecursionlimit(10 ** 6)


def solution(nodeinfo):
    def preOrder(arr_y):
        cur = arr_y[0]

        left = []
        right = []
        for i in range(1, len(arr_y)):
            if arr_y[i][0] < cur[0]:  # x 좌표
                left.append(arr_y[i])
            else:
                right.append(arr_y[i])

        pre_answer.append(cur[2])
        if len(left) > 0:
            preOrder(left)
        if len(right) > 0:
            preOrder(right)

    def postOrder(arr_y):
        cur = arr_y[0]

        left = []
        right = []
        for i in range(1, len(arr_y)):
            if arr_y[i][0] < cur[0]:  # x 좌표
                left.append(arr_y[i])
            else:
                right.append(arr_y[i])

        if len(left) > 0:
            postOrder(left)
        if len(right) > 0:
            postOrder(right)
        post_answer.append(cur[2])

    pre_answer = []
    post_answer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    arr_y = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    preOrder(arr_y)
    postOrder(arr_y)

    return [pre_answer, post_answer]


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
