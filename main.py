import pandas as pd

df = pd.read_excel(
    'pedido.xlsx',
    usecols= ["ID_PRODUTO", "QUANTIDADE"]).set_index("ID_PRODUTO")
print(df)