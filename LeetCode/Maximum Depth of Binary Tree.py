# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque()
        q.append(root)
        depth = 0
        while q:
            temp = deque()
            while q:
                cur = q.popleft()
                if cur.left is not None:
                    temp.append(cur.left)
                if cur.right is not None:
                    temp.append(cur.right)
            q = temp
            depth += 1
        return depth
