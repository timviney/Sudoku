import json
import traceback

class JsonResult:
    def __init__(self, success: bool, result):
        self.Success: bool = success
        self.Result = result if success else None
        self.Error = None if success else result

    def AsJson(self):
        return {
            'statusCode': 200 if self.Success else 400,
            'success': self.Success,
            'result': self.Result,
            'error': self._get_detailed_error_message(self.Error) if self.Error else None
        }

    def _get_detailed_error_message(self, error):
        if isinstance(error, Exception):
            error_message = f"{type(error).__name__}: {str(error)}"
            stack_trace = ''.join(traceback.format_exception(None, error, error.__traceback__))
            return f"{error_message}\nStack Trace:\n{stack_trace}"
        return str(error)
