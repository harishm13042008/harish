# Data Flow Diagram

**Project Title:** Comic Craft AI: AI Comic Story Creator using Gemini Models  
**Team ID:** SWUID2026383027  
**Team Size:** 4  
**Team Leader:** Harish M  
**Team Members:** Bhuvanesh, Gowtham S, V Sanjay Kumar

## DFD Level 0 (Context Level)

| Element | Type | Description |
|---|---|---|
| User | External Entity | Provides story idea, style and character details; receives the finished comic |
| Comic Craft AI System | Process | Converts story prompt into scripted panels and images using Gemini models |
| Gemini Models (API) | External System | Generates story script and panel images |
| Comic Storage / Export | Data Store | Holds generated comics for download |

## DFD Level 1

| Process ID | Process Name | Input | Output | Data Store / System Used |
|---|---|---|---|---|
| 1.0 | Collect User Input | Story idea, genre, style, characters | Validated prompt | Session data |
| 2.0 | Generate Story Script | Validated prompt | Panel-wise script with dialogue and scene descriptions | Gemini text model |
| 3.0 | Generate Panel Images | Scene descriptions and character sheet | Comic panel images | Gemini image model |
| 4.0 | Compose Comic Layout | Panel images and dialogue | Complete comic page with speech bubbles | Image processing (Pillow) |
| 5.0 | Preview, Edit and Export | Composed comic, user edits | Final PDF/PNG comic | Comic storage |

## Data Flow Summary

| Flow ID | From | To | Data |
|---|---|---|---|
| F1 | User | Process 1.0 | Story idea and preferences |
| F2 | Process 1.0 | Process 2.0 | Structured prompt |
| F3 | Process 2.0 | Process 3.0 | Panel scene descriptions |
| F4 | Process 3.0 | Process 4.0 | Generated panel images |
| F5 | Process 4.0 | Process 5.0 | Composed comic |
| F6 | Process 5.0 | User | Final downloadable comic |
