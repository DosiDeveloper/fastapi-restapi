from fastapi import FastAPI
from routes.user import user_routes

app = FastAPI(
    title="My first API",
    description="This is my first API with Fastapi",
    version="0.0.1",
    openapi_tags=[{
        "name": "Users",
        "description": "Users routes"
    }]
)

app.include_router(user_routes)

@app.get("/")
def index():
    return {"version": "alpha"}
