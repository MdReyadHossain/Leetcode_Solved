/** Definition for singly-linked list. */
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
    public ListNode RemoveNthFromEnd(ListNode head, int n)
    {
        int len = 0;
        ListNode current = head, prev = null;
        while (current != null)
        {
            current = current.next;
            len++;
        }
        int index = len - n + 1;
        if (len == 1)
        {
            head = null;
            return head;
        }
        else if (index == 1)
        {
            head = head.next;
            return head;
        }

        current = head;
        while (len > 0)
        {
            if (len == n + 1) prev = current;
            else if (len == n) break;
            current = current.next;
            len--;
        }
        prev.next = current.next;
        return head;
    }
}