import sqlite3
import pandas as pd

# Conecta ao banco de dados SQLite
conexao = sqlite3.connect("apadami.db")

# Cria um arquivo Excel com uma aba para cada tabela do banco
with pd.ExcelWriter("dados_apadami.xlsx", engine="openpyxl") as writer:
    # Lista com o nome de todas as suas tabelas
    tabelas = [
        "pessoa_atipica",
        "responsavel",
        "condicao_atipica",
        "escolaridade",
        "situacao_familiar",
        "autorizacao"
    ]
    
    for tabela in tabelas:
        # Lê a tabela do banco
        df = pd.read_sql_query(f"SELECT * FROM {tabela}", conexao)
        # Salva como uma aba no Excel
        df.to_excel(writer, sheet_name=tabela, index=False)

conexao.close()
print("✅ Dados exportados com sucesso para o arquivo 'dados_apadami.xlsx'!")