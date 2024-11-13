from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_engine(settings.CONNECTION)


# Criado uma seção
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Receber os metadados das tabelas
Base = declarative_base()

def get_session():
    #abare uma section com o database e fecha quando acabar de executar

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Criação das tabelas
# Acoplando o banco de dados no repositorio
def create_tables():
    Base.metadata.create_All(bind=engine)