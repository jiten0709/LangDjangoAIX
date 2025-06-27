# =========== IF USING GITHUB API =========== 

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
        model (str): The model to use.
    
    Returns:
        ChatOpenAI: An instance of the OpenAI model.
    """

    token = get_openai_api_key()
    endpoint = "https://models.github.ai/inference"
    model = "openai/gpt-4.1"

    return ChatOpenAI(
        model=model,
        temperature=0,
        max_retries=2,
        api_key=token, 
        base_url=endpoint
    )


# =========== IF USING OPENAI API =========== 

# from django.conf import settings
# from langchain_openai import ChatOpenAI


# def get_openai_api_key():
#     return settings.OPENAI_API_KEY


# def get_openai_model(model="gpt-4o"):
#     if model is None:
#         model = "gpt-4o-mini"
#     return ChatOpenAI(
#         model=model,
#         temperature=0,
#         max_retries=2,
#         api_key=get_openai_api_key(), 
#     )