class PeekingIterator
{
    IEnumerator<int> enumerator;
    int count = 0;
    int i = 0;
    public PeekingIterator(IEnumerator<int> iterator)
    {
        this.enumerator = iterator;
        while (this.enumerator.MoveNext())
        {
            this.count++;
        }
        this.enumerator.Reset();
        this.enumerator.MoveNext();
    }

    // Returns the next element in the iteration without advancing the iterator.
    public int Peek()
    {
        return this.enumerator.Current;
    }

    // Returns the next element in the iteration and advances the iterator.
    public int Next()
    {
        int current = Peek();
        this.enumerator.MoveNext();
        this.i++;
        return current;
    }

    // Returns false if the iterator is refering to the end of the array of true otherwise.
    public bool HasNext()
    {
        return i <= count;
    }
}