import sqlite3

connection = sqlite3.connect('RentCar.db')
cursor = connection.cursor()


sql = """
CREATE TABLE CARS(
    carNum INTEGER PRIMARY KEY,
    carName TEXT,
    colar TEXT,
    company TEXT)
"""

sql = """
CREATE TABLE MEMBERS(
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone TEXT)
"""

sql = """
CREATE TABLE RESERVATION(
    id INTEGER PRIMARY KEY,
    carNumber TEXT,
    startDate TEXT)


"""
cursor.execute(sql)
connection.commit()
connection.close()




