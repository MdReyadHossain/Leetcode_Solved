public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution
{
    public ListNode ReverseList(ListNode head)
    {
        if (head == null)
            return head;

        ListNode currentPtr = head, prevPtr = null, nextPtr;
        while (currentPtr != null)
        {
            nextPtr = currentPtr.next;
            currentPtr.next = prevPtr;
            prevPtr = currentPtr;
            currentPtr = nextPtr;
        }
        head = prevPtr;
        return head;
    }
}