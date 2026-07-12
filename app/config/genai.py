from google import genai

from app.config.settings import settings

client = genai.Client(
    api_key=settings.GOOGLE_API_KEY
)