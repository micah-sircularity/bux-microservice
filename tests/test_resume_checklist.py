import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_resume_checklist():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/check-resume", json={
            "username": "testuser",
            "resume": "Experienced software engineer with a strong background in Python and JavaScript.",
            "linkedin_text": "Passionate about developing scalable web applications and working across the full stack."
        })
        assert response.status_code == status.HTTP_200_OK
        assert "checklist" in response.json()
        assert isinstance(response.json()["checklist"], list)
        assert len(response.json()["checklist"]) > 0  # Assuming the checklist should have at least one item
