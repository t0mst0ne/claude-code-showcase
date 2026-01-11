---
name: spec-deep-interview
description: Deep interview methodology for refining specifications. Use when reviewing SPEC files, PRDs, or feature requirements. Conducts thorough interviews covering technical implementation, UI/UX, edge cases, and design trade-offs using ultrathink mode.
---

# Spec Deep Interview

## Core Principle

**NEVER SKIM SPECIFICATIONS. INTERROGATE EVERY ASSUMPTION.**

Specifications often hide implicit assumptions, unexplored edge cases, and accumulated technical debt. Surface these through systematic deep questioning before implementation begins.

## When to Use

- Reviewing a new SPEC or PRD document
- Refining feature requirements before implementation
- Identifying gaps in product specifications
- Validating technical feasibility of proposed designs

## The Interview Framework

### Phase 1: Ultrathink Analysis

Before asking ANY question, perform deep analysis on the specification:

```
1. Hidden Assumptions
   - What does this spec assume about the system state?
   - What user behaviors are implicitly expected?
   - What infrastructure dependencies are not mentioned?
   - What data formats/structures are assumed to exist?

2. Unexplored Edge Cases
   - What happens at scale (0, 1, many, max)?
   - What about concurrent operations?
   - What if external services fail?
   - What about partial success scenarios?
   - What about malformed or malicious input?

3. Technical Debt Accumulation Points
   - Where will shortcuts be tempting?
   - What parts will be "temporary" but become permanent?
   - Where does this design constrain future changes?
   - What monitoring/observability gaps will emerge?

4. Second/Third Order Effects
   - How does this change affect adjacent systems?
   - What user behaviors might this inadvertently encourage?
   - What operational burden does this create?
   - How does this impact system performance holistically?
```

### Phase 2: Systematic Questioning

Cover ALL dimensions through AskUserQuestion tool:

#### Technical Implementation
- Architecture decisions and trade-offs
- Data model implications
- API contract definitions
- Performance requirements and constraints
- Security considerations
- Integration points with existing systems

#### UI/UX
- User flow completeness
- Error state handling
- Loading state design
- Empty state scenarios
- Accessibility requirements
- Responsive design needs
- Internationalization considerations

#### Operational Concerns
- Deployment strategy
- Rollback procedures
- Monitoring and alerting
- Data migration needs
- Feature flag requirements
- A/B testing considerations

#### Business Logic
- Edge case handling
- Validation rules
- Business rule exceptions
- Compliance requirements
- Audit trail needs

### Phase 3: Gap Documentation

After each interview round, document:

1. **Clarified Items** - Questions answered
2. **New Questions** - Questions that emerged from answers
3. **Identified Risks** - Potential issues discovered
4. **Design Decisions** - Choices made and rationale
5. **Open Items** - Questions still pending

### Phase 4: Specification Finalization

Once all critical aspects are clarified:

1. Consolidate all findings
2. Update specification with clarifications
3. Document all assumptions explicitly
4. List known limitations
5. Write complete refined spec to file

## Interview Question Patterns

### For Technical Depth
```
- "What happens when [X] fails?"
- "How does this behave with [boundary condition]?"
- "What's the expected latency/throughput for [operation]?"
- "How does this interact with [existing system]?"
```

### For UI/UX Depth
```
- "What does the user see while [async operation] is in progress?"
- "How do we handle [error scenario] in the UI?"
- "What's the empty state for [feature]?"
- "How does this work on [device/screen size]?"
```

### For Design Trade-offs
```
- "Why [approach A] over [approach B]?"
- "What are we trading off by choosing [decision]?"
- "What would we need to change if [requirement] changes?"
- "What's the migration path if this design doesn't scale?"
```

## Anti-Patterns

- **Surface-level questions** - "Is this correct?" vs "What happens when X?"
- **Assumption acceptance** - Taking implicit requirements as given
- **Single-dimension focus** - Only asking about tech, ignoring UX
- **Premature closure** - Ending interview before all gaps are identified
- **Leading questions** - Suggesting answers in questions

## Output Format

After completing the interview, write the refined specification to a file with:

```markdown
# [Feature Name] - Refined Specification

## Overview
[Clarified summary]

## Requirements
### Functional
[Detailed functional requirements]

### Non-Functional
[Performance, security, scalability requirements]

## Technical Design
[Architecture decisions with rationale]

## UI/UX Specifications
[User flows, states, error handling]

## Edge Cases & Error Handling
[Comprehensive edge case coverage]

## Assumptions & Constraints
[Explicitly documented assumptions]

## Open Questions
[Any remaining uncertainties]

## Interview Log
[Summary of key clarifications made]
```

## Success Metrics

A thorough spec interview achieves:
- Zero "I didn't think of that" moments during implementation
- All edge cases documented before coding
- Clear rationale for every design decision
- Explicit assumptions that can be validated
- Implementation estimates based on complete understanding

## Integration with Other Skills

- **testing-patterns**: Use clarified edge cases to drive test cases
- **systematic-debugging**: Apply same analytical rigor to spec analysis
- **react-ui-patterns**: Ensure all UI states are specified
