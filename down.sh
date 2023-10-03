#!/bin/sh

USER_ID=$(id -u) GROUP_ID=$(id -g) docker-compose down
docker rm rs-calc-api-app-server
docker rm rs-calc-api-proxy-server
docker rm rs-calc-front-end