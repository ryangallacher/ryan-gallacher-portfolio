# Design System & Agent Guidelines

This is a UX design portfolio built with static HTML, CSS, and vanilla JS. All styles live in a single `styles.css` file. Follow these rules when creating or modifying any page.

---

## Fonts

| Token | Family | Usage |
|-------|--------|-------|
| `--ff-serif` | Lora | Headings (h1–h3), display text, logo, stat numbers |
| `--ff-sans` | Source Sans 3 | Body text, labels, buttons, navigation, everything else |

Headings use `font-weight: 400`. Body uses `font-weight: 400`, with `600` for emphasis/buttons.

---

## Typography Scale

All text must use these tokens. Never hardcode font sizes.

| Token | Size | Line-height | Ratio | Usage |
|-------|------|-------------|-------|-------|
| `--fs-display-lg` / `--lh-display-lg` | 60px | 72px | 1.20 | Homepage h1 |
| `--fs-display-sm` / `--lh-display-sm` | 48px | 56px | 1.17 | About page section heading |
| `--fs-h1` / `--lh-h1` | 36px | 44px | 1.22 | Project page h1 |
| `--fs-h2` / `--lh-h2` | 32px | 40px | 1.25 | Section headings |
| `--fs-h3` / `--lh-h3` | 24px | 36px | 1.50 | Sub-section headings |
| `--fs-body` / `--lh-body` | 16px | 24px | 1.50 | Default body text |
| `--fs-body-sm` / `--lh-body-sm` | 14px | 20px | 1.43 | Eyebrow text, labels, buttons, table text |
| `--fs-body-compact` / `--lh-body-compact` | 12px | 16px | 1.33 | Captions, meta text |
| `--fs-label-lg` / `--lh-label-lg` | 14px | 20px | 1.43 | Large labels |
| `--fs-label` / `--lh-label` | 12px | 16px | 1.33 | Tags, small labels |

Aliases: `--fs-button` and `--fs-table` both map to `--fs-body-sm`.

---

## Spacing Scale

Based on a 4px grid. Use `--sp-*` tokens for all margin and padding values.

| Token | Value | Common use |
|-------|-------|------------|
| `--sp-1` | 4px | Tight gaps |
| `--sp-2` | 8px | Between label and field, caption to image |
| `--sp-3` | 12px | Minor internal spacing |
| `--sp-4` | 16px | Heading to its content |
| `--sp-5` | 20px | — |
| `--sp-6` | 24px | Inner padding, nav gaps |
| `--sp-8` | 32px | Card content padding, grid gaps |
| `--sp-10` | 40px | **Section spacing, heading margin-top** |
| `--sp-12` | 48px | Large section padding |
| `--sp-16` | 64px | Major vertical gaps |
| `--sp-20` | 80px | Page-level padding |

### Spacing Rules

- **40px (`--sp-10`)** between sections, between content blocks, and above h2/h3 headings
- Heading-to-content gap scales with font size:
  - **24px (`--sp-6`)** — `display-lg` (60px, homepage h1)
  - **24px (`--sp-6`)** — `display-sm` (48px, about page h1)
  - **16px (`--sp-4`)** — `h1` (36px) and smaller
- **8px (`--sp-2`)** from image to caption, label to field
- First heading in a section gets `margin-top: 0` (the section spacing handles it)
- h3 directly after h2: use `--sp-4` (tighter coupling)
- h3 inside `.research-header`: use `--sp-6` top, `--sp-4` bottom
- Component-internal headings (post-it cards, panels, etc.): `margin-top: 0`

---

## Colour Palette

Always use CSS variables. Never hardcode hex values.

