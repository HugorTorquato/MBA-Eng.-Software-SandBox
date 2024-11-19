

from abc import ABC, abstractmethod
from typing import Any

class UseCaseInterface(ABC):

    #Alguem vai receber esse contrato e quem receber tem de implementar tudo que está 
    # definido nesse contrato

    @abstractmethod
    def execute(input: Any) -> Any:
        raise NotImplementedError