#install mysql on your computer
#pip install mysql
#pip install mysql-connector-python

import mysql.connector

#the database connection
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'keith'
)

#preparing a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE primecore")

print("DONE!!")

# 