### Neutrals
| Token | Hex | Usage |
|-------|-----|-------|
| `--n-0` | #FFFFFF | Surface background |
| `--n-50` | #F9FAFA | Body background |
| `--n-100` | #F0F4F4 | Alternate surface, input background |
| `--n-200` | #E1E8E8 | Borders, tags, footer, disabled backgrounds |
| `--n-300` | #9BA9A9 | Stronger borders, disabled text |
| `--n-400` | #7A8B8D | — |
| `--n-500` | #5E6E70 | Secondary text |
| `--n-600` | #455456 | — |
| `--n-800` | #233D4D | Primary text (`--color-ink`) |
| `--n-900` | #142224 | Darkest, used sparingly |

### Brand Petrol (Primary)
| Token | Hex | Usage |
|-------|-----|-------|
| `--p-base` | #034C53 | Primary buttons, focus rings, logo |
| `--p-hover` | #023D42 | Button hover |
| `--p-active` | #012629 | Button active |
| `--p-tint` | #E6EDEE | Light petrol backgrounds |

### Teal
| Token | Hex | Usage |
|-------|-----|-------|
| `--teal-base` | #007074 | Accents, timeline nodes |
| `--teal-hover` | #005B5E | — |
| `--teal-active` | #004547 | — |
| `--teal-vivid` | #00C4C8 | Highlight accents |
| `--teal-light` | #E6F1F1 | Light teal backgrounds |

### Peach
| Token | Hex | Usage |
|-------|-----|-------|
| `--peach-base` | #F79B72 | Stat borders, decorative accents |
| `--peach-hover` | #DF8C67 | — |
| `--peach-active` | #C77D5C | — |
| `--peach-light` | #FFF7F1 | Light peach backgrounds |

### Accent Orange
| Token | Hex | Usage |
|-------|-----|-------|
| `--a-base` | #FE7F2D | Icons/borders only — never for text |
| `--a-hover` | #E57229 | — |
| `--a-active` | #CC6624 | — |
| `--a-light` | #FFF3E6 | Warning backgrounds |

### Semantic
| Token | Hex | Usage |
|-------|-----|-------|
| `--red-base` | #DA1E28 | Errors |
| `--green-base` | #4A9A51 | Success |
| `--blue-base` | #0066CC | Links |

### Functional Mappings (prefer these)
Use these over raw palette tokens when the context is clear:

| Token | Maps to | Usage |
|-------|---------|-------|
| `--color-ink` | `--n-800` | Primary text |
| `--color-text-secondary` | `--n-500` | Secondary/muted text |
| `--color-text-disabled` | `--n-300` | Disabled text |
| `--color-bg-body` | `--n-50` | Page background |
| `--color-bg-surface` | `--n-0` | Card/panel backgrounds |
| `--color-bg-surface-alt` | `--n-100` | Alternate surfaces |
| `--color-border-default` | `--n-200` | Default borders |
| `--color-border-strong` | `--n-300` | Emphasized borders |
| `--color-link-default` | `--blue-base` | Link text |
| `--color-focus-ring` | `--p-base` | Keyboard focus outlines |

---

## Shadows & Motion

| Token | Value |
|-------|-------|
| `--shadow-sm` | `0 2px 4px rgba(20, 34, 36, 0.08)` |
| `--shadow-md` | `0 4px 12px rgba(20, 34, 36, 0.12)` |
| `--shadow-level-3` | `0 8px 16px rgba(20, 34, 36, 0.14)` |
| `--motion-fast` | `150ms ease-in-out` |

---

## Layout

Two content column widths are used depending on page type. Never mix them on the same page.

| Page type | Max-width | Horizontal padding | CSS pattern |
|-----------|-----------|-------------------|-------------|
| Project pages | 1400px | 40px | `.hero-wrapper`, `.research-section` |
| Homepage / About / Contact | 1200px | 24px (`--sp-6`) | `.content-container` |

- **Prose max-width**: 720px for body text within `.research-header-body`
- **Border radius**: 4px for images and cards, 6px for buttons and inputs, 8px for timeline cards, 50% for circular buttons
- Hero and all content sections on a project page share the same 1400px/40px constraint — this is what keeps the left edge aligned throughout the page

