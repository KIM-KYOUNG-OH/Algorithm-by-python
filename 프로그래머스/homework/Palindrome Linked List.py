# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        stack = []
        while head != None:
            val = head.val
            stack.append(val)
            head = head.next

        if stack == stack[::-1]:
            return True
        return False