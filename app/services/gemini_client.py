from google import genai

from app.config import get_settings


_client: genai.Client | None = None


def get_client() -> genai.Client:
    global _client

    settings = get_settings()
    if not settings.gemini_api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured. Set it in .env or enable demo mode."
        )

    if _client is None:
        _client = genai.Client(api_key=settings.gemini_api_key)

    return _client
