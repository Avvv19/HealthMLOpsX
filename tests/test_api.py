# tests/test_api.py

import pytest
from httpx import AsyncClient
from app.api import app

@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        r = await client.get("/health")
        assert r.status_code == 200
        data = r.json()
        assert data.get("status") == "ok"

@pytest.mark.asyncio
async def test_root_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        r = await client.get("/")
        assert r.status_code == 200
        assert "message" in r.json()

@pytest.mark.asyncio
async def test_ask_endpoint_success():
    async with AsyncClient(app=app, base_url="http://test") as client:
        r = await client.get("/ask", params={"query": "healthy"})
        assert r.status_code == 200
        data = r.json()
        # Should include answer and sources
        assert "answer" in data and isinstance(data["answer"], str)
        assert "sources" in data and isinstance(data["sources"], list)

@pytest.mark.asyncio
async def test_ask_endpoint_empty_query():
    async with AsyncClient(app=app, base_url="http://test") as client:
        r = await client.get("/ask", params={"query": "   "})
        assert r.status_code == 422
