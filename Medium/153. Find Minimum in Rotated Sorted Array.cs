public class Solution
{
    public int FindMin(int[] nums)
    {
        if (nums.Length == 1)
            return nums[0];

        int left = 0, right = nums.Length - 1;
        while (left <= right)
        {
            int mid = (left + right) / 2;

            if (nums[mid] <= nums[right])
            {
                if (mid == 0)
                    return nums[mid];
                else if (nums[mid - 1] > nums[mid])
                    return nums[mid];
                else
                    right = mid - 1;
            }
            else
                left = mid + 1;
        }

        return nums[left];
    }
}