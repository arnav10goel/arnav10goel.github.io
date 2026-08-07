---
title: Everything this blog can do
subtitle: A scratchpad showing the formatting available — delete or rewrite this whenever
date: 2026-08-07
draft: true
---

This post is a **draft**, so it will not appear on the site until you change
`draft: true` to `draft: false` in the frontmatter above. It exists to show you
what the formatting looks like. Delete it once you have written something real.

To write a post, drop a file in `posts/` named `YYYY-MM-DD-your-slug.md` and run
`python3 build.py`. The URL comes from the slug, so this file would publish to
`/blog/example-post/`.

## Headings and text

Second-level headings break up the page like the one above. You get *italics*,
**bold**, `inline code`, and [links](https://arnav10goel.github.io) as you would
expect. Quotes get curled automatically — "like this" — and dashes become
en/em dashes.

### Third-level headings

Useful for subsections inside a longer argument.

## Lists

- Unordered lists work
- With multiple items
    - And nesting, if you indent by four spaces

1. Ordered lists too
2. Numbered automatically

## Code

Fenced blocks are syntax-highlighted at build time, so there is no JavaScript
involved and the colours follow light and dark mode:

```python
def sample(model, prompt, temperature=0.7, max_tokens=256):
    """Greedy-ish decoding with a temperature knob."""
    tokens = model.tokenize(prompt)
    for _ in range(max_tokens):
        logits = model(tokens)[-1] / temperature
        tokens.append(logits.softmax(-1).multinomial(1))
        if tokens[-1] == model.eos_id:
            break
    return model.detokenize(tokens)
```

## Math

Inline math like $O(n \log n)$ works, and so do display equations:

$$\mathcal{L}(\theta) = -\mathbb{E}_{x \sim \mathcal{D}} \left[ \log p_\theta(x) \right]$$

MathJax only loads on posts that actually contain math, so pages without
equations stay fast.

## Tables

| Model | Params | Accuracy | Latency |
|---|---|---|---|
| GPT-4o | — | 0.91 | 1.00× |
| Distilled 8B | 8B | 0.89 | 0.01× |
| Baseline | 8B | 0.71 | 0.01× |

## Quotes and asides

> Pull out a sentence worth sitting with, and it renders like this.

You can also add footnotes,[^1] which collect at the bottom of the post.

[^1]: Like this one. They are automatically numbered and linked both ways.

## Images

Drop an image in `assets/` and reference it:

```markdown
![A caption for the figure](/assets/my-figure.png)
```

---

That is the whole toolkit. Write markdown, run `python3 build.py`, commit, push.
