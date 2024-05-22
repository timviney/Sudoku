from typing import Optional, Tuple

from ortools.linear_solver.python import model_builder
from ortools.linear_solver.python.model_builder import Model, Solver, Variable

class SudokuVariables:
    def __init__(self, size: int):
        self.size: int = size
        self.variables: list[list[list[Optional[Variable]]]] = [[[None for val in range(size)] for col in range(size)] for row in range(size)]

    def add(self, var, row: int, col: int, val: int):
        self.variables[row-1][col-1][val-1] = var

    def __getitem__(self, rowColVal: Tuple[int, int, int]) -> Optional[Variable]:
        row, col, val = rowColVal
        return self.variables[row-1][col-1][val-1]
                    