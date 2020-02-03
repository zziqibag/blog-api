# blog-api

## 配置
conda env export -n blog-api -f env.yml --no-builds


## gunicorn启动
gunicorn -c config/gunicorn.conf.py main:app
