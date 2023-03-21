from collections import deque


class Solution:
    def canJump(self, nums):
        cur = 0
        q = deque()
        q.append(cur)
        visit = [False] * len(nums)
        visit[0] = True
        while q:
            idx = q.popleft()
            for i in range(nums[idx] + 1):
                next_idx = idx + i
                if next_idx >= len(nums) - 1:
                    return True
                if not visit[next_idx]:
                    visit[next_idx] = True
                    q.append(next_idx)
        return False
