from pydantic import main
import os
from typing import Dict
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.job_suggestion import router as get_job_titles
from api.role_labeling import router as analyze_profile
from api.job_translator import router as create_jobs_list
from api.resume_checklist import router as check_resume
from api.linkedin.linkedin_checklist import router as check_linkedin
from api.strengths import router as strengths
import logfire

app = FastAPI()

# Enable CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(get_job_titles, prefix="/api")
app.include_router(analyze_profile, prefix="/api")
app.include_router(create_jobs_list, prefix="/api")
app.include_router(check_resume, prefix="/api")
app.include_router(check_linkedin, prefix="/api")
app.include_router(strengths, prefix="/api")

logfire.instrument_fastapi(app)
logfire.configure(pydantic_plugin=logfire.PydanticPlugin(record="all"))

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "API Root"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        log_level="info"
    )