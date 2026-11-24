#!/usr/bin/env python3
"""
Regenerate publications/index.html from a single list.

Keeping the papers in one place means the venue, authors and links cannot
drift between here and the homepage's selected list. Edit PAPERS, rerun.

  python3 tools/gen_pubs.py
"""
import pathlib

ROOT = pathlib.Path(__file__).parent.parent
ME = "Arnav Goel"

# ── link-type icons ───────────────────────────────────────────────────────
_F = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    "arxiv": f'<svg viewBox="0 0 24 24" {_F}><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/></svg>',
    "pdf":   f'<svg viewBox="0 0 24 24" {_F}><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
    "code":  '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.37.5 0 5.87 0 12.5c0 5.3 3.44 9.8 8.2 11.39.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.09-.75.08-.73.08-.73 1.2.08 1.84 1.24 1.84 1.24 1.07 1.84 2.81 1.31 3.5 1 .11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.34-5.47-5.95 0-1.31.47-2.38 1.24-3.22-.12-.3-.54-1.52.12-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.29-1.55 3.3-1.23 3.3-1.23.66 1.66.24 2.88.12 3.18.77.84 1.24 1.91 1.24 3.22 0 4.62-2.81 5.64-5.49 5.94.43.37.81 1.1.81 2.22v3.29c0 .32.22.7.83.58C20.56 22.29 24 17.79 24 12.5 24 5.87 18.63.5 12 .5z"/></svg>',
    "data":  f'<svg viewBox="0 0 24 24" {_F}><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v6c0 1.66 3.58 3 8 3s8-1.34 8-3V5M4 11v6c0 1.66 3.58 3 8 3s8-1.34 8-3v-6"/></svg>',
    "site":  f'<svg viewBox="0 0 24 24" {_F}><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.8 3.8 9S14.5 18.3 12 21c-2.5-2.7-3.8-5.8-3.8-9S9.5 5.7 12 3z"/></svg>',
    "hf":    '<span class="hf-emoji" aria-hidden="true">\U0001F917</span>',
}
LABELS = {"arxiv": "arXiv", "pdf": "PDF", "code": "Code", "data": "Dataset",
          "site": "OpenReview", "hf": "HuggingFace"}

