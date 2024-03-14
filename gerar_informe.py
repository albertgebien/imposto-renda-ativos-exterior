import pandas as pd
from datetime import datetime
from dolar import Dolar

dicionario_dolar_venda = {}

df = pd.read_excel('dados/transacoes.xlsx')
df['Negociação'] = df['Negociação'].dt.strftime('%Y-%m-%d')

for indice, linha in df.iterrows():
    
    data_str = linha['Negociação']
    
    dolar_venda = 0

    # valida se há chave no dicionario
    if dicionario_dolar_venda.get(data_str) is None:
        data_obj = datetime.strptime(data_str, '%Y-%m-%d').date()  
        cotacao = Dolar(data=data_obj)
        dicionario_dolar_venda[data_str] = cotacao.dolar_venda_ptax()
        dolar_venda = cotacao.dolar_venda_ptax()
        df.at[indice, 'dolar_venda'] = cotacao.dolar_venda_ptax()
    else:
        df.at[indice, 'dolar_venda'] = dicionario_dolar_venda.get(data_str)

    df['Preço reais'] = df['Preço'] * df['dolar_venda']
    df['Preço total reais'] = df['Preço reais'] * df['Quantidade']


preco_total_por_ativo = df.groupby('Ativo').apply(lambda x: (x['Preço total reais']).sum(), include_groups=False)
quantidade_por_ativo = df.groupby('Ativo').apply(lambda x: (x['Quantidade']).sum(), include_groups=False)
preco_total_dolares = df.groupby('Ativo').apply(lambda x: (x['Quantidade'] * x['Preço']).sum(), include_groups=False)

# Inicializa um DataFrame vazio com as colunas desejadas
df2 = pd.DataFrame(columns=['Ativo', 'Descrição','Valor em Reais (R$)'])

ativos = df.groupby('Ativo')
chaves = ativos.groups.keys()
for key in chaves:
    ativo = f'{key}'
    desc =  ativo + ' - ' + str(quantidade_por_ativo[ativo]) + 'AÇÕES COM CUSTO TOTAL DE $' +str(preco_total_dolares[ativo])+ ' COM DOLAR MÉDIO DE R$ '+ str((preco_total_por_ativo[ativo] / quantidade_por_ativo[ativo]))
    vlr_reais = str(preco_total_por_ativo[ativo])

    # Adiciona os dados ao DataFrame
    df2 = df2._append({'Ativo': ativo, 'Descrição': desc, 'Valor em Reais (R$)':vlr_reais}, ignore_index=True)


# gera nova planilha com nome de Saída
writer = pd.ExcelWriter('Saída.xlsx', engine = 'xlsxwriter')
df2.to_excel(writer, sheet_name = 'Planilha1',index=False)
df.to_excel(writer, sheet_name = 'Planilha2',index=False)

writer.close()