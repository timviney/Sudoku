import json
from json_result import JsonResult
import sudoku_solver
from sudoku import Sudoku

def lambda_handler(event, context):
    result = run(event)
    return result.AsJson()
    
def run(event) -> JsonResult:
    try:        
        method = event['method']
        if method == 'solveMatrix': return solve_matrix(event)
        # Can fill in more methods here
        else:
            return JsonResult(False, 'Method Not Allowed')
        
    except Exception as e:
        return JsonResult(False, e)

def solve_matrix(event) -> JsonResult:
    matrix = event.get('matrix', [[]])

    sudoku = Sudoku(matrix)
    sudoku_solver.solve(sudoku)
    
    return JsonResult(True, sudoku.to_dict())

