from collections import deque


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        q = deque(prices)
        buy = q.popleft()
        answer = 0
        while q:
            cur = q.popleft()
            if buy > cur:
                buy = cur
            elif buy < cur:
                answer = max(answer, cur - buy)
        return answer
