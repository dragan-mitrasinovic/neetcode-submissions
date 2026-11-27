# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.height(root)
        return self.balanced

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        height_left = self.height(root.left)
        height_right = self.height(root.right)
        
        if abs(height_left - height_right) > 1:
            self.balanced = False
        
        return 1 + max(height_left, height_right)