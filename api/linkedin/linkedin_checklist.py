###THIS ROUTE RUNS AND RETURNS THE RESULT OF THE LINKEDIN CHECKLIST BY FETCHING THE LINKEDINPROFILE 
from typing import List, Optional

import instructor
from config import client, logfire
from fastapi import APIRouter
from openai import OpenAI
from api.linkedin.linkedin_models import (
    LinkedInChecklist, Summary, VanityURL, ProfilePicture,
    BannerImage, HeadlineTitle, About, Connections,
    WorkHistoryJobTitles, WorkHistoryBullets, Score
)

from .linkedin_scraper_profile import get_linkedin

router = APIRouter()

# Initialize the instructor client
openai_client = OpenAI()
client = instructor.from_openai(openai_client, mode=instructor.Mode.MD_JSON)
logfire.instrument_openai(openai_client)
logfire.configure(pydantic_plugin=logfire.PydanticPlugin(record="all"))

# Asynchronous function to scrape LinkedIn profiles
async def main(url):
    url = url
    profile = await get_linkedin(url)

    profile_url = profile.profile_picture
    banner_image = profile.banner_image

    linkedin_text = (f"name: {profile.name}\n"
                     f"headline: {profile.headline}\n"
                     f"city: {profile.city}\n"
                     f"state: {profile.state}\n"
                     f"country: {profile.country}\n"
                     f"summary: {profile.summary}\n"
                     f"education: {profile.education}\n"
                     f"experience: {profile.experience}\n"
                     f"skills: {profile.skills}\n"
                     f"connection_count: {profile.connection_count}")

    return linkedin_text, profile_url, banner_image

@logfire.instrument("read_linkedin_images", extract_args=True)
def read_images(text_input: str, image_urls: List[str]) -> LinkedInChecklist:
    valid_image_urls = [url for url in image_urls if url.startswith("http")]

    print(f"Evaluating with text: {text_input}")
    for url in valid_image_urls:
        print(f"Testing Image URL: {url}")

    return client.chat.completions.create(
        model="accounts/fireworks/models/llama-v3p1-8b-instruct",
        response_model=LinkedInChecklist,
        temperature=0,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"""Evaluate the following 
                        LinkedIn profile text refer to the person as if you are 
                        talking to them:
                        \n{text_input}""",
                },
                *[{
                    "type": "image_url",
                    "image_url": {
                        "url": url
                    }
                } for url in image_urls],
            ],
        }],
    )

### API ENDPOINT
@router.post("/linkedin_checklist", response_model=LinkedInChecklist)
async def linkedin_checklist_api(url: str) -> LinkedInChecklist:
    """
    API Endpoint to analyze a LinkedIn profile.
    Args:
        url (str): The LinkedIn profile URL to analyze.
    Returns:
        LinkedInChecklist: The profile analysis.
    """
    linkedin_text, profile_url, banner_image = await main(url)
    linkedin_text += f"\nLinkedIn URL: {url}"
    result = read_images(linkedin_text, [profile_url, banner_image])
    return result
