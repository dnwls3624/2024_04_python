import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

sql = """
CREATE TABLE BOOKS(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    published_year TEXT,
    in_stock BOOLEAN

)


"""

cursor.execute(sql)
connection.commit()
connection.close()
