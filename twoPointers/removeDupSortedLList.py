class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        p = self
        res = []
        while p:
            res.append(str(p.val))
            p = p.next

        return " ".join(res)


def deleteDuplicate2(head):
    slow = head
    fast = head

    while fast:
        if slow.val != fast.val:
            slow.next = fast
            slow = slow.next

        fast = fast.next

    slow.next = None

    return head

def deleteDuplicate(head):
    p = head
    
    while p and p.next:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
            
    return head


def createLL(l):
    dummy = ListNode()
    p = dummy

    for item in l:
        p.next = ListNode(val=item)
        p = p.next

    return dummy.next


node = createLL([1, 1, 2])
print(node)
print(deleteDuplicate(node))

node = createLL([1, 1, 2, 3, 3])
print(node)
print(deleteDuplicate(node))
