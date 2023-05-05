# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        lst = []
        q = deque()
        q.append(root)
        while q:
            cur = q.popleft()
            lst.append(cur.val)
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        lst.sort()
        return lst[k - 1]