# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        resultList: ListNode = ListNode()
        resPtr: ListNode = resultList
        if list1 and list2:
            if list1.val < list2.val:
                resPtr.next = list1
                list1 = list1.next
            else:
                resPtr.next = list2
                list2 = list2.next
            resPtr = resPtr.next

        while list1 and list2:
            if list1.val < list2.val:
                resPtr.next = list1
                list1 = list1.next
            else:
                resPtr.next = list2
                list2 = list2.next
            resPtr = resPtr.next

        while list1:
            resPtr.next = list1
            list1 = list1.next
            resPtr = resPtr.next

        while list2:
            resPtr.next = list2
            list2 = list2.next
            resPtr = resPtr.next

        return resultList.next