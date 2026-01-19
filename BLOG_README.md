# Blog Contributor Guide

This guide explains how to write, preview, and submit blog posts to the CMU-CLeaR Group website.

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/CMU-CLeaR/CMU-CLeaR-Group-Website.git
cd CMU-CLeaR-Group-Website
```

### 2. Create Your Draft
Create a new file in the `_drafts/` folder with format `YYYY-MM-DD-your-title.md`:

```bash
touch _drafts/2025-02-01-my-new-post.md
```

### 3. Write Your Post
Use this template:

```markdown
---
layout: distill
title: "Your Post Title"
date: 2025-02-01
description: "A brief description of your post"
tags: tag1 tag2

authors:
  - name: Your Name
    url: "https://your-website.com"
    affiliations:
      name: CLeaR, CMU
---

Your content here. You can use:
- Markdown formatting
- LaTeX math: $E = mc^2$ or $$\int_0^\infty e^{-x} dx$$
- Images, code blocks, etc.
```

### 4. Preview Locally with Docker

**To preview drafts** (recommended during development):
```bash
JEKYLL_DRAFTS=true docker-compose up --build
```

**To preview without drafts** (matches production):
```bash
docker-compose up --build
```

Open http://localhost:8080/dietrich/causality/blog/ in your browser. The site auto-reloads when you save changes.

### 5. Submit Your Post

When ready to publish:

1. **Create a new branch:**
   ```bash
   git checkout -b blog/your-post-name
   ```

2. **Move your draft to posts** (or keep in drafts for review):
   ```bash
   # If ready for immediate publication after merge:
   mv _drafts/2025-02-01-my-new-post.md _posts/2025-02-01-my-new-post.md

   # Or keep in _drafts/ if you want feedback before publishing
   ```

3. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add blog post: Your Post Title"
   git push origin blog/your-post-name
   ```

4. **Create a Pull Request** on GitHub and request review.

## Folder Structure

| Folder | Purpose |
|--------|---------|
| `_drafts/` | Work-in-progress posts (not visible in production) |
| `_posts/` | Published posts (visible on the live site) |

## Tips

- **Images:** Place in `assets/img/blogs` and reference as `![alt](/dietrich/causality/assets/img/YYYY-MM-DD-your-title/image.png)`
- **Math:** LaTeX is enabled. Use `$...$` for inline and `$$...$$` for display math
- **Date:** The date in the filename determines the post order
- **Preview drafts:** Always use `JEKYLL_DRAFTS=true` when developing to see your draft posts

## Troubleshooting

**Docker issues:**
```bash
docker-compose down
docker-compose up --build
```

**Port already in use:**
```bash
docker-compose down
# Or change port in docker-compose.yml
```

**Changes not showing:**
- Check browser cache (hard refresh: Cmd+Shift+R or Ctrl+Shift+R)
- Ensure livereload is connected (check terminal output)
