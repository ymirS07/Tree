# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        que = deque([root])
        res = []
        p = root
        while que:
            level = []
            # 先进先出，分层加入结果
            for _ in range(len(que)):
                p = que.popleft()
                level.append(p.val)
                if p.left:
                    que.append(p.left)
                if p.right:
                    que.append(p.right)
            res.append(level)
        return res     
