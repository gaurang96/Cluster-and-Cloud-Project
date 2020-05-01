#!/bin/bash

echo "== Add node to cluster =="
curl -X POST -H "Content-Type: application/json" http://user:123@172.26.132.80:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "user", "password":"123", "port": 5984, "node_count": "2", "remote_node": "172.26.131.46", "remote_current_user": "user", "remote_current_password": "123" }'
curl -X POST -H "Content-Type: application/json" http://user:123@172.26.132.80:5984/_cluster_setup -d '{"action": "add_node", "host":"172.26.131.46", "port": 5984, "username": "user", "password":"123"}'
