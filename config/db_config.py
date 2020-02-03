from config.env_config import EnvConfig

if EnvConfig.run_env <= EnvConfig.ENV_TEST:
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = 'egcc123456'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'zq_blog'
else:
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'zqdb'
    PASSWORD = 'Zqdb=123'
    HOST = '127.0.0.1'
    PORT = '16608'
    DATABASE = 'zq_blog'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 5
