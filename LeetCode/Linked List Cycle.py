# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if head is None or head.next is None:
            return False
        history = set()
        while head is not None:
            if head in history:
                return True
            else:
                history.add(head)
                head = head.next
        return False