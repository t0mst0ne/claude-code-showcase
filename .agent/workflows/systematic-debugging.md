---
description: Four-phase debugging methodology with root cause analysis. Use when investigating bugs or troubleshooting unexpected behavior.
---

# Systematic Debugging

This workflow enforces a rigorous, scientific approach to debugging to ensure root causes are fixed, not just symptoms.

## When to Use

Use this workflow when:
- Investigating bugs
- Fixing test failures
- Troubleshooting unexpected behavior

## Instructions

**Core Principle**: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.

1.  **Phase 1: Root Cause Investigation**:
    -   Read error messages thoroughly.
    -   Reproduce the issue consistently.
    -   Trace data flow backward from the symptom.
    -   **Don't touch code** until you know *why* it fails.

2.  **Phase 2: Pattern Analysis**:
    -   Compare with working examples.
    -   Identify what changed or what is different.

3.  **Phase 3: Hypothesis and Testing**:
    -   Formulate a clear hypothesis ("The error occurs because X").
    -   Design a minimal test to prove/disprove it.

4.  **Phase 4: Implementation**:
    -   Create a **failing test case** first.
    -   Implement the fix.
    -   Verify the test passes.

## Red Flags to Stop

-   "Quick fix for now, investigate later"
-   "Let me just try..." (random changes)
-   "It works on my machine"
-   Three consecutive failed fix attempts (Stop and re-evaluate/discuss).
