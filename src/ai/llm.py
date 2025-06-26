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
    if model is None:
        model = "gpt-4o-mini"
    return ChatOpenAI(
        model=model,
        temperature=0,
        max_retries=2,
        api_key=get_openai_api_key(), 
    )
