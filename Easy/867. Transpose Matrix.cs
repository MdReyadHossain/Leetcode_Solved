public class Solution
{
    public int[][] Transpose(int[][] matrix)
    {
        int row = matrix.Length, col = matrix[0].Length;
        int[][] transMatrix = new int[col][];

        for (int i = 0; i < col; i++)
        {
            int[] transRow = new int[matrix.Length];
            for (int j = 0; j < row; j++)
            {
                transRow[j] = matrix[j][i];
            }
            transMatrix[i] = transRow;
        }

        return transMatrix;
    }
}