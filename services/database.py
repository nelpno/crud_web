import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='171261',
    database='crud_python',
)

cursor = conexao.cursor()