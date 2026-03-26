# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        
        sum_ = 0

        def dfs(node,granpa,parent):
            if not node:
                return 0
            return (node.val if granpa.val % 2 == 0 else 0) + dfs(node.left,parent,node) + dfs(node.right,parent,node)

        if root.left and root.left.left:
            sum_ += dfs(root.left.left,root,root.left)
        if root.left and root.left.right:
            sum_ += dfs(root.left.right,root,root.left)
        if root.right and root.right.left:
            sum_ += dfs(root.right.left,root,root.right)
        if root.right and root.right.right:
            sum_ += dfs(root.right.right,root,root.right)
        
        
        return sum_

        
