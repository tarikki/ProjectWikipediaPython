__author__ = 'extradikke'
import mysql.connector

connection = mysql.connector.connect(user='python', password='123', host='127.0.0.1', database='my_schema')
cursor = connection.cursor()
add_name = "INSERT INTO yolo(name, name2) VALUES (%s, %s)"
data_name = ("yolo", "tuubis")
cursor.execute(add_name, data_name)
connection.commit()
cursor.execute("SELECT * FROM my_schema.dikketest")
row = cursor.fetchone()
print(row)

connection.close()

