

from abc import abc, abstractclassmethod
from typing import Any

class UseCaseInterface(ABC):

    #Alguem vai receber esse contrato e quem receber tem de implementar tudo que está 
    # definido nesse contrato

    @abstractclassmethod
    def execute(input: Any) -> Any:
        raise NotImplementedError