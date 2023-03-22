from collections import deque


class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        answer = deque()
        while intervals:
            if len(intervals) == 1:
                answer.appendleft(intervals.pop())
                break
            cur = intervals.pop()
            peek = intervals[-1]
            if cur[0] <= peek[1]:
                peek = intervals.pop()
                intervals.append([min(peek[0], cur[0]), cur[1]])
            else:
                answer.appendleft(cur)
        return answer