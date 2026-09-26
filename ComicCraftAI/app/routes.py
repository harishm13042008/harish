from fastapi import (
    APIRouter,
    Form,
    HTTPException,
    Request,
)

from fastapi.responses import (
    HTMLResponse,
)

from fastapi.templating import (
    Jinja2Templates,
)

from app.models import PromptRequest

from app.services.comic_service import (
    generate_comic,
)

from app.services.image_generator import (
    generate_image,
)


router = APIRouter()

templates = Jinja2Templates(
    directory="templates"
)


@router.get(
    "/",
    response_class=HTMLResponse,
)
def home(request: Request):

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "request": request
        },
    )


@router.post(
    "/generate",
    response_class=HTMLResponse,
)
def generate(
    request: Request,

    story_prompt: str = Form(...),

    character_name: str = Form(...),

    setting: str = Form(...),

    tone: str = Form(...),

    art_style: str = Form(...),
):

    try:

        payload = PromptRequest(
            story_prompt=story_prompt,
            character_name=character_name,
            setting=setting,
            tone=tone,
            art_style=art_style,
        )

        comic = generate_comic(
            payload
        )

        return templates.TemplateResponse(
            request,
            "comic_preview.html",
            {
                "request": request,
                "comic": comic,
                "pdf_url": comic.get("pdf_url"),
            },
        )

    except Exception as exc:

        return templates.TemplateResponse(
            request,
            "error.html",
            {
                "request": request,
                "message": str(exc),
            },
            status_code=500,
        )


@router.post(
    "/generate-comic/json"
)
def generate_json(
    payload: PromptRequest,
):

    try:

        return generate_comic(
            payload
        )

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc


@router.get(
    "/export-success",
    response_class=HTMLResponse,
)
def export_success(
    request: Request,
    pdf_url: str | None = None,
):

    return templates.TemplateResponse(
        request,
        "export_success.html",
        {
            "request": request,
            "pdf_url": pdf_url,
        },
    )


@router.get(
    "/test-image"
)
def test_image(
    prompt: str = (
        "A friendly fox exploring "
        "an enchanted forest, "
        "comic book art"
    ),
):

    try:

        image_url = generate_image(
            prompt,
            0,
        )

        return {
            "image_url": image_url
        }

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        ) from exc