import pandas as pd

class ProcessadorCSV:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.arquivo_csv)

    def remover_celular_vazias(self):
        self.df = self.df.dropna()    

    def filtrar_estado(self, estado):
        self.df = self.df[self.df['Estado'] == estado]

    def processar(self, estado):
        """
        Carregar CSV, remover celular vazias e filtrar por estado
        """    
        self.carregar_csv()
        self.remover_celular_vazias()
        self.filtrar_estado( estado)

        return self.df
    
# Exemplo de uso

arquivo_csv = './data/vendas.csv'
estado = 'RJ'


# Instanciando o objeto

processador = ProcessadorCSV(arquivo_csv)
processador_filtrado = processador.processar(estado)
print(processador_filtrado)


