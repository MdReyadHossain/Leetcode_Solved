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
    public ListNode MiddleNode(ListNode head)
    {
        if (head == null || head.next == null)
            return head;
        int length = 0;
        ListNode currentPtr = head;
        while (currentPtr != null)
        {
            length++;
            currentPtr = currentPtr.next;
        }
        int mid = length / 2 + 1;
        currentPtr = head;
        while (currentPtr != null)
        {
            mid--;
            if (mid == 0)
                break;
            currentPtr = currentPtr.next;
        }

        return currentPtr;
    }
}