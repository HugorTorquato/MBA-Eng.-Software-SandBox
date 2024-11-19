
from usecases.user.find_user.find_user_dto import FindUserOutputDTO

class UserPresenter:

    @staticmethod
    def toJSON(user_dtop: FindUserOutputDTO) -> dict: # can be other types
        return {
            "id" : str(user_dtop.id), # pode fazer o cast
            "name" : user_dtop.name
        }