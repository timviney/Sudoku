from typing import Optional, Tuple
from highs import highs_var

class SudokuVariables:
    def __init__(self, size: int):
        self.size: int = size
        self.variables: list[list[list[Optional[highs_var]]]] = [[[None for val in range(size)] for col in range(size)] for row in range(size)]

    def add(self, var, row: int, col: int, val: int):
        self.variables[row][col][val] = var

    def __getitem__(self, rowColVal: Tuple[int, int, int]) -> Optional[highs_var]:
        row, col, val = rowColVal
        return self.variables[row-1][col-1][val-1]
