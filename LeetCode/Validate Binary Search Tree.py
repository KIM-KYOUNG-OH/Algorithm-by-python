import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isPossible(self, cur, lower=sys.maxsize * (-1), upper=sys.maxsize):
        if cur is None:
            return True
        if lower < cur.val < upper:
            return self.isPossible(cur.left, lower, cur.val) and self.isPossible(cur.right, cur.val, upper)
        else:
            return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isPossible(root)
