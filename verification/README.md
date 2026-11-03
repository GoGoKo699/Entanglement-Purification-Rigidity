# Verification and its scope

The universal statements are established by the [written proof](../science/ordered_purification.md) and its [branch lemmas](../science/product_branch_rigidity.md). The calculations here check two concrete risks: complex transpose/conjugation conventions in the proof, and the success accounting of physical examples. They are finite numerical checks, not an exhaustive search over separable maps or a proof certificate.

## Run

Use Python 3.10 or later and the pinned NumPy dependency. The recorded executions used Python 3.12.14 and NumPy 2.3.5.

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_rigidity_algebra.py
python3 verification/verify_examples.py
```

Both commands print JSON and exit successfully only after their checks pass. An optional `--output verification/latest-algebra.json` or `--output verification/latest-examples.json` saves a fresh report. Floating-point residuals may vary between numerical-library builds; compare the stated tolerances and scientific quantities rather than requiring identical decimal text.

## Complex filters and annihilating branches

`verify_rigidity_algebra.py` uses a fixed random seed and 12 genuinely complex reciprocal filters in each dimension 2, 3 and 4. It checks both left and right Bell-vector identities and compares direct matrix multiplication with the derived fidelity formula at input fidelities 0.6, 0.9 and 0.999. The sampled filters are unnormalized algebraic representatives; local scaling makes them physical contractions without changing their conditional fidelity.

The script also constructs a branch that annihilates the perfect first-pair support and retains an entangled spectator. It checks the positive-operator lower bound and strict Bell-error leakage in Lemma 4. A negative partial-transpose eigenvalue confirms that this example's output is entangled, guarding against the false shortcut that all annihilating outputs are separable.

The [recorded reference report](expected/rigidity_algebra_checks.json) has Bell-vector and fidelity residuals below $`10^{-14}`$; the enforced tolerance is $`10^{-11}`$. The lower-bound comparison permits roundoff of that size. These checks do not establish the theorem for arbitrary dimension or every product Kraus operator; the analytical arguments do.

## Dense local-operation examples

`verify_examples.py` builds local filters, measurement bras and controlled-NOT gates, then applies the resulting Kraus matrices to density operators. It checks the six exact rational rows in [Scope and worked examples](../science/scope_and_examples.md#exact-values-for-implementation-checks):

- A nonunitary reciprocal filter degrades an isotropic input.
- Spectator postselection preserves the independent retained pair while having zero all-perfect success.
- The same recurrence circuit improves identical isotropic inputs and degrades the better input in the specified unequal example.
- A rank-two bit-flip family escapes the full-rank-isotropic obstruction.
- Correlated inputs with full-rank isotropic marginals can increase conditional fidelity after spectator postselection.

Every constructed accepted operation is checked to be trace nonincreasing. The correlated example is also checked to be full rank, have the stated marginal, and differ from the product of its marginals. The [reference report](expected/example_checks.json) records success probability, target numerator and normalized fidelity. The numerical acceptance tolerance is $`10^{-12}`$.

## Analytical review boundaries

The proof's decisive steps are full-rank boundary support, product-slice factorization, the reciprocal-filter equality condition, and strictly positive annihilator leakage. None is inferred from the numerical reports. The [related-work account](../references/RELATED_WORK.md) records which prior results and source versions were compared. Internal algebraic review and these reproducible calculations do not constitute independent peer review.
