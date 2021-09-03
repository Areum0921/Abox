# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find(root):
            if root is None:
                return 0

            left = find(root.left)
            right = find(root.right)

            if abs(left - right) > 1 or left == -1 or right == -1: # -1이거나 높이차이가 1초과 일경우
                return -1

            return max(left, right) + 1

        return find(root) != -1