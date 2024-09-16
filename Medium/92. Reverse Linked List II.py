# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        cnt: int = 1
        currentPtr: ListNode = head
        prevNode: ListNode = None
        leftNode: ListNode = None
        leftPrev: ListNode = None
        rightNode: ListNode = None
        rightNext: ListNode = None

        while currentPtr.next:
            if cnt == left - 1:
                leftPrev = currentPtr
                leftNode = currentPtr.next
            if cnt == right:
                rightNext = currentPtr.next
                rightNode = currentPtr
            currentPtr = currentPtr.next
            cnt += 1

        if left == 1:
            leftNode = head

        if right == cnt:
            rightNode = currentPtr

        currentPtr = leftNode
        while currentPtr != rightNode:
            nextNode: ListNode = currentPtr.next
            currentPtr.next = prevNode
            prevNode = currentPtr
            currentPtr = nextNode
        currentPtr.next = prevNode

        if left > 1:
            leftPrev.next = currentPtr
        else:
            head = currentPtr
        if right < cnt:
            leftNode.next = rightNext

        return head
