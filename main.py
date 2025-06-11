from fastapi import FastAPI # Importando a Biblioteca fastapi
from pydantic import BaseModel # Importando a Biblioteca pydantic
import mysql.connector as my

app = FastAPI()

def conectar_banco():
    conexao = my.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'eventos_db'
    )
    return conexao

class User(BaseModel):
    nome: str
    idade: int
    email: str
    cidade: str

@app.get('/')
def rotaUsuarios():
    return 'oi'