public class Solution
{
    public string ReverseVowels(string s)
    {
        if (s.Length == 1) return s;
        char[] vowels = new char[] { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' };
        string res = "";
        bool isSwap = false;
        Stack<char> stack = new Stack<char>();
        int j = s.Length - 1;
        for (int i = 0; i < s.Length; i++)
        {
            if (!vowels.Contains(s[i]))
            {
                res += s[i];
                continue;
            }
            if (i > j)
            {
                if (stack.Count() == 0)
                {
                    res += s[i];
                    continue;
                }
                res += stack.Pop();
            }
            else
            {
                while (i < j)
                {
                    if (vowels.Contains(s[j]))
                    {
                        res += s[j];
                        isSwap = true;
                        stack.Push(s[i]);
                        j--;
                        break;
                    }
                    j--;
                }
                if (isSwap)
                {
                    isSwap = false;
                    continue;
                }
                res += s[i];
            }

        }
        return res;
    }
}