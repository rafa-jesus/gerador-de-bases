import pandas as pd
from funcoes import calcular_bases

# Carrega e filtra os dados do arquivo Excel de pedidos
df_pedido = pd.read_excel(
    'pedido.xlsx',
    usecols= ["ID_PRODUTO", "NOME_PRODUTO", "QUANTIDADE"]
    ).set_index("ID_PRODUTO")

# Carrega e filtra os dados do arquivo Excel de pallets inteiros
df_inteiros = pd.read_excel(
    'QTD_INTEIRO.xlsx',
    usecols= ["ID_PRODUTO", "NOME_PRODUTO", "QTD_INTEIRO"]
    ).set_index("ID_PRODUTO")

calcular_bases(df_pedido, df_inteiros)