# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        q = deque()
        cur = head
        while True:
            if cur is None:
                break
            q.append(cur)
            cur = cur.next

        if not q:
            return head
        top = q.pop()
        answer = top
        while q:
            last = q.pop()
            top.next = last
            top = last
        top.next = None
        return answer