# ── the papers ────────────────────────────────────────────────────────────
# (year, title, authors, venue, note, [(kind, url), ...])
PAPERS = [
 (2026, "Is Persona Generalization Predictable?",
  "Olina Mukherjee, {me}, Aditi Raghunathan, Jacob Mitchell Springer",
  "Preprint", "",
  [("arxiv", "https://arxiv.org/abs/2611.12864")]),

 (2026, "Mind the Gap: Multilingual Divide in LLM Bias Detection and Reasoning",
  "Medha Hira, Prachi Goyal, Raj Maheshwari, {me}",
  "ACL 2026", "Student Research Workshop", []),

 (2026, "MORPHOGEN: A Multilingual Benchmark for Evaluating Gender-Aware Morphological Generation",
  "Mehul Agarwal, Aditya Aggarwal, {me}, Medha Hira, Anubha Gupta",
  "ACL 2026", "Main Conference",
  [("pdf", "https://aclanthology.org/2026.acl-long.105/"),
   ("arxiv", "https://arxiv.org/abs/2604.18914"),
   ("code", "https://github.com/arnav10goel/Morphogen")]),

 (2026, "HORIZON: A Benchmark for In-the-wild User Behaviour Modeling",
  "{me}, Pranjal A. Chitale, Bhawna Paliwal, Bishal Santra, Amit Sharma",
  "Findings of ACL 2026", "LLMEval Workshop @ NeurIPS 2025",
  [("pdf", "https://aclanthology.org/2026.findings-acl.1503/"),
   ("arxiv", "https://arxiv.org/abs/2604.17259"),
   ("code", "https://github.com/microsoft/horizon-benchmark")]),

 (2026, "On Defining Erasure Harms for NLP",
  "Yu Lu Liu, {me}, Jackie Chi Kit Cheung, Alexandra Olteanu, Ziang Xiao, Su Lin Blodgett",
  "Preprint", "",
  [("arxiv", "https://arxiv.org/abs/2606.15815")]),

 (2025, "Enhancing Scientific Visual Question Answering via Vision-Caption aware Supervised Fine-Tuning",
  "Janak Kapuriya, Anwar Shaikh, {me}, Medha Hira, Apoorv Singh, Jay Saraf, Sanjana, "
  "Vaibhav Nauriyal, Avinash Anand, Zhengkui Wang, Rajiv Ratn Shah",
  "LAVA Workshop @ ACM Multimedia 2025", "Oral",
  [("pdf", "https://dl.acm.org/doi/10.1145/3728483.3760194"),
   ("arxiv", "https://arxiv.org/abs/2509.16628")]),

 (2025, "Attributing Culture-Conditioned Generations to Pretraining Corpora",
  "Huihan Li*, {me}*, Keyu He, Xiang Ren",
  "ICLR 2025", "",
  [("arxiv", "https://arxiv.org/abs/2412.20760"),
   ("code", "https://github.com/huihanlhh/CultureGenAttr")]),

 (2024, "Exploring Multilingual Unseen Speaker Emotion Recognition: "
        "Leveraging Co-Attention Cues in Multitask Learning",
  "{me}*, Medha Hira*, Anubha Gupta",
  "INTERSPEECH 2024", "",
  [("pdf", "https://www.isca-archive.org/interspeech_2024/goel24_interspeech.html"),
   ("code", "https://github.com/arnav10goel/CAMuLeNet")]),

 (2024, "LLMGuard: Guarding Against Unsafe LLM Behavior",
  "Shubh Goyal*, Medha Hira*, Shubham Mishra*, Sukriti Goyal*, {me}*, Niharika Dadu*, "
  "Kirushikesh DB, Sameep Mehta, Nishtha Madaan",
  "AAAI 2024", "Demonstration Track",
  [("pdf", "https://ojs.aaai.org/index.php/AAAI/article/view/30566"),
   ("arxiv", "https://arxiv.org/abs/2403.00826")]),

 (2024, "Multilingual Prosody Transfer: Comparing Supervised &amp; Transfer Learning",
  "{me}*, Medha Hira*, Anubha Gupta",
  "ICLR 2024 Tiny Track", "Invited to Present",
  [("pdf", "https://openreview.net/forum?id=DKF7YCwCmd"),
   ("code", "https://github.com/NLP-SBILAB/Multilingual-Prosody-Transfer")]),

 (2024, "CrossVoice: Crosslingual Prosody Preserving Cascade-S2ST using Transfer Learning",
  "Medha Hira*, {me}*, Anubha Gupta",
  "ICLR 2024 Tiny Track", "Invited to Present",
  [("pdf", "https://openreview.net/forum?id=zEdBzTxXHl"),
   ("code", "https://github.com/NLP-SBILAB/CrossVoice")]),

 (2023, "SciPhyRAG: Retrieval Augmentation to Improve LLMs on Physics Q&amp;A",
  "Avinash Anand, {me}, Medha Hira, Snehal Buldeo, Jatin Kumar, Astha Verma, "
  "Rushali Gupta, Rajiv Ratn Shah",
  "BDA 2023", "",
  [("pdf", "https://doi.org/10.1007/978-3-031-49601-1_4"),
   ("code", "https://github.com/arnav10goel/SciPhy-RAG")]),

 (2023, "Revolutionizing High School Physics Education: A Novel Dataset",
  "Avinash Anand, Krishnasai Addala, Kabir Baghel, {me}, Medha Hira, Rushali Gupta, Rajiv Ratn Shah",
  "BDA 2023", "",
  [("pdf", "https://doi.org/10.1007/978-3-031-49601-1_5")]),

 (2023, "Advancements in Scientific Controllable Text Generation Methods",
  "{me}, Medha Hira, Avinash Anand, Siddhesh Bangar, Rajiv Ratn Shah",
  "Preprint", "",
  [("arxiv", "https://arxiv.org/abs/2307.05538")]),

]

