# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        result = []
        q = deque([root])
        while q:
            parent_lst, children_list = [], deque()
            while q:
                cur = q.popleft()
                parent_lst.append(cur.val)
                if cur.left is not None:
                    children_list.append(cur.left)
                if cur.right is not None:
                    children_list.append(cur.right)
            q = children_list
            result.append(parent_lst)
        return result
