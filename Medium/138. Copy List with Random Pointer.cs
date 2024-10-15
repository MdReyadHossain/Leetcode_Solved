public class Node
{
    public int val;
    public Node next;
    public Node random;

    public Node(int _val)
    {
        val = _val;
        next = null;
        random = null;
    }
}


public class Solution
{
    public Node CopyRandomList(Node head)
    {
        if (head == null)
            return null;
        Dictionary<Node, Node> hashMap = new Dictionary<Node, Node>();
        Node currentPtr = head, copyPtr;

        while (currentPtr != null)
        {
            copyPtr = new Node(currentPtr.val);
            hashMap[currentPtr] = copyPtr;
            currentPtr = currentPtr.next;
        }

        currentPtr = head;
        while (currentPtr != null)
        {
            copyPtr = hashMap[currentPtr];
            copyPtr.next = currentPtr.next == null ? null : hashMap[currentPtr.next];
            copyPtr.random = currentPtr.random == null ? null : hashMap[currentPtr.random];
            currentPtr = currentPtr.next;
        }

        return hashMap[head];
    }
}