# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.check(root.left, root.right)

    def check(self, left, right):

        if left is None and right is None:  # 둘다 끝까지 다다랐다는건 대칭 조건을 노드 끝까지 만족
            return True

        if left is None or right is None:  # 하나는 끝까지 다다르지 못했는데 다른 하나가 끝이면, 대칭 x
            return False

        if left.val != right.val: # 값이 다르면 대칭 x
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left) # 대칭이 되려면 오른쪽과 왼쪽 비교