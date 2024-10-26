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
    public ListNode RemoveElements(ListNode head, int val)
    {
        if (head == null)
            return head;
        ListNode currentPtr = head;
        while (currentPtr != null)
        {
            if (head.val == val)
            {
                head = head.next;
            }
            else
            {
                if (currentPtr.next != null)
                {
                    if (currentPtr.next.val == val)
                    {
                        currentPtr.next = currentPtr.next.next;
                        continue;
                    }
                }
            }
            currentPtr = currentPtr.next;
        }

        return head;
    }
}