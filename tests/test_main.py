from fastapi.testclient import TestClient
from fastapi_using_poetry_project.main import app

def test_route_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()=={"Hello":"World"}

def test_piaic_path():
    client = TestClient(app=app)
    response = client.get("/PIAIC")
    assert response.status_code == 200
    assert response.json()=={"organization":"PIAIC"}