from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)
VITE_ORIGIN = "http://localhost:5173"


def test_cors_preflight_allows_get_info():
    response = client.options(
        "/api/info",
        headers={
            "Origin": VITE_ORIGIN,
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == VITE_ORIGIN


def test_cors_get_info_includes_allow_origin():
    response = client.get("/api/info", headers={"Origin": VITE_ORIGIN})
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == VITE_ORIGIN