NAV = ('<a href="/">home</a><span class="nav-sep">/</span>'
       '<a href="/#about">about</a><span class="nav-sep">/</span>'
       '<a href="/#research">research</a><span class="nav-sep">/</span>'
       '<a href="/cv/">cv</a><span class="nav-sep">/</span>'
       '<a href="/publications/" class="active">publications</a><span class="nav-sep">/</span>'
       '<a href="/blog/">blog</a>')

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
TOGGLE = """<script>
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


def links_html(links):
    if not links:
        return ""
    out = []
    for kind, url in links:
        out.append(f'<a class="plink {kind}" href="{url}">{ICONS[kind]}{LABELS[kind]}</a>')
    return '<div class="plinks">' + "".join(out) + "</div>"


def build():
    rows, last_year = [], None
    for year, title, authors, venue, note, links in PAPERS:
        if year != last_year:
            if last_year is not None:
                rows.append("    </div>\n  </div>\n")
            rows.append(f'  <div class="pubgroup">\n'
                        f'    <div class="pubrail">{year}</div>\n'
                        f'    <div class="pubitems">\n')
            last_year = year
        au = authors.replace("{me}", f'<span class="me">{ME}</span>')
        badge = f' <span class="hl">&middot; {note}</span>' if note else ""
        rows.append(
            f'      <article class="pubentry">\n'
            f'        <h3 class="pub-title">{title}</h3>\n'
            f'        <p class="pub-authors">{au}</p>\n'
            f'        <p class="vlabel">{venue}{badge}</p>\n'
            f'        {links_html(links)}\n'
            f'      </article>\n')
    rows.append("    </div>\n  </div>\n")

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Publications &mdash; {ME}</title>
<meta name="description" content="Publications by {ME} — language models, reasoning, reliability, multilingual NLP and speech.">
<link rel="icon" href="/assets/favicon.ico">
<link rel="stylesheet" href="/assets/style.css">
{NOFLASH}
<link rel="canonical" href="https://arnav10goel.github.io/publications/">
</head>
<body>
<div class="wrap">

  <header class="site-header">
    <a class="site-name" href="/">{ME}</a>
    <div class="nav-wrap">
      <nav class="nav">{NAV}</nav>
      <button class="theme-toggle" type="button" aria-label="Switch colour theme" title="Switch colour theme">{SUN}{MOON}</button>
    </div>
  </header>

  <div class="page-intro">
    <h1>Publications</h1>
    <p><span class="star">*</span> denotes equal contribution.
       <a href="https://scholar.google.com/citations?user=PPozs9sAAAAJ&amp;hl=en">Google Scholar</a>
       has the most current list.</p>
  </div>

{''.join(rows)}
  <p class="note">I have reviewed for ACL Rolling Review (Feb 2025, May 2025, May 2026, Oct 2026),
     AAAI 2025 and 2026, ACM FAccT 2026, ACM Multimedia 2024 and ICLR 2024 (Tiny Track).</p>

  <footer class="site-footer">
    <span>&copy; 2026 {ME}</span>
    <span>Pittsburgh, PA</span>
  </footer>

</div>
{TOGGLE}</body>
</html>
"""
    out = ROOT / "publications" / "index.html"
    out.write_text(html, encoding="utf-8")
    n_links = sum(len(p[5]) for p in PAPERS)
    print(f"  wrote {out.relative_to(ROOT)} — {len(PAPERS)} papers, {n_links} links")
    missing = [p[1][:46] for p in PAPERS if not p[5]]
    if missing:
        print("  no links yet:")
        for m in missing:
            print(f"    - {m}…")


if __name__ == "__main__":
    build()
