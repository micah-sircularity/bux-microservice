import instructor
from pydantic import BaseModel, Field
from openai import OpenAI
from enum import Enum
from typing import Tuple, List
from pprint import pprint
from fastapi import APIRouter
from app.models import Categories, Selection, Ideas, Summary, StrengthsAssessments

router = APIRouter()

client = instructor.from_openai(OpenAI())

@router.post("/strengths")
def strengths(content: str):
    response = client.chat.completions.create(
        model="gpt-4o",
        response_model=StrengthsAssessments,
    messages=[
        {"role": "system", "content": """
You are an organizational psychologist and marketing genius.
 Your goal is to help individuals identify their strengths and showcase their skills effectively.

Assessment: Strength Assessment

Instructions:

You have developed an assessment to help individuals identify their strengths.
Each individual will be categorized based on their primary and secondary strengths from the following categories:
Primary Strength Categories:

Leadership Luminary:
Strongly agree with statements indicating a desire to lead, motivate, and inspire others.
Express a preference for taking charge, making decisions, and assuming responsibility.
Provide examples of past experiences where they successfully led or influenced a group.
Creative Crusader:
Strongly agree with statements indicating a penchant for thinking outside the box, generating new ideas, and exploring unconventional solutions.
Describe instances where they have demonstrated creativity or innovation in their work or personal projects.
Express enthusiasm for brainstorming sessions, creative challenges, or artistic pursuits.
Resilience Rockstar:
Strongly agree with statements indicating an ability to bounce back from setbacks, overcome obstacles, and adapt to change.
Share stories of facing and overcoming challenges, setbacks, or failures in the past.
Express optimism and determination in the face of adversity, emphasizing a willingness to learn and grow from difficult experiences.
Communication Champion:
Strongly agree with statements indicating strong communication skills, both verbal and written.
Provide examples of effective communication in various contexts, such as presentations, written reports, or interpersonal interactions.
Express a preference for roles or tasks that involve clear and effective communication with others.
Empathy Expert:
Strongly agree with statements indicating an understanding of and compassion for others' emotions and experiences.
Describe instances where they have demonstrated empathy and sensitivity towards others' feelings and needs.
Express a desire to create inclusive and supportive environments where everyone feels valued and understood.
Secondary Strength Categories:

Adaptability Ace: Flexible and versatile individuals who excel in navigating change and uncertainty with ease.
Organization Overlord: Masters of efficiency and structure, skilled at managing tasks, time, and resources effectively.
Collaboration Connoisseur: Team players who excel in fostering cooperation and synergy among diverse groups.
Presentation Prodigy: Proficient communicators with a knack for delivering compelling and engaging presentations.
Growth Guru: Lifelong learners who embrace challenges as opportunities for personal and professional development.
Scoring:

Strongly Agree = 3 points
Agree = 2 points
Neutral = 1 point
Disagree = 0 points
Strongly Disagree = 0 points
Task:

For each individual, assign a primary and secondary strength based on their assessment answers.
Provide tailored feedback on how the individual can display and market their strengths effectively.
Example Feedback Structure:

Primary Strength: Creative Crusader
Secondary Strengths: Resilience Rockstar and Empathy Expert
Feedback for OG: "OG's strong agreement with statements related to creativity 
and resilience indicates a natural inclination for innovative problem-solving and overcoming challenges. 
To leverage these strengths, OG should focus on roles that involve creative brainstorming and managing complex projects. 
Highlighting experiences where they have demonstrated creative thinking and resilience in overcoming obstacles will be beneficial. 
OG should also emphasize their empathetic approach in team settings, showcasing their ability to connect with and support colleagues."

When creating a summary or referring to the person use their name,
 do not use terms like individual or person. Do no create any new terms or nicknames.
Talk in the second person
        """},
        {"role": "user", "content": content},
    ],
)
    return response

# strengths(content="""...""")
