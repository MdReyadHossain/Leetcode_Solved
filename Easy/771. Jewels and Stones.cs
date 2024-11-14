public class Solution
{
    public int NumJewelsInStones(string jewels, string stones)
    {
        int cnt = 0;
        int[] freq = new int[128];
        foreach (char c in jewels)
        {
            freq[(int)c] = 1;
        }

        foreach (char c in stones)
        {
            if (freq[(int)c] == 1)
                cnt++;
        }

        return cnt;
    }
}