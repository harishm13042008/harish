# Solution Architecture

**Project Title:** Comic Craft AI: AI Comic Story Creator using Gemini Models  
**Team ID:** SWUID2026383027  
**Team Size:** 4  
**Team Leader:** Harish M  
**Team Members:** Bhuvanesh, Gowtham S, V Sanjay Kumar

## Architecture Layers

| Layer | Component | Technology | Description |
|---|---|---|---|
| Presentation | Web UI | Streamlit / HTML-CSS-JS | Story input, style selection, comic preview, download |
| Application | Backend Logic | Python | Handles prompt building, request flow and comic composition |
| AI Story Engine | Text Generation | Gemini text model (Google Gemini API) | Creates panel-wise script, dialogue and scene descriptions |
| AI Image Engine | Image Generation | Gemini image model | Generates panel artwork in the selected style |
| Composition | Layout Engine | Pillow / ReportLab | Places images, speech bubbles and captions into pages |
| Storage | Output Storage | Local storage / cloud bucket | Saves generated comics as PNG/PDF |
| Security | API Key Handling | Environment variables | Keeps Gemini API key private |

## Request Flow

| Step | Action |
|---|---|
| 1 | User submits story idea, genre, style and characters |
| 2 | Backend builds a structured prompt |
| 3 | Gemini text model returns panel script with dialogue |
| 4 | Gemini image model generates each panel using the character sheet |
| 5 | Layout engine composes panels and speech bubbles |
| 6 | User previews, edits and exports the comic |
