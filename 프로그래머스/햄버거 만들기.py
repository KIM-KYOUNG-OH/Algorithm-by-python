from collections import deque


def solution(ingredient):
    stack = deque([])
    answer = 0
    for i in ingredient:
        stack.append(i)
        if i == 1:
            if len(stack) >= 4 and isHamburger(stack):
                for _ in range(4):
                    stack.pop()
                answer += 1

    return answer


def isHamburger(stack):
    l = len(stack)
    hamburger = [1, 3, 2, 1]
    temp = []
    for i in range(l - 1, l - 5, -1):
        temp.append(stack[i])
    if temp == hamburger:
        return True
    return False


solution([2, 1, 1, 2, 3, 1, 2, 3, 1])