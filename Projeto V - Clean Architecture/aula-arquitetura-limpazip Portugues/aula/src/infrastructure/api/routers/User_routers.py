from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from infrastructure.api.database import get_session

from usecases.user.add_user.add_user_dto import AddUserInputDTO
from usecases.user.add_user.add_user_usecase import AddUserUseCase
from infrastructure.User.sqlalchemy.user_repository import UseRepository
from usecases.user.find_user.find_user_dto import FindUserInputDTO
from usecases.user.find_user.find_user_usecase import FindUserUseCase
from usecases.user.list_users.list_users_dto import ListUserInputDTO
from usecases.user.list_users.list_users_usecase import ListUsertsUseCase


# Definição das rotas pensando nos casos de uso

router = APIRouter(prefix="/users", tags=["Users"])

# http://localhost:8000/users/
@router.post("/")
def add_user(request: AddUserInputDTO, session: Session = Depends(get_session)):
    try:
        # Instanciar um repositorio
        user_repository = UseRepository(session=session)

        # Criar um caso de uso
        usecase = AddUserUseCase(user_repository=user_repository)

        # entregar o output
        output = usecase.execute(input=request)

        return output
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# http://localhost:8000/users/{$user_id}
@router.get("/{user_id}")
def find_user(user_id: UUID, session: Session = Depends(get_session)):
    try:
        # Instanciar um repositorio
        user_repository = UseRepository(session=session)

        # Criar um caso de uso
        usecase = FindUserUseCase(user_repository=user_repository)

        # entregar o output
        output = usecase.execute(input=FindUserInputDTO(id=user_id))

        return output
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
# http://localhost:8000/users/
@router.get("/")
def list_user(session: Session = Depends(get_session)):
    try:
        # Instanciar um repositorio
        user_repository = UseRepository(session=session)

        # Criar um caso de uso
        usecase = ListUsertsUseCase(user_repository=user_repository)

        # entregar o output
        output = usecase.execute(input=ListUserInputDTO)

        return output
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
