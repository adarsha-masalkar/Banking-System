import mysql.connector
import datetime
import random


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='BankingData'
)
cursor = db.cursor()

# data = """CREATE TABLE Users (
#                     id int PRIMARY KEY AUTO_INCREMENT,
#                     Name varchar(100) NOT NULL,
#                     Balance DOUBLE NOT NULL)"""
#
# data = """CREATE TABLE Transactions (
#                     id int NOT NULL,
#                     Sender varchar(100) NOT NULL,
#                     Receiver varchar(100) NOT NULL,
#                     Amount DOUBLE NOT NULL)"""

# db.commit()
