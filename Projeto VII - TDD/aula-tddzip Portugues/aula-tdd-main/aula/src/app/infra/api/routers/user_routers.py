
from application.user.create_user_use_case import CreateUserUseCase, CreateUserResponse, CreateUserRequest
from fastapi import APIRouter, HTTPException
from infra.user.in_memory_user_repo import InMemoryUserRepository




router = APIRouter(prefix="/users")
repository=InMemoryUserRepository()

@router.post("/")
def create_user(request: CreateUserRequest):
    try:
        usecase = CreateUserUseCase(repository)
        response = usecase.execute(request)
        return response
    except Exception as e:
        return HTTPException(status_code=404, detail=str(e))