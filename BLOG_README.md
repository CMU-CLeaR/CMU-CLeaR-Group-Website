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

## 5. Submission Workflow (Fork-based)

We use a **fork-based PR workflow** to keep the main repository clean. All contributors (including group members) should follow this process.

### First-Time Setup

```bash
# 1. Fork the repository on GitHub (click "Fork" button on the repo page)

# 2. Clone YOUR fork (not the original repo)
git clone https://github.com/YOUR-USERNAME/CMU-CLeaR-Group-Website.git
cd CMU-CLeaR-Group-Website

# 3. Add the original repo as "upstream" for syncing
git remote add upstream https://github.com/CMU-CLeaR/CMU-CLeaR-Group-Website.git

# Verify remotes
git remote -v
# origin    https://github.com/YOUR-USERNAME/CMU-CLeaR-Group-Website.git (your fork)
# upstream  https://github.com/CMU-CLeaR/CMU-CLeaR-Group-Website.git (original)
```

### Contributing a New Post

```bash
# 1. Ensure your main branch is up-to-date with upstream
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# 2. Create a feature branch
git checkout -b blog/your-post-title

# 3. Write your post in _drafts/, add images and .bib files

# 4. When ready to publish, move to _posts/
mv _drafts/YYYY-MM-DD-title.md _posts/YYYY-MM-DD-title.md

# 5. Commit and push to YOUR fork
git add .
git commit -m "Add blog post: [Title]"
git push origin blog/your-post-title

# 6. Create a Pull Request on GitHub
#    From: YOUR-USERNAME/CMU-CLeaR-Group-Website:blog/your-post-title
#    To:   CMU-CLeaR/CMU-CLeaR-Group-Website:main
```

### After Your PR is Merged

```bash
# 1. Sync your fork's main branch
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# 2. Delete your local feature branch
git branch -d blog/your-post-title

# 3. Delete the remote branch on your fork
git push origin --delete blog/your-post-title

# 4. Clean up stale remote references
git fetch --prune
```

### Visual Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  Original Repo (CMU-CLeaR/CMU-CLeaR-Group-Website)          │
│  main: ──●──●──●────────────────[squashed commit]──►        │
└─────────────────────────────────────────────────────────────┘
                    ▲                    ▲
                    │ PR (Squash Merge)  │ fetch upstream
                    │                    │
┌─────────────────────────────────────────────────────────────┐
│  Your Fork (YOUR-USERNAME/CMU-CLeaR-Group-Website)          │
│  main: ──●──●──●                                            │
│  blog/your-post: ──●──A──B──C  (push here, then PR)         │
└─────────────────────────────────────────────────────────────┘
                    ▲
                    │ push origin
                    │
┌─────────────────────────────────────────────────────────────┐
│  Your Local Machine                                         │
│  main: synced with upstream                                 │
│  blog/your-post: your working branch                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 6. PR Merge Policy

- All PRs are merged using **Squash and Merge** to keep the main branch history clean.
- Each PR becomes a single commit on main.
- Delete your feature branch after the PR is merged.

---

## Tips & Troubleshooting

- **Live Reload**: The Docker container supports live reload. Most changes show up instantly after saving, but changes to `_config.yml` require a container restart.
- **Base URL**: Always include `/dietrich/causality` in hardcoded links to assets.
- **Clean Up**: If Docker acts up, run `docker-compose down` followed by a fresh `up --build`.
- **Sync Often**: Before starting new work, always sync your fork with upstream to avoid merge conflicts.
