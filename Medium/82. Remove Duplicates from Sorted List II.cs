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
    public ListNode DeleteDuplicates(ListNode head)
    {
        if (head == null) return null;
        int cnt = 1;
        bool isHead = false;
        ListNode currentPtr = head, checkPtr = head;
        while (checkPtr.next != null)
        {
            if (checkPtr.val != checkPtr.next.val) cnt++;
            else cnt = 0;
            if (cnt == 2)
            {
                if (isHead)
                {
                    currentPtr.next = checkPtr;
                }
                else
                {
                    head = checkPtr;
                    isHead = true;
                }
                currentPtr = checkPtr;
                cnt = 0;
                continue;
            }
            checkPtr = checkPtr.next;
        }
        if (cnt == 1 && isHead)
        {
            currentPtr.next = checkPtr;
        }
        else if (cnt == 1 && !isHead)
        {
            head = checkPtr;
        }
        else if (!isHead)
        {
            head = null;
        }
        else
        {
            currentPtr.next = null;
        }

        return head;
    }
}