import os
from typing import Optional
import instructor
from openai import OpenAI
import logfire

def create_client() -> OpenAI:
    """
    Creates and configures an OpenAI client with Fireworks API integration.
    
    Returns:
        OpenAI: Configured OpenAI client with instructor and logfire instrumentation
        
    Raises:
        ValueError: If FIREWORKS_API_KEY environment variable is not set
    """
    base_url: str = "https://api.fireworks.ai/inference/v1"
    api_key: Optional[str] = os.getenv("FIREWORKS_API_KEY")
    if not api_key:
        raise ValueError("FIREWORKS_API_KEY is not set in the environment variables.")

    original_client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )

    # Instrument the original client before creating the Instructor instance
    logfire.configure(pydantic_plugin=logfire.PydanticPlugin(record="all"))
    logfire.instrument_openai(original_client)

    # Now apply the Instructor patch to the original client
    instructor_client = instructor.patch(
        original_client,
        # Customize further if other modes or configurations are needed
    )

    # Convert to Instructor with Mode.MD_JSON
    client = instructor.from_openai(instructor_client, mode=instructor.Mode.MD_JSON)
    return client

client: OpenAI = create_client()