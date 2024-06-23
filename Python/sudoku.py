from typing import Optional, Tuple


class Sudoku:

    # This class allows us to hold a matrix that is indexed (1-9) to be consistent with Sudoku.

    def __init__(self, matrix: Optional[list[list[int]]] = None, size: int = 9):

        self.size : int = size

        if matrix == None:
            self.matrix: list[list[int]] = [[0 for col in range(size)] for row in range(size)]
        else:
            assert matrix is not None
            self.matrix = matrix

    def __getitem__(self, rowCol: Tuple[int, int]) -> int:
        row, col = rowCol
        return self.matrix[row-1][col-1]

    def __setitem__(self, rowColVal: Tuple[int, int], value: int):
        row, col = rowColVal
        self.matrix[row-1][col-1] = value