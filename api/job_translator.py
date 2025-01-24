import json
from typing import List

import instructor
from fastapi import APIRouter, HTTPException, Request
from openai import OpenAI
from pydantic import BaseModel, ValidationError
from app.models import JobInput, JobDetails, Jobs

router = APIRouter()

client = instructor.from_openai(OpenAI())


@router.post("/job-translator", response_model=Jobs)
async def create_job_list(input: JobInput):
    try:
        text = input.text
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            response_model=Jobs,
            messages=[{
                "role": "system",
                "content": """
                    Your job is to clean unstructured data about jobs whether html, text, or json, 
                    and convert it to a list of jobs with the following schema:
                    job_title, job_description, job_url, job_details_url, company_name, location, salary, other_metadata
                    You should respond with JSON ONLY.
                    If there is only one job, please only respond with one job.
                """
            }, {
                "role": "user",
                "content": f"""Extract all the 
                    jobs from the content below:
                    {text}"""
            }])
        return response
    except ValidationError as ve:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
