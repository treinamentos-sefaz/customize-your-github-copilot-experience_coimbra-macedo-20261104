# 📘 Atividade: Meu Primeiro Banco de Dados com DuckDB

## 🎯 Objetivo

Nesta atividade você vai aprender a criar e acessar um **banco de dados embarcado** usando o DuckDB — um banco de dados moderno que roda direto no seu programa Python, sem precisar instalar nenhum servidor! Ao final, você terá criado seu próprio banco de dados, inserido registros e feito consultas com SQL. 🦆

> 💡 **O que é um banco de dados embarcado?** É um banco que vive dentro da sua aplicação, armazenando os dados em um simples arquivo local. Perfeito para aprender SQL e para projetos pessoais!

Antes de começar, instale o DuckDB com:

```bash
pip install duckdb
```

## 📝 Tarefas

### 🛠️ Tarefa 1: Criar o banco de dados e a primeira tabela

#### Descrição

Abra o arquivo `starter-code.py` e complete a função `criar_tabela()`. Ela deve conectar ao banco de dados (o arquivo `escola.duckdb` será criado automaticamente) e criar uma tabela chamada `alunos`.

#### Requisitos

O programa concluído deve:

- Conectar ao banco usando `duckdb.connect("escola.duckdb")`
- Criar a tabela `alunos` com as colunas: `id` (INTEGER), `nome` (VARCHAR) e `nota` (DOUBLE)
- Usar `CREATE TABLE IF NOT EXISTS` para não dar erro se a tabela já existir

### 🛠️ Tarefa 2: Inserir registros

#### Descrição

Complete a função `inserir_alunos()` para adicionar pelo menos 5 alunos na tabela usando o comando SQL `INSERT INTO`.

#### Requisitos

O programa concluído deve:

- Inserir pelo menos 5 alunos com `id`, `nome` e `nota`
- Usar valores de nota variados (entre 0 e 10)
- Exibir a mensagem `"Alunos inseridos com sucesso!"` ao final

### 🛠️ Tarefa 3: Consultar os dados

#### Descrição

Complete a função `listar_alunos()` para buscar e exibir todos os alunos cadastrados, ordenados da maior nota para a menor.

#### Requisitos

O programa concluído deve:

- Usar `SELECT` para buscar todos os alunos
- Ordenar os resultados pela nota em ordem decrescente (`ORDER BY nota DESC`)
- Exibir cada aluno no formato: `Nome: <nome> | Nota: <nota>`

### 🛠️ Tarefa 4: Filtrar com WHERE (desafio!)

#### Descrição

Complete a função `alunos_aprovados()` para listar apenas os alunos com nota maior ou igual a 7. Este é o seu primeiro filtro SQL — você consegue! 💪

#### Requisitos

O programa concluído deve:

- Usar `SELECT` com a cláusula `WHERE nota >= 7`
- Exibir quantos alunos foram aprovados (dica: use `len()` no resultado de `fetchall()`)
- Exibir o nome de cada aluno aprovado

## ✅ Como testar

Execute o programa com:

```bash
python starter-code.py
```

Se tudo estiver certo, você verá a lista de alunos ordenada por nota e a lista de aprovados. Repare que o arquivo `escola.duckdb` foi criado na sua pasta — esse é o seu banco de dados embarcado! 🎉
