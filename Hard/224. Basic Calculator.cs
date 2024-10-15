public class Solution
{
    public int Calculate(string s)
    {
        s += ' ';
        bool isUnary = false;
        int res = 0, sign = 1, val = 0;
        Stack<int> stack = new Stack<int>();

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '+' || s[i] == '-')
            {
                if (isUnary)
                {
                    sign = s[i] == '+' ? sign : -sign;
                    isUnary = false;
                    continue;
                }
                sign = s[i] == '+' ? 1 : -1;
                isUnary = true;
            }
            else if (s[i] == '(')
            {
                isUnary = false;
                stack.Push(sign);
                stack.Push(res);
                res = 0;
                sign = 1;
                val = 0;
            }
            else if (s[i] == ')')
            {
                isUnary = false;
                val = stack.Pop();
                res *= stack.Pop();
                res += val;
                val = 0;
            }
            else if ((int)s[i] >= 48 && (int)s[i] <= 57)
            {
                isUnary = false;
                val = (val * 10) + (int)s[i] - 48;
                if ((int)s[i + 1] < 48 || (int)s[i + 1] > 57)
                {
                    val *= sign;
                    res += val;
                    val = 0;
                }
            }
        }
        return res;
    }
}