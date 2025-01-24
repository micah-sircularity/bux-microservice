from typing import List, Optional
from pydantic import BaseModel, Field

# LinkedIn Profile Models
class LinkedInProfile(BaseModel):
    name: str
    headline: str
    city: str
    state: Optional[str] = None
    country: str
    summary: Optional[str] = None
    education: str
    experience: str
    skills: str
    profile_picture: str
    public_profile_url: str
    banner_image: str
    connection_count: Optional[int] = 0

# LinkedIn Checklist Models
class Summary(BaseModel):
    text: Optional[str] = Field(
        None,
        description="Overall feedback and suggestions on how to improve the LinkedIn profile."
    )

class VanityURL(BaseModel):
    feedback: Optional[str] = Field(
        None,
        description="Feedback on the use of a vanity URL instead of the default link."
    )
    is_correct: bool = Field(
        False,
        description="Use a custom URL that is easy to remember and looks clean on printed materials."
    )

class ProfilePicture(BaseModel):
    feedback: Optional[str] = Field(
        None,
        description="Feedback on the profile picture quality and appropriateness."
    )
    is_correct: bool = Field(
        False,
        description="Clear, head-on photo that stands out to recruiters."
    )

class BannerImage(BaseModel):
    feedback: Optional[str] = Field(
        None,
        description="Feedback on the effectiveness and appeal of the banner image."
    )
    is_correct: bool = Field(
        False,
        description="Eye-catching and relevant to professional branding."
    )

class HeadlineTitle(BaseModel):
    feedback: Optional[str] = Field(
        None,
        description="Feedback on the headline/title effectiveness."
    )
    is_correct: bool = Field(
        False,
        description="Incorporates searchable keywords and skills beyond basic job titles."
    )

class About(BaseModel):
    feedback: Optional[str] = Field(
        None,
        description="Feedback on the completeness and appeal of the 'About' section."
    )
    is_correct: bool = Field(
        False,
        description="Comprehensive, engaging, and reflective of professional achievements and skills."
    )

class Connections(BaseModel):
    feedback: Optional[str] = Field(
        None,
        description="Feedback on the number and relevance of connections."
    )
    is_correct: bool = Field(
        False,
        description="Having 500+ connections to improve visibility in recruiter searches."
    )

class WorkHistoryJobTitles(BaseModel):
    feedback: Optional[str] = Field(
        None,
        description="Feedback on the descriptiveness and optimization of job titles."
    )
    is_correct: bool = Field(
        False,
        description="Includes up to 100 characters of descriptive and searchable content."
    )

class WorkHistoryBullets(BaseModel):
    feedback: Optional[str] = Field(
        None,
        description="Feedback on the effectiveness and relevance of bullet points under each job."
    )
    is_correct: bool = Field(
        False,
        description="Accomplishment-focused and quantifiable where possible."
    )

class Score(BaseModel):
    reasoning: str = Field(..., description="Reasoning for the grade given")
    score: int = Field(
        ...,
        description="Assign a grade between 0 and 100 based on criteria fulfillment."
    )

class LinkedInChecklist(BaseModel):
    summary: Summary
    Score: Score
    vanity_url: VanityURL
    profile_picture: ProfilePicture
    banner_image: BannerImage
    headline_title: HeadlineTitle
    about: About
    connections: Connections
    work_history_job_titles: WorkHistoryJobTitles
    work_history_bullets: WorkHistoryBullets 