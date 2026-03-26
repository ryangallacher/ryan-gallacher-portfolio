import re

with open('styles_step3.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Handle transition duration replacements
# 0.2s ease -> var(--duration-medium) var(--easing-standard) -- but 0.2s=200ms which is close to medium (150ms) or slow(300ms)
# 0.2s = 200ms -- between medium(150ms) and slow(300ms). Closest is medium. Flag as gap.
# 0.3s ease -> var(--duration-slow) var(--easing-standard)
# 0.25s ease -> gap
# transition: all 0.3s ease -> var(--duration-slow) var(--easing-standard)

transition_replacements = [
    ('transition: transform 0.2s;', 'transition: transform var(--duration-medium);'),
    ('transition: transform 0.2s ease;', 'transition: transform var(--duration-medium) var(--easing-standard);'),
    ('transition: background-color 0.3s ease', 'transition: background-color var(--duration-slow) var(--easing-standard)'),
    ('transition: all 0.3s ease', 'transition: all var(--duration-slow) var(--easing-standard)'),
    ('transition: color 0.2s', 'transition: color var(--duration-medium) /* TODO: token gap - 0.2s (200ms) not in motion scale; using --duration-medium (150ms) */'),
    ('transition: width 0.3s ease', 'transition: width var(--duration-slow) var(--easing-standard)'),
    ('transition: opacity 0.2s ease', 'transition: opacity var(--duration-medium) var(--easing-standard)'),
    ('transition: opacity 0.25s ease, visibility 0.25s ease', 'transition: opacity var(--duration-medium) var(--easing-standard), visibility var(--duration-medium) var(--easing-standard) /* TODO: token gap - 0.25s not in motion scale */'),
    ('transition: all 0.3s;', 'transition: all var(--duration-slow);'),
    ('transition: max-width 0.2s ease, max-height 0.2s ease', 'transition: max-width var(--duration-medium) var(--easing-standard), max-height var(--duration-medium) var(--easing-standard)'),
    ('transition: background 0.2s ease', 'transition: background var(--duration-medium) var(--easing-standard)'),
    ('transition: border-color 0.2s, color 0.2s, background 0.2s', 'transition: border-color var(--duration-medium), color var(--duration-medium), background var(--duration-medium)'),
]

for old, new in transition_replacements:
    count = css.count(old)
    if count > 0:
        css = css.replace(old, new)
        print(f"  Replaced {count}x transition: {old[:60]}")

# Handle rgba() shadow values
shadow_replacements = [
    # box-shadow: -4px 0 24px 0 rgba(20, 34, 36, 0.10) -> close to shadow-lg but custom offset
    ('box-shadow: -4px 0 24px 0 rgba(20, 34, 36, 0.10)',
     'box-shadow: -4px 0 24px 0 rgba(20, 34, 36, 0.10) /* TODO: token gap - custom directional shadow, no token equivalent */'),
    # box-shadow: 0 4px 12px rgba(3, 76, 83, 0.3) -> petrol-tinted shadow, close to shadow-focus
    ('box-shadow: 0 4px 12px rgba(3, 76, 83, 0.3)',
     'box-shadow: 0 4px 12px rgba(3, 76, 83, 0.3) /* TODO: token gap - petrol-tinted box-shadow (back-to-top) not in token scale */'),
    # box-shadow: 0 6px 16px rgba(3, 76, 83, 0.4)
    ('box-shadow: 0 6px 16px rgba(3, 76, 83, 0.4)',
     'box-shadow: 0 6px 16px rgba(3, 76, 83, 0.4) /* TODO: token gap - petrol-tinted hover shadow not in token scale */'),
    # postit-card shadow
    ('box-shadow: 0 4px 6px rgba(31, 42, 55, 0.1)',
     'box-shadow: var(--shadow-sm) /* TODO: token gap - 0 4px 6px rgba(31,42,55,0.1) mapped to shadow-sm as closest */'),
    # postit-card::after shadow
    ('box-shadow: -2px 2px 3px rgba(31, 42, 55, 0.15)',
     'box-shadow: -2px 2px 3px rgba(31, 42, 55, 0.15) /* TODO: token gap - directional corner shadow not in token scale */'),
]

for old, new in shadow_replacements:
    count = css.count(old)
    if count > 0:
        css = css.replace(old, new)
        print(f"  Replaced {count}x shadow: {old[:60]}")

# Handle border: 1px solid rgba(3, 76, 83, 0.25) -> petrol-tinted border
css = css.replace(
    'border: 1px solid rgba(3, 76, 83, 0.25)',
    'border: 1px solid rgba(3, 76, 83, 0.25) /* TODO: token gap - semi-transparent petrol border not in token scale */'
)

# Handle radius values
radius_replacements = [
    # border-radius: 6px -> --radius-md
    ('border-radius: 6px', 'border-radius: var(--radius-md)'),
    # border-radius: 4px -> --radius-sm
    ('border-radius: 4px', 'border-radius: var(--radius-sm)'),
    # border-radius: 8px -> --radius-lg
    ('border-radius: 8px', 'border-radius: var(--radius-lg)'),
    # border-radius: 2px -> --radius-xs
    ('border-radius: 2px', 'border-radius: var(--radius-xs)'),
    # border-radius: 50% -> --radius-circle
    ('border-radius: 50%', 'border-radius: var(--radius-circle)'),
    # border-radius: 4px 4px 0 0 -> partial, keep with tokens where possible
    ('border-radius: 4px 4px 0 0', 'border-radius: var(--radius-sm) var(--radius-sm) 0 0'),
    ('border-radius: 4px 0 0 4px', 'border-radius: var(--radius-sm) 0 0 var(--radius-sm)'),
    # 20px is for pill/tag shape — not in token scale
    ('border-radius: 20px', 'border-radius: 20px /* TODO: token gap - pill radius (20px) not in token scale; consider 999px */'),
    # border-radius: 0 — no change needed (explicit none)
]

for old, new in radius_replacements:
    count = css.count(old)
    if count > 0:
        css = css.replace(old, new)
        print(f"  Replaced {count}x radius: {old}")

print("\nStep 4 done.")
with open('styles_step4.css', 'w', encoding='utf-8') as f:
    f.write(css)
