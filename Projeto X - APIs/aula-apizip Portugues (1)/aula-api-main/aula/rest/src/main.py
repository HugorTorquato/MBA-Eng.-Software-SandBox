# Aqui é onde começamos a instanciar tudo que precisa para criar a API

from fastapi import FastAPI
from banco_de_dados import Base, motor
from configuracao import logger
from rotas import rotas_usuarios

#Definida a instancia da API
app = FastAPI(
    title="API de Exemplo - FastAPI",
    version="1.0",
    description=" Está é uma API exemplo.",
    openapi_url="/api/v1/openapi.json"
)

# Criar rotas inicial para testar a aplicação ( rotas para serem consumidas )
# Rota ara saber se o componente está online ou n


#decoratos é uma função que engloba outra função
# Endpoint /helthz
@app.get("/helthz")
def healthz():
    return {"messagem": "Aplicação funcionando"}

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=motor)
    logger.info("Tabelas do banco de dados criadas om sucesso.")

app.include_router(rotas_usuarios.router)
