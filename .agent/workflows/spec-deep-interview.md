---
description: Deep interview methodology for refining specifications. Use when reviewing SPEC files, PRDs, or feature requirements.
---

# Spec Deep Interview

This workflow provides a structured approach to reviewing and refining specifications using the "Ultrathink" and "Deep Interview" methodology.

## When to Use

Use this workflow when:
- Reviewing a new SPEC or PRD.
- Refining feature requirements.
- Identifying gaps or technical feasibility issues.

## Instructions

1.  **Analyze (Ultrathink)**:
    -   Identify hidden assumptions (system state, user behavior).
    -   Find unexplored edge cases (scale, concurrency, failures).
    -   Spot technical debt accumulation points.
    -   Consider second/third order effects.

2.  **Question (Systematic)**:
    -   **Technical**: Architecture, data models, API contracts, performance.
    -   **UI/UX**: User flows, error states, empty states, responsiveness.
    -   **Operational**: Deployment, monitoring, data migration.
    -   **Business**: Edge cases, validation rules, compliance.

3.  **Document Gaps**:
    -   Record clarified items, new questions, risks, and design decisions.

4.  **Finalize Spec**:
    -   Update the specification file with all clarifications.
    -   Explicitly document assumptions and constraints.

## Question Patterns

-   "What happens when [X] fails?"
-   "What's the empty state for [feature]?"
-   "Why [approach A] over [approach B]?"
-   "What user behaviors are implicitly expected?"

## Anti-Patterns to Avoid

-   Surface-level "Is this correct?" questions.
-   Accepting implicit assumptions without challenge.
-   Ignoring UX or Operational dimensions.
