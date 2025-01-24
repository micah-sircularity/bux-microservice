###THIS FUNCTION RUNS AND RETURNS THE RESULT OF THE LINKEDIN PROFILE SCRAPER

import json
from config import client, logfire
from typing import Optional
from proxycurl.asyncio import Proxycurl
from pydantic import ValidationError
from api.linkedin.linkedin_models import LinkedInProfile


async def get_linkedin(url):
    proxycurl = Proxycurl()
    person = await proxycurl.linkedin.person.get(linkedin_profile_url=url,
                                               use_cache='if-recent')
    profile = LinkedInProfile(
        name=person["full_name"],
        headline=person["headline"],
        city=person["city"],
        state=person["state"],
        country=person["country"],
        summary=person["summary"],
        education=json.dumps(person["education"]),  # Serialize list to JSON string
        experience=json.dumps(person["experiences"]),  # Serialize list to JSON string
        skills=','.join(person["skills"]),  # Convert list of skills to comma-separated string
        profile_picture=person["profile_pic_url"],
        public_profile_url=person["public_identifier"],
        banner_image=person["background_cover_image_url"] or
        'https://032db1c80cd87b85bcaac172a902c818.cdn.bubble.io/f1715177256028x579450772742863700/Screenshot_2.png?_gl=1*162joo6*_gcl_au*MTg1NDE1OTQxOS4xNzEzNDYyOTA2*_ga*MzQ2MjM0NDI0LjE3MTM0NjI5MDY.*_ga_BFPVR2DEE2*MTcxNTE3NzIxMS4xNi4xLjE3MTUxNzcyMjMuNDguMC4w',  # Provide a default value
        connection_count=person["connections"])

    # Print the LinkedIn profile information
    print(f"LinkedIn Profile:\n{profile.model_dump_json(indent=2)}")
    return profile
