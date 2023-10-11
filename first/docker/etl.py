import pandas as pd
from time import time
import logging
import sqlalchemy as db

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

tables = {
    "Users": "BX-Users.csv",
    "Books": "BX-Books.csv",
    "Book_Ratings": "BX-Book-Ratings.csv",
}

# connect to database
engine = db.create_engine("mysql+pymysql://root:root_password@mysql_database:3306/books")
connection = engine.connect()
logging.info("Initializating database:              (remember, warnings are not errors)")
for table in tables:
    a = time()

    # Extract & transform, removing wrong formatted rows, and replacing NaN with 0
    df = pd.read_csv(
        tables[table],
        sep=';',
        encoding="ISO-8859-1",
        error_bad_lines=False,
        warn_bad_lines=False,
    )
    if table == "Books":
        df["Year-Of-Publication"] = pd.to_numeric(df["Year-Of-Publication"], errors='coerce')
        df['Book-Title'] = df['Book-Title'].str.slice(0, 255)
    elif table == "Book_Ratings":
        df['ISBN'] = df['ISBN'].str.slice(0, 13)
    df = df.fillna(0)

    # Load
    df.to_sql(table, connection, if_exists="append", index=False, chunksize=10000)
    logging.info(" {} rows\t {} seconds to insert {},".format(len(df), int(time() - a), table))
