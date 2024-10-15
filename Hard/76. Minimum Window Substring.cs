public class Solution
{
    public string MinWindow(string s, string t)
    {
        if (s.Length < t.Length) return "";
        if (t.Length == 1)
        {
            if (s.Contains(t))
                return t;
            return "";
        }

        int reqLetters = 0, hvLetters = 0;
        int[] res = new int[2] { 0, int.MaxValue };
        Dictionary<char, int> reqHash = new Dictionary<char, int>();
        Dictionary<char, int> compHash = new Dictionary<char, int>();
        foreach (char c in t)
        {
            compHash[c] = 0;
            if (reqHash.ContainsKey(c))
            {
                reqHash[c]++;
                continue;
            }
            reqLetters++;
            reqHash[c] = 1;
        }
        for (int i = 0, j = -1; j < s.Length;)
        {
            if (reqLetters <= hvLetters)
            {
                if ((res[1] - res[0]) > (j - i))
                {
                    (res[0], res[1]) = (i, j);
                }
                if (compHash.ContainsKey(s[i]))
                {
                    if (compHash[s[i]] == reqHash[s[i]]) hvLetters--;
                    compHash[s[i]]--;
                }
                i++;
                continue;
            }
            if (++j == s.Length) break;
            if (compHash.ContainsKey(s[j]))
            {
                if (compHash[s[j]] + 1 == reqHash[s[j]]) hvLetters++;
                compHash[s[j]]++;
            }
        }

        if (res[1] == int.MaxValue) return "";

        t = "";
        for (int i = res[0]; i <= res[1]; i++)
            t += s[i];
        return t;
    }
}