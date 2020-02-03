import os


class EnvConfig(object):
    ENV_PROD = 2
    ENV_TEST = 1
    ENV_DEV = 0

    env_conf = os.environ.get('ENV', None)
    print('env=%s' % env_conf)

    if env_conf == 'prod':
        run_env = ENV_PROD
    elif env_conf == 'test':
        run_env = ENV_TEST
    else:
        run_env = ENV_DEV
