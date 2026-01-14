---
description: Modern React UI patterns for loading states, error handling, and data fetching. Use when building UI components, handling async data, or managing UI states.
---

# React UI Patterns

This workflow defines standard patterns for UI states, error handling, and data management.

## When to Use

Use this workflow when:
- Building UI components
- Handling async data fetching
- Managing loading, error, or empty states

## Instructions

1.  **Loading States**:
    -   **Golden Rule**: Show loading indicator ONLY when there is no data to display.
    -   Avoid flashing spinners if cached data is available.
    -   Use Skeletons for known shapes, Spinners for unknown/overlay.

2.  **Error Handling**:
    -   **Never** swallow errors silently.
    -   Hierarchy: Inline > Toast > Banner > Full Screen.
    -   Use Error State components with retry options.

3.  **Empty States**:
    -   Always provide an explicit empty state for lists/collections.
    -   Make empty states actionable if possible (e.g., "Create Item").

4.  **Button States**:
    -   Show loading state on the button itself.
    -   Disable the button during async operations.

## Anti-Patterns to Avoid

-   Showing a full-page spinner when refreshing data that is already visible.
-   Using `console.log(error)` as the only error handling.
-   Leaving buttons enabled during submission.
