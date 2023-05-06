class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root

        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)

        if min_val < root.val < max_val:
            return root
        elif root.val < min_val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)