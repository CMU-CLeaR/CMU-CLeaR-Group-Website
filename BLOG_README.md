# CMU-CLeaR Blog Contributor Guide

This guide outlines the workflow for contributing research blog posts to the CMU-CLeaR group website. The site is built with Jekyll using the `al-folio` template with `distill` layout support.

---

## 1. Lifecycle of a Blog Post

1.  **Drafting**: Create a file in `_drafts/` to work privately.
2.  **Previewing**: Run a local server to see changes in real-time.
3.  **Publishing**: Move the file to `_posts/` and submit a Pull Request.
4.  **Deployment**: Once merged to `main`, the post goes live automatically.

---

## 2. Writing Your Post

### File Naming
Files must follow the format: `YYYY-MM-DD-title-of-post.md` (e.g., `2026-02-01-identifiability.md`).

### Front Matter (Template)
Every post starts with a YAML header. Use the following template for consistency:

```yaml
---
layout: distill
title: "Your Post Title"
description: "A brief summary for the blog list page"
date: 2026-02-01

# Citations (Optional)
bibliography: 2026-02-01-identifiability.bib

authors:
  - name: Your Name
    url: "https://your-website.com"
    affiliations:
      name: CLeaR, CMU

toc:
  - name: Introduction
  - name: Main Theory
---
```

### Content Features
- **Math**: Use `$$...$$` for both inline math and display blocks (MathJax).
- **Citations**: Use `<d-cite key="ref_id"></d-cite>` to cite from your `.bib` file.
- **Asides**: Use `<aside>Your side note here</aside>` for marginalia.

---

## 3. Assets & Bibliography

To keep the repository clean, please follow these directory conventions:

- **Images**: Place in `assets/img/blogs/YYYY-MM-DD-title/`.
  - *Reference as*: `/dietrich/causality/assets/img/blogs/YYYY-MM-DD-title/fig1.png`
- **Bibliography**: Place in `assets/bibliography/`.
  - *Name*: `YYYY-MM-DD-title.bib`

---

## 4. Local Development & Preview

We recommend using Docker to ensure your environment matches the production server.

```bash
# Preview WITH drafts (Development mode)
JEKYLL_DRAFTS=true docker-compose up --build

# Preview WITHOUT drafts (Production mode)
docker-compose up --build
```
View the site at: `http://localhost:8080/dietrich/causality/blog/`.

---

## 5. Submission Workflow

We use a branch-based PR workflow. If you are working on multiple posts, create a separate branch for each.

### Step 1: Create a Feature Branch
```bash
git checkout -b blog/your-post-title
```

### Step 2: Finalize for Publication
Move your post from the drafts folder to the posts folder:
```bash
mv _drafts/YYYY-MM-DD-title.md _posts/YYYY-MM-DD-title.md
```

### Step 3: Commit & Push
```bash
git add .
git commit -m "Add blog post: [Title]"
git push origin blog/your-post-title
```

### Step 4: Create a Pull Request
Use the GitHub CLI or web interface to create a PR against the `main` branch. Provide a brief summary of the post's contributions.

---

## Tips & Troubleshooting
- **Live Reload**: The Docker container supports live reload. Most changes show up instantly after saving, but changes to `_config.yml` require a container restart.
- **Base URL**: Always include `/dietrich/causality` in hardcoded links to assets.
- **Clean Up**: If Docker acts up, run `docker-compose down` followed by a fresh `up --build`.
