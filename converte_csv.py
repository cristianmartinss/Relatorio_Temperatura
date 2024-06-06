import pandas as pd
import logging

logging.basicConfig(filename='logfile.log', level=logging.INFO)

def converter(arquivo):
    try:
        df = pd.read_csv(arquivo, sep='\t', encoding='utf-16')
    except pd.errors.ParserError as e:
        print('Erro na leitura da linha.')
        logging.error(str(e))
        with open(arquivo, 'r', encoding='utf-16') as file:
            lines = file.readlines()
        df = pd.DataFrame([line.split('\t') for line in lines if len(line.split('\t')) == 5])

    caminho_arquivo_excel = arquivo.replace('.txt', '.xlsx')
    df.to_excel(caminho_arquivo_excel, index=False)

