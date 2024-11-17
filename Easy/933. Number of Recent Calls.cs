public class RecentCounter
{
    List<int> counters;
    public RecentCounter()
    {
        counters = new List<int>();
    }

    public int Ping(int t)
    {
        int cnt = 0;
        counters.Add(t);
        foreach (int counter in counters)
        {
            if (t - 3000 <= counter && counter <= t)
            {
                cnt++;
            }
        }
        return cnt;
    }
}