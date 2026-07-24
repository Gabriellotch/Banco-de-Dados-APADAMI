import sqlite3

# Conecta (ou cria) o arquivo do banco de dados na mesma pasta
conexao = sqlite3.connect("apadami.db")
cursor = conexao.cursor()

# Lê e executa todas as tabelas
script_sql = """
CREATE TABLE IF NOT EXISTS pessoa_atipica (
    id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo VARCHAR(150) NOT NULL,
    data_nascimento DATE,
    contato VARCHAR(20),
    genero VARCHAR(30),
    cpf VARCHAR(14) UNIQUE,
    rg VARCHAR(20),
    email VARCHAR(150),
    endereco VARCHAR(200),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    cep VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS responsavel (
    id_responsavel INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INTEGER NOT NULL,
    nome VARCHAR(150) NOT NULL,
    grau_parentesco VARCHAR(50),
    telefone VARCHAR(20),
    FOREIGN KEY (id_pessoa) REFERENCES pessoa_atipica(id_pessoa)
);

CREATE TABLE IF NOT EXISTS condicao_atipica (
    id_condicao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INTEGER NOT NULL,
    possui_laudo BOOLEAN,
    possui_diagnostico VARCHAR(30),
    cid VARCHAR(20),
    diagnostico VARCHAR(150),
    outra_condicao VARCHAR(150),
    FOREIGN KEY (id_pessoa) REFERENCES pessoa_atipica(id_pessoa)
);

CREATE TABLE IF NOT EXISTS escolaridade (
    id_escolaridade INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INTEGER NOT NULL,
    matriculado BOOLEAN,
    nome_escola VARCHAR(150),
    serie_ano VARCHAR(50),
    turno VARCHAR(20),
    apoio_pedagogico BOOLEAN,
    tipo_apoio VARCHAR(100),
    escola_inclusiva BOOLEAN,
    motivo_nao_inclusao TEXT,
    FOREIGN KEY (id_pessoa) REFERENCES pessoa_atipica(id_pessoa)
);

CREATE TABLE IF NOT EXISTS situacao_familiar (
    id_situacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INTEGER NOT NULL,
    recebe_beneficio BOOLEAN,
    beneficio VARCHAR(100),
    reside_com VARCHAR(100),
    renda_familiar VARCHAR(50),
    dificuldades TEXT,
    FOREIGN KEY (id_pessoa) REFERENCES pessoa_atipica(id_pessoa)
);

CREATE TABLE IF NOT EXISTS autorizacao (
    id_autorizacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INTEGER NOT NULL,
    autoriza_dados BOOLEAN,
    autoriza_imagem BOOLEAN,
    data_autorizacao DATE,
    FOREIGN KEY (id_pessoa) REFERENCES pessoa_atipica(id_pessoa)
);
"""

cursor.executescript(script_sql)
conexao.commit()
conexao.close()

print("🚀 Todas as tabelas foram criadas com sucesso no arquivo 'apadami.db'!")