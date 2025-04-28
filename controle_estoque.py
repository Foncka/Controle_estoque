import pandas as pd

estoque = pd.read_excel(r'C:\Users\mathe\Desktop\projetos\Projeto estoque da planilha\Controle_estoque\estoque.xlsx')

print(estoque.head())

print(estoque.columns)  # Localiza a coluna 'Produto'


