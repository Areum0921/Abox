# 문제는 안어려운데 ListNode 사용 미숙

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''

        while l1 != None:
            num1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            num2 += str(l2.val)
            l2 = l2.next

        answer = int(num1[::-1]) + int(num2[::-1])  # 두 값 더한거

        head = None
        answer_list = None

        for i in str(answer):
            if not head: # 노드 첫부분
                head = ListNode(int(i))
                answer_list = head
            else:
                cur = ListNode(int(i), answer_list)
                answer_list = cur
            print(answer_list)

        return answer_list

