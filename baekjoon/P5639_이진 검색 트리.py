import sys


def post_order(start, end):
    if start > end:
        return
    root = pre_order[start]
    idx = start + 1

    # 오른쪽 서브 트리 시작 idx 찾기
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    # 왼쪽 서브 트리
    post_order(start + 1, idx - 1)

    # 오른쪽 서브 트리
    post_order(idx, end)

    # root
    print(root)


sys.setrecursionlimit(10 ** 9)
pre_order = []  # 전위 순회
cnt = 0
while cnt <= 10000:
    try:
        temp = int(sys.stdin.readline().rstrip())
    except:
        break
    pre_order.append(temp)
    cnt += 1

post_order(0, len(pre_order) - 1)
