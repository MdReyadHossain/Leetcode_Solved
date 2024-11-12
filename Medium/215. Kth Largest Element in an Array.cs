public class Solution
{
    public int FindKthLargest(int[] nums, int k)
    {
        int pIndex = 0, pInv = nums.Length - 1, pivot = nums[^1];
        int left = 0, right = nums.Length - 1;
        int[] resArr = new int[nums.Length];

        while (left < right)
        {
            for (int i = left; i <= right - 1; i++)
            {
                if (nums[i] < pivot)
                    resArr[pIndex++] = nums[i];
                else
                    resArr[pInv--] = nums[i];
            }
            resArr[pIndex] = pivot;
            if (nums.Length - k == pIndex)
                return resArr[pIndex];
            else if (nums.Length - k > pIndex)
                left = pIndex + 1;
            else
                right = pIndex - 1;
            nums = (int[])resArr.Clone();
            pivot = nums[right];
            pIndex = left;
            pInv = right;
        }

        return nums[right];
    }
}

public class Solution
{
    public int FindKthLargest(int[] nums, int k)
    {
        Array.Sort(nums);
        return nums[^k];
    }
}