from fastapi import APIRouter, HTTPException
from config import client
from app.models import Label, LabelEnum, UserProfile

router = APIRouter()

@router.post("/analyze-profile", response_model=Label)
async def analyze_profile(user_profile: UserProfile):
    try:
        response = client.chat.completions.create(
            model="accounts/fireworks/models/llama-v3-70b-instruct",
            response_model=Label,
            messages=[
                {"role": "system", "content": """
                    Your job is to label the user given their resume and LinkedIn text.
                    Here are your options:
                    RESEARCHER = "Researcher"
                    DESIGNER = "Designer"
                    ENGINEER = "Engineer"
                    MANAGER = "Manager"
                """},
                {"role": "user", "content": f"""
                    Name: {user_profile.username}
                    Resume: {user_profile.resume}
                    LinkedIn: {user_profile.linkedin_text}
                """}
            ]
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Command to run: uvicorn main:app --reload