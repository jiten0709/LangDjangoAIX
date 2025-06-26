from django.conf import settings
from langchain_openai import ChatOpenAI
from typing import Optional

def get_openai_api_key():
    """
    Retrieve the OpenAI API key from Django settings.
    """
    return settings.GITHUB_TOKEN

def get_openai_model(model: Optional[str] = None):
    """
    Get an instance of the OpenAI model with specified parameters.
    
    Args:
        model (str): The model to use, defaults to "gpt-4o".
    
    Returns:
        ChatOpenAI: An instance of the OpenAI model.
    """

    token = get_openai_api_key()
    endpoint = "https://models.github.ai/inference"
    model = "openai/gpt-4.1"

    if model is None:
        model = "openai/gpt-4.1"
    return ChatOpenAI(
        model=model,
        temperature=0,
        max_retries=2,
        api_key=token, 
        base_url=endpoint
    )
