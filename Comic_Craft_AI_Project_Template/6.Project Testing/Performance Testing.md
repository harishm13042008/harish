# Performance Testing

**Project Title:** Comic Craft AI: AI Comic Story Creator using Gemini Models  
**Team ID:** SWUID2026383027  
**Team Size:** 4  
**Team Leader:** Harish M  
**Team Members:** Bhuvanesh, Gowtham S, V Sanjay Kumar

## Model Performance Testing

| S.No | Parameter | Values / Screenshot |
|---|---|---|
| 1 | Story Script Quality (panels follow the prompt) | Evaluated on 20 sample prompts; script matched the requested story in 18 of 20 |
| 2 | Panel Image Relevance | Images matched scene description in 17 of 20 prompts |
| 3 | Character Consistency | Character stayed recognisable across panels in 16 of 20 comics |
| 4 | Average Story Generation Time | About 5-8 seconds |
| 5 | Average Time per Panel Image | About 8-15 seconds |
| 6 | Average Time for a 6-Panel Comic | About 60-100 seconds |
| 7 | Export Time (PDF/PNG) | Under 3 seconds |

## Test Cases

| Test ID | Scenario | Input | Expected Result | Result | Tester |
|---|---|---|---|---|---|
| TC-01 | Valid story prompt | "A brave robot saves a village" | Comic with panels and dialogue generated | Pass | V Sanjay Kumar |
| TC-02 | Empty prompt | (blank) | Validation message shown | Pass | V Sanjay Kumar |
| TC-03 | Style selection | Manga style | Panels drawn in manga style | Pass | Bhuvanesh |
| TC-04 | Panel regenerate | Edit panel 3 dialogue | Only panel 3 updates | Pass | Harish M |
| TC-05 | Export PDF | Click download PDF | PDF downloads with all panels | Pass | V Sanjay Kumar |
| TC-06 | Invalid API key | Wrong key | Clear error message, no crash | Pass | Gowtham S |
| TC-07 | Long prompt | 1000-word story | Handled or trimmed gracefully | Pass | Gowtham S |
