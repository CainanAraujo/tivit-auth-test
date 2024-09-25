# API de Autenticação com JWT

Esta API permite a autenticação utilizando JWT e fornece acesso a rotas protegidas para usuários com papéis diferentes (usuário e administrador). A API está integrada com um Serviço FAKE que simula o comportamento real dos endpoints.

## Requisitos

- Python 3.8+
- FastAPI
- Uvicorn

## Instalação

1. **Clone o repositório:**

   git clone git@github.com:CainanAraujo/tivit-auth-test.git
   cd tivit-auth-test


2. **CRIE O AMBIENTE VIRUTAL E ATIVE-O:**

python -m venv venv
source venv/bin/activate  # No Linux/Mac
venv\Scripts\activate  # No Windows

3. **INSTALE AS DEPENDENCIAS:**

pip install -r requirements.txt


4. **INICIALIZE O BANCO:**

python initialize_db.py

5. **EXECUTE O SERVER**

uvicorn app.main:app --reload

A API estará disponível em http://127.0.0.1:8000.


**POSTMAN PARA TESTES ESTÁ NA RAIZ DO PROJETO.**


1. Gerando um Token
Para gerar um token de autenticação, execute o seguinte comando curl:



curl -X POST "http://127.0.0.1:8000/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=user&password=L0XuwPOdS5U"

2. Acessando Rotas Protegidas
Acesso à Rota de Usuário
Use o token gerado para acessar a rota de usuário:



curl -X GET "http://127.0.0.1:8000/user" \
     -H "Authorization: Bearer <seu_token_aqui>"
Acesso à Rota de Administrador
Para acessar a rota de administrador:


curl -X GET "http://127.0.0.1:8000/admin" \
     -H "Authorization: Bearer <seu_token_de_admin_aqui>"