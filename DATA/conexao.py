import mysql.connector

def get_conexao():
    conn = mysql.connector.connect(host="localhost", port=3306, user="root", password="root", database="db_feedback")
    return conn

def close_conexao(conn, cursor):
    cursor.close()
    conn.close()