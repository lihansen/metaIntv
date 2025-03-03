import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = []
        p = self
        while p:
            res.append(str(p.val))
            p = p.next
        return ",".join(res)


class Node:
    def __init__(self, node):
        self.node = node

    def __lt__(self, o):
        return self.node.val < o.node.val


class Solution:
    def mergeKLists(self, lists):
        heap = []
        dummy = ListNode()
        p = dummy

        for node in lists:
            if node:
                heap.append(Node(node))

        heapq.heapify(heap)

        while heap:
            top = heapq.heappop(heap).node
            p.next = top
            p = p.next
            top = top.next
            if top:
                heapq.heappush(heap, Node(top))

        return dummy.next


def mergeKLists(lists):
    heap = []
    dummy = ListNode()
    p = dummy
    
    for node in lists:
        if node:
            heap.append(Node(node))
    
    heapq.heapify(heap)
    
    while heap:
        top = heapq.heappop(heap).node
        p.next = top
        p = p.next
        if top.next:
            heapq.heappush(heap, Node(top.next))
            
    return dummy.next



# create a linklist
'''
[
  1->4->5,
  1->3->4,
  2->6,
]
'''


def create_linklist(l):
    dummy = ListNode()
    p = dummy
    for val in l:
        p.next = ListNode(val)
        p = p.next
    return dummy.next


node_list = [
    create_linklist([1, 4, 5]),
    create_linklist([1, 3, 4]),
    create_linklist([2, 6])
]

sol = Solution()
# res = sol.mergeKLists(node_list)
res = mergeKLists(node_list)
print(res)
