import requests
from fastapi import HTTPException

BASE_URL = "https://api-onecloud.multicloud.tivit.com/fake"

def check_health():
    try:
        response = requests.get(f"{BASE_URL}/health", verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")

def get_admin_data(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{BASE_URL}/admin", headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Admin data access failed: {str(e)}")

def get_user_data(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{BASE_URL}/user", headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"User data access failed: {str(e)}")

def generate_token(username: str, password: str):
    """
    Gera um token usando o serviço externo de autenticação.
    """
    params = {"username": username, "password": password}  
    try:
        print(f"Enviando dados para geração de token: {params}")
        response = requests.post(f"{BASE_URL}/token", params=params, verify=False)  
        response.raise_for_status()
        print(f"Resposta da geração de token: {response.json()}")  
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao gerar token: {http_err}, Response: {http_err.response.text}")
        raise HTTPException(status_code=500, detail=f"Token generation failed: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Erro de conexão ao acessar o serviço: {conn_err}")
        raise HTTPException(status_code=500, detail=f"Connection error: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Erro de timeout: {timeout_err}")
        raise HTTPException(status_code=500, detail=f"Timeout error: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Erro na requisição: {req_err}")
        raise HTTPException(status_code=500, detail=f"Request error: {req_err}")
