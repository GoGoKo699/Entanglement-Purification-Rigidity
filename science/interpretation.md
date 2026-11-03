# What exact universality forces

Several good entangled pairs can have different fidelities because they were generated or stored under different conditions. If their numerical qualities are unavailable, one natural demand is that a successful purification step should never do worse than the best pair it consumes. This is an exact guarantee over a family of possible sources. The [ordered theorem](ordered_purification.md) explains why that demand is especially restrictive, even when all pairs are close to perfect.

## A perfect possible input constrains every accepted branch

Hold the spectator pairs at any fixed interior fidelities and let the promised best pair approach the perfect target. A universally nondegrading protocol must then have zero accepted population orthogonal to that target. This conclusion is expressed with unnormalized output operators, so it remains valid when success disappears in the limit.

Errors from different accepted records cannot cancel: each record contributes a positive output operator. Full-rank spectators therefore force each product Kraus operator to send the entire perfect-pair support into the target ray, or annihilate that support. The [extraction lemma](product_branch_rigidity.md#product-kraus-extraction) turns this support constraint into a precise operational form. A surviving branch must extract the distinguished pair through reciprocal local filters and apply local bras to the spectators.

This is the step at which the spatial restriction matters. Alice's and Bob's maps factor. Their spectator slices are square matrices whose product must be a scalar identity for every pair of local spectator basis vectors. One invertible slice pair forces every other slice to be proportional to it. A general joint operation has no corresponding product-slice restriction.

## Two possible sources of error, both with the same sign

A reciprocal filter preserves the perfect Bell state, but it can amplify the isotropic error component. The singular-value inequality in [Lemma 3](product_branch_rigidity.md#reciprocal-local-filters) shows that it never suppresses that component relative to the target. Equality requires a unitary up to scale.

A branch that annihilates the perfect-pair support is more subtle. It may transfer entanglement from the spectators, so its output need not be separable. Nevertheless, full-rank spectator support gives it strictly positive Bell-error leakage. [Lemma 4](product_branch_rigidity.md#strict-leakage-from-an-annihilating-branch) establishes that fact without assuming separable spectators or a separable output.

The [ordered proof](ordered_purification.md#proof-of-theorem-1) collects these effects in four nonnegative coefficients. Extraction branches contribute target weight $`g`$ and error weight $`h\ge g`$; annihilating branches contribute target weight $`c`$ and total weight $`z\ge c`$, with strict inequality if any such branch is present. For the distinguished-pair fidelity $`F`$,

```math
N(F)-Fp(F)
=(1-F)\bigl[c+F(g-h-z)\bigr].
```

As $`F`$ approaches one, the bracket approaches $`(g-h)+(c-z)`$. Both terms have the same nonpositive sign. Requiring nondegradation arbitrarily close to one leaves no compensation mechanism: the annihilating branches disappear and every reciprocal filter must attain equality. The remaining conjugate local unitaries fix the Bell target exactly.

## What order information changes

Knowing which pair is best makes a safe operation possible: retain it. The theorem classifies the additional freedom in every universally safe separable map. Spectator measurements may decide whether to accept and which conjugate local unitary to apply. For an independent retained pair, those choices only weight fidelity-preserving transformations. For an isotropic retained state, they preserve the entire normalized state.

Without order information, the same fixed map must satisfy the guarantee in each possible ordering region. Its behavior in the region where pair 1 is best already forces it to retain pair 1's fidelity everywhere on independent isotropic inputs. A tuple with a better pair 2 defeats it. Enlarging a finite batch or allowing non-Clifford local processing does not remove that obstruction.

The ordering promise can select a separate map for each supplied ordering. The structural statement then applies after relabeling the best pair in each case. Supplying exact numerical fidelities and choosing a different operation for each tuple changes the information model and is outside this theorem.

## Practical guarantees remain useful

An ordinary recurrence protocol can improve identical inputs and can work well for heterogeneous pairs in a suitable parameter region. It fails the stronger guarantee because a nearly perfect input can be degraded when combined with a less faithful one. The [worked recurrence examples](scope_and_examples.md) calculate both behaviors for the same operation.

Noise support also matters. A rank-two bit-flip family admits exact best-input improvement by a parity check; that family lacks the full support used by the rigidity proof. Classical correlations between inputs can likewise make spectator postselection increase the retained pair's conditional fidelity. These are changes to the hypotheses, with explicit examples in the scope account.

The result rules out an exact best-input guarantee; it does not supply an optimal approximation error or a quantitative tradeoff between fidelity and success probability. Such an optimization would require a separate specification of the allowed error, source region and success criterion. Additional shared entanglement, variable output dimension and unbounded input consumption likewise require their own models.

## Relation to previous work

The [primary-source comparison](../references/RELATED_WORK.md) separates the inherited universality task and previous Clifford restrictions from the arbitrary-SEP structural result. It also distinguishes guarantees against average or randomized baselines and purification with an unknown target. Those benchmarks describe different operational tasks.

The consequential conclusion here is precise: restricting every source to a high-fidelity isotropic interval does not restore exact universal best-input purification by any fixed finite unassisted separable success map. With a best-input label supplied, the entire allowed success map is rigid. The proof and its explicit exceptions explain which assumptions support that conclusion.
