import logfire
from fastapi import APIRouter
from pydantic import BaseModel

from config import client
from app.models import ResumeFile, ResumeChecklist

router = APIRouter()

@logfire.instrument("resume_checklist", extract_args=True)
@router.post("/resume-checklist", response_model=ResumeChecklist)
async def check_resume(resume_file: ResumeFile):
    response = client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p1-405b-instruct",
        response_model=ResumeChecklist,
        messages=[{
            "role":
            "system",
            "content":
            """
                You are Recruiting Assistant your job is to check the resume for errors and provide feedback. Based on the Guidelines below:
                Typographical Accuracy: Ensure that all your contact information is error-free.
                Essentials: Include your phone number, email, LinkedIn profile, portfolio (if applicable), and location.
                Location: List your city and state only. Full address is not necessary unless it is for a federal job application.
                Email: Utilize a professional email address. Preferably use a Gmail or similar account over a university email if applicable.
                LinkedIn: Ensure your LinkedIn URL is both hyperlinked and written out to cater to different applicant tracking systems.
                Professional Summary
                Summary vs. Objective: Include a clear, professional summary that outlines your capabilities and experiences, avoiding the use of an objective statement.
                Education
                Graduation Details: Listing your year of graduation is optional unless you are a current student or a recent graduate.
                GPA: Mention your GPA only if it is above 3.0.
                Employment History
                Date Format: Format employment dates as MM/YYYY or spell out the complete month.
                Quantifiable Achievements
                Metrics: Focus on quantifiable achievements rather than routine job responsibilities. For example, 'Onboarded 20+ new hires over 6 months' instead of 'Trained new hires.'
                References
                Availability: Do not include statements like 'References available upon request.'
                """
        }, {
            "role":
            "user",
            "content":
            f"Please provide feedback on my resume below:\n{resume_file.text}"
        }])
    try:
        data = response.model_dump_json(indent=2)
        print(data)
    except Exception as e:
        print(f"Error: {e}")
    return response
