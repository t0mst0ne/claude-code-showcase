---
description: Formik form handling with validation patterns. Use when building forms, implementing validation, or handling form submission.
---

# Formik Patterns

This workflow provides best practices for building forms using Formik and Yup.

## When to Use

Use this workflow when:
- Building forms
- Implementing validation
- Handling form submission

## Instructions

1.  **Form Setup**:
    -   Use `useFormik` hook.
    -   Define `initialValues` and `validationSchema` (using `yup`).
    -   Implement `onSubmit` handler.

2.  **Validation**:
    -   Use `yup` for schema validation.
    -   Common patterns: `email`, `required`, `min`, `max`, `matches`.
    -   Conditional validation using `when`.

3.  **UI Integration**:
    -   Connect fields using `value`, `onChangeText`, `onBlur`.
    -   Display validation errors when `touched`.
    -   Disable submit button when invalid or submitting.

4.  **Submission**:
    -   Handle loading state.
    -   Handle errors (try/catch/_onError_ logic).
    -   Reset form or flags (e.g., `setSubmitting(false)`) in `finally`.

## Anti-Patterns to Avoid

-   Not showing validation errors.
-   Allowing submission while invalid or already submitting.
-   Swallowing submission errors without user feedback.
