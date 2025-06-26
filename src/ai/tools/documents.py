from documents.models import Document
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from django.db.models import Q
from asgiref.sync import async_to_sync
from mypermit import permit_client as permit
from typing import Optional

@tool
def search_query_documents(query: str, limit: int = 5, config: RunnableConfig = {}):
    """
    Search the most recent LIMIT documents for the current user  with maximum of 25.

    arguments:
    query: string or lookup search across title or content of document
    limit: number of results
    """

    if limit > 25:
        limit = 25

    configurable = config.get('configurable') or config.get('metadata')
    if not configurable:   
        raise Exception("Configuration is required to search documents.")
    user_id = configurable.get('user_id')
    default_lookups = {
        "active": True
    }
    has_permissions = async_to_sync(permit.check)(f"{user_id}", "read", "document")
    if not has_permissions:
        raise Exception("You do not have permission to search the documents.")
    
    queryset = Document.objects.filter(**default_lookups).filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).order_by("-created_at")
    response_data = []
    for obj in queryset[:limit]:
        response_data.append({
            "id": obj.pk,
            "title": obj.title
        })

    return response_data

@tool
def list_documents(limit: int = 5, config: RunnableConfig = {}):
    """
    List the most recent LIMIT documents for the current user with maximum of 25.

    agruments
    limit: number of results
    """

    if limit > 25:
        limit = 25
    configurable = config.get('configurable') or config.get('metadata')
    if not configurable:
        raise Exception("Configuration is required to list documents.")
    user_id = configurable.get('user_id')
    has_perms = async_to_sync(permit.check)(f"{user_id}", "read", "document")
    if not has_perms:
        raise Exception("You do not have permission to list all documents.")
    qs = Document.objects.filter(active=True).order_by("-created_at")
    response_data = []
    for obj in qs[:limit]:
        response_data.append(
            {
                "id": obj.pk,
                "title": obj.title
            }
        )
    return response_data

@tool
def get_document(document_id: int, config: RunnableConfig = {}):
    """
    Get a document by its ID.

    arguments:
    document_id: ID of the document to retrieve
    """
    configurable = config.get('configurable') or config.get('metadata')
    if not configurable:
        raise Exception("Configuration is required to get the document.")
    user_id = configurable.get('user_id')
    has_perms = async_to_sync(permit.check)(f"{user_id}", "read", "document")
    if not has_perms:
        raise Exception("You do not have permission to get the document.")
    
    try:
        obj = Document.objects.get(pk=document_id, active=True)
    except Document.DoesNotExist:
        raise Exception("Document not found.")
    except Exception as e:
        raise Exception(f"An error occurred while retrieving the document: {str(e)}")
    
    response_data = {
        "pk": obj.pk,
        "title": obj.title,
        "content": obj.content,
        "created_at": obj.created_at.isoformat(),
    }

    return response_data

@tool
def create_document(title: str, content: str = "", config: RunnableConfig = {}):
    """
    Create a new document.

    arguments:
    title: Title of the document
    content: Content of the document (optional)
    """
    
    configurable = config.get('configurable') or config.get('metadata')
    if not configurable:
        raise Exception("Configuration is required to create a document.")
    user_id = configurable.get('user_id') 
    has_perms = async_to_sync(permit.check)(f"{user_id}", "create", "document")
    if not has_perms:
        raise Exception("You do not have permission to create a document.")
    
    document = Document.objects.create(
        owner_id=user_id,
        title=title,
        content=content,
        active=True
    )

    response_data = {
        "pk": document.pk,
        "title": document.title,
        "content": document.content,
        "created_at": document.created_at.isoformat(),
    }

    return response_data

def update_document(document_id: int, title: Optional[str] = None, content: Optional[str] = None, config: RunnableConfig = {}):
    """
    Update a document by its ID.

    arguments:
    document_id: ID of the document to update
    title: New title for the document (optional)
    content: New content for the document (optional)
    """
    
    configurable = config.get('configurable') or config.get('metadata')
    if not configurable:
        raise Exception("Configuration is required to update the document.")
    user_id = configurable.get('user_id')
    has_perms = async_to_sync(permit.check)(f"{user_id}", "update", "document")
    if not has_perms:
        raise Exception("You do not have permission to update the document.")
    
    try:
        obj = Document.objects.get(pk=document_id, active=True)
        if title is not None:
            obj.title = title
        if content is not None:
            obj.content = content
        obj.save()
    except Document.DoesNotExist:
        raise Exception("Document not found.")
    
    response_data = {
        "pk": obj.pk,
        "title": obj.title,
        "content": obj.content,
        "created_at": obj.created_at.isoformat(),
    }

    return response_data

@tool
def delete_document(document_id: int, config: RunnableConfig = {}):
    """
    Delete a document by its ID.

    arguments:
    document_id: ID of the document to delete
    """
    
    configurable = config.get('configurable') or config.get('metadata')
    if not configurable:
        raise Exception("Configuration is required to delete the document.")
    user_id = configurable.get('user_id')
    has_perms = async_to_sync(permit.check)(f"{user_id}", "delete", "document")
    if not has_perms:
        raise Exception("You do not have permission to delete the document.")
    
    try:
        obj = Document.objects.get(pk=document_id, active=True)
        obj.delete()
    except Document.DoesNotExist:
        raise Exception("Document not found.")
    
    return {"message": "Document deleted successfully."}

document_tools = [
    search_query_documents,
    list_documents,
    get_document,
    create_document,
    update_document,
    delete_document
]
