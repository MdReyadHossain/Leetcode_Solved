public class Solution
{
    public int HammingWeight(int n)
    {
        int cnt = 0;
        long sum = 0;
        long x = (int)Math.Log2(n);
        for (long i = x; i >= 0; i--)
        {
            sum += (long)Math.Pow(2, i);
            if (sum <= n)
            {
                cnt++;
            }
            else
            {
                sum -= (long)Math.Pow(2, i);
            }
        }
        return cnt;
    }
}