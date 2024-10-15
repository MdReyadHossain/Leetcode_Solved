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
    public ListNode Partition(ListNode head, int x)
    {
        if (head == null)
            return null;

        ListNode currntPtr = head;
        ListNode left = null, right = null, leftPtr = null, rightPtr = null;
        while (currntPtr != null)
        {
            if (currntPtr.val < x)
            {
                if (left == null)
                {
                    left = currntPtr;
                    leftPtr = currntPtr;
                }
                else
                {
                    leftPtr.next = currntPtr;
                    leftPtr = leftPtr.next;
                }
            }
            else
            {
                if (right == null)
                {
                    right = currntPtr;
                    rightPtr = currntPtr;
                }
                else
                {
                    rightPtr.next = currntPtr;
                    rightPtr = rightPtr.next;
                }
            }
            currntPtr = currntPtr.next;
        }

        if (left == null)
            return right;

        else if (right == null)
            return left;

        leftPtr.next = right;
        rightPtr.next = null;
        return left;
    }
}