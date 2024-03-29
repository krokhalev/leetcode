class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


s = Solution()
print(s.isSameTree(
    TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)),
    TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
))
