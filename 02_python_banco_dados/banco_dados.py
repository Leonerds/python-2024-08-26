import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="127.0.0.1",  # 127.0.0.1 (localhost) na nossa máquina, na máquina do DEV
        port=3306,
        user="root",
        password="admin",
        database="dev_motors"
    )
    print("Conectado com sucesso")  # Coloquei esta linha aqui
    return conexao
