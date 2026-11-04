"""
Construindo REST APIs com FastAPI - Starter Code

Instale as dependências:
    pip install fastapi uvicorn

Execute o servidor:
    uvicorn main:app --reload

Depois acesse a documentação interativa em:
    http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Biblioteca Mergington", version="1.0.0")

# Catálogo inicial de livros (use esta lista nas suas tarefas)
books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019},
    {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart", "year": 2020},
    {"id": 3, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2022},
]


# Tarefa 1: Primeiro Endpoint
# TODO: Crie o endpoint GET / retornando a mensagem de boas-vindas
# TODO: Crie o endpoint GET /status retornando o nome e a versão da API


# Tarefa 2: Listando e Buscando Livros
# TODO: Crie o endpoint GET /books
# TODO: Crie o endpoint GET /books/{book_id} (use HTTPException para o erro 404)


# Tarefa 3: Adicionando Livros com Validação
# TODO: Defina o modelo Pydantic Book (id, title, author, year)
# TODO: Crie o endpoint POST /books


# Tarefa 4: CRUD Completo (Desafio)
# TODO: Crie os endpoints PUT /books/{book_id} e DELETE /books/{book_id}
# TODO: (Extra) Adicione o filtro por autor em GET /books
