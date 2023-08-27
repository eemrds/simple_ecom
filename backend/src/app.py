
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from src.views import router

def create_app():
    app = FastAPI(version="1.0.0")
    app.include_router(router=router)


    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Adjust this in production!
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    return app