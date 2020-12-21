import sqlite3
# from sqlite3 import sql

# Comandos básicos para interagir com o banco de dados
class Banco():
    database = 'pessoas.db'
    conn = None
    cursor = None
    connected = False

    # Conectar ao banco
    def conectar_banco(self):
        Banco.conn = sqlite3.connect(Banco.database)
        Banco.cursor = Banco.conn.cursor()
        Banco.connected = True

    # Desconectar
    def desconectar_banco(self):
        Banco.conn.close()
        Banco.connected = False
    
    # Executar comando no banco
    def execute_comand(self, sql, params=None):
        if Banco.connected == True:
            if params == None:
                Banco.cursor.execute(sql)
            else:
                Banco.cursor.execute(sql, params)
            return (True,)
        else:
            return str(False)
        
    # Efetivar alterações
    def persist(self):
        if Banco.connected == True:
            Banco.conn.commit()
            return True
        else:
            return False

def InitDB():
    alt = Banco()
    alt.conectar_banco()
    alt.execute_comand("""CREATE TABLE IF NOT EXISTS pessoas_dados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            tel INTEGER
        )""")
    alt.persist()
    alt.desconectar_banco()

InitDB()

def view():
    alt = Banco()
    alt.conectar_banco()
    alt.execute_comand('SELECT * FROM pessoas')