---

## Responsive Breakpoints

| Breakpoint | Target |
|------------|--------|
| `1200px` | Large desktops (min-width for wider grids) |
| `1024px` | Tablets landscape |
| `900px` | Tablets / timeline adjustments |
| `768px` | Tablets / typography scaling |
| `600px` | Large phones / timeline collapse |
| `480px` | Mobile phones |
| `360px` | Small mobiles |

### Responsive Token Scaling

Font and spacing tokens are overridden via `:root` at breakpoints — do not hardcode values at each breakpoint, update the token instead.

**Typography (`768px` and `480px`)**

| Token | Desktop | 768px | 480px |
|-------|---------|-------|-------|
| `--fs-display-lg` / `--lh-display-lg` | 60px / 72px | 40px / 48px | 32px / 40px |
| `--fs-display-sm` / `--lh-display-sm` | 48px / 56px | 32px / 40px | 24px / 32px |
| `--fs-h1` / `--lh-h1` | 36px / 44px | 28px / 36px | 24px / 32px |
| `--fs-h2` / `--lh-h2` | 32px / 40px | 24px / 32px | 20px / 24px |
| `--fs-h3` / `--lh-h3` | 24px / 36px | 20px / 28px | 18px / 24px |

**Spacing (`768px` and `480px`)**

| Token | Desktop | 768px | 480px |
|-------|---------|-------|-------|
| `--sp-8` | 32px | 32px | 24px |
| `--sp-10` | 40px | 32px | 24px |
| `--sp-12` | 48px | 40px | 32px |
| `--sp-16` | 64px | 48px | 40px |
| `--sp-20` | 80px | 56px | 48px |

Tokens `--sp-1` through `--sp-6` do not scale — they are small enough to remain consistent.

---

## Accessibility

- **Focus states**: Use `:focus-visible` with `outline: 3px solid var(--color-focus-ring); outline-offset: 3px`. Always include `@supports not selector(:focus-visible)` fallback.
- **Semantic HTML**: Use `section`, `nav`, `main`, `header`, `footer`, `article`, `dl`/`dt`/`dd` where appropriate.
- **Colour contrast**: Never use orange (`--a-base`) or peach (`--peach-base`) as text colours — they fail WCAG contrast on light backgrounds. Use them only for icons, borders, and decorative elements.
- **Images**: Always include meaningful `alt` text. Use `loading="lazy"` and `decoding="async"` for below-fold images. Use `fetchpriority="high"` for hero images.

---

## Component Patterns

These are the reusable patterns in the codebase. Reference existing HTML pages for exact markup.

### Header
- `.header-container` — 48px height, logo left, nav right
- Logo uses `--ff-serif` in `--p-base` colour
- Nav links use animated underline on hover

### Footer
- `footer` — `--n-200` background, centred nav links and copyright
- Copyright year set dynamically via JS (`id="year"`)

### Buttons
- **Primary** (`.btn-primary`, `.cta-button`): 40px height, 24px horizontal padding, 6px radius, `--p-base` background
- **Secondary** (`.btn-secondary`): Same dimensions, white background with 2px border
- Both shift to hover states using `--p-hover`

### Hero — Homepage
- `.hero` inside `.content-container` — two-column flex (text left, image right)
- Uses `.line-grid-accent` for background pattern
- h1 uses `display-lg` size

### Hero — Project Pages
- `.hero-section > .hero-wrapper` — dark background, full-width
- Includes `.back-button`, `.eyebrow-text`, h1 (uses `--fs-h1`), description paragraphs, and `.hero-stats` (dl/dt/dd)
- `.hero-image` holds the project screenshot

### Value Banner
- `.value-banner-section > .value-banner > .value-banner-stats`
- Grid of `.value-banner-item` with `.value-banner-eyebrow` (large number) and `.value-banner-value` (description)

### Research Section
- `.research-section > .research-header > div` containing h2/h3 and `.research-header-body` with paragraphs
- This is the primary content wrapper for project pages

