# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        p = root
        st = [p]
        #直接反向思考，最后反向输出
        while st:
            p = st.pop()
            res.append(p.val)
            if p.left:
                st.append(p.left)
            if p.right:
                st.append(p.right)
        return res[::-1] 

