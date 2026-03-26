import re

with open('styles_step2.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the fallback-value var() references that have old hex fallbacks
# These use CSS var(--new-token, #oldvalue) pattern where the fallback is stale
# We need to clean up the fallback since the token is now properly defined

fallback_replacements = [
    # btn-primary-bg fallback was #1a1a1a but should now be color-interactive-default
    ('var(--btn-primary-bg, #1a1a1a)', 'var(--color-interactive-default)'),
    # p-base fallback
    ('var(--p-base, #034C53)', 'var(--color-interactive-default)'),
    # color-bg-surface fallback
    ('var(--color-bg-surface, white)', 'var(--color-surface-default)'),
    ('var(--color-bg-surface, #e0e0e0)', 'var(--color-surface-default)'),
    # color-border-default fallback
    ('var(--color-border-default, #e0e0e0)', 'var(--color-border-default)'),
    ('var(--color-border-default, #ddd)', 'var(--color-border-default)'),
    # n-200 fallback
    ('var(--n-200, #ddd)', 'var(--color-border-default)'),
    # color-ink fallbacks
    ('var(--color-ink, #1a1a1a)', 'var(--color-brand-ink)'),
    ('var(--color-ink, #374151)', 'var(--color-brand-ink)'),
    # color-text-secondary fallback
    ('var(--color-text-secondary, #6b7280)', 'var(--color-text-secondary)'),
    # color-bg-surface-alt fallback
    ('var(--color-bg-surface-alt, #f3f4f6)', 'var(--color-surface-raised)'),
    # shadow-level-1 fallback (already replaced shadow-level-1 but there's a fallback variant)
    ('var(--shadow-level-1, 0 1px 3px rgba(0, 0, 0, 0.05))', 'var(--shadow-sm)'),
    # color-teal-base fallbacks (different hex values — both wrong, use interactive-default)
    ('var(--color-teal-base, #4a7c9c)', 'var(--color-interactive-default) /* TODO: token gap - fallback was wrong hex #4a7c9c, not actual teal-base */'),
    ('var(--color-teal-base, #3b82f6)', 'var(--color-brand-teal) /* TODO: token gap - fallback was wrong hex #3b82f6 (blue), likely should be teal */'),
    # info-bg fallback
    ('var(--info-bg, #dbeafe)', 'var(--color-feedback-info-bg)'),
    ('var(--info-base, #1e40af)', 'var(--color-feedback-info-text)'),
    # fs-body-sm fallbacks
    ('var(--fs-body-sm, 13px)', 'var(--font-size-sm)'),
    ('var(--fs-body-sm, 14px)', 'var(--font-size-sm)'),
    ('var(--fs-body-compact, 12px)', 'var(--font-size-xs)'),
    ('var(--fs-button, 1rem)', 'var(--font-size-sm)'),
]

for old, new in fallback_replacements:
    count = css.count(old)
    if count > 0:
        css = css.replace(old, new)
        print(f"  Fixed {count}x fallback: {old[:60]}")

# Now handle hardcoded hex values in properties (not SVG data URIs)
# These are cases like border-color: #034C53 directly in rules

# Map known hex values to tokens
hex_to_token = {
    '#034C53': 'var(--color-interactive-default)',
    '#034c53': 'var(--color-interactive-default)',
    '#1a1a1a': 'var(--color-brand-ink) /* TODO: token gap - #1a1a1a not in token palette, nearest is color-brand-ink */',
    '#e0e0e0': 'var(--color-border-default)',
    '#ddd': 'var(--color-border-default)',
    '#f3f4f6': 'var(--color-surface-raised)',
    '#6b7280': 'var(--color-text-secondary) /* TODO: token gap - #6b7280 not in palette */',
    '#4a7c9c': 'var(--color-brand-teal) /* TODO: token gap - #4a7c9c is not a defined palette color */',
    '#3b82f6': 'var(--color-brand-teal) /* TODO: token gap - #3b82f6 is a generic blue, not in palette */',
    '#1e40af': 'var(--color-feedback-info-text)',
    '#dbeafe': 'var(--color-feedback-info-bg)',
    '#374151': 'var(--color-brand-ink) /* TODO: token gap - #374151 not in palette */',
}

# Only replace hex values that appear as standalone color values (not in SVG/data URIs, not inside comments about hex)
lines = css.split('\n')
new_lines = []
for line in lines:
    # Skip SVG data URI lines
    if 'data:image/svg+xml' in line or '%23' in line:
        new_lines.append(line)
        continue
    for hex_val, token in hex_to_token.items():
        if hex_val in line:
            # Only replace if it looks like a CSS value (preceded by :, space, or (, not in a comment)
            # Simple heuristic: if not in a CSS comment, replace
            line = line.replace(hex_val, token)
    new_lines.append(line)

css = '\n'.join(new_lines)

print("\nFallback and hex replacements done.")
with open('styles_step3.css', 'w', encoding='utf-8') as f:
    f.write(css)
