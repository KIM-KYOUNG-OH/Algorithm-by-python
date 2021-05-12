import sys

t = int(input())
for _ in range(t):
    l, num = map(int, sys.stdin.readline().rstrip().split())
    ants = []
    for _ in range(num):
        ants.append(int(input()))
    max_time = 0
    min_time = 0
    for ant in ants:
        if ant <= l-ant:
            if min_time < ant:
                min_time = ant
            if max_time < l - ant:
                max_time = l - ant
        else:
            if min_time < l - ant:
                min_time = l - ant
            if max_time < ant:
                max_time = ant

    print(min_time, max_time)