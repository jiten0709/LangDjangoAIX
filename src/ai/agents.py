from langgraph.prebuilt import create_react_agent
from ai.llm import get_openai_model
from ai.tools import (
    document_tools,
    movie_discovery_tools
)
from django.conf import settings

# model = settings.GITHUB_TOKEN
model = "openai/gpt-4.1" 

def get_document_agent(model=model, checkpointer=None):
    llm_model = get_openai_model(model=model)

    agent = create_react_agent(
        model=llm_model,
        tools=document_tools,
        prompt="You are a helpful assistant in managing a user's documents within this app.",
        checkpointer=checkpointer,
        name="document-assistant"
    )

    return agent

def get_movie_discovery_agent(model=model, checkpointer=None):
    llm_model = get_openai_model(model=model)

    agent = create_react_agent(
        model=llm_model,
        tools=movie_discovery_tools,
        prompt="You are a helpful assistant in finding and discovering information about movies.",
        checkpointer=checkpointer,
        name="movie-discovery-assistant"
    )

    return agent
