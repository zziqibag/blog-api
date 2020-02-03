#!/bin/bash


if [ ! -d /data/logs/blog-api ];then
    sudo mkdir -p /data/logs/blog-api
    sudo chmod -R 777 /data/logs/blog-api
fi

export ENV=prod

ps aux | grep 'main:app' | awk '{print $2}' | xargs kill

#nohup /opt/anaconda3/envs/blog-api/bin/gunicorn -c config/gunicorn.conf.py main:app >nohup.out 2>&1 &
# for supervisorctl
/opt/anaconda3/envs/blog-api/bin/gunicorn -c config/gunicorn.conf.py main:app