from fastapi import APIRouter, HTTPException
from src.model.graph import add_application, get_applications, add_business_capability, get_business_capabilities

router = APIRouter()

@router.get("/applications")
def list_applications():
    apps = get_applications()
    return {"applications": apps}

@router.post("/applications")
def create_application(name: str, description: str = ""):
    add_application(name, description)
    return {"status": "application_added", "name": name}

@router.get("/business_capabilities")
def list_business_capabilities():
    capabilities = get_business_capabilities()
    return {"business_capabilities": capabilities}

@router.post("/business_capabilities")
def create_business_capability(name: str, description: str = ""):
    add_business_capability(name, description)
    return {"status": "business_capability_added", "name": name}
