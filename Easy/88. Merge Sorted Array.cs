public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        int i = m - 1, j = n - 1;
        int r = nums1.Length - 1;
        while (i >= 0 && j >= 0)
        {
            if (nums1[i] > nums2[j])
            {
                nums1[r] = nums1[i];
                i--;
            }
            else
            {
                nums1[r] = nums2[j];
                j--;
            }
            r--;
        }

        while (i >= 0)
        {
            nums1[r] = nums1[i];
            i--;
            r--;
        }

        while (j >= 0)
        {
            nums1[r] = nums2[j];
            j--;
            r--;
        }
    }
}