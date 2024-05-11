from typing import Optional


class Sudoku:

    # This class allows us to hold a matrix that is indexed (1-9) to be consistent with Sudoku.

    def __init__(self, matrix: Optional[list[list[Optional[int]]]] = None, size: int = 9):

        self.size : int = size

        if matrix == None:
            self.matrix: list[list[Optional[int]]] = [[None for col in range(size)] for row in range(size)]
        else:
            assert matrix is not None
            self.matrix = matrix

    def __getitem__(self, row: int, col: int) -> Optional[int]:
        return self.matrix[row-1][col-1]

    def __setitem__(self, row: int, col: int, value: int):
        self.matrix[row-1][col-1] = value