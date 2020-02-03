from error.ExceptionCenter import UserExistedException, UsernamePwdErrorException
from model.blog_user import BlogUser
from config.db_exts import db
from utils.codec_util import generate_password, check_password


def blog_user_login(request):
    data = request.json
    username = data.get("username")
    password = data.get("password")
    user = BlogUser.query.filter_by(username=username).first()
    if user is None:
        raise UsernamePwdErrorException()

    checkPwd = check_password(user.password, password)

    if not checkPwd:
        raise UsernamePwdErrorException()

    return user


def blog_user_signup(request):
    data = request.json
    username = data.get('username')

    user = BlogUser.query.filter_by(username=username).first()
    if user is not None and user.id > 0:
        raise UserExistedException()

    password = data.get('password')
    nickname = data.get('nickname')
    email = data.get('email')
    phone = data.get('phone')
    pwhash = generate_password(password)

    user = BlogUser(username=username, password=pwhash, nickname=nickname, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()
    new_user = BlogUser.query.filter_by(username=username).first()

    return new_user


def blog_users(request):
    users = BlogUser.query.all()
    return users
