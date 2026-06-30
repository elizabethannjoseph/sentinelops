from app.core.logging import setup_logging
import logging
from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title=settings.app_name)
setup_logging()

logger = logging.getLogger(__name__)

logger.info("SentinelOps backend started")

@app.get("/")
async def root():
    return {
        "application": settings.app_name,
        "message": "SentinelOps backend is running"
    }