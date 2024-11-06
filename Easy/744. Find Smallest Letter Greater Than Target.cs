public class Solution
{
    public char NextGreatestLetter(char[] letters, char target)
    {
        char res = '~';
        foreach (char c in letters)
        {
            if (c > target && res > c)
            {
                res = c;
            }
        }
        return res == '~' ? letters[0] : res;
    }
}