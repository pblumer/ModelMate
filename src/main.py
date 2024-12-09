from fastapi import FastAPI
from api.endpoints import router as api_router

app = FastAPI(title="ModelMates PoC")

# Include the API routes
app.include_router(api_router)

# For running the server (uvicorn) if needed:
# uvicorn src.main:app --reload
