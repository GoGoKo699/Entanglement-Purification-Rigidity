# Entanglement Purification Rigidity

**A fixed finite-input purification protocol cannot always match the unknown best input pair, even when every input is arbitrarily close to a known maximally entangled state.** This project proves the obstruction for all unassisted separable success operations, and therefore for local operations and classical communication (LOCC).

The central result is a structural theorem. If the best input is identified and one fixed operation must never degrade it throughout an open high-fidelity isotropic family, every accepted product Kraus operator reduces to a conjugate pair of local unitaries on that input and local bras on the remaining pairs. The accepted Bell fidelity is exactly the retained input's fidelity.

| Available source information | Consequence of an exact guarantee for every allowed tuple |
|---|---|
| A best-input label, or the complete fidelity ordering | Every universally nondegrading SEP success map has the fidelity-preserving extraction form. |
| Unknown ordering | No nonzero SEP success map can always achieve the best input fidelity. |

Both statements hold for every fixed finite number of inputs $`n\ge2`$, every local dimension $`d\ge2`$, and every fidelity floor $`1/d\le f_\star\lt 1`$. The inputs are independent isotropic pairs,

```math
\omega(F_i)=F_iP+(1-F_i)\frac{I-P}{d^2-1},
\qquad f_\star\lt F_i\lt 1,
```

with a known target $`P=|\Phi_d\rangle\langle\Phi_d|`$. Success can become arbitrarily rare near perfect inputs; the theorem assumes no success floor at that boundary.

## Read the science

Start with the [model, information assumptions and connected reading route](science/model.md). The [product-branch lemmas](science/product_branch_rigidity.md) establish the mechanism, and the [ordered theorem and unknown-order corollary](science/ordered_purification.md) state and prove the complete result.

| To inspect | Read |
|---|---|
| Exact operation class, input family and success convention | [Model](science/model.md) |
| Factorization, reciprocal filters and strictly positive annihilator leakage | [Product-branch rigidity](science/product_branch_rigidity.md) |
| Structural classification and the universal-purification obstruction | [Ordered purification](science/ordered_purification.md) |
| Postselection, recurrence, restricted noise and correlated inputs | [Scope and worked examples](science/scope_and_examples.md) |
| Why the proof has an operational consequence | [Interpretation](science/interpretation.md) |
| Closest theorems, inherited ingredients and versioned sources | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Reproducible finite calculations and their limits | [Verification](verification/README.md) |

The universality task and earlier no-go results are due to [Zang et al. (2025)](https://doi.org/10.1103/PhysRevLett.134.190803). The [comparison](references/RELATED_WORK.md#relation-to-the-2025-universal-purification-no-go) identifies the arbitrary-SEP high-fidelity strengthening and keeps the earlier catalytic Clifford results separate.

## Learn the argument

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [Watrous bridge](learning/WATROUS_BRIDGE.md) connects its notation, fidelity convention, quantum operations and separability results to this project's proof. The [30-milestone map](learning/MILESTONES.md) develops 12 background milestones followed by 18 milestones tracing the argument and its physical boundaries. Each milestone links back to the canonical scientific account.

## Reproduce the checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_rigidity_algebra.py
python3 verification/verify_examples.py
```

The first script tests complex reciprocal filters and a boundary-annihilating branch with entangled output. The second constructs the local operations in the worked examples as dense matrices and checks their success probabilities and accepted fidelities. The [verification guide](verification/README.md) records the dimensions, tested inputs, tolerances and expected results. The general theorem is established by the written proof, rather than by these finite calculations.

## Scope

The guarantee is exact, conditional on success, and required throughout an independently variable input family. The protocol is fixed across that family and receives no extra shared entangled resource. Ordinary identical-input distillation, average-baseline improvements, rank-deficient noise families and protocols selected from exact source parameters are different tasks. No approximation-gap scaling or arbitrary entangled-catalyst extension is asserted.

The [LLM reading guide](llms.txt) maps scientific questions to the authoritative pages and preserves these distinctions.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
