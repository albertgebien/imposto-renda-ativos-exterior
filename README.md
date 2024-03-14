<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Planilha para Informe de Imposto de Renda</title>
</head>
<body>
    <h1>Planilha para Informe de Imposto de Renda - Ativos no Exterior</h1>

    <h2>Introdução</h2>
    <p>Este é um projeto desenvolvido em Python 3.11.8 para auxiliar na geração de uma planilha para o informe de imposto de renda para quem possui ativos no exterior, como ações (stocks), REITs e ETFs. A entrada de dados é feita através de uma planilha Excel chamada <code>transacoes.xlsx</code>, e o script consulta o valor do dólar de venda do dia da transação no site do Banco Central do Brasil (BCB). Ao final do processo, é gerada uma planilha chamada <code>Saída.xlsx</code> com os dados que devem ser inseridos no programa do imposto de renda.</p>

    <h2>Requisitos</h2>
    <ul>
        <li>Python 3.11.8 ou superior</li>
        <li>Bibliotecas Python: pandas, openpyxl, requests, BeautifulSoup</li>
    </ul>

    <h2>Instalação das Bibliotecas</h2>
    <p>Você pode instalar as bibliotecas necessárias utilizando o gerenciador de pacotes pip. Basta executar o seguinte comando:</p>
    <pre><code>pip install pandas openpyxl requests beautifulsoup4</code></pre>

    <h2>Utilização</h2>
    <ol>
        <li>Certifique-se de ter a planilha <code>transacoes.xlsx</code> na mesma pasta que o script <code>gerar_informe.py</code>.</li>
        <li>Execute o script <code>gerar_informe.py</code> utilizando o Python 3.11.8 ou superior.</li>
        <li>Aguarde o processo de consulta do dólar de venda do dia e a geração da planilha <code>Saída.xlsx</code>.</li>
        <li>Abra a planilha <code>Saída.xlsx</code> e insira os dados gerados no programa do imposto de renda.</li>
    </ol>

    <h2>Estrutura da Planilha <code>transacoes.xlsx</code></h2>
    <p>A planilha <code>transacoes.xlsx</code> deve seguir a seguinte estrutura:</p>
    <table>
        <thead>
            <tr>
                <th>Ativo</th>
                <th>Data de Negociação</th>
                <th>Quantidade</th>
                <th>Preço</th>
                <th>Ordem</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>AAPL</td>
                <td>2022-01-05</td>
                <td>10</td>
                <td>150.00</td>
                <td>Compra</td>
            </tr>
            <tr>
                <td>AAPL</td>
                <td>2022-02-15</td>
                <td>5</td>
                <td>160.00</td>
                <td>Venda</td>
            </tr>
            <tr>
                <td>AMZN</td>
                <td>2022-03-10</td>
                <td>2</td>
                <td>3000.00</td>
                <td>Compra</td>
            </tr>
            <tr>
                <td>AMZN</td>
                <td>2022-04-20</td>
                <td>1</td>
                <td>3200.00</td>
                <td>Compra</td>
            </tr>
        </tbody>
    </table>

    <h2>Observações</h2>
    <ul>
        <li>Certifique-se de ter uma conexão com a internet durante a execução do script para que seja possível consultar o valor do dólar de venda.</li>
        <li>Caso haja alguma dificuldade ou erro durante a execução do script, verifique se os dados na planilha <code>transacoes.xlsx</code> estão corretamente formatados e se a conexão com a internet está funcionando adequadamente.</li>
    </ul>

    <h2>Saída do Programa</h2>
    <p>Aqui está a saída do programa no formato esperado para a planilha de informe de Imposto de Renda:</p>
    <table>
        <thead>
            <tr>
                <th>Ativo</th>
                <th>Descrição</th>
                <th>Valor em Reais (R$)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>EIMI</td>
                <td>EIMI - 11.0 AÇÕES COM CUSTO TOTAL DE $306.3 COM DOLAR MÉDIO DE R$ 147.1413390909091</td>
                <td>1618.55473</td>
            </tr>
            <tr>
                <td>SLYV</td>
                <td>SLYV - 141.66033894 AÇÕES COM CUSTO TOTAL DE $10658.1128437691 COM DOLAR MÉDIO DE R$ 377.9006622789902</td>
                <td>53533.53590409223</td>
            </tr>
            <tr>
                <td>SPHQ</td>
                <td>SPHQ - 172.97710531 AÇÕES COM CUSTO TOTAL DE $8530.1445053373 COM DOLAR MÉDIO DE R$ 248.12740948641377</td>
                <td>42920.36104102889</td>
            </tr>
        </tbody>
    </table>
    
</body>
</html>
