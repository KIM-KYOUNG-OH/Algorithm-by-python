# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        root = ListNode()
        cur = root
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))
        while pq:
            v, idx, node = heapq.heappop(pq)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(pq, (cur.next.val, idx, cur.next))
        return root.next
