public class Solution
{
    public int RangeBitwiseAnd(int left, int right)
    {
        int cnt = 0;
        while (left != right)
        {
            left >>= 1;
            right >>= 1;
            cnt++;
        }
        left <<= cnt;
        return left;
    }
}