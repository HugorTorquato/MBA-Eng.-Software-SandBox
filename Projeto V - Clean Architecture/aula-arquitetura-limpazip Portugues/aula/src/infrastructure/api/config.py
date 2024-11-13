
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    CONNECTION: str = Field(..., env= "CONNECTION")
    # pEGAR OS DADOS QU ESTÃO DENTRO DO .ENV DEIFNIDOS DENTRO DA VARIÁVEL DE AMBIENTE
    
#Variável que veio dos arquivos de configuração dos containers
settings = Settings()

