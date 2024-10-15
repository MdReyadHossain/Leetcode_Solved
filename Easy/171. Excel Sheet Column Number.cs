public class Solution
{
    public int TitleToNumber(string columnTitle)
    {
        int sum = 0;
        for (int i = 0; i < columnTitle.Length; i++)
        {
            sum = (sum * 26) + ((int)columnTitle[i] - 64);
        }
        return sum;
    }
}