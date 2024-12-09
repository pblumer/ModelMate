from fastapi import APIRouter
from model.graph import get_applications, add_application

router = APIRouter()

@router.get("/applications")
def list_applications():
    # Returns a list of application names from the graph
    return {"applications": get_applications()}

@router.post("/applications")
def create_application(name: str):
    # Adds an application node to the graph
    add_application(name)
    return {"status": "application_added", "name": name}
