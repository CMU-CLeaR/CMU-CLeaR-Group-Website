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

### First-Time Setup (Everyone)

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

---

### Scenario A: Single-Author Blog Post

**Example**: Alice writes a post about "Causal Discovery Methods"

```bash
# 1. Sync with upstream
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# 2. Create a feature branch
git checkout -b blog/causal-discovery-methods

# 3. Write your post
#    - Create: _drafts/2026-03-01-causal-discovery-methods.md
#    - Add images to: assets/img/blogs/2026-03-01-causal-discovery-methods/
#    - Add bibliography: assets/bibliography/2026-03-01-causal-discovery-methods.bib

# 4. Preview locally
JEKYLL_DRAFTS=true docker-compose up --build

# 5. When ready, move draft to posts
mv _drafts/2026-03-01-causal-discovery-methods.md _posts/

# 6. Commit and push
git add .
git commit -m "Add blog post: Causal Discovery Methods"
git push origin blog/causal-discovery-methods

# 7. Create PR on GitHub
#    From: alice/CMU-CLeaR-Group-Website:blog/causal-discovery-methods
#    To:   CMU-CLeaR/CMU-CLeaR-Group-Website:main
```

---

### Scenario B: Multi-Author Collaborative Post

When multiple authors contribute to a single post, designate one person as the **Lead Author** who owns the PR. There are two recommended approaches:

#### Option 1: Shared Fork (Recommended for Close Collaboration)

The lead author grants collaborators push access to their fork.

**Example**: Alice (lead) and Bob co-author "Identifiability in Causal Models"

**Step 1: Alice sets up the branch**
```bash
# Alice creates the branch on her fork
git checkout main && git pull upstream main
git checkout -b blog/identifiability-causal-models
git push origin blog/identifiability-causal-models
```

**Step 2: Alice adds Bob as a collaborator**
1. Go to `github.com/alice/CMU-CLeaR-Group-Website` → Settings → Collaborators
2. Add Bob's GitHub username
3. Bob accepts the invitation via email/GitHub notification

**Step 3: Bob clones Alice's fork**
```bash
# Bob adds Alice's fork as a remote
git remote add alice https://github.com/alice/CMU-CLeaR-Group-Website.git
git fetch alice
git checkout -b blog/identifiability-causal-models alice/blog/identifiability-causal-models
```

**Step 4: Both authors contribute**
```bash
# Bob makes changes and pushes to Alice's fork
git add .
git commit -m "Add section on linear identifiability"
git push alice blog/identifiability-causal-models

# Alice pulls Bob's changes
git pull origin blog/identifiability-causal-models
```

**Step 5: Alice creates the PR when ready**
```bash
# Move to _posts/ and create PR
mv _drafts/2026-03-15-identifiability-causal-models.md _posts/
git add . && git commit -m "Add blog post: Identifiability in Causal Models"
git push origin blog/identifiability-causal-models
# Create PR from alice/...:blog/identifiability-causal-models → CMU-CLeaR/...:main
```

#### Option 2: PR-Based Review (Recommended for Async Collaboration)

Co-authors contribute through GitHub's PR review features without needing fork access.

**Example**: Alice (lead) writes the initial draft, Bob reviews and suggests changes

**Step 1: Alice creates the draft PR**
```bash
# Alice creates branch, writes initial content, and opens a Draft PR
git checkout -b blog/causal-representation
# ... write content ...
git push origin blog/causal-representation
# On GitHub: Create "Draft Pull Request"
```

**Step 2: Bob reviews via GitHub**
- Bob opens the PR on GitHub
- Uses "Add a suggestion" in review comments to propose text changes
- Alice can click "Commit suggestion" to accept inline

**Step 3: Bob can also push directly (if given access)**
```bash
# If Alice enabled "Allow edits from maintainers" on the PR,
# Bob (with write access to upstream) can push directly:
git fetch origin pull/42/head:blog/causal-representation
git checkout blog/causal-representation
# ... make changes ...
git push origin blog/causal-representation
```

**Step 4: Finalize and merge**
- Alice marks PR as "Ready for Review" when complete
- After approval, squash-merge into main

---

### Multi-Author Front Matter

For collaborative posts, list all authors in the YAML front matter:

```yaml
authors:
  - name: Alice Chen
    url: "https://alice-chen.github.io"
    affiliations:
      name: CLeaR, CMU
  - name: Bob Smith
    url: "https://bobsmith.com"
    affiliations:
      name: CLeaR, CMU
```

---

### After Your PR is Merged

```bash
# 1. Sync your fork's main branch
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# 2. Delete your local feature branch (use -D because squash-merge creates new commit hashes)
git branch -D blog/your-post-title

# 3. Delete the remote branch on your fork
git push origin --delete blog/your-post-title

# 4. Clean up stale remote references
git fetch --prune

# 5. (For collaborators) Remove the collaborator's remote if no longer needed
git remote remove alice  # Bob removes Alice's fork remote
```

---

### Visual Workflow

**Single Author:**
```
┌─────────────────────────────────────────────────────────────┐
│  CMU-CLeaR/CMU-CLeaR-Group-Website (upstream)               │
│  main: ──●──●──●────────────────[squashed commit]──►        │
└─────────────────────────────────────────────────────────────┘
                    ▲
                    │ PR (Squash Merge)
                    │
┌─────────────────────────────────────────────────────────────┐
│  alice/CMU-CLeaR-Group-Website (fork)                       │
│  blog/post-title: ──●──A──B──C                              │
└─────────────────────────────────────────────────────────────┘
```

**Multi-Author (Shared Fork):**
```
┌─────────────────────────────────────────────────────────────┐
│  CMU-CLeaR/CMU-CLeaR-Group-Website (upstream)               │
│  main: ──●──●──●────────────────[squashed commit]──►        │
└─────────────────────────────────────────────────────────────┘
                    ▲
                    │ PR (Squash Merge)
                    │
┌─────────────────────────────────────────────────────────────┐
│  alice/CMU-CLeaR-Group-Website (lead author's fork)         │
│  blog/collab-post: ──●──A(alice)──B(bob)──C(alice)──►       │
└─────────────────────────────────────────────────────────────┘
                    ▲               ▲
                    │               │
              Alice pushes     Bob pushes
              (origin)         (alice remote)
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
