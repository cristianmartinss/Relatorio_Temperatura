import pandas as pd
import mysql.connector
from datetime import datetime, timedelta, date
import warnings
from io import StringIO
warnings.filterwarnings('ignore')


def conectar_banco():
    config = {
        'host': '',
        'user': '',
        'password': '',
        'database': '',
        'port': '',
    }
    conexao = mysql.connector.connect(**config)
    return conexao

def extrair_excel(xls_path):
    xls_path=xls_path
    conexao = conectar_banco()
    cursor = conexao.cursor()
    campos = []
    df =  pd.read_excel(xls_path)
    df = pd.DataFrame(df)
    for indice, linha in df.iterrows():
        query = f"INSERT INTO teste (var, date, temp) VALUES ('{linha[0]}', '{linha[1]}', '{linha[2]}')"
        print(query)
        try:
            cursor.execute(query)
            conexao.commit()
            print("Inserção bem-sucedida!")
        except Exception as e:
            print(f"Erro ao inserir no banco de dados: {e}")
            conexao.rollback()

