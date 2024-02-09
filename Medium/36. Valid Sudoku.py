class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        hashSet: list[str] = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if f'row-{j}-{board[i][j]}' in hashSet:
                        return False
                    if f'col-{i}-{board[i][j]}' in hashSet:
                        return False
                    if f'box-{(j//3) + ((i//3)*3)}-{board[i][j]}' in hashSet:
                        return False
                    hashSet.append(f'row-{j}-{board[i][j]}')
                    hashSet.append(f'col-{i}-{board[i][j]}')
                    hashSet.append(f'box-{(j//3) + ((i//3)*3)}-{board[i][j]}')
        return True
