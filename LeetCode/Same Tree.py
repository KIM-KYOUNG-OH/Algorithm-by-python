# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
p_path = ''
q_path = ''


def getPPath(cur):
    global p_path
    if cur is None:
        p_path += 'null'
        return
    else:
        p_path += str(cur.val)

    if cur.left is None and cur.right is None:
        return
    getPPath(cur.left)
    getPPath(cur.right)


def getQPath(cur):
    global q_path
    if cur is None:
        q_path += 'null'
        return
    else:
        q_path += str(cur.val)

    if cur.left is None and cur.right is None:
        return
    getQPath(cur.left)
    getQPath(cur.right)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        global p_path, q_path
        p_path = ''
        q_path = ''
        getPPath(p)
        getQPath(q)
        if p_path == q_path:
            return True
        else:
            return False
