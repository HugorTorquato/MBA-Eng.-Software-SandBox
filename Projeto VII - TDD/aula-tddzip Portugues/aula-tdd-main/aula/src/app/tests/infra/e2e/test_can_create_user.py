from fastapi.testclient import TestClient
from uuid import uuid4, UUID
from infra.api.main import app

client = TestClient(app)

# Test if it's possible to create an user using api
def test_can_Create_user():
    response = client.post("/users/", json={"name":"Hugo"})

    data = response.json()

    assert response.status_code == 200
    assert isinstance(UUID(data['id']), UUID)
    assert data['name'] == "Hugo"