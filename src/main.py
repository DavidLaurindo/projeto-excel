import pandas as pd

file_path = r'C:\Users\davis\Documents\Projetos\projeto-excel\data\Produtos.xlsx'

dataframe = pd.read_excel(file_path)

print(dataframe)