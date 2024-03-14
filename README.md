## Planilha para Informe de Imposto de Renda - Ativos no Exterior

## Introdução

Este é um projeto desenvolvido em Python 3.11.8 para auxiliar na geração de uma planilha para o informe de imposto de renda para quem possui ativos no exterior, como ações (stocks), REITs e ETFs. A entrada de dados é feita através de uma planilha Excel chamada `transacoes.xlsx`, e o script consulta o valor do dólar de venda do dia da transação no site do Banco Central do Brasil (BCB). Ao final do processo, é gerada uma planilha chamada `Saída.xlsx` com os dados que devem ser inseridos no programa do imposto de renda.

## Requisitos

- Python 3.11.8 ou superior
- Bibliotecas Python: pandas, openpyxl, requests, BeautifulSoup

## Instalação das Bibliotecas

Você pode instalar as bibliotecas necessárias utilizando o gerenciador de pacotes pip. Basta executar o seguinte comando:

pip install pandas requests


## Utilização

1. Certifique-se de ter a planilha `transacoes.xlsx` na mesma pasta que o script `gerar_informe.py`.
2. Execute o script `gerar_informe.py` utilizando o Python 3.11.8 ou superior.
3. Aguarde o processo de consulta do dólar de venda do dia e a geração da planilha `Saída.xlsx`.
4. Abra a planilha `Saída.xlsx` e insira os dados gerados no programa do imposto de renda.

## Estrutura da Planilha `transacoes.xlsx`

A planilha `transacoes.xlsx` deve seguir a seguinte estrutura:

| Ativo    | Data de Negociação | Quantidade | Preço  | Ordem   |
|----------|---------------------|------------|--------|---------|
| AAPL     | 2022-01-05          | 10         | 150.00 | Compra  |
| AAPL     | 2022-02-15          | 5          | 160.00 | Venda   |
| AMZN     | 2022-03-10          | 2          | 3000.00| Compra  |
| AMZN     | 2022-04-20          | 1          | 3200.00| Compra  |

## Observações

- Certifique-se de ter uma conexão com a internet durante a execução do script para que seja possível consultar o valor do dólar de venda.
- Caso haja alguma dificuldade ou erro durante a execução do script, verifique se os dados na planilha `transacoes.xlsx` estão corretamente formatados e se a conexão com a internet está funcionando adequadamente.

## Saída do Programa

Aqui está a saída do programa no formato esperado para a planilha de informe de Imposto de Renda:

| Ativo | Descrição | Valor em Reais (R$) |
|-------|------------|---------------------|
| EIMI  | EIMI - 11.0 AÇÕES COM CUSTO TOTAL DE $306.3 COM DOLAR MÉDIO DE R$ 147.1413390909091 | 1618.55473 |
| SLYV  | SLYV - 141.66033894 AÇÕES COM CUSTO TOTAL DE $10658.1128437691 COM DOLAR MÉDIO DE R$ 377.9006622789902 | 53533.53590409223 |
| SPHQ  | SPHQ - 172.97710531 AÇÕES COM CUSTO TOTAL DE $8530.1445053373 COM DOLAR MÉDIO DE R$ 248.12740948641377 | 42920.36104102889 |

Esses são os dados que devem ser inseridos no programa do Imposto de Renda.
