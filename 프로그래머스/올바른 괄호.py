from collections import deque

def solution(s):
    q = deque()
    for br in s:
        if br == "(":
            q.append(br)
        elif br == ")":
            if len(q) == 0:
                return False
            q.popleft()
    if len(q) != 0:
        return False
    return True
