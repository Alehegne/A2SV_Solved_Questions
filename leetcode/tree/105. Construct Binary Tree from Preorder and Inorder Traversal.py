# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pid = 0

        def build(inorder):
            nonlocal pid
            p_val = preorder[pid]
            parent = TreeNode(p_val)
            pid += 1

            if len(inorder) == 1:
                return parent
            
            pidx = inorder.index(p_val)
            left_inor = inorder[:pidx]
            right_inor = inorder[pidx+1:]
           
            if left_inor:
                parent.left = build(left_inor)
            if right_inor:
                parent.right = build(right_inor)

            return parent

        return build(inorder)

        
