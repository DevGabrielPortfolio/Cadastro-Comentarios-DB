import mysql.connector

conn = mysql.connector.connect(host="localhost", port=3306, user="root", password="root", database="db_feedback")

cursor = conn.cursor()

print (conn)