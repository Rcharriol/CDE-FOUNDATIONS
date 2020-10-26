#!/bin/bash
docker exec -i mysql_database mysql -uroot -proot_password mysql < sql/create_schema.sql
