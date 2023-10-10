#!/bin/sh

USER_ID=$(id -u) GROUP_ID=$(id -g) docker-compose up rs-calc-api-app-server rs-calc-api-proxy-server --build