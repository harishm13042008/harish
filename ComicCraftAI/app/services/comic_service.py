from pathlib import Path
from uuid import uuid4

from fpdf import FPDF

from app.ai.gemini_flash import generate_outline
from app.config import get_settings
from app.models import PromptRequest
from app.services.image_generator import generate_image


def _demo_outline(request: PromptRequest) -> list[dict]:
    panel_count = get_settings().panel_count
    return [
        {
            "number": number,
            "title": f"Panel {number}",
            "scene_description": (
                f"{request.character_name} continues the story in "
                f"{request.setting}."
            ),
            "image_prompt": (
                f"{request.art_style} comic art of {request.character_name} "
                f"in {request.setting}, panel {number}, {request.tone} tone."
            ),
        }
        for number in range(1, panel_count + 1)
    ]


def _generate_pdf_file(comic: dict) -> str:
    output_dir = Path("static/generated")
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_name = f"comic_{uuid4().hex}.pdf"
    pdf_path = output_dir / pdf_name

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, txt=comic["character_name"] + "'s Comic", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 8, comic["story_prompt"])

    for panel in comic["panels"]:
        image_url = panel.get("image_url", "")
        if not image_url:
            continue

        image_path = Path(".") / image_url.lstrip("/")
        if image_path.exists():
            pdf.add_page()
            pdf.set_font("Helvetica", "B", 14)
            pdf.cell(0, 10, txt=f"Panel {panel['number']}: {panel.get('title', '')}", ln=True)
            pdf.image(str(image_path), x=10, y=25, w=190)
            pdf.ln(130)
            pdf.set_font("Helvetica", "", 10)
            pdf.multi_cell(0, 6, panel.get("scene_description", ""))

    pdf.output(str(pdf_path))
    return f"/static/generated/{pdf_name}"


def generate_comic(request: PromptRequest) -> dict:
    settings = get_settings()
    try:
        panels = (
            _demo_outline(request)
            if settings.demo_mode
            else generate_outline(request)
        )
    except Exception:
        panels = _demo_outline(request)
    comic = {
        "story_prompt": request.story_prompt,
        "character_name": request.character_name,
        "panels": panels,
        "pdf_url": "",
    }

    for panel in comic["panels"]:
        panel["image_url"] = generate_image(
            panel["image_prompt"],
            panel["number"],
        )

    comic["pdf_url"] = _generate_pdf_file(comic)
    return comic
