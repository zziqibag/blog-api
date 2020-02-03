from datetime import datetime as cdatetime

from model.base_model import BaseModel
from utils.time_util import format_datetime


def queryToDict(models, show=None):
    if isinstance(models, list):
        if isinstance(models[0], BaseModel):
            lst = []
            for model in models:
                gen = model.model_to_dict(show)
                dit = dict((g[0], g[1]) for g in gen)
                lst.append(dit)
            return lst
        else:
            res = result_to_dict(models)
            return res
    else:
        if isinstance(models, BaseModel):
            gen = models.model_to_dict(show)
            dit = dict((g[0], g[1]) for g in gen)
            return dit
        else:
            res = dict(zip(models.keys(), models))
            find_datetime(res)
            return res


# 当结果为result对象列表时，result有key()方法
def result_to_dict(results):
    res = [dict(zip(r.keys(), r)) for r in results]
    # 这里r为一个字典，对象传递直接改变字典属性
    for r in res:
        find_datetime(r)
    return res


def find_datetime(value):
    for v in value:
        if isinstance(value[v], cdatetime):
            value[v] = format_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改
