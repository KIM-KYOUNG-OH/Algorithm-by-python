import sys
from collections import deque


class Gear:
    def __init__(self, sows):
        self.sows = sows

    def getRight(self):
        return self.sows[2]

    def getLeft(self):
        return self.sows[-2]

    def rotateClockWise(self):
        temp = self.sows
        self.sows = temp[-1] + temp[:-1]

    def rotateReverseClockWise(self):
        temp = self.sows
        self.sows = temp[1:] + temp[0]

    def getTop(self):
        return self.sows[0]


gears = [0]
for _ in range(4):
    s = sys.stdin.readline().rstrip()
    gears.append(Gear(s))

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    target, direction = map(int, sys.stdin.readline().rstrip().split())
    directions = [0] * 5
    directions[target] = direction
    # left
    for i in range(target - 1, 0, -1):
        prev = gears[i + 1]
        cur = gears[i]
        if prev.getLeft() != cur.getRight():
            directions[i] = directions[i + 1] * -1
        else:
            break

    # right
    for i in range(target + 1, 5):
        prev = gears[i - 1]
        cur = gears[i]
        if prev.getRight() != cur.getLeft():
            directions[i] = directions[i - 1] * -1
        else:
            break

    for i in range(1, 5):
        if directions[i] == 1:
            gears[i].rotateClockWise()
        elif directions[i] == -1:
            gears[i].rotateReverseClockWise()

answer = 0
for i in range(1, 5):
    if gears[i].getTop() == '1':
        answer += 2 ** (i - 1)
print(answer)
