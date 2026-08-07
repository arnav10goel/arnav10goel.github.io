#!/usr/bin/env python3
"""
Build the blog.

Write a post as `posts/YYYY-MM-DD-some-slug.md`, then run:

    python3 build.py

That regenerates `blog/index.html` and `blog/<slug>/index.html`.
Nothing else on the site is touched.

Post format — YAML-ish frontmatter, then markdown:

    ---
    title: Why verifiers are the hard part
    subtitle: A short note on agent reliability
    date: 2026-08-07
    draft: false
    ---

    Your text here. **Bold**, _italic_, [links](https://example.com),
    footnotes[^1], tables, ```python code blocks```, and math like
    $x^2$ or $$\\int_0^1 f(x)\\,dx$$ all work.

    [^1]: Like this.

Drafts (`draft: true`) are skipped entirely.
"""

import html
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

try:
    import markdown
    from pygments.formatters import HtmlFormatter
except ImportError:
    sys.exit("Missing dependencies. Run:  pip3 install markdown pygments")

ROOT = Path(__file__).parent
POSTS_DIR = ROOT / "posts"
BLOG_DIR = ROOT / "blog"
CODE_CSS = ROOT / "assets" / "code.css"

SITE_URL = "https://arnav10goel.github.io"
AUTHOR = "Arnav Goel"

NAV = (
    '<a href="/">home</a><span class="nav-sep">/</span>'
    '<a href="/#about">about</a><span class="nav-sep">/</span>'
    '<a href="/#research">research</a><span class="nav-sep">/</span>'
    '<a href="/cv/">cv</a><span class="nav-sep">/</span>'
    '<a href="/publications/">publications</a><span class="nav-sep">/</span>'
    '<a href="/blog/" class="active">blog</a>'
)

# Applied before first paint so a stored preference does not flash the wrong theme.
NOFLASH = ('<script>(function(){try{var t=localStorage.getItem("theme");'
           'if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t);}'
           'catch(e){}})();</script>')

SUN = ('<svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
       'stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/>'
       '<path d="M12 2.4v2.1M12 19.5v2.1M4.9 4.9l1.5 1.5M17.6 17.6l1.5 1.5M2.4 12h2.1M19.5 12h2.1'
       'M4.9 19.1l1.5-1.5M17.6 6.4l1.5-1.5"/></svg>')
MOON = ('<svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M20.2 14.8A8.6 8.6 0 1 1 9.2 3.8a6.7 6.7 0 0 0 11 11z"/></svg>')

TOGGLE_JS = """<script>
(function () {
  var btn = document.querySelector('.theme-toggle');
  if (!btn) return;
  btn.addEventListener('click', function () {
    var root = document.documentElement;
    var cur = root.getAttribute('data-theme');
    if (!cur) cur = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    var next = cur === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
  });
})();
</script>
"""

MATHJAX = """<script>
window.MathJax = {
  tex: { inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']] },
  options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'] }
};
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="/assets/favicon.ico">
<link rel="stylesheet" href="/assets/style.css">
<link rel="stylesheet" href="/assets/code.css">
<link rel="alternate" type="application/rss+xml" title="{author}" href="/blog/feed.xml">
<link rel="canonical" href="{canonical}">
{noflash}
{head_extra}</head>
<body>
<div class="wrap{wrap_class}">

  <header class="site-header">
    <a class="site-name" href="/">{author}</a>
    <div class="nav-wrap">
      <nav class="nav">{nav}</nav>
      <button class="theme-toggle" type="button" aria-label="Switch colour theme"
              title="Switch colour theme">{sun}{moon}</button>
    </div>
  </header>

{body}

  <footer class="site-footer">
    <span>&copy; {year} {author}</span>
    <span>Pittsburgh, PA</span>
  </footer>

</div>
{toggle}</body>
</html>
"""


def parse_frontmatter(raw: str) -> tuple[dict, str]:
    """Split `---` frontmatter off the top of a post."""
    if not raw.startswith("---"):
        return {}, raw
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}, raw
    meta = {}
    for line in parts[1].strip().splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip().lower()] = value.strip().strip("'\"")
    return meta, parts[2].lstrip("\n")


def protect_math(text: str) -> tuple[str, list[str]]:
    """Pull LaTeX out before markdown runs so `_` and `*` survive."""
    stash: list[str] = []

    def stash_it(match: re.Match) -> str:
        stash.append(match.group(0))
        return f"\x00MATH{len(stash) - 1}\x00"

    text = re.sub(r"\$\$.+?\$\$", stash_it, text, flags=re.S)
    text = re.sub(r"(?<!\$)\$(?!\s)(?:[^$\n]|\\\$)+?(?<!\s)\$(?!\$)", stash_it, text)
    return text, stash


def restore_math(text: str, stash: list[str]) -> str:
    """Put LaTeX back, in MathJax's \\( \\) / \\[ \\] delimiters."""
    for i, snippet in enumerate(stash):
        if snippet.startswith("$$"):
            body = snippet[2:-2].strip()
            replacement = f"\\[{body}\\]"
        else:
            replacement = f"\\({snippet[1:-1]}\\)"
        text = text.replace(f"\x00MATH{i}\x00", replacement)
    return text


def reading_time(text: str) -> int:
    return max(1, round(len(text.split()) / 220))


def render_markdown(body: str) -> tuple[str, bool]:
    body, stash = protect_math(body)
    md = markdown.Markdown(
        extensions=["extra", "codehilite", "sane_lists", "smarty", "admonition"],
        extension_configs={
            "codehilite": {"guess_lang": False, "linenums": False},
            "smarty": {"smart_dashes": True, "smart_quotes": True},
        },
    )
    rendered = md.convert(body)
    return restore_math(rendered, stash), bool(stash)


