# Design System & Agent Guidelines

This is a UX design portfolio built with static HTML, CSS, and vanilla JS. All styles live in a single `styles.css` file. Follow these rules when creating or modifying any page.

---

## Fonts

| Token | Family | Usage |
|-------|--------|-------|
| `--font-family-display` | Lora | Headings (h1–h3), display text, logo, stat numbers |
| `--font-family-sans` | Source Sans 3 | Body text, labels, buttons, navigation, everything else |

Headings use `font-weight: 400`. Body uses `font-weight: 400`, with `600` for emphasis/buttons.

---

## Typography Scale

All text must use these tokens. Never hardcode font sizes.

| Token | Size | Line-height token | Ratio | Usage |
|-------|------|-------------------|-------|-------|
| `--font-size-display-lg` | 60px | `--line-height-display-lg` | 1.20 | Homepage h1 |
| `--font-size-display-sm` | 48px | `--line-height-display-sm` | 1.17 | About page section heading |
| `--font-size-4xl` | 36px | `--line-height-tight` | 1.2 | Project page h1 |
| `--font-size-3xl` | 32px | `--line-height-snug` | 1.35 | Section headings |
| `--font-size-2xl` | 24px | `--line-height-snug` | 1.35 | Sub-section headings |
| `--font-size-md` | 16px | `--line-height-body` | 1.5 | Default body text |
| `--font-size-sm` | 14px | `1.25rem` | 1.43 | Eyebrow text, labels, buttons, table text |
| `--font-size-xs` | 12px | `1rem` | 1.33 | Captions, meta text |
| `--font-size-lg` | 18px | `--line-height-body` | 1.5 | Large body |
| `--font-size-xl` | 20px | `--line-height-body` | 1.5 | Oversize body / small heading |

Line heights for body-sm and smaller are hardcoded (`1.25rem`, `1rem`) — no design system token equivalent. Line heights for headings are unitless ratios that scale automatically with responsive font sizes.

Aliases: `--font-size-sm` covers button text and table text.

---

## Spacing Scale

Based on a 4px grid. Use `--space-*` tokens for all margin and padding values.

| Token | Value | Common use |
|-------|-------|------------|
| `--space-1` | 4px | Tight gaps |
| `--space-2` | 8px | Between label and field, caption to image |
| `--space-3` | 12px | Minor internal spacing |
| `--space-4` | 16px | Heading to its content |
| `--space-5` | 20px | — |
| `--space-6` | 24px | Inner padding, nav gaps |
| `--space-8` | 32px | Card content padding, grid gaps |
| `--space-10` | 40px | **Section spacing, heading margin-top** |
| `--space-12` | 48px | Large section padding |
| `--space-16` | 64px | Major vertical gaps |
| `--space-20` | 80px | Page-level padding |

### Spacing Rules

- **40px (`--space-10`)** between sections, between content blocks, and above h2/h3 headings
- Heading-to-content gap scales with font size:
  - **24px (`--space-6`)** — `display-lg` (60px, homepage h1)
  - **24px (`--space-6`)** — `display-sm` (48px, about page h1)
  - **16px (`--space-4`)** — `h1` (36px) and smaller
- **8px (`--space-2`)** from image to caption, label to field
- First heading in a section gets `margin-top: 0` (the section spacing handles it)
- h3 directly after h2: use `--space-4` (tighter coupling)
- h3 inside `.research-header`: use `--space-6` top, `--space-4` bottom
- Component-internal headings (post-it cards, panels, etc.): `margin-top: 0`

---

## Colour Palette

Always use CSS variables. Never hardcode hex values.

### Neutrals
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-neutral-0` | #FFFFFF | Surface background |
| `--color-neutral-50` | #F9FAFA | Body background |
| `--color-neutral-100` | #F0F4F4 | Alternate surface, input background |
| `--color-neutral-200` | #E1E8E8 | Borders, tags, footer, disabled backgrounds |
| `--color-neutral-300` | #9BA9A9 | Stronger borders, disabled text |
| `--color-neutral-400` | #7A8B8D | — |
| `--color-neutral-500` | #5E6E70 | Secondary text |
| `--color-neutral-600` | #455456 | — |
| `--color-neutral-800` | #233D4D | Primary text |
| `--color-neutral-900` | #142224 | Darkest, used sparingly |

### Brand Petrol (Primary)
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-petrol-500` | #034C53 | Primary buttons, focus rings, logo |
| `--color-petrol-700` | #023D42 | Button hover |
| `--color-petrol-900` | #012629 | Button active |
| `--color-petrol-50` | #E6EDEE | Light petrol backgrounds |

