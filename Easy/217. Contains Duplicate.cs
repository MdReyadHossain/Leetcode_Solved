public class Solution
{
    public bool ContainsDuplicate(int[] nums)
    {
        Dictionary<int, int> numHash = new Dictionary<int, int>();
        foreach (int num in nums)
        {
            if (numHash.ContainsKey(num))
                return true;
            numHash[num] = 1;
        }
        return false;
    }
}