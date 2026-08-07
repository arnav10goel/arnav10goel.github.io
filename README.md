# arnav10goel.github.io

Personal site. Plain static HTML with one stylesheet, plus a small Python script
that turns markdown into blog posts. No Jekyll, no Ruby, no build step for
anything except the blog.

```
index.html               home — intro + news
cv/index.html            full CV
publications/index.html  publication list
blog/                    generated — do not edit by hand
posts/*.md               blog posts, in markdown  ← write here
assets/style.css         the entire design
assets/code.css          generated — syntax highlighting
build.py                 markdown → blog HTML
tools/gen_art.py         regenerates the two SVG artworks
```

## The artwork

`assets/hero.svg` (a loss landscape with a simulated gradient-descent path) and
`assets/accent.svg` (a vector field with streamlines) are generated, not drawn:

```bash
python3 tools/gen_art.py
```

Both are deterministic — the seeds are fixed, so re-running produces the same
image. They carry their own light/dark palette and their own animation, and
every resting state is the finished drawing, so they still read correctly with
`prefers-reduced-motion` or anywhere CSS animation does not run. Edit the
constants at the top of each function to retune them.

## Previewing locally

Absolute paths (`/assets/style.css`) mean you need a server — opening the HTML
files directly from Finder will render them unstyled.

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

## Writing a blog post

Create `posts/YYYY-MM-DD-your-slug.md`:

```markdown
---
title: Why verifiers are the hard part
subtitle: An optional one-line deck
date: 2026-08-14
draft: false
---

Your text here.
```

Then build and publish:

```bash
python3 build.py && git add -A && git commit -m "New post" && git push
```

The post lands at `/blog/your-slug/`. Set `draft: true` to keep it unpublished.

Supported: headings, **bold**, *italic*, links, lists, tables, footnotes,
blockquotes, fenced code blocks with syntax highlighting, and LaTeX math
(`$inline$` and `$$display$$`). MathJax only loads on posts that contain math.
See `posts/2026-08-07-example-post.md` for a live demonstration of all of it.

First time only:

```bash
pip3 install -r requirements.txt
```

A GitHub Action (`.github/workflows/build-blog.yml`) also runs `build.py` on
every push to `master`, so the blog rebuilds even if you forget to run it.
For that to deploy, set **Settings → Pages → Source** to **GitHub Actions**.

## Updating the other pages

Home, CV and publications are hand-written HTML — edit the file directly. They
all share `assets/style.css`, and each page repeats the same header and footer
block, so if you change the nav, change it in all three (and in `NAV` inside
`build.py`).

## History

The previous version of this site used the
[Academic Pages](https://github.com/academicpages/academicpages.github.io)
Jekyll theme. It was replaced in August 2026. The old version is still in git
history before the redesign, and a full copy sits in
`../arnav10goel.github.io.backup-before-redesign-2026-07-20`.
