from pathlib import Path

from google.genai import types

from app.config import get_settings
from app.models import OutlineResponse, PromptRequest
from app.services.gemini_client import get_client


settings = get_settings()

OUTPUT_DIR = Path("static/generated")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_outline(request: PromptRequest) -> list[dict]:
    prompt = f"""
Create a coherent {settings.panel_count}-panel comic outline.

Story idea:
{request.story_prompt}

Main character:
{request.character_name}

Setting:
{request.setting}

Tone:
{request.tone}

Art style:
{request.art_style}

Requirements:

1. Create exactly {settings.panel_count} panels.
2. Number panels from 1 to {settings.panel_count}.
3. Maintain character and setting continuity.
4. Each panel needs a short title, scene description, and detailed image prompt.
5. Image prompts must describe characters, environment, action, composition, lighting, and visual style.
6. Do not include speech bubbles or written dialogue inside the image.
7. Give the story a clear beginning, middle, and ending.
"""

    client = get_client()
    response = client.models.generate_content(
        model=settings.gemini_outline_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.9,
            response_mime_type="application/json",
            response_schema=OutlineResponse,
        ),
    )

    parsed = response.parsed
    if parsed is None:
        parsed = OutlineResponse.model_validate_json(response.text)

    return [panel.model_dump() for panel in parsed.panels]


def generate_image(
    prompt: str,
    filename: str = "comic_panel.png",
) -> str:
    """
    Generate an AI image using Gemini and save it locally.
    """

    client = get_client()

    response = client.models.generate_content(
        model=settings.gemini_image_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
        ),
    )

    if not response.candidates:
        raise RuntimeError("Gemini did not return any image.")

    for candidate in response.candidates:
        if not candidate.content:
            continue

        for part in candidate.content.parts:
            if part.inline_data is not None:
                image_data = part.inline_data.data

                if not image_data:
                    continue

                output_path = OUTPUT_DIR / filename

                with open(output_path, "wb") as image_file:
                    image_file.write(image_data)

                return f"/static/generated/{filename}"

    raise RuntimeError("Gemini response did not contain an image.")


def generate_test_image() -> str:
    """
    Generate a test comic image.
    """

    prompt = """
    Create a high-quality comic book illustration.

    Scene:
    A young adventurous explorer walking through a magical futuristic city.

    Visual style:
    Detailed professional comic book art,
    cinematic composition,
    dynamic perspective,
    dramatic lighting,
    vibrant colors,
    expressive character,
    detailed background.

    Important:
    - No speech bubbles
    - No written text
    - No captions
    - No logos
    - Single comic panel
    """

    return generate_image(
        prompt=prompt,
        filename="test_comic_panel.png",
    )
    