from constant.status_code import StatusCode
from error.ApiException import ApiException


class UserExistedException(ApiException):
    code = 200
    msg = StatusCode.code_msg[StatusCode.user_existed_err_code]
    error_code = StatusCode.user_existed_err_code


class UsernamePwdErrorException(ApiException):
    code = 200
    msg = StatusCode.code_msg[StatusCode.username_pwd_error_err_code]
    error_code = StatusCode.username_pwd_error_err_code
