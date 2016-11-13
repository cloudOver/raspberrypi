#!/bin/bash
OSPF_TOKEN=`head -c 100 /dev/urandom | sha1sum | cut -f 1 -d ' '`
QUAGGA_PASSWORD=`head -c 100 /dev/urandom | sha1sum | cut -f 1 -d ' '`
INSTALLATION_ID=`head -c 100 /dev/urandom | sha1sum | cut -f 1 -d ' '`
AUTH_TOKEN=`head -c 100 /dev/urandom | sha1sum | cut -f 1 -d ' '`
SECRET_KEY=`head -c 100 /dev/urandom | sha1sum | cut -f 1 -d ' '`
MYSQL_DB_PASSWORD="change_me"
MYSQL_LOG_PASSWORD="change_me"
