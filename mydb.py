import MySQLdb
from decouple import config

# Test connection

dataBase = MySQLdb.connect(
    host = config('db_HOST'),
    user = config('db_USER'),
    password = config('db_PASSWORD'),
)
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("DB Created")

cursorObject.close()
dataBase.close()