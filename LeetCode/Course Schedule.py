from collections import defaultdict


def recurisve(parent, a, history):
    if parent[a] is None:
        return True
    elif a in history:
        return False

    b = parent[a]
    history = history | b
    return recurisve(parent, b, history)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        parent = defaultdict(set)
        for a, b in prerequisites:
            parent[a].add(b)
        print(parent)
        for a, b in prerequisites:
            result = recurisve(parent, a, set())
            if not result:
                return False
        return True
