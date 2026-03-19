# PM Dashboards — Design Standards

This repo powers `https://dawnnc.github.io/pm-dashboards/`.

---

## Favicon

Every HTML file in this repo must include the favicon. Use a relative path based on depth:

| File location | `<link>` tag |
|---|---|
| Root (`/index.html`) | `<link rel="icon" type="image/png" href="favicon.png">` |
| One level deep (`/roadmap-report-card/index.html`) | `<link rel="icon" type="image/png" href="../favicon.png">` |
| Two levels deep (`/industry-intelligence/archive/*.html`) | `<link rel="icon" type="image/png" href="../../favicon.png">` |

Place it immediately after `<meta charset="UTF-8">` in `<head>`.

The favicon file is `favicon.png` at the repo root. Do not duplicate it into subdirectories.

---

## Adding a New Dashboard

1. Create a subfolder under the repo root (e.g., `/my-dashboard/`)
2. Name the main file `index.html`
3. Include the favicon `<link>` tag at the correct relative depth
4. Add a card for it in `/index.html` following the existing card pattern
5. Commit and push — GitHub Pages deploys automatically
