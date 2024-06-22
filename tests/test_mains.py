"""Initial tests."""

from httpx import AsyncClient

from exopypi.main import app


async def test_root() -> None:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "exopypi!"}
