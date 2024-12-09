from fastapi import APIRouter, HTTPException
from src.model.graph import (
    add_application,
    get_applications,
    add_business_capability,
    get_business_capabilities,
    add_relationship,
)

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

@router.post("/relationships")
def create_relationship(source: str, target: str, relation_type: str):
    try:
        add_relationship(source, target, relation_type)
        return {
            "status": "relationship_added",
            "source": source,
            "target": target,
            "relation_type": relation_type,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
