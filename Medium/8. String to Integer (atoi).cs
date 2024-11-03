public class Solution
{
    public int MyAtoi(string s)
    {
        string modS = "";
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] != ' ')
            {
                modS = s.Substring(i);
                break;
            }
        }
        if (modS.Length == 0)
            return 0;
        bool isPositive = modS[0] != '-';
        int res = 0;
        for (int i = isPositive ? 0 : 1; i < modS.Length; i++)
        {
            if (modS[i] == '+' && i == 0) continue;
            if ((int)modS[i] < 48 || (int)modS[i] > 57)
            {
                return isPositive ? res : -res;
            }
            if (res > (int)(int.MaxValue / 10) || (res == (int)(int.MaxValue / 10) && (int)modS[i] - 48 > 7))
            {
                return isPositive ? int.MaxValue : int.MinValue;
            }
            res = res * 10 + (int)modS[i] - 48;
        }

        return isPositive ? res : -res;
    }
}