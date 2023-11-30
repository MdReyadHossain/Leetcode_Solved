# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result: ListNode = ListNode()
        resPtr: ListNode = result
        isHand: int = 0

        while l1 and l2:
            resPtr.next = l1
            resPtr = resPtr.next
            if l1.val + l2.val + isHand > 9:
                resPtr.val = (l1.val + l2.val + isHand) - 10
                isHand = 1
            else:
                resPtr.val = l1.val + l2.val + isHand
                isHand = 0
            l1 = l1.next
            l2 = l2.next

        while l1:
            resPtr.next = l1
            resPtr = resPtr.next
            if l1.val + isHand > 9:
                resPtr.val = (l1.val + isHand) - 10
                isHand = 1
            else:
                resPtr.val = l1.val + isHand
                isHand = 0
            l1 = l1.next

        while l2:
            resPtr.next = l2
            resPtr = resPtr.next
            if l2.val + isHand > 9:
                resPtr.val = (l2.val + isHand) - 10
                isHand = 1
            else:
                resPtr.val = l2.val + isHand
                isHand = 0
            l2 = l2.next

        if isHand == 1:
            resPtr.next = ListNode()
            resPtr.next.val = 1

        return result.next
