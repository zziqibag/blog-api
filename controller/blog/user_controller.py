from flask import request, jsonify

from controller.controller_helper import make_resp
from error.ApiException import ApiException
from main import app
from model.blog_user import blog_show
from service.blog.user_service import blog_user_login, blog_users, blog_user_signup
from utils.db_util import queryToDict


@app.route('/api/blog/login', methods=['GET', 'POST'])
def api_blog_login():
    try:
        user = blog_user_login(request)
    except ApiException as e:
        return jsonify(make_resp(e.error_code, e.msg))

    data = queryToDict(user, blog_show())
    resp = make_resp(data=data)
    return jsonify(resp)


@app.route('/api/blog/signup', methods=['POST'])
def api_blog_signup():
    try:
        user = blog_user_signup(request)
    except ApiException as e:
        return jsonify(make_resp(e.error_code, e.msg))

    data = queryToDict(user, blog_show())
    resp = make_resp(data=data)
    return jsonify(resp)


@app.route('/api/blog/users', methods=['GET'])
def api_blog_users():
    users = blog_users(request)
    data = queryToDict(users)
    resp = make_resp(data=data)
    return jsonify(resp)


def serialize(model):
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)
