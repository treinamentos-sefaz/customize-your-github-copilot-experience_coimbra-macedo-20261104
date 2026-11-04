"""
Meu Primeiro Banco de Dados com DuckDB
======================================
Complete as funções abaixo seguindo as instruções do README.md.

Antes de começar, instale o DuckDB:
    pip install duckdb
"""

import duckdb


def criar_tabela(conexao):
    """Tarefa 1: Crie a tabela 'alunos' com as colunas id, nome e nota.

    Dica: use conexao.execute("CREATE TABLE IF NOT EXISTS ...")
    """
    # TODO: escreva o comando CREATE TABLE aqui
    pass


def inserir_alunos(conexao):
    """Tarefa 2: Insira pelo menos 5 alunos na tabela.

    Dica: use conexao.execute("INSERT INTO alunos VALUES (...)")
    """
    # TODO: insira os alunos aqui
    print("Alunos inseridos com sucesso!")


def listar_alunos(conexao):
    """Tarefa 3: Liste todos os alunos ordenados da maior nota para a menor.

    Dica: use conexao.execute("SELECT ...").fetchall() e percorra os resultados.
    """
    print("\n--- Todos os alunos ---")
    # TODO: busque e exiba os alunos no formato "Nome: <nome> | Nota: <nota>"


def alunos_aprovados(conexao):
    """Tarefa 4 (desafio): Liste apenas os alunos com nota >= 7."""
    print("\n--- Alunos aprovados ---")
    # TODO: busque os aprovados com WHERE, exiba a quantidade e os nomes


def main():
    # Conecta ao banco embarcado: o arquivo escola.duckdb é criado automaticamente!
    conexao = duckdb.connect("escola.duckdb")

    criar_tabela(conexao)
    inserir_alunos(conexao)
    listar_alunos(conexao)
    alunos_aprovados(conexao)

    conexao.close()


if __name__ == "__main__":
    main()
