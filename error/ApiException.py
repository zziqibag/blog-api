from werkzeug.exceptions import HTTPException


class ApiException(HTTPException):
    code = 500
    msg = '服务器异常'
    error_code = 1000

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(ApiException, self).__init__(msg, None)
