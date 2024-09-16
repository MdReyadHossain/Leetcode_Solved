public class Solution
{
    public int SingleNumber(int[] nums)
    {
        Array.Sort(nums);
        if (nums.Length == 1)
        {
            return nums[0];
        }

        for (int i = 1; i < nums.Length; i += 3)
        {
            if (nums[i] != nums[i - 1])
            {
                return nums[i - 1];
            }
        }
        return nums[^1];
    }
}