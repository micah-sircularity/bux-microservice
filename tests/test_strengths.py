import pytest
from httpx import AsyncClient
from fastapi import status
from api.strengths import Categories

@pytest.mark.asyncio
async def test_strengths():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/assess-strengths", json={
            "assessment": Categories.LEADERSHIP_LUMINARY,
            "reasoning": "Demonstrated exceptional leadership skills in previous roles."
        })
        assert response.status_code == status.HTTP_200_OK
        assert "selection" in response.json()
        assert response.json()["selection"]["assessment"] == Categories.LEADERSHIP_LUMINARY.value
        assert "reasoning" in response.json()["selection"]
        assert len(response.json()["selection"]["reasoning"]) > 0
