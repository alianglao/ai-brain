# Mathematical Modeling Review Checklist

Review the current problem, data, code, and paper only. Do not treat examples or prior competition experience as evidence for the current task.

## Required dimensions

- Problem interpretation: objectives, variables, constraints, outputs, and subquestions map one-to-one.
- Assumptions: explicit, necessary, explainable, and not stronger than the data supports.
- Model choice: mechanism fit; objective, constraints, parameters, and notation are consistent.
- Data processing: source, units, missing values, outliers, splits, normalization, and leakage risk are documented.
- Solver correctness: formulas, code, boundary conditions, feasibility/convergence, numerical precision, and result checks agree.
- Sensitivity/robustness: key parameters, alternative assumptions, or perturbations are tested; instability is disclosed.
- Charts: titles, units, legends, axes, precision, and visual claims match the evidence.
- Paper logic: problem, method, results, discussion, and conclusion are coherent; claims do not exceed evidence.
- Reproducibility: data, environment, entry point, seed, parameters, and key intermediate outputs are sufficient to rerun.

## Blocking conditions

- A subquestion is unanswered or answered for the wrong object.
- Variables, units, or constraints conflict across sections or code.
- Code cannot run, results cannot be reproduced from code, or obvious leakage exists.
- A conclusion depends on an unvalidated key parameter without sensitivity analysis.
- The paper claims optimality, superiority, or robustness without the corresponding comparison or evidence.

## Lightweight order

In `终审模式`, prioritize problem mapping, core formula/code, key results, conclusion boundaries, and the reproduction entry point. In `严格监工`, add plan, data/model, solver/verification, and paper-delivery checkpoints.

