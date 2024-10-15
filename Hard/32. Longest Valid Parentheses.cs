public class Solution
{
    public int LongestValidParentheses(string s)
    {
        Dictionary<char, int> parantheses = new Dictionary<char, int>()
        {
            { '(', 0 }, { ')', 0 },
        };
        int max = 0;
        for (int i = 0; i < s.Length; i++)
        {
            parantheses[s[i]]++;
            if (parantheses['('] == parantheses[')'])
            {
                int validLen = parantheses['('] * 2;
                max = max < validLen ? validLen : max;
            }
            else if (parantheses['('] < parantheses[')'])
            {
                parantheses['('] = parantheses[')'] = 0;
            }
        }

        parantheses['('] = parantheses[')'] = 0;
        for (int i = s.Length - 1; i >= 0; i--)
        {
            parantheses[s[i]]++;
            if (parantheses['('] == parantheses[')'])
            {
                int validLen = parantheses['('] * 2;
                max = max < validLen ? validLen : max;
            }
            else if (parantheses['('] > parantheses[')'])
            {
                parantheses['('] = parantheses[')'] = 0;
            }
        }
        return max;
    }
}