from fastapi import FastAPI
from .routers import items, users

# Create the FastAPI app
app = FastAPI()

# Include the routers
app.include_router(items.router)
app.include_router(users.router)

# Root endpoint for testing 
@app.get("/")
async def root():
    return {"message": "Hello World"}