def load_posts() -> list[dict]:
    posts = []
    for path in sorted(POSTS_DIR.glob("*.md"), reverse=True):
        meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        if meta.get("draft", "").lower() == "true":
            print(f"  skipping draft: {path.name}")
            continue

        slug = meta.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
        date_str = meta.get("date") or path.stem[:10]
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            date = datetime.fromtimestamp(path.stat().st_mtime)

        rendered, has_math = render_markdown(body)
        plain = re.sub(r"<[^>]+>", " ", rendered)
        plain = re.sub(r"\s+", " ", plain).strip()

        posts.append({
            "slug": slug,
            "title": meta.get("title", slug.replace("-", " ").title()),
            "subtitle": meta.get("subtitle", ""),
            "date": date,
            "html": rendered,
            "has_math": has_math,
            "excerpt": meta.get("excerpt") or (plain[:180].rstrip() + "…" if len(plain) > 180 else plain),
            "minutes": reading_time(plain),
        })
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def write_post(post: dict) -> None:
    out_dir = BLOG_DIR / post["slug"]
    out_dir.mkdir(parents=True, exist_ok=True)

    subtitle = f'    <p class="post-subtitle">{html.escape(post["subtitle"])}</p>\n' if post["subtitle"] else ""
    body = f"""  <article class="post-wrap">
    <header class="post-header">
      <h1>{html.escape(post["title"])}</h1>
{subtitle}      <p class="post-meta">{post["date"].strftime("%B %-d, %Y")} &middot; {post["minutes"]} min read</p>
    </header>
    <div class="post-body">
{post["html"]}
    </div>
    <nav class="post-nav"><a href="/blog/">&larr; All posts</a></nav>
  </article>"""

    (out_dir / "index.html").write_text(PAGE.format(
        title=f'{html.escape(post["title"])} — {AUTHOR}',
        description=html.escape(post["excerpt"][:160], quote=True),
        canonical=f'{SITE_URL}/blog/{post["slug"]}/',
        head_extra=MATHJAX + "\n" if post["has_math"] else "",
        wrap_class="",
        nav=NAV,
        noflash=NOFLASH,
        sun=SUN,
        moon=MOON,
        toggle=TOGGLE_JS,
        author=AUTHOR,
        year=datetime.now().year,
        body=body,
    ), encoding="utf-8")
    print(f"  wrote blog/{post['slug']}/")


def write_index(posts: list[dict]) -> None:
    if posts:
        items = "\n".join(
            f'''  <a class="post-item" href="/blog/{p["slug"]}/">
    <p class="post-item-title">{html.escape(p["title"])}</p>
    <p class="post-item-meta">{p["date"].strftime("%B %-d, %Y")} &middot; {p["minutes"]} min read</p>
    <p class="post-item-excerpt">{html.escape(p["subtitle"] or p["excerpt"])}</p>
  </a>'''
            for p in posts
        )
    else:
        items = ('  <p class="empty-state">No posts yet. I am planning to write about efficient reasoning, '
                 'agent reliability, and things I get wrong along the way.</p>')

    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    (BLOG_DIR / "index.html").write_text(PAGE.format(
        title=f"Blog — {AUTHOR}",
        description=f"Writing by {AUTHOR} on machine learning, language models and research.",
        canonical=f"{SITE_URL}/blog/",
        head_extra="",
        wrap_class="",
        nav=NAV,
        noflash=NOFLASH,
        sun=SUN,
        moon=MOON,
        toggle=TOGGLE_JS,
        author=AUTHOR,
        year=datetime.now().year,
        body=items,
    ), encoding="utf-8")
    print(f"  wrote blog/index.html ({len(posts)} post{'s' if len(posts) != 1 else ''})")


def write_feed(posts: list[dict]) -> None:
    entries = "\n".join(
        f"""    <item>
      <title>{html.escape(p["title"])}</title>
      <link>{SITE_URL}/blog/{p["slug"]}/</link>
      <guid>{SITE_URL}/blog/{p["slug"]}/</guid>
      <pubDate>{p["date"].strftime("%a, %d %b %Y")} 00:00:00 +0000</pubDate>
      <description>{html.escape(p["excerpt"])}</description>
    </item>"""
        for p in posts
    )
    (BLOG_DIR / "feed.xml").write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
    <title>{AUTHOR}</title>
    <link>{SITE_URL}/blog/</link>
    <description>Writing by {AUTHOR}.</description>
{entries}
</channel></rss>
""", encoding="utf-8")


def write_code_css() -> None:
    light = HtmlFormatter(style="friendly").get_style_defs(".codehilite")
    dark = HtmlFormatter(style="nord").get_style_defs(".codehilite")
    CODE_CSS.write_text(
        f"/* generated by build.py — do not edit */\n{light}\n"
        f"@media (prefers-color-scheme: dark) {{\n{dark}\n}}\n",
        encoding="utf-8",
    )


def main() -> None:
    POSTS_DIR.mkdir(exist_ok=True)
    print("Building blog…")

    # Clear out stale post directories so renamed/deleted posts disappear.
    if BLOG_DIR.exists():
        for child in BLOG_DIR.iterdir():
            if child.is_dir():
                shutil.rmtree(child)

    posts = load_posts()
    for post in posts:
        write_post(post)
    write_index(posts)
    write_feed(posts)
    write_code_css()
    print("Done.")


if __name__ == "__main__":
    main()
