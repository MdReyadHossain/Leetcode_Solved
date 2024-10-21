public class Solution
{
    public int[] SearchRange(int[] nums, int target)
    {
        int[] res = [-1, -1];
        if (nums.Length == 0)
            return res;

        int left = 0, right = nums.Length - 1;

        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[left] == target)
            {
                res[0] = left;
                break;
            }

            if (nums[mid] == target)
            {
                if (nums[mid] > nums[mid - 1])
                {
                    res[0] = mid;
                    break;
                }
                else right = mid - 1;
            }
            else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }

        if (res[0] == -1) return res;
        left = 0;
        right = nums.Length - 1;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[right] == target)
            {
                res[1] = right;
                break;
            }

            if (nums[mid] == target)
            {
                if (nums[mid] < nums[mid + 1])
                {
                    res[1] = mid;
                    break;
                }
                else left = mid + 1;
            }
            else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return res;
    }
}