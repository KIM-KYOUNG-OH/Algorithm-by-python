parent = [[(r, c) for c in range(51)] for r in range(51)]
cells = [['EMPTY'] * 51 for _ in range(51)]
result = []


def find(r, c):
    if (r, c) != parent[r][c]:
        pr, pc = parent[r][c]
        parent[r][c] = find(pr, pc)
    return parent[r][c]


def update(r, c, value):
    pr, pc = find(r, c)
    cells[pr][pc] = value


def update_val(value1, value2):
    for r in range(51):
        for c in range(51):
            pr, pc = find(r, c)
            if cells[pr][pc] == value1:
                cells[pr][pc] = value2


def union(r1, c1, r2, c2):
    parent[r2][c2] = parent[r1][c1]


def merge(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)

    if (r1, c1) == (r2, c2):
        return
    if cells[r1][c1] != 'EMPTY':
        union(r1, c1, r2, c2)
    else:
        union(r2, c2, r1, c1)


def unmerge(r, c):
    pr, pc = find(r, c)
    value = cells[pr][pc]

    merge_list = []
    for i in range(51):
        for j in range(51):
            pi, pj = find(i, j)
            if (pi, pj) == (pr, pc):
                merge_list.append((i, j))

    for i, j in merge_list:
        parent[i][j] = (i, j)
        if (i, j) != (r, c):
            cells[i][j] = 'EMPTY'
        else:
            cells[i][j] = value


def printCell(r, c):
    pr, pc = find(r, c)
    result.append(cells[pr][pc])


def solution(commands):
    for command in commands:
        cmd, *arg = command.split()
        if cmd == 'UPDATE':
            if len(arg) == 3:
                r, c, value = arg
                update(int(r), int(c), value)
            else:
                value1, value2 = arg
                update_val(value1, value2)
        elif cmd == 'MERGE':
            r1, c1, r2, c2 = map(int, arg)
            merge(r1, c1, r2, c2)
        elif cmd == 'UNMERGE':
            r, c = map(int, arg)
            unmerge(r, c)
        else:
            r, c = map(int, arg)
            printCell(r, c)
    return result


