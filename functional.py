import pandas as pd

def carregar_csv_e_filtrar(arquivo_csv, estado):
    """
    Carregar o arquivo CDV em um DataFrame
    """
    df = pd.read_csv(arquivo_csv)

    """
    Verificar e remover célular vazias
    """
    df = df.dropna()

    """
    Filtrar as linhas pela coluna do estado
    """
    df_filtrado = df[df['Estado'] == estado]

    return df_filtrado


# Exemplo de uso
arquivo_csv = './data/vendas.csv'
estado = 'SP'

dados_filtrados = carregar_csv_e_filtrar(arquivo_csv, estado)
print(dados_filtrados)

