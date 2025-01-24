import asyncio
from linkedin_scraper_profile import get_linkedin
from api.linkedin.linkedin_models import (
    LinkedInChecklist, Summary, VanityURL, ProfilePicture,
    BannerImage, HeadlineTitle, About, Connections,
    WorkHistoryJobTitles, WorkHistoryBullets
)
from pydantic import ValidationError

extracted_info = {}

async def main():
    linkedin_profile_url = "https://www.linkedin.com/in/williamhgates/"
    try:
        profile = await get_linkedin(linkedin_profile_url)
        # Print the profile data in JSON format for readability
        print(profile.model_dump_json(indent=2))  # Using the correct method to print JSON

        # Extracting specific profile information and saving to the extracted_info dictionary
        extracted_info.update({
            "name": profile.name,
            "headline": profile.headline,
            "city": profile.city,
            "state": profile.state,
            "country": profile.country,
            "profile_picture": profile.profile_picture,
            "public_profile_url": profile.public_profile_url,
            "banner_image": profile.banner_image,
            "connection_count": profile.connection_count,
            "summary": profile.summary,
            "education": profile.education,
            "experience": profile.experience,
            "skills": profile.skills
        })
    except ValidationError as ve:
        print("Validation error:", ve.json())
    except Exception as e:
        print("An error occurred:", str(e))

    return extracted_info

# Run the main function using asyncio's event loop
asyncio.run(main())
# Print the extracted information
print(extracted_info)
