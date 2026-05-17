import pandas as pd

# Recebe os DataFrames de pedidos e pallets inteiros, calcula a quantidade de bases necessárias e salva o resultado em um arquivo Excel
def calcular_bases(df_pedido, df_inteiros):
    qtd_bases = df_pedido['QUANTIDADE'] % df_inteiros['QTD_INTEIRO']

    df_bases = pd.DataFrame({
        'NOME_PRODUTO': df_pedido['NOME_PRODUTO'],
        'QUANTIDADE_BASES': qtd_bases
    })

    df_filtrado = df_bases[df_bases['QUANTIDADE_BASES'] > 0]

    df_final = df_filtrado.to_excel('bases.xlsx')
    print("Arquivo 'bases.xlsx' criado com sucesso!")
    return df_final