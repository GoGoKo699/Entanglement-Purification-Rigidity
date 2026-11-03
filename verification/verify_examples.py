#!/usr/bin/env python3
"""Construct local operations and verify the six exact worked-example rows.

Expected values are rational expressions from science/scope_and_examples.md.
The calculation applies dense Kraus matrices directly to density matrices;
it does not evaluate the displayed fidelity formulas as its implementation.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

import numpy as np

from verify_rigidity_algebra import bell_operators, pair_order_to_laboratory_order


def run_checks():
    phi, target, noise = bell_operators(2)
    ident = np.eye(2)
    bras = ident[0:1], ident[1:2]
    psi = np.array([0, 1, 1, 0]) / np.sqrt(2)
    flipped = np.outer(psi, psi)

    def isotropic(f):
        return float(f) * target + (1 - float(f)) * noise

    def bit_flip(f):
        return float(f) * target + (1 - float(f)) * flipped

    def joint(first, second):
        return pair_order_to_laboratory_order(np.kron(first, second), 2)

    def keep_pair_one(a, b):
        return np.kron(np.kron(ident, bras[a]), np.kron(ident, bras[b]))

    cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                     [0, 0, 0, 1], [0, 0, 1, 0]], dtype=float)
    recurrence = []
    for outcome in (0, 1):
        local = np.kron(ident, bras[outcome]) @ cnot
        recurrence.append(np.kron(local, local))

    r = 2
    reciprocal = np.kron(np.diag([1, 1/r]), np.diag([1/r, 1]))
    correlated = (joint(isotropic(Fraction(9, 10)), isotropic(Fraction(9, 10)))
                  + joint(isotropic(Fraction(3, 5)), isotropic(Fraction(3, 5)))) / 2
    cases = [
        ("reciprocal_filter", isotropic(Fraction(9, 10)), [reciprocal],
         (Fraction(43, 160), Fraction(9, 40), Fraction(36, 43))),
        ("spectator_01", joint(isotropic(Fraction(9, 10)), isotropic(Fraction(3, 5))),
         [keep_pair_one(0, 1)], (Fraction(2, 15), Fraction(3, 25), Fraction(9, 10))),
        ("isotropic_recurrence_identical", joint(isotropic(Fraction(9, 10)), isotropic(Fraction(9, 10))),
         recurrence, (Fraction(197, 225), Fraction(73, 90), Fraction(365, 394))),
        ("isotropic_recurrence_unequal", joint(isotropic(Fraction(99, 100)), isotropic(Fraction(9, 10))),
         recurrence, (Fraction(2087, 2250), Fraction(401, 450), Fraction(2005, 2087))),
        ("bit_flip_recurrence", joint(bit_flip(Fraction(9, 10)), bit_flip(Fraction(3, 5))),
         recurrence, (Fraction(29, 50), Fraction(27, 50), Fraction(27, 29))),
        ("correlated_spectator_00", correlated, [keep_pair_one(0, 0)],
         (Fraction(5, 12), Fraction(8, 25), Fraction(96, 125))),
    ]
    rows = []
    for name, state, kraus, expected in cases:
        effect = sum(k.conj().T @ k for k in kraus)
        tni_gap = np.linalg.eigvalsh(np.eye(state.shape[0]) - effect).min()
        if tni_gap < -1e-12:
            raise AssertionError(f"{name}: success map is not trace nonincreasing")
        output = sum(k @ state @ k.conj().T for k in kraus)
        p = np.trace(output).real
        numerator = (phi.conj() @ output @ phi).real
        observed = np.array([p, numerator, numerator / p])
        prediction = np.array([float(x) for x in expected])
        np.testing.assert_allclose(observed, prediction, atol=1e-12, rtol=0, err_msg=name)
        rows.append({"case": name, "success_probability": float(p),
                     "bell_numerator": float(numerator), "accepted_fidelity": float(numerator / p),
                     "exact_reference": [str(x) for x in expected],
                     "maximum_absolute_error": float(np.max(np.abs(observed - prediction)))})

    # A legal ordered protocol can have zero success on the all-perfect tuple.
    boundary = joint(target, target)
    branch = keep_pair_one(0, 1)
    boundary_success = np.trace(branch @ boundary @ branch.conj().T).real
    np.testing.assert_allclose(boundary_success, 0.0, atol=1e-12, rtol=0)

    # Reorder to pair axes, then trace pair 2: the correlated input has the
    # promised isotropic marginal, but it is not the product of its marginals.
    paired = correlated.reshape((2,)*8).transpose(0, 2, 1, 3, 4, 6, 5, 7).reshape(4, 4, 4, 4)
    marginal = np.einsum("abcb->ac", paired)
    np.testing.assert_allclose(marginal, isotropic(Fraction(3, 4)), atol=1e-12, rtol=0)
    correlated_minimum_eigenvalue = np.linalg.eigvalsh(correlated).min()
    if correlated_minimum_eigenvalue <= 0:
        raise AssertionError("The correlated example must be full rank")
    nonproduct_distance = np.linalg.norm(correlated - joint(marginal, marginal))
    if nonproduct_distance < 1e-3:
        raise AssertionError("The correlated example must not be a product")

    return {"status": "passed", "scope": "Dense-matrix checks of local operations in six worked-example rows",
            "rows": rows, "all_perfect_spectator_01_success": float(boundary_success),
            "correlated_input_minimum_eigenvalue": float(correlated_minimum_eigenvalue),
            "correlated_input_nonproduct_frobenius_distance": float(nonproduct_distance)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON result file")
    args = parser.parse_args()
    result = json.dumps(run_checks(), indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result + "\n")
    print(result)


if __name__ == "__main__":
    main()
