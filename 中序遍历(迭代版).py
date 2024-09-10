# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        st = []
        res = []
        p = root
        while p or st:
            if p: #直接走到最左开始
                st.append(p)
                p = p.left
            else: #p为null的时候的·回头·操作：按中-->右的顺序加入res 这个condition就类似谦虚前序的右
                p = st.pop()
                res.append(p.val)
                p = p.right
        return res
