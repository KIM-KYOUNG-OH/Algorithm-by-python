from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = deque()
        for ch in s:
            if not ch.isalpha() and not ch.isdigit():
                continue
            q.append(ch.lower())

        while len(q) > 1:
            left = q.popleft()
            right = q.pop()
            if left != right:
                return False
        return True