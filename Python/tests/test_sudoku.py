from Python.sudoku import Sudoku
from tests.helpers import problems
import solver

def test_given_solved_grid_when_solver_runs_then_returns_same_grid():
        problem1: Sudoku = problems.Problem1
        solver.solve(problem1)
        assert problem1 == problems.Answer1

