---
description: Core component library and design system patterns. Use when building UI, using design tokens, or working with the component library.
---

# Core Components

This workflow outlines the usage of the core component library and design system patterns.

## When to Use

Use this workflow when:
- Building UI components
- Styling elements
- Working with the component library

## Instructions

1.  **Use Design Tokens**:
    -   **NEVER** hard-code values (spacing, colors, typography).
    -   Use `spacing` tokens (e.g., `$4` for 16px).
    -   Use `color` tokens (e.g., `$textPrimary`, `$primary500`).
    -   Use `typography` tokens (e.g., `$lg` for font size).

2.  **Use Core Components**:
    -   Use `Box` for layout instead of `View` or `div`.
    -   Use `HStack` and `VStack` for flex layouts.
    -   Use `Text` for typography.
    -   Use `Button` for actions (solid, outline, ghost).
    -   Use `Input` for form fields.

3.  **Component Props**:
    -   Create components with token-based props.
    -   Example: `padding?: '$2' | '$4' | '$6'`

## Anti-Patterns to Avoid

-   Hard-coding values (e.g., `padding={16}`).
-   Using raw platform components (`View`, `Text` from react-native) instead of core components.
-   Inline styles.
