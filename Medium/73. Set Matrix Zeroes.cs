public class Solution
{
    public void SetZeroes(int[][] matrix)
    {
        List<List<int>> zeros = new List<List<int>>();
        int row = matrix.Length, col = matrix[0].Length;

        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                if (matrix[i][j] != 0)
                    continue;
                zeros.Add([i, j]);
            }
        }
        foreach (List<int> zero in zeros)
        {
            for (int i = 0; i < row; i++)
            {
                matrix[i][zero[1]] = 0;
            }

            for (int i = 0; i < col; i++)
            {
                matrix[zero[0]][i] = 0;
            }
        }
    }
}