from werkzeug.security import generate_password_hash, check_password_hash


def generate_password(password):
    enc_pwd = generate_password_hash(password)
    return enc_pwd


def check_password(pwhash, password):
    return check_password_hash(pwhash, password)
