# ✅ API de Gerenciamento de Tarefas (To-Do List)

Esta é uma API RESTful leve e segura desenvolvida em Python com **FastAPI** para o gerenciamento de tarefas diárias. O projeto foca em boas práticas de persistência de dados utilizando ORM e segurança de endpoints.

## 🚀 Tecnologias Utilizadas

*   **Framework:** FastAPI
*   **Persistência de Dados:** SQLAlchemy (ORM) & SQLite
*   **Validação de Dados:** Pydantic
*   **Segurança:** HTTP Basic Authentication & Módulo Secrets

## 🏗️ Diferenciais Técnicos do Projeto

*   **Segurança Robusta (Anti-Timing Attack):** Implementação de autenticação via HTTP Basic utilizando a função `secrets.compare_digest`. Isso impede ataques de tempo (timing attacks) ao validar as credenciais do usuário.
*   **Paginação e Ordenação Dinâmica:** A rota de listagem de tarefas possui paginação customizável via parâmetros de query (`page` e `size`), além de permitir ordenar os resultados de forma dinâmica por nome ou por descrição.
*   **Injeção de Dependências:** Uso nativo do sistema de `Depends` do FastAPI para gerenciar o ciclo de vida das sessões do banco de dados e aplicar barreiras de autenticação nas rotas.
*   **Mapeamento Objeto-Relacional (ORM):** Isolamento da camada de banco de dados utilizando SQLAlchemy para operações seguras de CRUD, evitando SQL Injection.

## 🔀 Rotas da API

Todas as rotas abaixo exigem autenticação **HTTP Basic** (Credenciais padrão: Usuário `adm` / Senha `adm`).

*   `POST /adiciona` - Cria uma nova tarefa validando se ela já existe no banco.
*   `GET /exibir` - Lista as tarefas com suporte a paginação dinâmica e ordenação (`ordem=nome` ou `ordem=descricao`).
*   `PUT /atualizar` - Modifica o nome e a descrição de uma tarefa existente.
*   `PUT /concluir/{nome_tarefa}` - Atualiza o status da tarefa para concluída (`concluir_tarefa = True`).
*   `DELETE /delete/{nome_tarefa}` - Remove permanentemente uma tarefa do banco de dados.

## 🔧 Como Executar o Projeto

### Pré-requisitos
*   Python 3.10 ou superior instalado.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd NOME_DO_REPOSITORIO_TAREFAS
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale o FastAPI e o SQLAlchemy:**
   ```bash
   pip install fastapi sqlalchemy uvicorn pydantic
   ```

4. **Inicie o servidor de desenvolvimento:**
   ```bash
   py -m fastapi dev nomearquivo.py
   ```

A API criará o banco de dados `tarefas.db` automaticamente e estará disponível em `http://127.0.0.1:8000`. Acesse `http://127.0.0` para testar os endpoints diretamente pela interface interativa.
