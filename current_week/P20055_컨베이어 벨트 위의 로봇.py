import sys


def rot(lst):
    result = [lst[-1]]
    result.extend(lst[:len(lst)-1])
    return result


n, k = map(int, sys.stdin.readline().rstrip().split())
convey = list(map(int, sys.stdin.readline().rstrip().split()))
robot = [0] * n
answer = 0
while True:
    convey = rot(convey)
    robot = rot(robot)
    robot[-1] = 0
    if sum(robot):
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and convey[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                convey[i+1] -= 1
        robot[-1] = 0
    if convey[0] >= 1 and robot[0] == 0:
        convey[0] -= 1
        robot[0] = 1
    answer += 1
    if convey.count(0) >= k:
        break
print(answer)
