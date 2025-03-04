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

        return (" ".join(res))


def createLinkList(arr):
    dummy = ListNode()
    p = dummy
    for val in arr:
        p.next = ListNode(val=val)
        p = p.next

    return dummy.next


head = createLinkList([1, 2, 3, 4, 5])
print(head)
