import pandas as pd

# Caminho para o arquivo de texto
caminho_arquivo_txt = 'arquivo.txt'

# Tentar ler o arquivo sem tratar erros de tokenização
try:
    df = pd.read_csv(caminho_arquivo_txt, sep='\t', encoding='utf-16')
except pd.errors.ParserError:
    print("Erro na leitura do arquivo. Ignorando possíveis erros de tokenização.")

    # Abrir o arquivo e ler linha por linha
    with open(caminho_arquivo_txt, 'r', encoding='utf-16') as file:
        lines = file.readlines()

    # Criar DataFrame a partir das linhas válidas
    df = pd.DataFrame([line.split('\t') for line in lines if len(line.split('\t')) == 5])

# Caminho para salvar o arquivo Excel
caminho_arquivo_excel = 'arquivo.xlsx'

# Salvar o DataFrame em um arquivo Excel
df.to_excel(caminho_arquivo_excel, index=False)