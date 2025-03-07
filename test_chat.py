from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_english_chat():
    response = client.post("/chat", json={"message": "Hello, how are you?"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_farsi_chat():
    response = client.post("/chat", json={"message": "سلام، چطوری؟"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_invalid_language():
    response = client.post("/chat", json={"message": "Bonjour, ça va?"})
    assert response.status_code == 400
    assert response.json()["detail"] == "فقط از زبان‌های فارسی و انگلیسی پشتیبانی می‌شود."
