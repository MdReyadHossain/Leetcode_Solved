public class Solution
{
    public int AddDigits(int num)
    {
        if (num < 10) return num;
        if (num % 9 == 0) return 9;
        else return num % 9;
    }
}