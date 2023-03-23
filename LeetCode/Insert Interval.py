from collections import deque


class Solution:
    def insert(self, intervals, newInterval):
        q = deque(intervals)
        answer = []
        while q:
            if newInterval is None:
                answer.extend(q)
                break
            cur = q.popleft()
            if newInterval[0] <= cur[1]:
                if newInterval[1] < cur[0]:
                    answer.append(newInterval)
                    answer.append(cur)
                    newInterval = None
                else:
                    newInterval = [min(newInterval[0], cur[0]), max(newInterval[1], cur[1])]
            else:
                answer.append(cur)
        if newInterval is not None:
            answer.append(newInterval)
        return answer
