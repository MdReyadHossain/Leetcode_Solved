public class Solution
{
    public int FindMinArrowShots(int[][] points)
    {
        int cnt = 0, i = 0;
        int[] comp = [0, 0];
        Array.Sort(points, (a, b) => a[0].CompareTo(b[0]));

        while (i < points.Length)
        {
            int[] reset = [0, 0];
            if (comp[0] == 0 && comp[1] == 0)
            {
                comp = points[i];
                i++;
                continue;
            }
            else if (points[i][0] > comp[1])
            {
                comp = reset;
                cnt++;
                continue;
            }
            comp[0] = points[i][0];
            if (points[i][1] < comp[1]) comp[1] = points[i][1];
            i++;
        }
        return ++cnt;
    }
}