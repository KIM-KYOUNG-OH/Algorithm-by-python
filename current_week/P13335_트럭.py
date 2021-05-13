import sys

n, w, l = map(int, sys.stdin.readline().rstrip().split())
right_side = list(map(int, sys.stdin.readline().rstrip().split()))
time = 0
left_side = []
bridge = []
while len(left_side) != n:
    temp = bridge[:]
    while temp:
        truck = temp.pop(0)
        if time - truck[1] == w:
            t = bridge.pop(0)
            left_side.append(t)
    if right_side:
        if sum(i[0] for i in bridge) + right_side[0] <= l:
            bridge.append((right_side.pop(0), time))
    time += 1
print(time)