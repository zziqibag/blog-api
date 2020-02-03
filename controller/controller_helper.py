from model.base_model import BaseModel


def make_resp(errcode=0, errmsg='OK', data=None):
    """构建返回的字典"""
    if not data:
        data = {}
    if (errcode != 0) and (errmsg == "OK"):
        errmsg = "Error"

    resp = {"errcode": errcode, "errmsg": errmsg, "data": data}
    return resp

