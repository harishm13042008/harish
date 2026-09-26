from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from app.config import get_settings


def _create_placeholder_panel_image(prompt: str, panel_number: int) -> str:
    output_dir = Path("static/generated")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"panel_{panel_number}.png"

    width, height = 1024, 1024
    image = Image.new("RGB", (width, height), color=(245, 232, 214))
    draw = ImageDraw.Draw(image)

    for y in range(0, height, 32):
        shade = 245 - (y // 12)
        draw.rectangle([0, y, width, y + 20], fill=(shade, 225, 210))

    moon_x, moon_y = 820, 180
    draw.ellipse([moon_x - 65, moon_y - 65, moon_x + 65, moon_y + 65], fill=(255, 233, 156))
    draw.ellipse([moon_x - 45, moon_y - 45, moon_x + 45, moon_y + 45], fill=(245, 232, 214))

    for hill_y in [760, 820, 880]:
        draw.ellipse([0, hill_y - 180, 420, hill_y + 60], fill=(94, 118, 95))
        draw.ellipse([300, hill_y - 220, 820, hill_y + 40], fill=(122, 146, 118))
        draw.ellipse([560, hill_y - 160, 1024, hill_y + 50], fill=(80, 102, 88))

    lantern_x, lantern_y = 470, 510
    draw.ellipse([lantern_x - 40, lantern_y - 40, lantern_x + 40, lantern_y + 40], fill=(250, 192, 85))
    draw.line([lantern_x, lantern_y + 40, lantern_x, lantern_y + 220], fill=(116, 82, 52), width=6)
    draw.rectangle([lantern_x - 30, lantern_y + 220, lantern_x + 30, lantern_y + 300], fill=(170, 125, 90))

    fox_x, fox_y = 300, 600
    draw.ellipse([fox_x - 120, fox_y - 90, fox_x + 120, fox_y + 60], fill=(202, 110, 60))
    draw.polygon([(fox_x - 30, fox_y - 30), (fox_x - 110, fox_y - 110), (fox_x + 10, fox_y - 95)], fill=(195, 96, 54))
    draw.ellipse([fox_x + 20, fox_y - 10, fox_x + 70, fox_y + 40], fill=(255, 240, 220))
    draw.ellipse([fox_x + 12, fox_y - 10, fox_x + 36, fox_y + 12], fill=(25, 22, 20))

    draw.rounded_rectangle(
        [70, 70, width - 70, height - 70],
        radius=26,
        outline=(105, 76, 57),
        width=7,
        fill=None,
    )

    title = f"Panel {panel_number}"
    try:
        font_large = ImageFont.truetype("arial.ttf", 58)
        font_small = ImageFont.truetype("arial.ttf", 28)
    except OSError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    draw.text((100, 90), title, fill=(88, 55, 42), font=font_large)

    prompt_text = prompt[:110]
    wrapped = []
    current = ""
    for word in prompt_text.split():
        if len((current + " " + word).strip()) <= 22:
            current = (current + " " + word).strip()
        else:
            wrapped.append(current)
            current = word
    if current:
        wrapped.append(current)

    y = 840
    for line in wrapped[:3]:
        draw.text((100, y), line, fill=(91, 57, 45), font=font_small)
        y += 36

    image.save(output_path)
    return f"/static/generated/{output_path.name}"


def generate_image(prompt: str, panel_number: int) -> str:
    settings = get_settings()

    if settings.image_provider == "placeholder":
        return "/static/demo-panel.svg"

    if settings.image_provider == "gemini":
        try:
            from app.ai.gemini_flash import generate_image as generate_gemini_image

            filename = f"panel_{panel_number}.png"
            return generate_gemini_image(prompt=prompt, filename=filename)
        except Exception:
            return _create_placeholder_panel_image(prompt, panel_number)

    if settings.image_provider != "hf":
        raise RuntimeError(
            f"Unsupported image provider: {settings.image_provider}. "
            "Use 'gemini', 'hf' or 'placeholder'."
        )

    if not settings.hf_token:
        raise RuntimeError(
            "HF_TOKEN is not configured. Set it in .env or enable demo mode."
        )

    from huggingface_hub import InferenceClient

    image = InferenceClient(token=settings.hf_token).text_to_image(
        prompt=prompt,
        model=settings.image_model,
    )
    output_path = Path("static/generated") / f"panel_{panel_number}.png"
    image.save(output_path)
    return f"/static/generated/{output_path.name}"
