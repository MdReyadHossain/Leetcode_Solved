# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr: ListNode = head
        length: int = 1
        while curr.next:
            curr = curr.next
            length += 1
        tail: ListNode = curr
        midIndex = (int)(length / 2)

        if length == 1:
            return True

        mid = head
        while midIndex > 1:
            mid = mid.next
            midIndex -= 1

        list2: ListNode = mid.next
        mid.next = None

        prev = None
        next = list2.next
        while list2.next:
            list2.next = prev
            prev = list2
            list2 = next
            next = list2.next
        list2.next = prev

        while tail and head:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next

        return True
