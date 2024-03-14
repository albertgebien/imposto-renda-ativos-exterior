import pandas as pd


dados = {'ativo': ['A', 'B', 'A', 'B', 'A'],
         'quantidade': [10, 20, 15, 10, 25],
         'valor_pago': [100, 150, 120, 200, 180]}
df = pd.DataFrame(dados)
print(df.head)


preco_medio_por_ativo = df.groupby('ativo').apply(lambda x: (x['quantidade'] * x['valor_pago']).sum() / x['quantidade'].sum(), include_groups=False)

print("Preço médio por ativo:")
print(preco_medio_por_ativo)