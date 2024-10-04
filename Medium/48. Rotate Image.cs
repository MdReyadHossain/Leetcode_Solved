public class Solution
{
    public void SwapBetween(int[][] matrix, int a, int b, int x, int y)
    {
        matrix[a][b] += matrix[x][y];
        matrix[x][y] = matrix[a][b] - matrix[x][y];
        matrix[a][b] -= matrix[x][y];
    }

    public void Rotate(int[][] matrix)
    {
        if(matrix.Length == 1)
        {
            return;
        }
        int jStart = 0;
        int iRev = matrix.Length - 1, jRev = matrix.Length - 1;
        for (int i = 0; i < matrix.Length / 2; i++)
        {
            for (int j = jStart; j < iRev; j++)
            {
                SwapBetween(matrix, i, j, j, iRev);
                SwapBetween(matrix, i, j, iRev, jRev);
                SwapBetween(matrix, i, j, jRev, i);
                jRev--;
            }
            jStart++;
            iRev--;
            jRev = matrix.Length - 1 - jStart;
        }
    }
}