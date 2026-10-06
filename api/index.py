
from fastapi import FastAPI

app = FastAPI(
    title="Web Scraping and Data Processing Pipeline",
    description="API for the Python web scraping assignment",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "project": "Web Scraping and Data Processing Pipeline",
        "status": "running",
        "description": (
            "A Python pipeline for scraping books and quotes, "
            "cleaning records, validating data, and removing duplicates."
        ),
        "endpoints": {
            "health": "/health",
            "documentation": "/docs",
        },
    }


@app.get("/health")
def health():
    return {"status": "healthy"}