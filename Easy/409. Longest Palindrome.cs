public class Solution
{
    public int LongestPalindrome(string s)
    {
        Dictionary<char, int> hash = new Dictionary<char, int>();
        int evenSum = 0, oddSum = 0, odd = 0;

        foreach (char c in s)
        {
            if (hash.ContainsKey(c))
            {
                hash[c]++;
                continue;
            }
            hash[c] = 1;
        }

        foreach (var pair in hash)
        {
            if (pair.Value % 2 == 0)
            {
                evenSum += pair.Value;
            }
            else
            {
                if (odd < pair.Value)
                {
                    oddSum = odd == 0 ? oddSum : oddSum - 1;
                    oddSum += pair.Value;
                    odd = pair.Value;
                }
                else
                {
                    oddSum += pair.Value - 1;
                }
            }
        }

        return evenSum + oddSum;
    }
}