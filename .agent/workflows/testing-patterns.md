---
description: Jest testing patterns, factory functions, mocking strategies, and TDD workflow.
---

# Testing Patterns

This workflow provides standards for writing tests, using factories, and following TDD.

## When to Use

Use this workflow when:
- Writing unit or integration tests
- Creating test factories
- Following TDD (Red-Green-Refactor)

## Instructions

1.  **Philosophy**:
    -   **TDD**: Write failing test -> Implement -> Refactor.
    -   **Behavior**: Test behavior (public API), not implementation details.

2.  **Structure**:
    -   Use `describe` blocks to organize by component/feature.
    -   Use `beforeEach` to clear mocks.
    -   Use descriptive `it` names.

3.  **Factories**:
    -   **Always** use factory functions for data/props (e.g., `getMockUser()`).
    -   Allow overrides in factories (`...overrides`).
    -   Keep tests DRY.

4.  **Mocking**:
    -   Mock modules and hooks properly.
    -   Use `jest.mock()` and `jest.requireMock()`.

5.  **User Interactions**:
    -   Use `fireEvent` and `screen` from testing library.
    -   Await async operations with `waitFor`.

## Anti-Patterns to Avoid

-   Testing mock behavior instead of real behavior.
-   Duplicating test data objects (not using factories).
-   writing production code before writing a test.
