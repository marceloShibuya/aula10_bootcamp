from .sqlite  import BancoDeDadosSQLite
from .postgre import BancoDeDadosPost
from .encaps  import BancoDeDados

########## SQLITE #############

nome_arquivo = "exemplo.db"
banco_sql = BancoDeDadosSQLite(nome_arquivo)
banco_sql.conectar()

# Inserindo dados na tabela
insert_query = """
INSERT INTO usuarios (nome, email) VALUES
('João', 'joao@example.com'),
('Maria', 'maria@example.com');
"""
banco_sql.executar_query(insert_query)
banco_sql.desconectar()

########## POSTGRES #############

host = 'localhost'
porta = '5432'
banco = 'nome_do_banco'
usuario = 'usuario'
senha = 'senha'

banco_post = BancoDeDadosPost(host, porta, banco, usuario, senha)
banco_post.conectar()

# Inserindo dados na tabela
insert_query = """
INSERT INTO usuarios (nome, email) VALUES
('João', 'joao@example.com'),
('Maria', 'maria@example.com');
"""
banco_post.executar_query(insert_query)
banco_post.desconectar()

########## ENCAPSULAMENTO #############

tipo_banco = 'sqlite'
banco = BancoDeDados(tipo_banco)
banco.conectar()

# Inserindo dados na tabela
insert_query = """
INSERT INTO usuarios (nome, email) VALUES
('João', 'joao@example.com'),
('Maria', 'maria@example.com');
"""
banco.executar_query(insert_query)
banco.desconectar()



