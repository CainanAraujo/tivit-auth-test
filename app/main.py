import requests
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

BASE_URL = "https://api-onecloud.multicloud.tivit.com/fake"

# OAuth2 para autenticação
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def generate_token(username: str, password: str):
    """
    Gera um token usando o serviço externo de autenticação.
    """
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/token", params=data, verify=False)
    response.raise_for_status()  # Levanta um erro se a resposta for um erro
    return response.json()

@app.post("/token")
def generate_token_endpoint(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        token_response = generate_token(form_data.username, form_data.password)
        return {"access_token": token_response["access_token"], "token_type": "bearer"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to generate token from external service")

def get_user_data(token: str):
    """
    Acessa a rota de dados do usuário com um token.
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/user", headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

@app.get("/user")
def read_user_data(token: str = Depends(oauth2_scheme)):
    try:
        user_data = get_user_data(token)
        return user_data
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to access user data from external service")

def get_admin_data(token: str):
    """
    Acessa a rota de dados do admin com um token.
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/admin", headers=headers, verify=False)
    response.raise_for_status()
    return response.json()

@app.get("/admin")
def read_admin_data(token: str = Depends(oauth2_scheme)):
    try:
        admin_data = get_admin_data(token)
        return admin_data
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to access admin data from external service")

@app.get("/health")
def health_check():
    """
    Verifica a saúde do serviço externo.
    """
    response = requests.get(f"{BASE_URL}/health", verify=False)
    return response.json()
