public class Node
{
    public int val;
    public int key;
    public Node next;
    public Node prev;
    public Node(int val, int key, Node? next = null, Node? prev = null)
    {
        this.val = val;
        this.key = key;
        this.next = next;
        this.next = prev;
    }
}

public class LRUCache
{
    private Dictionary<int, Node> hashSet;
    private int capacity;
    private int size;
    private Node lru;
    private Node mru;

    private void insertNode(Node node)
    {
        if (this.size == 0 || this.mru == null)
        {
            this.mru = this.lru = node;
            return;
        }
        this.mru.prev = node;
        node.next = mru;
        this.mru = node;
        this.mru.prev = null;
        return;
    }

    private void removeNode(Node node)
    {
        if (node.next == null)
        {
            this.lru = node.prev;
            this.lru.next = null;
            node.prev = null;
            return;
        }
        else if (node.prev == null)
        {
            this.mru = this.mru.next;
            this.mru.prev = null;
            node.next = null;
            return;
        }
        Node prevNode = node.prev;
        Node nextNode = node.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
        node.prev = null;
        node.next = null;
        return;
    }

    public LRUCache(int capacity)
    {
        hashSet = new Dictionary<int, Node>();
        this.capacity = capacity;
        this.size = 0;
    }

    public int Get(int key)
    {
        if (hashSet.TryGetValue(key, out Node? node))
        {
            if (this.size == 1)
            {
                return node.val;
            }
            removeNode(node);
            insertNode(node);
            return node.val;
        }
        return -1;
    }

    public void Put(int key, int value)
    {
        if (hashSet.ContainsKey(key))
        {
            if (this.size == 1)
            {
                hashSet[key].val = value;
                return;
            }
            removeNode(hashSet[key]);
            hashSet[key].val = value;
            insertNode(hashSet[key]);
            return;
        }
        hashSet[key] = new Node(value, key);
        insertNode(hashSet[key]);

        if (this.size == this.capacity)
        {
            hashSet.Remove(this.lru.key);
            removeNode(this.lru);
            return;
        }
        this.size++;
    }
}