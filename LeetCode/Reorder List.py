# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        cur = head
        while cur:
            q.append(cur)
            cur = cur.next

        if q:
            q.popleft()
        direction = 1
        cur = head
        while q:
            if direction == 1:
                temp = q.pop()
                cur.next = temp
                cur = temp
            else:
                temp = q.popleft()
                cur.next = temp
                cur = temp
            direction *= -1

