import sys


def is_movable(stores, x, y):
    if (end_x - x) + (end_y - y) <= 1000:
        return True
    if len(stores) == 0:
        return False
    store_x, store_y = stores.pop()
    diff_x = store_x - x
    diff_y = store_y - y
    if diff_x + diff_y <= 1000:
        return is_movable(stores, store_x, store_y)
    else:
        return False


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    start_x, start_y = map(int, sys.stdin.readline().rstrip().split())
    stores = []
    for _ in range(n):
        store_x, store_y = map(int, sys.stdin.readline().rstrip().split())
        stores.append((store_x, store_y))
    end_x, end_y = map(int, sys.stdin.readline().rstrip().split())
    stores.sort(key=lambda x: (-x[0], -x[1]))
    if is_movable(stores, 0, 0):
        print('happy')
    else:
        print('sad')
