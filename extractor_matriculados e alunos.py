import mysql.connector
import csv
from datetime import datetime
 
# Criar a conexão com o banco
conn= mysql.connector.connect(
    host = 'localhost',
    port = 3307,
    user = 'root',
    password = 'senac',
    database = 'fitlife',
    use_pure = True # força a entrada do script no banco de dados
)
 
# Criar o cursor para executar comandos SQL
cursor = conn.cursor()
 
# Executar a consulta SQL
cursor.execute("""
    SELECT al.nome, mt.numero_matricula, al.cpf, al.data_nascimento, pl.nome
    FROM matriculas mt
    INNER JOIN alunos al ON mt.codigo_aluno = al.codigo
    INNER JOIN planos pl ON mt.codigo_plano = pl.codigo;
""")
 
# Buscar todos os resultados
resultados = cursor.fetchall()
 
# CSV
with open("dados.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Matricula", "CPF", "Data_nascimento", "Plano"])
 
    for linha in resultados:
        nome = linha[0].upper()
        matricula = f"{linha[1]:08d}"
        cpf = f"{linha[2][:2]}.***.***-{linha[2][-2:]}"
        data_nascimento = linha[3].strftime('%d/%m/%Y')
        plano = linha[4]
 
        writer.writerow([nome, matricula, cpf, data_nascimento, plano])
        print(nome, matricula, cpf, data_nascimento, plano)
 
# Fechar cursor e conexão
cursor.close()
conn.close()