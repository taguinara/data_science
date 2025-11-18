import mysql.connector
import csv
from datetime import datetime

# Conecta com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='***',
    database='loja_simples',
    use_pure=True
)

# Pega todas as respostas e coloca numa lista
cursor = conexao.cursor()

# Socilita no banco os dados das colunas vendas
query = """
SELECT
    c.id AS id_cliente, 
    c.nome AS Cliente,
    p.nome_produto AS Produto,
    v.quantidade AS Quantidade,
    p.preco_produto AS Preco_Unitario,
    (v.quantidade * p.preco_produto) AS Valor_Total,
    v.data_venda AS Data_Venda
FROM venda v
JOIN cliente c ON v.id_cliente = c.id
JOIN produto p ON v.id_produto = p.id;
"""

cursor.execute(query) # Coloca todas as vendas com o nome do cliente, produto, quantidade, preço, valor total e data
resultados = cursor.fetchall() # Pega todas as respostas e coloca numa lista que chamamos de resultados.
resultados_formatados = []

# Preparar os dados 
for row in resultados:
    nova_linha = list(row) # copia a linha
    nova_linha[4] = f"R$ {row[4]:.2f}"  # Preço Unitário
    nova_linha[5] = f"R$ {row[5]:.2f}"  # Valor Total
    
    # Data de venda formatada no modelo BR
    nova_linha[6] = row[6].strftime("%d/%m/%Y")  # <--- aplica somente na data

    resultados_formatados.append(nova_linha)


# Nomes das colunas
colunas = [desc[0] for desc in cursor.description]

# Cabeçalho textual do relatório, escreve um título, com a data e hora de quando o relatório foi feito
data_geracao = datetime.now().strftime("%d/%m/%Y %H:%M")
cabecalho = [
    "=== RELATÓRIO DE VENDAS 2025 ===",
    f"Gerado em: {data_geracao}",
    "----------------------------------------",
]

nome_arquivo = "relatorio_vendas.csv"

# Exportar para CSV, escrever cabeçalho textual

with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    
# Escrever cabeçalho textual, cria e escreve o CSV estruturado
    for linha in cabecalho: 
        arquivo_csv.write(linha + "\n")
    arquivo_csv.write("\n")  # linha em branco antes do CSV

    writer = csv.writer(arquivo_csv)
    writer.writerow(colunas)
    writer.writerows(resultados_formatados)

# Calcular total geral de vendas, quanto a loja vendeu no total
total_geral = sum(row[5] for row in resultados) 

print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
print(f"Total de vendas registradas: R$ {total_geral:.2f}")

# Fechar conexão e banco
cursor.close()
conexao.close()


