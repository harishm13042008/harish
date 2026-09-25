from types import SimpleNamespace

from app.config import Settings
from app.services import image_generator


def test_settings_include_gemini_image_model():
    settings = Settings(gemini_api_key="test-key")
    assert settings.gemini_image_model


def test_generate_image_supports_gemini_provider(monkeypatch):
    captured = {}

    def fake_generate_image(prompt: str, filename: str = "comic_panel.png"):
        captured["prompt"] = prompt
        captured["filename"] = filename
        return "/static/generated/panel_1.png"

    monkeypatch.setattr(
        image_generator,
        "get_settings",
        lambda: SimpleNamespace(
            image_provider="gemini",
            hf_token=None,
            image_model="black-forest-labs/FLUX.1-schnell",
            gemini_image_model="imagen-3.0-generate-002",
        ),
    )
    monkeypatch.setattr(
        "app.ai.gemini_flash.generate_image",
        fake_generate_image,
    )

    result = image_generator.generate_image("a brave fox", 1)

    assert result == "/static/generated/panel_1.png"
    assert captured["prompt"] == "a brave fox"
    assert captured["filename"] == "panel_1.png"
