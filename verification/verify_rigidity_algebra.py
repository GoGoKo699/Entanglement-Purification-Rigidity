#!/usr/bin/env python3
"""Reproduce two algebra checks used in the rigidity proof.

The first uses genuinely complex reciprocal filters to check both left and
right Bell-vector identities and the exact accepted-fidelity formula.
The second constructs an annihilating product branch whose accepted output
is entangled. It checks the strict-leakage operator bound without assuming
separable spectators or a separable branch output.

These finite calculations corroborate matrix identities. They are not a
numerical proof of the universal theorem.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def bell_operators(d: int):
    phi = np.eye(d).reshape(-1) / np.sqrt(d)
    target = np.outer(phi, phi)
    noise = (np.eye(d * d) - target) / (d * d - 1)
    return phi, target, noise


def random_unitary(d: int, rng: np.random.Generator):
    z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, _ = np.linalg.qr(z)
    return q


def pair_order_to_laboratory_order(matrix: np.ndarray, d: int):
    # (A1 B1 A2 B2; A1' B1' A2' B2') -> (A1 A2 B1 B2; A1' A2' B1' B2').
    return matrix.reshape((d,) * 8).transpose(0, 2, 1, 3, 4, 6, 5, 7).reshape(d**4, d**4)


def partial_transpose_b(matrix: np.ndarray, d: int):
    return matrix.reshape(d, d, d, d).transpose(0, 3, 2, 1).reshape(d * d, d * d)


def run_checks():
    rng = np.random.default_rng(394381)
    rows = []
    for d in (2, 3, 4):
        phi, target, noise = bell_operators(d)
        maximum_vector_residual = 0.0
        maximum_formula_residual = 0.0
        maximum_fidelity_gain = -np.inf

        for _ in range(12):
            left = random_unitary(d, rng)
            right = random_unitary(d, rng)
            singular_values = np.exp(rng.uniform(-1.0, 1.0, d))
            m = left @ np.diag(singular_values) @ right.conj().T
            lam = 0.7 + 0.4j
            n = lam * np.linalg.inv(m).T
            operation = np.kron(m, n)

            maximum_vector_residual = max(
                maximum_vector_residual,
                np.linalg.norm(operation @ phi - lam * phi),
                np.linalg.norm(operation.conj().T @ phi - lam.conjugate() * phi),
            )
            chi = (
                np.trace(m.conj().T @ m).real
                * np.trace(n.conj().T @ n).real
                / abs(lam) ** 2
            )
            assert chi >= d * d - 1e-11
            for fidelity in (0.6, 0.9, 0.999):
                state = fidelity * target + (1.0 - fidelity) * noise
                output = operation @ state @ operation.conj().T
                observed = (phi.conj() @ output @ phi).real / np.trace(output).real
                predicted = fidelity / (
                    fidelity + (1.0 - fidelity) * (chi - 1.0) / (d * d - 1.0)
                )
                maximum_formula_residual = max(maximum_formula_residual, abs(observed - predicted))
                maximum_fidelity_gain = max(maximum_fidelity_gain, observed - fidelity)

        # Measure pair 1 locally with unequal outcomes, and output pair 2.
        # This kills the perfect first pair but retains entangled spectators
        # when a noisy first pair makes the branch possible.
        a = np.kron(np.eye(d)[0:1, :], np.eye(d))
        b = np.kron(np.eye(d)[1:2, :], np.eye(d))
        annihilator = np.kron(a, b)
        perfect_support = pair_order_to_laboratory_order(np.kron(target, np.eye(d * d)), d)
        annihilation_residual = np.linalg.norm(annihilator @ perfect_support)

        spectator_fidelity = 0.93
        spectator = spectator_fidelity * target + (1.0 - spectator_fidelity) * noise
        mu = np.linalg.eigvalsh(spectator).min()
        sigma = annihilator @ pair_order_to_laboratory_order(np.kron(noise, spectator), d) @ annihilator.conj().T
        product_output = annihilator @ annihilator.conj().T
        lower_operator = mu * product_output / (d * d - 1)
        minimum_operator_gap = np.linalg.eigvalsh(sigma - lower_operator).min()
        leakage = np.trace((np.eye(d * d) - target) @ sigma).real
        certified_leakage = mu * (1.0 - 1.0 / d) * np.trace(product_output).real / (d * d - 1)
        normalized_sigma = sigma / np.trace(sigma)
        partial_transpose_minimum = np.linalg.eigvalsh(partial_transpose_b(normalized_sigma, d)).min()

        assert maximum_vector_residual < 1e-11
        assert maximum_formula_residual < 1e-11
        assert maximum_fidelity_gain <= 1e-11
        assert annihilation_residual < 1e-11
        assert minimum_operator_gap > -1e-11
        assert leakage >= certified_leakage - 1e-11
        assert certified_leakage > 0
        assert partial_transpose_minimum < -1e-3
        rows.append({
            "dimension": d,
            "complex_filter_trials": 12,
            "maximum_bell_vector_residual": float(maximum_vector_residual),
            "maximum_fidelity_formula_residual": float(maximum_formula_residual),
            "maximum_filter_fidelity_gain": float(maximum_fidelity_gain),
            "annihilating_branch_support_residual": float(annihilation_residual),
            "annihilating_branch_operator_gap_minimum": float(minimum_operator_gap),
            "annihilating_branch_bell_leakage": float(leakage),
            "certified_positive_leakage": float(certified_leakage),
            "normalized_branch_partial_transpose_minimum": float(partial_transpose_minimum),
        })
    return {
        "status": "passed",
        "scope": "Finite checks of complex reciprocal-filter identities and strict annihilator leakage",
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON result file")
    args = parser.parse_args()
    result = run_checks()
    text = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
