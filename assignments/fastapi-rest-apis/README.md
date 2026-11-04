# 📘 Atividade: Construindo REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a construir uma REST API usando o framework FastAPI, criando endpoints para gerenciar uma biblioteca de livros — do primeiro "Hello, World" até operações CRUD completas com validação de dados.

## 📝 Tarefas

### 🛠️ Primeiro Endpoint

#### Descrição
Comece pelo básico! Use o starter code para colocar sua API no ar e criar seu primeiro endpoint. Execute o servidor com `uvicorn main:app --reload` e explore a documentação interativa em `http://localhost:8000/docs`.

#### Requisitos
O programa concluído deve:

- Executar sem erros com `uvicorn main:app --reload`
- Ter um endpoint `GET /` que retorne `{"message": "Bem-vindo à Biblioteca Mergington!"}`
- Ter um endpoint `GET /status` que retorne o nome da API e sua versão


### 🛠️ Listando e Buscando Livros

#### Descrição
Toda biblioteca precisa de um catálogo! Usando a lista de livros fornecida no starter code, crie endpoints para listar todos os livros e buscar um livro específico pelo seu `id`.

#### Requisitos
O programa concluído deve:

- Ter um endpoint `GET /books` que retorne a lista completa de livros
- Ter um endpoint `GET /books/{book_id}` que retorne o livro com o `id` informado
- Retornar erro `404` com uma mensagem amigável quando o livro não existir


### 🛠️ Adicionando Livros com Validação

#### Descrição
Agora vamos permitir que novos livros entrem no catálogo. Crie um modelo Pydantic para representar um livro e um endpoint `POST` que valide e adicione o livro à lista.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic `Book` com os campos `id` (int), `title` (str), `author` (str) e `year` (int)
- Ter um endpoint `POST /books` que receba um `Book` no corpo da requisição e o adicione à lista
- Retornar erro `400` se já existir um livro com o mesmo `id`


### 🛠️ CRUD Completo (Desafio)

#### Descrição
Complete sua API com as operações que faltam: atualizar e remover livros. Como desafio extra, adicione um filtro de busca por autor usando query parameters.

#### Requisitos
O programa concluído deve:

- Ter um endpoint `PUT /books/{book_id}` que atualize um livro existente
- Ter um endpoint `DELETE /books/{book_id}` que remova um livro da lista
- Retornar erro `404` ao tentar atualizar ou remover um livro inexistente
- (Extra) Aceitar um query parameter opcional em `GET /books?author=...` para filtrar livros por autor
