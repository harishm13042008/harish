# Code-Layout, Readability and Reusability

**Project Title:** Comic Craft AI: AI Comic Story Creator using Gemini Models  
**Team ID:** SWUID2026383027  
**Team Size:** 4  
**Team Leader:** Harish M  
**Team Members:** Bhuvanesh, Gowtham S, V Sanjay Kumar

## Project Folder Layout

| Path | Purpose |
|---|---|
| app.py | Entry point and UI |
| modules/story_generator.py | Story and script generation |
| modules/image_generator.py | Panel image generation |
| modules/comic_composer.py | Layout and speech bubbles |
| modules/exporter.py | PNG/PDF export |
| config.py | Settings and API key loading |
| requirements.txt | Python dependencies |
| assets/ | Fonts, bubble templates, sample outputs |
| tests/ | Unit and integration tests |

## Code Quality Practices

| Aspect | Practice Followed | Owner |
|---|---|---|
| Layout | Modular structure with one responsibility per file | Harish M |
| Readability | Meaningful names, PEP 8 style, docstrings and inline comments | Bhuvanesh |
| Reusability | Functions accept parameters (style, panels, characters) so they can be reused | Gowtham S |
| Configuration | API keys and constants kept outside code in environment variables | Gowtham S |
| Error Handling | Try-except around API calls with clear user messages and retries | V Sanjay Kumar |
| Version Control | Git with meaningful commit messages and branches per feature | Harish M |
