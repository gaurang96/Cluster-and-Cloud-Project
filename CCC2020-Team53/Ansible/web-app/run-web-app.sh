#!/bin/bash

. ./openrc.sh; ansible-playbook -i hosts -u ubuntu --key-file=~/.ssh/test1.pem run-web-app.yaml