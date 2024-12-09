import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

from src.api.endpoints import router as api_router
from fastapi import FastAPI

app = FastAPI(title="ModelMates PoC")

# Include the API routes
app.include_router(api_router)
