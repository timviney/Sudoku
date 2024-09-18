from flask import Flask, request
from lambda_function import lambda_handler

app = Flask(__name__)

@app.route('/sudoku', methods=['POST'])
def sudoku_solver():
    try:
        event = request.get_json()
        result = lambda_handler(event, None)
        return result
    except Exception as e:
        return {"success": False, "message": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
