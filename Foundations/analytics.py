import pandas as pd
import logging
import sqlalchemy as db

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

tables = {
    "Users": "BX-Users.csv",
    "Books": "BX-Books.csv",
    "Book_Ratings": "BX-Book-Ratings.csv",
}

# connect to database
engine = db.create_engine("mysql+pymysql://root:root_password@localhost:3306/books")
connection = engine.connect()

avg = connection.execute("""
    select
        avg(`Book-Rating`)
    from Book_Ratings
    """)

avg = avg.first()[0]
logging.info("The average rating of a book is {}".format(avg))

logging.info("\nGiven that the default value is 0")

r_avg = connection.execute("""
    select
        avg(`Book-Rating`)
    from Book_Ratings
    where `Book-Rating` > 0
    """)

r_avg = r_avg.first()[0]
logging.info("The average rating of a rated book is {}".format(r_avg))

good_books = connection.execute("""
    select
        B.ISBN,
        avg(R.`Book-Rating`),
        B.`Book-Title`
    from Book_Ratings R
    inner join Books B
    on B.ISBN = R.ISBN
    group by B.ISBN, B.`Book-Title`
    having avg(R.`Book-Rating`) > {}
    order by avg(R.`Book-Rating`) * count(*) DESC
    limit 10""".format(r_avg))

logging.info("\nWe dont have much money to start this business, thats why we picked the best 10 books")
logging.info("based on rate and fame:")
for book in good_books:
    logging.info("Isbn:{}\t Rate:{}\t{}".format(*book))

logging.info("\nBooks that sell are not always good, and we are a business after all")

famous_books = connection.execute("""
    select
        B.ISBN,
        avg(R.`Book-Rating`),
        count(*),
        B.`Book-Title`
    from Book_Ratings R
    inner join Books B
    on B.ISBN = R.ISBN
    group by B.ISBN, B.`Book-Title`
    order by count(*) DESC
    limit 10""".format(r_avg))

logging.info("So we thougt a good idea; Pick the most rated books, wether is a good or a bad rate")
logging.info("because those are famous:")
for book in famous_books:
    logging.info("Isbn:{}\t Rate:{} fame:{}\t{}".format(*book))

logging.info("\nOk, watching that data, i dont want to buy crap books either")

famous_books = connection.execute("""
    select
        B.ISBN,
        avg(R.`Book-Rating`),
        count(*),
        B.`Book-Title`
    from Book_Ratings R
    inner join Books B
    on B.ISBN = R.ISBN
    group by B.ISBN, B.`Book-Title`
    having avg(R.`Book-Rating`) > {}
    order by count(*) DESC
    limit 10""".format(float(avg)))

logging.info("the most famous which arent absolute crap:")
for book in famous_books:
    logging.info("Isbn:{}\t Rate:{} fame:{}\t{}".format(*book))
