---
description: GraphQL queries, mutations, and code generation patterns. Use when creating GraphQL operations, working with Apollo Client, or generating types.
---

# GraphQL Schema Patterns

This workflow guides you through creating and using GraphQL operations using best practices for this project.

## When to Use

Use this workflow when:
- Creating or modifying GraphQL queries/mutations
- Working with Apollo Client
- Generating types

## Instructions

1.  **Define Operations**:
    -   Create `.gql` files (NEVER inline strings).
    -   Place queries near components, shared mutations in `graphql/mutations`.

2.  **Generate Types**:
    -   Run `npm run gql:typegen` after modifying `.gql` files.

3.  **Use Generated Hooks**:
    -   Import hooks from `.generated.ts` files (e.g., `useGetItemsQuery`).
    -   **NEVER** write raw `useQuery` or `useMutation` hooks manually.

4.  **Handle Mutations Correctly**:
    -   Use `onCompleted` for success actions.
    -   **ALWAYS** provide an `onError` handler.
    -   Show loading state and disable triggers during execution.

5.  **Query Best Practices**:
    -   Handle loading, error, and empty states.
    -   Use Fragments for reusable fields.

## Anti-Patterns to Avoid

-   Inline `gql` template literals.
-   Ignoring mutation errors.
-   Not disabling buttons during mutations.
