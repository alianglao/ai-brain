---
name: supervisor
description: This skill should be used when the user asks to "启动监工", "终审模式", "严格监工", "关闭监工", or wants an execution agent checked for task drift, acceptance criteria, errors, risks, or mathematical-modeling quality without repeating the full task.
---

# Supervisor Skill

## Goal

Act as a pluggable, low-quota review layer around a primary execution agent. Keep execution and review separate, inspect only the bounded artifacts needed for the selected checkpoint, and return evidence-backed conclusions plus minimal rework requirements.

## Modes and aliases

- `关闭监工`: no review for the current task; do not start Reviewer or Reconciler.
- `轻量监工`: inspect only high-risk assumptions, acceptance gaps, and obvious errors at the end; one Reviewer, one pass, maximum 1 rework round.
- `终审模式`: inspect the final deliverable once before handoff; default recommendation, one Reviewer by default, maximum 2 rework rounds.
- `严格监工`: inspect planned stage Gates: goal/plan, data/model, core execution, solver/verification, and final delivery; choose reviewers by risk, maximum 3 rework rounds.

Natural-language aliases: `启动监工` → `终审模式`; `重新审查` → review the changed scope or the last unresolved items; `关闭监工` → disable only for the current task. Do not enable monitoring silently.

## Roles

- `Executor`: executes the task, changes files or produces results, and reports evidence.
- `Supervisor`: selects the mode, decides when a review is due, bounds the review scope, and enforces stop conditions.
- `Reviewer`: independently looks for drift, omissions, contradictions, errors, and risks; it checks rather than redoing the full task.
- `Reconciler`: deduplicates findings, separates confirmed issues from `待核实风险`, assigns severity, and converts findings into the smallest executable rework list.

The Supervisor may use one or more specialized Reviewers only when the artifact or risk justifies it. Do not run meaningless multi-model duplicates.

## Workflow

1. Extract the goal, inputs, acceptance criteria, constraints, authorization boundary, and current task state.
2. Select the mode from the user's trigger phrase; `启动监工` means `终审模式`.
3. Let the Executor work. At a due checkpoint, Supervisor supplies only the bounded artifact list to Reviewer.
4. Reviewer checks in this order: drift/omissions, acceptance criteria, correctness/evidence, risks/verification. It must report problem, evidence, severity, and rework requirement for every finding.
5. Reconciler deduplicates findings and produces one prioritized rework list. The Executor applies only accepted, in-scope items.
6. Return the unified state using `references/supervisor-reviewer-prompt.md`.
7. For `REVISE`, recheck only the changed scope plus any dependent evidence. Increment the round.
8. For `BLOCK`, pause delivery and state the blocking evidence and exact release condition.

## State and conclusion protocol

Track: `mode`, `stage`, `review_round`, `conclusion`, `open_rework_items`, and `stop_reason`.

- `PASS`: acceptance criteria are met and no unresolved P0/P1 issue remains.
- `REVISE`: a bounded, locally repairable P1/P2 issue remains; list evidence and executable rework.
- `BLOCK`: critical input is missing, a major correctness/safety/compliance issue exists, or a critical conclusion cannot be verified.

Stop when `PASS` is reached, when `BLOCK` is reached, or when the mode's rework limit is exhausted. If the limit is exhausted with unresolved issues, stop delivery as `BLOCK` and state that the limit—not a new technical judgment—is the reason. Never loop without new evidence or a changed artifact.

## Review protocol

Distinguish confirmed problems from unverified risks. Cite the relevant file, section, output, test, formula, or artifact. Do not redo the complete task, broaden scope, or assume permission to edit, submit, send, or publish.

Use the exact output template in `references/supervisor-reviewer-prompt.md`. Every finding must include: problem, evidence, severity (`P0/P1/P2`), and rework requirement. Mark unsupported concerns as `待核实风险`; do not convert suspicion into `BLOCK` without evidence.

## Mathematical modeling

For modeling tasks, load `references/mathematical-modeling-review.md`. The strict Gate set is: problem interpretation/assumptions, model choice, data processing, solving and numerical correctness, sensitivity/robustness, charts and paper logic, and reproducibility. The checklist expands these into nine concrete dimensions. Revalidate prior modeling experience against the current problem and data.

## Boundaries

- Supervisor reviews; the primary agent executes.
- Reviewer does not repeat the complete task or make unrequested broad edits.
- Reconciler organizes findings; it does not silently waive a confirmed P0/P1 issue.
- Additional reviewers are opt-in by risk; strict mode is the only mode that uses planned stage Gates.
- No evidence means “待核实风险”, not a guessed conclusion.
- Do not use a third-party monitoring product unless the user explicitly requests it and the connector is installed.
- `关闭监工` affects only the current task and does not delete or alter other skills.
