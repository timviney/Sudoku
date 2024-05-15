import highspy # type: ignore
from highspy import kHighsInf as inf
from highs import highs_var
from sudoku import Sudoku
from sudokuVariables import SudokuVariables
import numpy as np
from typing import cast

def solve(sudoku: Sudoku):
    problem = highspy.Highs
    size: int = sudoku.size
    variables: SudokuVariables = SudokuVariables(sudoku.size)
    
    # Add Variables.
    # Here, there is only one type, f(row, col, val), for r,c,v 1-9.
    # This in the binary value that defines whether entry (row, col) = value or not.

    add_variables(problem, size, variables)

    # One value per entry
    for row in range(1, size+1):
        for col in range(1, size+1):
            variables_in_constraint: list[highs_var] = [cast(highs_var, variables[row, col, val]) for val in range(1, size+1)]
            multipliers: list[float] = [1.0 for m in range(0, size)]
            add_constraint(problem, variables_in_constraint, multipliers, 1, 1)
    
    # Each value once per col
    for row in range(1, size+1):
        for val in range(1, size+1):
            variables_in_constraint2: list[highs_var] = [cast(highs_var, variables[row, col, val]) for col in range(1, size+1)]
            multipliers2: list[float] = [1.0 for m in range(0, size)]
            add_constraint(problem, variables_in_constraint2, multipliers2, 1, 1)

    # Each value once per row
    for val in range(1, size+1):
        for col in range(1, size+1):
            variables_in_constraint3: list[highs_var] = [cast(highs_var, variables[row, col, val]) for row in range(1, size+1)]
            multipliers3: list[float] = [1.0 for m in range(0, size)]
            add_constraint(problem, variables_in_constraint3, multipliers3, 1, 1)

    problem.run()

def add_variables(problem: highspy.Highs, size: int, variables: SudokuVariables):
    for row in range(1, size+1):
        for col in range(1, size+1):
            for val in range(1, size+1):
                add_variable(problem, variables, row, col, val)

def add_variable(problem: highspy.Highs, variables: SudokuVariables, row, col, val):
    variable = problem.addBinary(0, f(row, col, val))
    variables.add(variable, row, col, val)

def f(row: int, col: int, val: int) -> str:
        # This returns the string representation for HiGHS to recognize our variables.
        return f"f({row},{col},{val})"

def add_constraint(problem: highspy.Highs, variables: list[highs_var],
                    multipliers: list[float], min: float = -inf, max: float = inf):
    num_nz = variables.count
    index = np.array([var.index for var in variables])
    value = np.array([multipliers])
    problem.addRow(min, max, num_nz, index, value)