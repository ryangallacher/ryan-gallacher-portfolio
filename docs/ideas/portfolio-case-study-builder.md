# Portfolio Case Study Builder

## The problem

Ryan can't remember the details of what he worked on last year. When it comes time to write a case study, blog post, or run a lunch and learn, the story is gone — dates, decisions, what broke, what worked, why.

## The solution

A three-layer capture-and-synthesis system:

1. **Per-project session journals** — every project repo auto-captures session stories via the `session-story.py` hook on `SessionEnd`. Captures: what the user asked for, key decisions, pivots, metrics, files changed.

2. **Synthesis hub** — `ryan-gallacher-portfolio` holds the templates and voice. On demand, an agent reads the accumulated journals from a project, plus `voice.md` and `case-study-template.md`, and produces a structured first draft.

3. **First-draft HTML** — the draft follows the page skeleton in `AGENT.md`. It's a scaffold for Ryan to rewrite, not a publishable output. Ryan edits and approves before anything goes live.

## Key files

| File | Location | Purpose |
|------|----------|---------|
| `session-story.py` | per-project `.claude/hooks/` | Auto-capture on SessionEnd — fires when files changed |
| `project-story/` | per-project root | Journal directory — one file per session |
| `voice.md` | `ryan-gallacher-portfolio/` | Ryan's personal professional tone, phrases to use/avoid |
| `case-study-template.md` | `ryan-gallacher-portfolio/` | Schema, story beats, structural preferences |

## Constraints

- `voice.md` and `case-study-template.md` live only in `ryan-gallacher-portfolio`. Other projects reference by path — no copying, no syncing.
- The synthesis step is on-demand and human-supervised. No automation beyond the session capture.
- First-draft output is always a scaffold. Ryan rewrites before it goes anywhere public.
- `main` branch of `ryan-gallacher-portfolio` is live GitHub Pages. All changes on `post-guardrails` branch only.

## What `session-story.py` currently captures

- User prompts from the session
- Decision sentences (signal words: decided, chose, will use, going with, settled on)
- Pivot sentences (signal words: actually, instead, changed, rethinking, scrapping)
- Metric sentences (contains numbers + performance-related words)
- Files changed during the session
- Commands run

**Gap:** only fires when files were changed — pure planning/thinking sessions are not captured.

## What synthesis looks like

When Ryan wants a case study for a project:

1. Agent reads all `project-story/*.md` files from that project repo
2. Agent reads `voice.md` and `case-study-template.md` from this repo
3. Agent produces a structured draft following the template schema
4. Ryan edits → publishes as HTML following `AGENT.md` page skeleton

## Nice-to-haves (not in scope now)

- Blog post format
- Lunch and learn slides
- Multiple output formats from one synthesis pass
