# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def dfs(node, s):
            if node is None:
                return False
            if node.left == None and node.right == None:
                if s == targetSum:
                    return True
            # if s > targetSum:
            #     return False
            left = False
            right = False
            if node.left:
                left = dfs(node.left, s + node.left.val)
            if node.right:
                right = dfs(node.right, s + node.right.val)

            return left or right
        
        return dfs(root, root.val)