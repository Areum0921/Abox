# l1, l2는 이미 정렬된 상태이므로 하나씩 비교해서 넣기.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        print(l1, l2)
        print("val", l1.val, l2.val)
        if l1.val > l2.val:
            merge = ListNode(l2.val)
            merge.next = self.mergeTwoLists(l1, l2.next)
        else:
            merge = ListNode(l1.val)
            merge.next = self.mergeTwoLists(l1.next, l2)

        return merge