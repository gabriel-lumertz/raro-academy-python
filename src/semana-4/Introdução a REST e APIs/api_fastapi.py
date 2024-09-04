from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    idade: int


usuarios_db = []


@app.post("/users/", response_model=Usuario, status_code=201)
def criar_usuario(usuario: Usuario):
    for u in usuarios_db:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="Usuário com este ID já existe.")
    
    usuarios_db.append(usuario)
    return usuario

@app.get("/users/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios_db

@app.get("/users/{usuario_id}", response_model=Usuario)
def obter_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado.")

@app.put("/users/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: int, usuario_atualizado: Usuario):
    for index, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            usuarios_db[index] = usuario_atualizado
            return usuario_atualizado
    raise HTTPException(status_code=404, detail="Usuário não encontrado.")

@app.delete("/users/{usuario_id}", response_model=dict)
def deletar_usuario(usuario_id: int):
    for index, usuario in enumerate(usuarios_db):
        if usuario.id == usuario_id:
            del usuarios_db[index]
            return {"message": "Usuário removido com sucesso."}
    raise HTTPException(status_code=404, detail="Usuário não encontrado.")