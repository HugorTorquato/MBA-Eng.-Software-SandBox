# Arquivo principal da API

from fastapi import FastAPI
from infrastructure.api.database import create_tables
from infrastructure.api.routers import User_routers


app = FastAPI()

app.include_router(User_routers.router)

create_tables()


# Quero criar as tabelas quando o serviço subir

