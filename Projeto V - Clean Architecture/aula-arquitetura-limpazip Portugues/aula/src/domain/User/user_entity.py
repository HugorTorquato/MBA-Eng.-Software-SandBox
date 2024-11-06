from uuid import UUID, uuid4

# Entity, where there is a value of the software

class User:

    # List of atributes
    id: UUID
    name: str

    # Constructor
    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name

        self.validate()

    def validate(self):
        if not isinstance(self.id, UUID):
            raise Exception("ID must be UUID")
        
        if not isinstance(self.name, str) or len(self.name) == 0:
            raise Exception("Name must be a str and not empty")
    

# User_1 = User(id=uuid4(), name="Hugo")
# User_2 = User(id=uuid4(), name="Tay")
# User_3 = User(id=4, name="Hugoo") ## Caso de falha que precisa de verificação

# User_3.validate() # Will print an error