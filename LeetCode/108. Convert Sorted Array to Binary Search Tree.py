# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.sortTo(nums)

    def sortTo(self, nums):
        if len(nums) == 0:
            return None

        mid = nums[len(nums) // 2]

        root = TreeNode(mid)
        root.left = self.sortTo(nums[:len(nums) // 2])
        root.right = self.sortTo(nums[(len(nums) // 2) + 1:])

        return root

