# LangDjangoAIX 🚀: Multi-Agent AI System with Django & LangChain

## Overview

LangDjangoAIX is a Django-based project that integrates AI agents for document management and movie discovery. It leverages language models to provide users with intelligent assistance in organizing their documents and exploring movie information.

✅ **Django-native AI Agents** - Query your ORM directly (no vector DB required)  
✅ **Role-Based Access Control** - Secure agents with [Permit.io](https://www.permit.io/)  
✅ **Multi-Agent Supervision** - Coordinate agents with [LangGraph](https://langchain.com/langgraph)  
✅ **LLM Agnostic** - Swap between OpenAI, Anthropic, local models, etc.  
✅ **Tool Creation** - Turn any Python function into an agent tool

## Features

- **Document Management:**
  - Create, retrieve, and manage documents.
  - Search documents by title or content.
  - AI-powered assistance for document-related tasks.
- **Movie Discovery:**
  - Search for movies using the TMDB API.
  - Retrieve detailed information about movies.
  - AI-driven recommendations for movie exploration.
- **User Authentication and Permissions:**
  - Built-in Django user authentication.
  - Role-based permission management using Permit.
- **AI Agents:**
  - Document management agent.
  - Movie discovery agent.
  - Supervisor agent for task assignment.

## Technologies Used

- **Django:** Web framework
- **Langchain:** Framework for building language model applications
- **OpenAI API:** Language model
- **TMDB API:** Movie database
- **Permit:** Permission management
- **uv:** Python package installer and resolver
- **SQLite:** Database

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/jiten0709/LangDjangoAIX.git
    cd LangDjangoAIX
    ```

2.  **Create a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    uv pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python src/manage.py migrate
    ```

5.  **Create a superuser:**

    ```bash
    python src/manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python src/manage.py runserver
    ```

## Configuration

- **Environment Variables:**
  - Create a `.env` file in the root directory by refering .env.example file.

## Usage

1.  **Access the Django admin interface:**

    - Navigate to `http://localhost:8000/admin/` in your browser.
    - Log in with the superuser credentials created during setup.

2.  **Create and manage documents:**

    - Use the admin interface to create, edit, and delete documents.

3.  **Interact with the AI agents:**

    - Use the provided functions in the notebooks to interact with the AI agents for document management and movie discovery.

## Key Components

- **`src/ai/`:** Contains the AI-related components.
  - `agents.py`: Defines the AI agents.
  - `llm.py`: Manages the language model.
  - `supervisor.py`: Orchestrates the AI agents.
  - `tools/`: Contains the tools used by the AI agents.
- **`src/documents/`:** Contains the Django app for document management.
  - `models.py`: Defines the document model.
  - `views.py`: Handles the document views.
- **`src/main/`:** Contains the main Django project settings.
- **`notebooks/`:** Contains Jupyter notebooks for testing and demonstration.
  - `1-django-users-permissions.ipynb`: Demonstrates Django user and permission management.
  - `2-django-built-in-permissions.ipynb`: Demonstrates Django built-in permissions.
  - `3-verify-llm-django.ipynb`: Verifies the integration of the language model with Django.
  - `4-roles-and-permissions.ipynb`: Demonstrates role-based permission management.
  - `5-ai-agent.ipynb`: Demonstrates the usage of AI agents.

## Permit Usage

- The project uses Permit for role-based access control.
- Roles and permissions are defined in the notebooks.
- The `mypermit` package is used to interact with the Permit API.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

##
