# CDE-FOUNDATIONS

### 1: Pick a dataset
Downlad and unzip with
```sh
curl http://www2.informatik.uni-freiburg.de/\~cziegler/BX/BX-CSV-Dump.zip --output csv_dump.zip
unzip csv_dump.zip
```
A book dataset, with 3 tables. Books, users and reviews.
You can answer which books are better based on user reviews, to buy and sell them.

### 2: Create a container with database.
```
docker run --name=user_mysql_1 --env="MYSQL_ROOT_PASSWORD=root_password" -p 3306:3306 -d mysql:latest
```

### 3: Bash script that creates schema.
```sh
./create_schema.sh
```

### 4: Python ETL
```sh
# Maybe you'll want to use a virtualenv
pip3 install sqlalchemy pandas
python3 Docker/etl.py
```
### 5:
    First we check
    select avg(book_rating) as average from book_ratings;

    select
        isbn,
        avg(book_rating) as average,
        count(*) as count
    from book_ratings
    group by isbn
    order by avg(book_rating) DESC
    having avg(book_rating) > 3.5
    limit 5;
