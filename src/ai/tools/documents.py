from documents.models import Document
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from django.db.models import Q
from asgiref.sync import async_to_sync
from mypermit import permit_client as permit

