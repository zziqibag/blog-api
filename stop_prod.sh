#!/bin/bash

ps aux | grep 'main:app' | awk '{print $2}' | xargs kill

