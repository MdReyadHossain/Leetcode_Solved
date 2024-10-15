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
    public ListNode RotateRight(ListNode head, int k)
    {
        if (head == null)
            return head;

        ListNode currentPtr = head;
        int lenList = 0, cnt = 0;

        while (currentPtr != null)
        {
            currentPtr = currentPtr.next;
            lenList++;
        }

        if (k == lenList || k == 0 || k % lenList == 0)
            return head;

        currentPtr = head;

        k = lenList - (k % lenList) + 1;
        ListNode prevPtr = head, kPtr = head;

        while (currentPtr.next != null)
        {
            cnt++;
            if (cnt == k - 1)
            {
                prevPtr = currentPtr;
                kPtr = currentPtr.next;
            }
            currentPtr = currentPtr.next;
        }
        currentPtr.next = head;
        prevPtr.next = null;
        head = kPtr;
        return head;
    }
}