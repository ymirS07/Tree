# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        que = collections.deque([root])
        while que:
          # 一层一层换
            for _ in range(len(que)):
                p = que.popleft()
                if p.left:
                    que.append(p.left)
                if p.right:
                    que.append(p.right)
                p.left, p.right = p.right, p.left
        
        return root
