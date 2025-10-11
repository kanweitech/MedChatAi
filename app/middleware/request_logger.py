import logging
from fastapi import Request

# Configure logging (only once)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def log_requests(request: Request, call_next):
    """
    Middleware to log incoming HTTP requests.
    """
    logger.info(f"📥 Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"📤 Response status: {response.status_code}")
    return response
