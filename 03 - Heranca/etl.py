import pandas as pd

class ETLProcess:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados

    def extrair_dados(self):
        raise NotImplementedError("Método extrair_dados deve ser implementado nas classes filhas.")

    def transformar_dados(self, dados):
        raise NotImplementedError("Método transformar_dados deve ser implementado nas classes filhas.")

    def carregar_dados(self, dados_transformados: str):
        raise NotImplementedError("Método carregar_dados deve ser implementado nas classes filhas.")

    def executar_etl(self):
        dados_extraidos = self.extrair_dados()
        dados_transformados = self.transformar_dados(dados_extraidos)
        self.carregar_dados(dados_transformados)


class ETLCSV(ETLProcess):
    def extrair_dados(self):
        return pd.read_csv(self.fonte_dados)

    def transformar_dados(self, dados):
        """
        Exemplo de transformação para UpperCase
        """
        return dados.map(lambda x: x.upper() if isinstance(x, str) else x)

    def carregar_dados(self, dados_transformados):
        """
        Salvando os dados transformados em um arquivo CSV
        """
        caminho_output = './data/dados_transformados.csv'
        dados_transformados.to_csv(caminho_output, index=False)
        print(f"Os dados transformados foram salvos em: {caminho_output}")        


# Exemplo de uso
if __name__ == "__main__":
    fonte_csv = './data/vendas.csv'  
    etl_csv = ETLCSV(fonte_csv)
    etl_csv.executar_etl()