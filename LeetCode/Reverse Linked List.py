# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 함수 정의
        def reverse(node: ListNode, prev: ListNode = None):
            # base case
            if not node:
                return prev

            # recursive case
            # next 변수에 현재 노드의 next를 넣고 매개변수 node로 재귀 호출, node.next에는 이전 호출의 노드를 재할당
            next, node.next = node.next, prev
            # next가 재귀 호출 시 매개변수 node 자리로 들어감, 현재 node는 prev 자리로 들어감
            return reverse(next, node)

            # 함수 실행

        return reverse(head)