### Post-it Grid
- `.postit-grid` with `.postit-card` items
- Each card has `.postit-card-icon`, h3, and p

### Core Value Panels
- `.core-value-panels` — before/after comparison with `.core-value-arrow` between
- `.core-value-panel--after` modifier for the "after" state

### Dependency Chain
- `.dependency-chain` — horizontal flow of `.dependency-node` connected by `.dependency-arrow`
- `.dependency-node--critical` modifier for emphasis

### User Need Statement
- `blockquote.user-need` — structured as/I need/so that format
- `.user-need-label` and `.user-need-statement` pairs

### Project Cards
- `.project-card` — horizontal layout (40% image, 60% content)
- Image wrapper uses dot-pattern background
- Content includes h3, `.tags`, description, and optional `.project-card-stats`

### Tags
- `.tags` container with `.tag` spans — `--n-200` background, `--fs-label` size, 6px radius

### Lightbox
- Images with `.zoomable` class trigger a `#lightbox` overlay on click
- Lightbox markup: `.lightbox-overlay > .lightbox-close + .lightbox-img`

### Back to Top
- `#back-to-top` button — fixed position, circular, petrol background
- Shown/hidden via `.visible` class toggled by JS on scroll

### Timeline (About page)
- `.timeline-section.timeline-colored > .timeline-container`
- `.timeline-item` with `.timeline-node` (circle on line) and `.timeline-content` (card)
- About page variant uses 2-column grid with date left, content right

### Eyebrow Text
- `.eyebrow-text` — `--fs-body-sm`, uppercase, `letter-spacing: 0.05em`, `--color-text-secondary`

### Utility Classes
- `.cta-group` — flex container for CTA button groups (gap: `--sp-4`)
- `.btn-icon` — inline icon inside buttons (uses petrol SVG filter)
- `.img-full` — `width: 100%` for full-width images
- `.img-card` — full-width image with 8px radius, border, and subtle shadow
- `.grid-2-equal` — 2-column equal grid, collapses to 1 column on mobile (768px)
- `.callout-success` — green-bordered callout box for key stats/results
- `.callout-stat` — large stat number inside callouts (1.4rem)
- `.callout-highlight` — emphasized paragraph text (1.25rem, weight 600)

---

## Grid System

A 12-column grid with gap and responsive utilities.

### Base
- `.grid-12` — `display: grid; grid-template-columns: repeat(12, 1fr); gap: var(--sp-6)`

### Column Spans
- `.col-span-1` through `.col-span-12`

### Gap Utilities
- `.gap-1` through `.gap-10` — maps to `--sp-*` tokens

### Responsive Variants
- `@media (max-width: 768px)`: `.col-span-md-6`, `.col-span-md-12`
- `@media (max-width: 480px)`: `.col-span-sm-12`

### Quick Layouts
- `.grid-2-equal` — simple 2-column layout, collapses on mobile

---

## Page Types

### Homepage (`index.html`)
- Body: no special class
- Structure: header → `.content-container > main` → hero → featured work → video section → footer
- h1 uses `display-lg` scale

### Project Pages (e.g. `scotaccount-project.html`)

**Never use `.content-container` on project pages.** All sections are full-width at the `<body>` level; width is constrained internally by `.hero-wrapper` and `.research-section` (both 1400px max-width, 40px horizontal padding). This shared constraint is what keeps the hero left edge and content left edge aligned.

Body class: `.page-[slug]` (e.g. `.page-cs`, `.page-scotaccount`)
h1 uses `--fs-h1` scale

#### Required HTML skeleton — copy this exactly for every new project page

