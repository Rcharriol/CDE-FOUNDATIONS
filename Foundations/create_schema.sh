#!/bin/bash
docker exec -i user_mysql_1 mysql -uroot -proot_password mysql < Docker/sql/create_schema.sql
