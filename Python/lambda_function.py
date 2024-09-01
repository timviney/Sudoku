import json
import sudoku_solver
from sudoku import Sudoku

def lambda_handler(event, context):
    # Parse the request body
    body = json.loads(event['body'])
    
    method = body.get('method', [])

    if method == 'solveMatrix': solve_matrix(body)
    else:
        return {
            'statusCode': 405,
            'body': json.dumps('Method Not Allowed')
        }

def solve_matrix(body):
    matrix = body.get('matrix', [[]])

    sudoku = Sudoku(matrix)
    sudoku_solver.solve(sudoku)
    
    return {
        'statusCode': 200,
        'body': json.dumps(sudoku.matrix)
    }

