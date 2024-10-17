public class Solution {
    public int FindPeakElement(int[] nums) {
        if (nums.Length == 1)
            return 0;

        int left = 0, right = nums.Length - 1;
        bool isLeft = false, isRight = false;
        while (left < right)
        {
            int mid = (left + right) / 2;

            if (mid == left)
            {
                isLeft = true;
            }
            else if (nums[mid] > nums[mid - 1])
            {
                isLeft = true;
            }

            if (mid == right)
            {
                isRight = true;
            }
            else if (nums[mid] > nums[mid + 1])
            {
                isRight = true;
            }

            if(isLeft && isRight) return mid;

            if(!isLeft)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
            isLeft = false;
            isRight = false;
        }
        return nums[left] > nums[right] ? left : right;
    }
}