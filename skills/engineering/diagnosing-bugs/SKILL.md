---
name: diagnosing-bugs
description: Diagnose hard bugs and performance regressions by first building a tight red-capable feedback loop, then minimizing, hypothesizing, instrumenting, fixing, and regression-testing.
---

# Diagnosing Bugs

## Core discipline

Do not start with a theory. First build a feedback loop that can reliably detect the user's exact symptom.

Redact secrets from commands, logs, traces, and captured artifacts.

## 1. Build a tight feedback loop

Prefer, roughly in order: failing test, HTTP/CLI repro, headless browser, captured-trace replay, throwaway harness, fuzz/property loop, automated bisection, differential old/new comparison, structured human-in-the-loop repro.

A usable loop is:

- **red-capable** for this exact bug;
- deterministic or high-reproduction-rate;
- fast enough to iterate;
- agent-runnable where possible.

If no such loop can be built, state what evidence/access is missing instead of inventing a hypothesis.

## 2. Reproduce and minimize

Verify the loop matches the user's symptom, then remove inputs/config/steps one at a time until every remaining element is load-bearing.

## 3. Hypothesize

Generate 3–5 ranked, falsifiable hypotheses. Each must predict what observation or controlled change would support/refute it.

## 4. Instrument

Use debugger/inspection first, then targeted logs or measurements at boundaries that distinguish hypotheses. Change one variable at a time. For performance, establish measurements/profiles before changing code.

## 5. Fix and lock down

At a correct seam, turn the minimized repro into a failing regression test before the fix. Apply the smallest supported fix, watch the test pass, then rerun the original feedback loop.

## 6. Cleanup

Remove temporary instrumentation/prototypes, run appropriate checks, and record the actual root cause in the commit/PR context.
