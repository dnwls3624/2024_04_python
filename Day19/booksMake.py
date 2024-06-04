import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

sql = """
INSERT INTO BOOKS (id,title,author,published_year,in_stock)
VALUES (1,'개미','베르나르베르베르','1991',True);


"""

cursor.execute(sql)
connection.commit()
connection.close()
