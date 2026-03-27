# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        ans = 0

        def dfs(path,node,curr):
            nonlocal ans
            if not node:
                return

            curr += node.val
            if curr - targetSum in path:
                ans += path[curr - targetSum]
            
            path[curr] += 1
            dfs(path,node.left,curr)
            dfs(path,node.right,curr)
            path[curr] -= 1
            curr -= node.val
        hash_ = Counter({0:1})
        dfs(hash_,root,0)
        return ans
        
