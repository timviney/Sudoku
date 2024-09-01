import pytest
from sudoku import Sudoku
from tests.helpers import problems
import sudoku_solver

def test_given_incomplete_grid_when_solver_runs_then_returns_correct_solution():
        problem1: Sudoku = problems.Problem1()
        sudoku_solver.solve(problem1)
        assert problem1 == problems.Answer1()

def test_given_solved_grid_when_solver_runs_then_returns_same_grid():
        problem1: Sudoku = problems.Answer1()
        sudoku_solver.solve(problem1)
        assert problem1 == problems.Answer1()
        
def test_given_invalid_grid_when_solver_runs_then_raises_error():
        problem1: Sudoku = problems.InsolvableProblem1()
        with pytest.raises(sudoku_solver.InvalidSudokuError, match="Invalid Sudoku grid"):
                sudoku_solver.solve(problem1)