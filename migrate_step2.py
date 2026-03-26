with open('styles_step1.css', 'r', encoding='utf-8') as f:
    css = f.read()

replacements = [
    # Typography - font families
    ('var(--ff-sans)', 'var(--font-family-sans)'),
    ('var(--ff-serif)', 'var(--font-family-display)'),
    # Font sizes - order from most specific to least
    ('var(--fs-display-lg)', 'var(--font-size-6xl)'),
    ('var(--fs-display-sm)', 'var(--font-size-5xl)'),
    ('var(--fs-h1)', 'var(--font-size-4xl)'),
    ('var(--fs-h2)', 'var(--font-size-3xl)'),
    ('var(--fs-h3)', 'var(--font-size-2xl)'),
    ('var(--fs-body-compact)', 'var(--font-size-xs)'),
    ('var(--fs-body-sm)', 'var(--font-size-sm)'),
    ('var(--fs-body)', 'var(--font-size-md)'),
    ('var(--fs-label-lg)', 'var(--font-size-sm)'),
    ('var(--fs-label)', 'var(--font-size-xs)'),
    ('var(--fs-button)', 'var(--font-size-sm)'),
    ('var(--fs-table)', 'var(--font-size-sm)'),
    ('var(--fs-small)', 'var(--font-size-sm)'),
    # Line heights - display sizes have tokens
    ('var(--lh-display-lg)', 'var(--line-height-display-lg)'),
    ('var(--lh-display-sm)', 'var(--line-height-display-sm)'),
    # Line heights without tokens - keep var name, add TODO comment
    ('var(--lh-h1)', 'var(--lh-h1) /* TODO: token gap - heading line-height (2.75rem) not in token scale */'),
    ('var(--lh-h2)', 'var(--lh-h2) /* TODO: token gap - heading line-height (2.5rem) not in token scale */'),
    ('var(--lh-h3)', 'var(--lh-h3) /* TODO: token gap - heading line-height (2.25rem) not in token scale */'),
    ('var(--lh-body-sm)', 'var(--lh-body-sm) /* TODO: token gap - body-sm line-height (1.25rem) not in token scale */'),
    ('var(--lh-body-compact)', 'var(--lh-body-compact) /* TODO: token gap - compact line-height (1rem) not in token scale */'),
    ('var(--lh-label-lg)', 'var(--lh-label-lg) /* TODO: token gap - label-lg line-height not in token scale */'),
    ('var(--lh-label)', 'var(--lh-label) /* TODO: token gap - label line-height not in token scale */'),
    ('var(--lh-body)', 'var(--line-height-body)'),
    # Spacing
    ('var(--sp-20)', 'var(--space-20)'),
    ('var(--sp-16)', 'var(--space-16)'),
    ('var(--sp-12)', 'var(--space-12)'),
    ('var(--sp-10)', 'var(--space-10)'),
    ('var(--sp-8)', 'var(--space-8)'),
    ('var(--sp-6)', 'var(--space-6)'),
    ('var(--sp-5)', 'var(--space-5)'),
    ('var(--sp-4)', 'var(--space-4)'),
    ('var(--sp-3)', 'var(--space-3)'),
    ('var(--sp-2)', 'var(--space-2)'),
    ('var(--sp-1)', 'var(--space-1)'),
    # Functional color vars - do these before primitives to avoid double-replacement
    ('var(--color-ink)', 'var(--color-brand-ink)'),
    ('var(--color-ink-subtle)', 'var(--color-text-secondary) /* TODO: token gap - --color-ink-subtle was undefined in source */'),
    ('var(--color-bg-body)', 'var(--color-surface-subtle)'),
    ('var(--color-bg-surface-raised)', 'var(--color-surface-raised)'),
    ('var(--color-bg-surface-alt)', 'var(--color-surface-raised)'),
    ('var(--color-bg-surface)', 'var(--color-surface-default)'),
    ('var(--color-bg-disabled)', 'var(--color-surface-disabled)'),
    ('var(--color-brand-ink-base)', 'var(--color-brand-ink)'),
    ('var(--color-brand-ink-pattern)', 'var(--color-surface-subtle)'),
    ('var(--color-teal-base)', 'var(--color-interactive-default)'),
    ('var(--color-teal-wash)', 'var(--color-brand-teal-wash)'),
    ('var(--color-teal-pattern)', 'var(--color-brand-primary-wash)'),
    ('var(--color-camel-base)', 'var(--color-brand-peach)'),
    ('var(--color-camel-wash)', 'var(--color-brand-peach-wash)'),
    ('var(--color-camel-pattern)', 'var(--color-feedback-warning-bg)'),
    ('var(--color-link-active)', 'var(--color-blue-700)'),
    ('var(--info-base)', 'var(--color-feedback-info-text)'),
    ('var(--info-bg)', 'var(--color-feedback-info-bg)'),
    ('var(--success-base)', 'var(--color-feedback-success-text)'),
    ('var(--success-bg)', 'var(--color-feedback-success-bg)'),
    ('var(--warning-base)', 'var(--color-feedback-warning-text)'),
    ('var(--warning-bg)', 'var(--color-feedback-warning-bg)'),
    ('var(--warning-accent)', 'var(--color-feedback-warning-border)'),
    ('var(--error-base)', 'var(--color-feedback-danger-text)'),
    ('var(--error-bg)', 'var(--color-feedback-danger-bg)'),
    # Button tokens
    ('var(--btn-primary-bg)', 'var(--color-interactive-default)'),
    ('var(--btn-primary-text)', 'var(--color-text-on-interactive)'),
    ('var(--btn-primary-hover-bg)', 'var(--color-interactive-hover)'),
    ('var(--btn-primary-disabled-bg)', 'var(--color-surface-disabled)'),
    ('var(--btn-primary-disabled-text)', 'var(--color-text-disabled)'),
    ('var(--btn-secondary-text)', 'var(--color-brand-ink)'),
    ('var(--btn-secondary-border)', 'var(--color-brand-ink)'),
    ('var(--btn-secondary-hover-bg)', 'var(--color-surface-raised)'),
    # Input tokens
    ('var(--input-bg)', 'var(--color-surface-raised)'),
    ('var(--input-border-hover)', 'var(--color-text-secondary)'),
    ('var(--input-border-focus)', 'var(--color-interactive-default)'),
    ('var(--input-focus-ring)', 'var(--color-brand-teal-wash)'),
    ('var(--input-inset-shadow)', 'var(--shadow-inset)'),
    ('var(--input-error-border)', 'var(--color-feedback-danger-text)'),
    ('var(--input-error-bg)', 'var(--color-feedback-danger-bg)'),
    ('var(--input-border)', 'var(--color-border-strong)'),
    # Hover bg variables
    ('var(--ink-hover-bg)', 'var(--color-brand-ink-wash) /* TODO: token gap - ink-hover-bg was translucent rgba; mapped to closest opaque token */'),
    ('var(--camel-hover-bg)', 'var(--color-brand-peach-wash) /* TODO: token gap - camel-hover-bg was translucent rgba */'),
    ('var(--teal-hover-bg)', 'var(--color-brand-teal-wash) /* TODO: token gap - teal-hover-bg was translucent rgba */'),
    ('var(--surface-hover)', 'var(--color-surface-subtle) /* TODO: token gap - surface-hover was rgba(0.03) translucent */'),
    # Motion
    ('var(--motion-fast)', 'var(--duration-medium) var(--easing-standard)'),
    # Shadows
    ('var(--shadow-level-1)', 'var(--shadow-sm)'),
    ('var(--shadow-level-2)', 'var(--shadow-md)'),
    ('var(--shadow-level-3)', 'var(--shadow-lg)'),
    # Petrol primitives
    ('var(--p-base)', 'var(--color-interactive-default)'),
    ('var(--p-hover)', 'var(--color-interactive-hover)'),
    ('var(--p-active)', 'var(--color-interactive-active)'),
    ('var(--p-tint)', 'var(--color-brand-primary-wash)'),
    # Teal primitives
    ('var(--teal-base)', 'var(--color-brand-teal)'),
    ('var(--teal-hover)', 'var(--color-teal-600)'),
    ('var(--teal-active)', 'var(--color-teal-700)'),
    ('var(--teal-vivid)', 'var(--color-teal-300)'),
    ('var(--teal-light)', 'var(--color-brand-teal-wash)'),
    # Peach primitives
    ('var(--peach-base)', 'var(--color-brand-peach)'),
    ('var(--peach-hover)', 'var(--color-peach-600)'),
    ('var(--peach-active)', 'var(--color-peach-700)'),
    ('var(--peach-light)', 'var(--color-brand-peach-wash)'),
    # Orange/accent primitives
    ('var(--a-base)', 'var(--color-feedback-warning-border)'),
    ('var(--a-hover)', 'var(--color-orange-600)'),
    ('var(--a-active)', 'var(--color-orange-700)'),
    ('var(--a-light)', 'var(--color-feedback-warning-bg)'),
    ('var(--a-text)', 'var(--color-text-primary)'),
    # Red primitives
    ('var(--red-base)', 'var(--color-feedback-danger-text)'),
    ('var(--red-hover)', 'var(--color-red-600)'),
    ('var(--red-active)', 'var(--color-red-700)'),
    ('var(--red-light)', 'var(--color-feedback-danger-bg)'),
    # Green primitives
    ('var(--green-base)', 'var(--color-feedback-success-text)'),
    ('var(--green-hover)', 'var(--color-green-600)'),
    ('var(--green-active)', 'var(--color-green-700)'),
    ('var(--green-light)', 'var(--color-feedback-success-bg)'),
    # Blue primitives
    ('var(--blue-base)', 'var(--color-link-default)'),
    ('var(--blue-hover)', 'var(--color-link-hover)'),
    ('var(--blue-active)', 'var(--color-blue-700)'),
    ('var(--blue-visited)', 'var(--color-link-visited)'),
    # Neutral primitives
    ('var(--n-0)', 'var(--color-surface-default)'),
    ('var(--n-50)', 'var(--color-surface-subtle)'),
    ('var(--n-100)', 'var(--color-surface-raised)'),
    ('var(--n-200)', 'var(--color-border-default)'),
    ('var(--n-300)', 'var(--color-border-strong)'),
    ('var(--n-400)', 'var(--color-text-muted)'),
    ('var(--n-500)', 'var(--color-text-secondary)'),
    ('var(--n-600)', 'var(--color-neutral-600)'),
    ('var(--n-800)', 'var(--color-brand-ink)'),
    ('var(--n-900)', 'var(--color-text-primary)'),
]

for old, new in replacements:
    count = css.count(old)
    if count > 0:
        css = css.replace(old, new)
        print(f"  Replaced {count}x: {old}")

print("\nDone.")
with open('styles_step2.css', 'w', encoding='utf-8') as f:
    f.write(css)
