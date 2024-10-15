public class Solution
{
    public int GetNumberOfNei(int[][] board, int r, int c)
    {
        int n = 0;
        for (int i = r - 1; i < r + 2; i++)
        {
            for (int j = c - 1; j < c + 2; j++)
            {
                if ((i == r && j == c) || i < 0 || j < 0 || i == board.Length || j == board[0].Length)
                    continue;
                if (board[i][j] == 1 || board[i][j] == -2)
                {
                    n++;
                }
            }
        }
        return n;
    }

    public void GameOfLife(int[][] board)
    {
        int rows = board.Length, cols = board[0].Length;

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                int n = GetNumberOfNei(board, i, j);
                if (board[i][j] == 1)
                {
                    if (n < 2 || n > 3) board[i][j] = -2;
                }
                else if (board[i][j] == 0)
                {
                    if (n == 3) board[i][j] = -1;
                }
            }
        }

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                board[i][j] = board[i][j] == -1 ? 1 : board[i][j] == -2 ? 0 : board[i][j];
            }
        }
    }
}