from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

# Job-related Models
class JobInput(BaseModel):
    text: str

class JobDetails(BaseModel):
    job_title: str
    job_description: str
    job_details_url: str
    job_url: str
    company_name: str
    location: str
    salary: str
    other_metadata: dict

class Jobs(BaseModel):
    jobs: List[JobDetails]

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

# Resume Checklist Models
class Location(BaseModel):
    feedback: str = Field(
        ...,
        description="Feedback on the correctness of the location according to resume standards"
    )
    is_correct: bool = Field(
        ...,
        description="Include city and state only, unless applying for a Federal position"
    )

class LinkedIn(BaseModel):
    feedback: str = Field(
        ...,
        description="Feedback on the correctness of the LinkedIn URL"
    )
    is_correct: bool = Field(
        ...,
        description="Include both hyperlink and typed URL for ATS compatibility"
    )

class ProfessionalSummary(BaseModel):
    feedback: str = Field(
        ...,
        description="Feedback on the correctness of the professional summary"
    )
    is_correct: bool = Field(
        ...,
        description="Must include a clear, professional summary, not an objective statement"
    )

class Education(BaseModel):
    feedback: str = Field(
        ...,
        description="Feedback on the correctness of the Educational listing"
    )
    is_correct: bool = Field(
        ...,
        description="Include graduation year only if current student/new graduate, GPA if above 3.0"
    )

class EmploymentDates(BaseModel):
    feedback: str = Field(
        ...,
        description="Feedback on the correctness of the employment dates"
    )
    is_correct: bool = Field(
        ...,
        description="Use MM/YYYY format or spell out complete month"
    )

class QuantifiableMetrics(BaseModel):
    feedback: str = Field(
        ...,
        description="Feedback on the correctness of quantifiable metrics or accomplishments"
    )
    is_correct: bool = Field(
        ...,
        description="Quantify achievements rather than listing job duties"
    )

class References(BaseModel):
    feedback: str = Field(
        ...,
        description="Feedback on including references"
    )
    is_correct: bool = Field(
        ...,
        description="Do not include 'References available upon request'"
    )

class Score(BaseModel):
    reasoning: str = Field(..., description="Reasoning for the grade given")
    score: int = Field(
        ...,
        description="Assign a grade between 0 and 100 based on criteria fulfillment"
    )

class ResumeChecklist(BaseModel):
    Location: Location
    LinkedIn: LinkedIn
    ProfessionalSummary: ProfessionalSummary
    Education: Education
    EmploymentDates: EmploymentDates
    QuantifiableMetrics: QuantifiableMetrics
    References: References
    Score: Score
    FeedbackSummary: str = Field(
        ...,
        description="Overall resume feedback with specific improvement actions"
    )

# Strengths Assessment Models
class Categories(Enum):
    LEADERSHIP_LUMINARY = "Leadership Luminary"
    CREATIVE_CRUSADER = "Creative Crusader"
    RESILIENCE_ROCKSTAR = "Resilience Rockstar"
    COMMUNICATION_CHAMPION = "Communication Champion"
    EMPATHY_EXPERT = "Empathy Expert"
    ADAPTABILITY_ACE = "Adaptability Ace"
    ORGANIZATION_OVERLORD = "Organization Overlord"
    COLLABORATION_CONNOISSEUR = "Collaboration Connoisseur"
    PRESENTATION_PRODIGY = "Presentation Prodigy"
    GROWTH_GURU = "Growth Guru"

class Selection(BaseModel):
    assessment: Categories
    reasoning: str = Field(
        ...,
        description="Detailed explanation of the selection reasoning"
    )
    description: str = Field(
        ...,
        description="Detailed description of the strength and its applications"
    )

class Ideas(BaseModel):
    selection: List[str] = Field(
        ...,
        description="Five suggestions for displaying and marketing strengths"
    )

class StrengthsAssessments(BaseModel):
    assessment: Categories
    SelectionOne: Selection
    SelectionTwo: Selection
    Ideas: Ideas
    Summary: Summary

# User Profile Models
class UserProfile(BaseModel):
    name: str
    resume: str
    linkedin_text: str

class ResumeFile(BaseModel):
    text: str

# Role Labeling Models
class LabelEnum(str, Enum):
    RESEARCHER = "Researcher"
    DESIGNER = "Designer"
    ENGINEER = "Engineer"
    MANAGER = "Manager"

class Label(BaseModel):
    label: LabelEnum
    reasoning: str

# Job Suggestion Models
class Opportunities(BaseModel):
    opportunities: str

class OpportunitiesList(BaseModel):
    titles: List[Opportunities]