### Teal
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-teal-500` | #007074 | Accents, timeline nodes |
| `--color-teal-600` | #005B5E | — |
| `--color-teal-700` | #004547 | — |
| `--color-teal-300` | #00C4C8 | Highlight accents |
| `--color-teal-50` | #E6F1F1 | Light teal backgrounds |

### Peach
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-peach-400` | #F79B72 | Stat borders, decorative accents |
| `--color-peach-600` | #DF8C67 | — |
| `--color-peach-700` | #C77D5C | — |
| `--color-peach-50` | #FFF7F1 | Light peach backgrounds |

### Accent Orange
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-orange-400` | #FE7F2D | Icons/borders only — never for text |
| `--color-orange-600` | #E57229 | — |
| `--color-orange-700` | #CC6624 | — |
| `--color-orange-50` | #FFF3E6 | Warning backgrounds |

### Semantic
| Token | Hex | Usage |
|-------|-----|-------|
| `--color-red-500` | #DA1E28 | Errors |
| `--color-green-500` | #4A9A51 | Success |
| `--color-blue-500` | #0066CC | Links |

### Semantic Surface & Text (prefer these)
Use these over raw palette tokens when the context is clear:

| Token | Maps to | Usage |
|-------|---------|-------|
| `--color-neutral-800` | — | Primary text (intentionally 800, not 900) |
| `--color-text-secondary` | `--color-neutral-500` | Secondary/muted text |
| `--color-text-disabled` | `--color-neutral-300` | Disabled text |
| `--color-text-on-interactive` | `--color-neutral-0` | Text on buttons |
| `--color-surface-subtle` | `--color-neutral-50` | Page background |
| `--color-surface-default` | `--color-neutral-0` | Card/panel backgrounds |
| `--color-surface-raised` | `--color-neutral-100` | Alternate surfaces |
| `--color-surface-elevated` | `--color-neutral-200` | Tooltip backgrounds, speech-bubble tails |
| `--color-surface-disabled` | `--color-neutral-200` | Disabled input backgrounds |
| `--color-border-default` | `--color-neutral-200` | Default borders |
| `--color-border-strong` | `--color-neutral-300` | Emphasized borders |
| `--color-link-default` | `--color-blue-500` | Link text |
| `--color-focus-ring` | `--color-petrol-500` | Keyboard focus outlines |
| `--color-interactive-default` | `--color-petrol-500` | Interactive elements at rest |
| `--color-interactive-hover` | `--color-petrol-700` | Interactive elements on hover |
| `--color-interactive-active` | `--color-petrol-900` | Interactive elements on press |

### Feedback tokens
| Token | Usage |
|-------|-------|
| `--color-feedback-danger-text` | Error text |
| `--color-feedback-danger-bg` | Error background |
| `--color-feedback-danger-border` | Error border |
| `--color-feedback-success-text` | Success text |
| `--color-feedback-success-bg` | Success background |
| `--color-feedback-info-text` | Info text |
| `--color-feedback-info-bg` | Info background |

---

## Shadows & Motion

| Token | Value |
|-------|-------|
| `--shadow-sm` | `0 2px 4px rgba(20, 34, 36, 0.08)` |
| `--shadow-md` | `0 4px 12px rgba(20, 34, 36, 0.12)` |
| `--shadow-lg` | `0 8px 16px rgba(20, 34, 36, 0.14)` |
| `--shadow-inset` | `inset 0 1px 2px rgba(20, 34, 36, 0.06)` |

For transitions, use `var(--duration-medium) var(--easing-standard)` (150ms ease-in-out). There is no single `--motion-fast` alias — write both tokens.

---

## Layout

Two content column widths are used depending on page type. Never mix them on the same page.

| Page type | Max-width | Horizontal padding | CSS pattern |
|-----------|-----------|-------------------|-------------|
| Project pages | 1400px | 40px | `.hero-wrapper`, `.research-section` |
| Homepage / About / Contact | 1200px | 24px (`--space-6`) | `.content-container` |

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

Font and spacing tokens are overridden via `:root` at breakpoints inside the design system token files — do not hardcode values at each breakpoint, update the token instead.

**Typography (`768px` and `480px`)**

| Token | Desktop | 768px | 480px |
|-------|---------|-------|-------|
| `--font-size-display-lg` (via `--font-size-6xl`) | 60px | 40px | 32px |
| `--font-size-display-sm` (via `--font-size-5xl`) | 48px | 32px | 24px |
| `--font-size-4xl` | 36px | 28px | 24px |
| `--font-size-3xl` | 32px | 24px | 20px |
| `--font-size-2xl` | 24px | 20px | 18px |

Line heights for headings are unitless ratios (`--line-height-tight` 1.2, `--line-height-snug` 1.35) — they scale automatically with font size.

**Spacing (`768px` and `480px`)**

| Token | Desktop | 768px | 480px |
|-------|---------|-------|-------|
| `--space-8` | 32px | 32px | 24px |
| `--space-10` | 40px | 32px | 24px |
| `--space-12` | 48px | 40px | 32px |
| `--space-16` | 64px | 48px | 40px |
| `--space-20` | 80px | 56px | 48px |

Tokens `--space-1` through `--space-6` do not scale — they are small enough to remain consistent.

---

## Accessibility

- **Focus states**: Use `:focus-visible` with `outline: 3px solid var(--color-focus-ring); outline-offset: 3px`. Always include `@supports not selector(:focus-visible)` fallback.
- **Semantic HTML**: Use `section`, `nav`, `main`, `header`, `footer`, `article`, `dl`/`dt`/`dd` where appropriate.
- **Colour contrast**: Never use orange (`--color-orange-400`) or peach (`--color-peach-400`) as text colours — they fail WCAG contrast on light backgrounds. Use them only for icons, borders, and decorative elements.
- **Images**: Always include meaningful `alt` text. Use `loading="lazy"` and `decoding="async"` for below-fold images. Use `fetchpriority="high"` for hero images.

---

## Component Patterns

These are the reusable patterns in the codebase. Reference existing HTML pages for exact markup.

### Header
- `.header-container` — 48px height, logo left, nav right
- Logo uses `--font-family-display` in `--color-petrol-500` colour
- Nav links use animated underline on hover

### Footer
- `footer` — `--color-neutral-200` background, centred nav links and copyright
- Copyright year set dynamically via JS (`id="year"`)

### Buttons
- **Primary** (`.btn-primary`, `.cta-button`): 40px height, 24px horizontal padding, 6px radius, `--color-interactive-default` background
- **Secondary** (`.btn-secondary`): Same dimensions, white background with 2px border
- Both shift to hover states using `--color-interactive-hover`

### Hero — Homepage
- `.hero` inside `.content-container` — two-column flex (text left, image right)
- Uses `.line-grid-accent` for background pattern
- h1 uses `--font-size-display-lg`

### Hero — Project Pages
- `.hero-section > .hero-wrapper` — dark background, full-width
- Includes `.back-button`, `.eyebrow-text`, h1 (uses `--font-size-4xl`), description paragraphs, and `.hero-stats` (dl/dt/dd)
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
- `.tags` container with `.tag` spans — `--color-neutral-200` background, `--font-size-xs` size, 6px radius

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
- `.eyebrow-text` — `--font-size-sm`, uppercase, `letter-spacing: 0.05em`, `--color-text-secondary`

### Utility Classes
- `.cta-group` — flex container for CTA button groups (gap: `--space-4`)
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
- `.grid-12` — `display: grid; grid-template-columns: repeat(12, 1fr); gap: var(--space-6)`

### Column Spans
- `.col-span-1` through `.col-span-12`

### Gap Utilities
- `.gap-1` through `.gap-10` — maps to `--space-*` tokens

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
- h1 uses `--font-size-display-lg`

### Project Pages (e.g. `scotaccount-project.html`)

**Never use `.content-container` on project pages.** All sections are full-width at the `<body>` level; width is constrained internally by `.hero-wrapper` and `.research-section` (both 1400px max-width, 40px horizontal padding). This shared constraint is what keeps the hero left edge and content left edge aligned.

Body class: `.page-[slug]` (e.g. `.page-cs`, `.page-scotaccount`)
h1 uses `--font-size-4xl`

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
- **Cite design sources:** Every design recommendation must cite a specific source — a named component or pattern from a design system (Carbon, GOV.UK, Material, etc.), a specific article or guideline, or a WCAG criterion by number. "General principles" is not an acceptable citation. This applies to conversational design opinions as well as implementation decisions. If no named pattern exists for a given case, say so explicitly before recommending.

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
- Use `--space-10` (40px) for spacing between sections and above headings
- Use `--space-4` (16px) between headings and their content
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
- Use old bridge token names (`--sp-*`, `--fs-*`, `--lh-*`, `--ff-*`, `--n-*`, `--p-base`, `--color-ink`, `--color-bg-*`, `--btn-*`, `--input-border`, `--motion-fast`) — the bridge has been removed; these names are undefined
