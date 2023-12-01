import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv("./questions.csv")

# Connect to (create) database.
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    "csv_category": "CharField",
    "csv_question": "CharField",
    "csv_code": "IntegerField", 
}
df.to_sql(name='polls_csvdata', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")
conn.close()