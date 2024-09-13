# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # 成对加入，因为左右子树要同时对比
        que = collections.deque([(root.left, root.right)])
        while que:
            left, right = que.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            que.append((left.left, right.right))
            que.append((left.right, right.left))
        return True
