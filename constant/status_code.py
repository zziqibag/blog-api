class StatusCode(object):
    params_err_code = 10001
    invalidate_user_err_code = 10002
    not_login_err_code = 10003
    is_login_err_code = 10004
    params_or_cookie_err_code = 10005
    sms_server_err_code = 10006
    sms_err_code = 10007
    token_or_sms_err_code = 10008
    token_err_code = 10009
    user_existed_err_code = 10010
    username_pwd_error_err_code = 10011
    unknown_err_code = 99999

    params_err_msg = "参数错误"
    invalidate_user_err_msg = "非法用户"
    not_login_err_msg = "用户没有登录"
    is_login_err_msg = "用户已经登录"
    params_or_cookie_err_msg = "您已在别处登录"
    sms_server_err_msg = "短信服务异常"
    sms_err_msg = "短信验证码错误"
    token_or_sms_err_msg = "token错误或短信验证码错误"
    token_err_msg = "token错误"
    unknown_err_msg = "未知错误"
    user_existed_err_msg = "用户名已存在"
    username_pwd_error_err_msg = "用户名密码错误"

    code_msg = {
        params_err_code: params_err_msg,
        invalidate_user_err_code: invalidate_user_err_msg,
        not_login_err_code: not_login_err_msg,
        is_login_err_code: is_login_err_msg,
        params_or_cookie_err_code: params_or_cookie_err_msg,
        sms_server_err_code: sms_server_err_msg,
        sms_err_code: sms_err_msg,
        token_or_sms_err_code: token_or_sms_err_msg,
        token_err_code: token_err_msg,
        unknown_err_code: unknown_err_msg,
        user_existed_err_code: user_existed_err_msg,
        username_pwd_error_err_code: username_pwd_error_err_msg,
    }

    unauthorized_code = [
        invalidate_user_err_code,
        not_login_err_code,
        is_login_err_code,
        params_or_cookie_err_code,
        sms_server_err_code,
        sms_err_code,
        token_or_sms_err_code,
        token_err_code,
        user_existed_err_code,
        username_pwd_error_err_code,
    ]
