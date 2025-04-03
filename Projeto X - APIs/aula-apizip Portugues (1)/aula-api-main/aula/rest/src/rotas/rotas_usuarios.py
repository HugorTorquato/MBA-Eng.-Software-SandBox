# boas praticas de separar recursos o que queremos mostrar na documentação

# http://localhost:8000/docs -> documentção da API

from fastapi import APIRouter, Depends, status, HTTPException
import esquemas, repositorio
from banco_de_dados import obter_sessao
from configuracao import logger
from sqlalchemy.orm import Session
import traceback

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

#criar umr ecurso
#ENDPOINT (http://localhost:8000/usuarios)
@router.post("/", response_model=esquemas.UsuarioResposta, status_code=status.HTTP_201_CREATED)
# Se for acessar o banco, cria a dependencia se está acessando o banco ou não
def criar_usuario(usuario: esquemas.UsuarioCriacao, db:Session=Depends(obter_sessao)):

    # Temos de cuidas com a forma do input e a forma do dado
    # Usar um dos esquemas já definidos na apicação
    print(usuario)
    try:
        repositorio.criar_usuario(db, usuario)
        logger.info("User criado com sucesso")
        return {"message":"Usuario criado"}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
# Rota para recuperar o user
#ENDPOINT (http://localhost:8000/usuarios/{user_id})
@router.get("/{usuario_id}")
def obter_usuario(usuario_id:int):
    return {"usuario_id":usuario_id}