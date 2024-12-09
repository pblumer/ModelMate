from fastapi import FastAPI
from src.api.endpoints import router as api_router

app = FastAPI(title="ModelMates PoC")

# Include the API routes
app.include_router(api_router)
