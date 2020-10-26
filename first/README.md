# CDE-FOUNDATIONS

### 1: Pick a dataset
Downlad and unzip with
```sh
curl http://www2.informatik.uni-freiburg.de/\~cziegler/BX/BX-CSV-Dump.zip --output docker/csv_dump.zip
cd docker
unzip csv_dump.zip
cd ..
```
A book dataset, with 3 tables. Books, users and reviews.
You can answer which books are better based on user reviews, to buy and sell them.

### 2: Create a container with the database.
```
docker network create mysql
docker run --name=mysql_database --network mysql --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql:latest
```

### 3: Bash script that creates schema.
```sh
./create_schema.sh
```
I had issues with this, because if you run it too fast, when the docker has just begun, it migth not work.
But it does work, you just have to wait a few seconds to execute it.

### 4: Python ETL using docker
```sh
docker build -t python_queries ./docker --network mysql
```

### 5: Python queries, using docker
```sh
docker run --network mysql python_queries
```
