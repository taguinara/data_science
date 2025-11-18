import mysql.connector
from datetime import datetime

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3307,
    password='***',
    database="fitlife",
    use_pure=True
)

# Cria objeto cursor para executar comandos SQL
cursor = conexao.cursor()

# Consulta SQL - Contar alunos matriculados por treino
cursor.execute('''
    SELECT codigo_treino, COUNT(numero_matricula) AS total_matriculas
    FROM matriculas_treinos
    GROUP BY codigo_treino
    ORDER BY codigo_treino
''')

resultados = cursor.fetchall()

# Tratamento dos dados
relatorio = []
total_geral = 0

for linha in resultados:
    codigo_treino = str(linha[0]).zfill(3)
    total_matriculas = linha[1]
    total_geral += total_matriculas
    relatorio.append(f'Treino {codigo_treino} -> {total_matriculas} alunos matriculados')

# Geração de relatório de texto
data_geracao = datetime.now().strftime("%d/%m/%Y")  # Apenas a data de hoje
nome_arquivo = "relatorio_matriculas_novas.txt"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("=== RELATÓRIO DE MATRÍCULAS FITLIFE ===\n")
    arquivo.write(f"Gerado em: {data_geracao}\n")
    arquivo.write("----------------------------------------\n")
    arquivo.write('\n'.join(relatorio) + '\n')
    arquivo.write("----------------------------------------\n")
    arquivo.write(f"TOTAL GERAL DE MATRÍCULAS: {total_geral}\n")

# Encerramento da conexão
cursor.close()
conexao.close()

