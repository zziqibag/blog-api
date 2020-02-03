from sqlalchemy import text

from model.base_model import BaseModel
from config.db_exts import db


def blog_show():
    return ['id', 'username', 'nickname', 'email', 'phone']


class BlogUser(BaseModel):
    # 设置表名
    __tablename__ = 'blog_user'
    # 设置字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))

    def __str__(self):
        return "BlogUser:{}".format(self.username)
