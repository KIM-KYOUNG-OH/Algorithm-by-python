# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

            # preorder의 맨 앞의 원소를 pop 한게 현재 범위에서 inorder의 루트임
        curr = TreeNode(preorder.pop(0))

        curr.left = self.buildTree(preorder, inorder[: inorder.index(curr.val)])
        curr.right = self.buildTree(preorder, inorder[inorder.index(curr.val) + 1:])

        return curr