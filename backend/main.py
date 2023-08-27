
from dotenv import load_dotenv
import uvicorn

from src.app import create_app

load_dotenv("backend/")

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)