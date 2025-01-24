from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config import client
from app.models import OpportunitiesList, UserProfile

router = APIRouter()


class opportunities(BaseModel):
  opportunities: str


class OpportunitiesList(BaseModel):
  titles: List[opportunities]


class UserProfile(BaseModel):
  name: str
  resume: str
  linkedin_text: str


@router.post("/job-titles", response_model=OpportunitiesList)
async def get_job_titles(user_profile: UserProfile):
  try:
    response = client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3-70b-instruct",
        response_model=OpportunitiesList,
        messages=[{
            "role":
            "system",
            "content":
            """
Your task is to generate sample job search queries that can be used to find job opportunities.

Definitions:

A job opportunity is defined as a position that aligns with the provided resume and LinkedIn text.

Output:

Return a list of 10 diverse job search queries in JSON format.

**Important Notes:**

- The goal is to create queries that can be used to search for job opportunities across multiple industries.
- These queries should be well-crafted search phrases that target specific job roles, industries, or requirements.
- Ensure the queries cover various aspects of job searching, including job titles, industries, and requirements.

Example Queries:
  "Marketing manager positions in tech startups",
  "Data scientist roles in environmental organizations",
  "Software engineer jobs in renewable energy companies",
  "Data analyst openings in finance for recent graduates",
  "Cybersecurity specialist positions in government agencies",
  "UX designer roles in non-profit organizations",
  "Full-stack developer jobs in e-commerce companies",
  "Product manager positions in healthcare technology",
  "DevOps engineer roles in cloud computing",
  "Artificial intelligence engineer jobs in robotics"

Instructions:

Generate 10 diverse job search queries based on the given resume and LinkedIn text, ensuring coverage of different aspects as outlined.

  
                """
        }, {
            "role":
            "user",
            "content":
            f"""
                    Name: {user_profile.name}
                    Resume: {user_profile.resume}
                    LinkedIn: {user_profile.linkedin_text}
                """
        }])
    return response
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
