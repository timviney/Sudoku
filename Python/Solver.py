from sudoku import Sudoku
from sudokuVariables import SudokuVariables
import numpy as np
from typing import cast
from ortools.linear_solver.python import model_builder
from ortools.linear_solver.python.model_builder import Model, Solver, Variable

def solve(sudoku: Sudoku):

    model: Model = Model()
    size: int = sudoku.size
    variables: SudokuVariables = SudokuVariables(sudoku.size)
    
    # Add Variables.
    # Here, there is only one type, f(row, col, val), for r,c,v 1-9.
    # This in the binary value that defines whether entry (row, col) = value or not.

    add_variables(model, size, variables)

    # One value per entry
    for row in range(1, size+1):
        for col in range(1, size+1):
            variables_in_constraint: list[Variable] = [variables[row, col, val] for val in range(1, size+1)]
            multipliers: list[float] = [1.0 for m in range(0, size)]
            add_constraint(model, variables_in_constraint, multipliers, 1, 1)
    
    # Each value once per col
    for row in range(1, size+1):
        for val in range(1, size+1):
            variables_in_constraint2: list[Variable] = [variables[row, col, val] for col in range(1, size+1)]
            multipliers2: list[float] = [1.0 for m in range(0, size)]
            add_constraint(model, variables_in_constraint2, multipliers2, 1, 1)

    # Each value once per row
    for val in range(1, size+1):
        for col in range(1, size+1):
            variables_in_constraint3: list[Variable] = [variables[row, col, val] for row in range(1, size+1)]
            multipliers3: list[float] = [1.0 for m in range(0, size)]
            add_constraint(model, variables_in_constraint3, multipliers3, 1, 1)

    # Each value once per box
    boxLength: int = int(np.sqrt(size))
    for val in range(1, size+1):
        for rowAdder in range(0, size, boxLength):
            for colAdder in range(0, size, boxLength):
                variables_in_constraint4: list[Variable] = [variables[rowAdder + row, colAdder + col, val] for row in range(1, boxLength+1) for col in range(1, boxLength+1)]
                multipliers4: list[float] = [1.0 for m in range(0, size)]
                add_constraint(model, variables_in_constraint4, multipliers4, 1, 1)

    solver: Solver = Solver("HiGHS")
    solver.solve(model)
    
    for row in range(1, size+1):
        for col in range(1, size+1):
            for val in range(1, size+1):
                variable = variables[row, col, val]
                binVal: np.double = solver.value(cast(Variable, variable))
                if (binVal == 1):
                    sudoku[row, col] = val
    
def add_variables(model: Model, size: int, variables: SudokuVariables):
    for row in range(1, size+1):
        for col in range(1, size+1):
            for val in range(1, size+1):
                add_variable(model, variables, row, col, val)

def add_variable(model: Model, variables: SudokuVariables, row, col, val):
    variable = model.new_bool_var(f(row, col, val))
    variables.add(variable, row, col, val)

def f(row: int, col: int, val: int) -> str:
        # This returns the string representation to recognize our variables.
        return f"f({row},{col},{val})"

def add_constraint(model: Model, variables: list[Variable],
                    multipliers: list[float], min: float = -999999999, max: float = 999999999):

    model.add(model_builder.LinearExpr.weighted_sum(variables, multipliers) <= max)
    model.add(model_builder.LinearExpr.weighted_sum(variables, multipliers) >= min) # type: ignore
