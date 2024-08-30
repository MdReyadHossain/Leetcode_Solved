class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MinStack:
    def __init__(self):
        self.head: ListNode = None
        self.min: ListNode = None

    def push(self, val: int) -> None:
        newNode: ListNode = ListNode(val)
        if self.head == None:
            self.head = newNode
            self.min = ListNode(val)
            return
        if self.min.val >= val:
            newMinNode: ListNode = ListNode(val, self.min)
            self.min = newMinNode
        newNode.next = self.head
        self.head = newNode
        return

    def pop(self) -> None:
        if self.head == None:
            return
        if self.head.val == self.min.val:
            self.min = self.min.next
        self.head = self.head.next
        return

    def top(self) -> int:
        if self.head:
            return self.head.val
        return False

    def getMin(self) -> int:
        return self.min.val
