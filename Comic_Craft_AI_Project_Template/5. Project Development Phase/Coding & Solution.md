# Coding & Solution

**Project Title:** Comic Craft AI: AI Comic Story Creator using Gemini Models  
**Team ID:** SWUID2026383027  
**Team Size:** 4  
**Team Leader:** Harish M  
**Team Members:** Bhuvanesh, Gowtham S, V Sanjay Kumar

## Module-wise Implementation

| S.No | Module | File Name | Description | Technology | Developed By |
|---|---|---|---|---|---|
| 1 | Main Application | app.py | Streamlit interface that takes story idea, style and characters and shows the comic | Python, Streamlit | Bhuvanesh |
| 2 | Story Generator | story_generator.py | Sends structured prompt to Gemini text model and returns panel script with dialogue | Python, Gemini API | Gowtham S |
| 3 | Image Generator | image_generator.py | Generates each panel image using Gemini image model and the character sheet | Python, Gemini API | Harish M |
| 4 | Comic Composer | comic_composer.py | Places panels, speech bubbles and captions into a page layout | Python, Pillow | Bhuvanesh |
| 5 | Exporter | exporter.py | Exports the final comic to PNG and PDF | Python, ReportLab | V Sanjay Kumar |
| 6 | Configuration | config.py | Loads API key and settings from environment variables | Python, dotenv | Gowtham S |

## Key Solution Features

| Feature | Implementation Approach |
|---|---|
| Story to script | Prompt asks Gemini for N panels with scene description, characters and dialogue in JSON |
| Character consistency | A character description sheet is reused in every image prompt |
| Style control | Style keywords (manga, cartoon, superhero, watercolor) appended to image prompts |
| Panel editing | User edits text and regenerates only the selected panel |
| Export | Composed pages saved as PNG and combined into a PDF |
