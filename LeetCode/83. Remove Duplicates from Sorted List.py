# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        print("cur",cur,"heeeeeeeee",head)
        while cur:

            if cur.next and cur.val == cur.next.val: # 다음노드가 있고 현재노드값과 다음노드 값이 같으면
                cur.next = cur.next.next # 다음 노드를 다다음 노드와 연결
            else:
                cur = cur.next
        print("cur",cur,head)
        return head