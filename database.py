import sqlite3
from sqlite3 import sql

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
    def execute(self, sql, params=None):
        if Banco.connected == True:
            if params == None:
                Banco.cursor.execute(sql)
            else:
                Banco.cursor.execute(sql, params)
            return True
        else:
            return False
        
    # Efetivar alterações
    def persist(self):
        if Banco.connected == True:
            Banco.conn.commit()
            return True
        else:
            return False