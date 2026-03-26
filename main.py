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

class CadastrarShow(BaseModel):
    nome: str
    data_show: str
    descricao: str

@app.get('/')
def rotaUsuarios():
    return {'msg': 'Cadastre o seu Show!!!'}

@app.get('/shows')
def listar_shows():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'SELECT * FROM shows'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado
# /shows/id









@app.post('/cadastrar_show')
def cadastrar_show(cadastro: CadastrarShow):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'INSERT INTO shows (nome, data_show, descricao) VALUES (%s, %s, %s)'
    cursor.execute(sql, (cadastro.nome, cadastro.data_show, cadastro.descricao))
    conexao.commit()
    conexao.close()
    print('Produto Cadastrado com Sucesso!!!')
    return {'msg': 'Produto Cadastrado com Sucesso!!!'}



















@app.delete('/deletar_show/{id_show}')
def deletar_show(id_show: int):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'DELETE FROM shows WHERE id = %s'
    cursor.execute(sql, (id_show, ))
    conexao.commit()
    conexao.close()
    print('Show Excluído com Sucesso!!!')
    return {'msg': 'Show Excluído com Sucesso!!!'}