```html
<body class="page-[slug]">
  <header>
    <div class="header-container">
      <a href="index.html" class="logo">Ryan Gallacher</a>
    </div>
  </header>

  <!-- Hero — full-width dark background, content constrained to 1400px/40px -->
  <section class="hero-section">
    <div class="hero-wrapper">
      <a href="index.html" class="back-button">← Back</a>
      <div class="hero-content">
        <p class="eyebrow-text">Client / Organisation</p>
        <h1>Project Title</h1>
        <p>One or two sentence summary.</p>
        <dl class="hero-stats">
          <div class="hero-stat">
            <dt class="hero-stat-label">My Responsibilities</dt>
            <dd class="hero-stat-number">UX Design, User Research</dd>
          </div>
          <div class="hero-stat">
            <dt class="hero-stat-label">Duration</dt>
            <dd class="hero-stat-number">~ N Months</dd>
          </div>
        </dl>
      </div>
      <div class="hero-image">
        <img src="..." alt="..." fetchpriority="high" decoding="async">
      </div>
    </div>
  </section>

  <!-- Value banner (optional) — only include if you have measurable outcomes -->
  <section class="value-banner-section"> ... </section>

  <!-- Content sections — each constrained to 1400px/40px, same as hero-wrapper -->
  <section class="research-section">
    <div class="research-header">
      <div>
        <h2>Section Title</h2>
      </div>
    </div>
    <!-- Sub-section: heading in col 1, body in col 2 -->
    <div class="research-header">
      <div>
        <h3>Sub-heading</h3>
      </div>
      <div class="research-header-body">
        <p>Body text.</p>
      </div>
    </div>
  </section>

  <!-- Repeat <section class="research-section"> for each major section -->

  <footer> ... </footer>
  <div id="lightbox"> ... </div>
  <button id="back-to-top"> ... </button>
</body>
```

#### research-header rules
- **One child** → spans full width automatically (CSS handles this)
- **Two children** → left column gets heading, right column gets body text
- Never put content outside `.research-section` directly in `<body>`

### About Page (`about.html`)
- Body class: `.about-page`
- Structure: header → `.content-container > main` → timeline section → footer

### Contact Page (`contact.html`)
- Structure: header → `.content-container > main` → contact form → footer
- Form validation via JS with error summary pattern

---

## Principles

- **Agent agnostic by default:** Any tooling, config, docs, or conventions should work across agents (Claude, Cursor, Copilot, etc.) unless there's a specific reason to go agent-specific. Prefer `AGENTS.md` over `CLAUDE.md`, repo-local files over agent memory, and open formats over proprietary ones.

## Information Architecture

When new information, documentation, or research arrives — use this table to decide where it goes.

| Type of content | Where it goes | Notes |
|----------------|---------------|-------|
| Design tokens and visual standards | `AGENT.md` (this file) | Single source of truth for agents and humans |
| New page templates or component patterns | `AGENT.md` under the relevant section | Keep co-located with other patterns |
| Research or external articles | Create `references/` and add a summary file | Summarise key points and relevance — don't just link |
| Sensitive config or secrets | `.env` (never committed) | Never write secrets to the repo |

**Rules:**
- Repo-local always beats agent-specific memory. If it's worth keeping, it belongs in the repo.
- All styles go in `styles.css` — do not create new CSS files.
- If content doesn't fit any category above, ask before creating a new top-level directory.

## Do's and Don'ts

**Do:**
- Use CSS variables for all colours, sizes, and spacing
- Use semantic HTML elements
- Add `:focus-visible` styles to all interactive elements
- Use `--sp-10` (40px) for spacing between sections and above headings
- Use `--sp-4` (16px) between headings and their content
- Test at all breakpoints
- Use `loading="lazy"` on below-fold images

**Don't:**
- Hardcode hex values, pixel font sizes, or spacing values
- Use orange/peach as text colours
- Skip the `:focus-visible` fallback
- Add navigation links to project page headers (they only show the logo)
- Use `!important` unless overriding third-party styles
- Create new CSS files — all styles go in `styles.css`
- Use `.content-container` on project pages — it uses the wrong max-width (1200px) and will misalign the hero and content columns
