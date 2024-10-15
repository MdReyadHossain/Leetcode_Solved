public class Solution
{
    public IList<IList<string>> GroupAnagrams(string[] strs)
    {
        IList<IList<string>> res = [];
        int[] freq = new int[128];
        Array.Clear(freq, 0, freq.Length);
        Dictionary<string, IList<string>> hash = new Dictionary<string, IList<string>>();
        foreach (string item in strs)
        {
            string key = "";
            Array.Clear(freq, 0, freq.Length);
            foreach (char letter in item)
            {
                freq[(int)letter]++;
            }
            for (int i = 0; i < 128; i++)
            {
                if (freq[i] > 0)
                {
                    key += $"{freq[i]}{(char)i}";
                }
            }
            Console.WriteLine(key);
            if (hash.ContainsKey(key))
            {
                hash[key].Add(item);
            }
            else
            {
                hash[key] = new List<string>() { item };
            }
        }

        foreach (IList<string> item in hash.Values)
        {
            res.Add(item);
        }

        return res;
    }
}