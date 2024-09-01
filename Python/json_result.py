import json

class JsonResult:
    def __init__(self, success: bool, result):
        self.Success: bool = success
        self.Result = result if success else None
        self.Error = None if success else result
    def AsJson(self):
        return {
            'statusCode': 200 if self.Success else 400,
            'success': self.Success,
            'result': json.dumps(self.Result),
            'error': str(self.Error)
        }
    