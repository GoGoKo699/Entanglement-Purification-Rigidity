# Thirty milestones for entanglement purification rigidity

This route connects the objects used in quantum information to the mechanism and scope of the purification result. The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, cited as `Watrous2018`. Section numbers below refer to the author's [standard-layout manuscript](https://cs.uwaterloo.ca/~watrous/TQI/). The [Watrous bridge](WATROUS_BRIDGE.md) translates its conventions and separates textbook foundations from the project's arguments.

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. The background assembles positive operators, composite states, conditional operations and spatial restrictions into the exact operational question. The narrative develops the three branch ingredients, combines their equality conditions into the structural theorem, and connects the resulting impossibility to its physical examples and boundaries. M12 and M30 integrate their respective phases. The exact statements and proofs remain in the canonical scientific pages linked below.

## Phase I — Background and preliminaries

<a id="m01"></a>
### M01 — Positive operators and support

**Phase:** Background/preliminaries.

**Central question:** How does a state operator encode both probabilities and the directions a state can occupy?

**Understanding target:** Distinguish positivity, trace normalization, rank and support. Understand why a positive-definite state has a strictly positive smallest eigenvalue and why a positive operator with zero trace must vanish.

**Dependencies and story role:** Entry point. These facts supply the local language for full-rank spectators and nonnegative error contributions.

**Conceptual connection:** A support statement can constrain an operation even when the operation's probability of success vanishes.

**Source pointers:** Watrous [§§1.1.2–1.1.3][W1] and [§2.1.2][W2]; [model: states and operations](../science/model.md#states-and-operations).

<a id="m02"></a>
### M02 — Spectral inequalities and their equality conditions

**Phase:** Background/preliminaries.

**Central question:** What additional information is contained in the equality case of a matrix inequality?

**Understanding target:** Relate singular values to the spectrum of $`M^\dagger M`$, recognize the Hilbert–Schmidt norm as a sum of nonnegative squares, and understand how Cauchy–Schwarz can force all singular values to agree.

**Dependencies and story role:** M01. Moves from positive operators to the algebraic tools that will distinguish a bound from a rigidity statement.

**Conceptual connection:** Equal singular values identify an invertible local filter as a scalar times a unitary.

**Source pointers:** Watrous [§1.1.1, Eq. (1.10), and §1.1.3][W1]; [reciprocal local filters](../science/product_branch_rigidity.md#reciprocal-local-filters).

<a id="m03"></a>
### M03 — Pairs and laboratories are different tensor groupings

**Phase:** Background/preliminaries.

**Central question:** How can the same input be grouped into shared pairs or into Alice's and Bob's laboratories?

**Understanding target:** Track the registers $`A_i,B_i`$, tensor-product bases and local input/output dimensions. Distinguish a product across pairs from a product operator across laboratories.

**Dependencies and story role:** M01. Introduces the composite-system organization needed to state the spatial restriction without changing which systems are independent.

**Conceptual connection:** A Kraus operator is local across laboratories while its local factors may act jointly on all inputs held in one laboratory.

**Source pointers:** Watrous [§1.1.1, tensor products][W1] and [§2.1.1][W2]; [model](../science/model.md#states-and-operations) and [product-Kraus extraction](../science/product_branch_rigidity.md#product-kraus-extraction).

<a id="m04"></a>
### M04 — Product states, marginals and independence

**Phase:** Background/preliminaries.

**Central question:** What information is missing when only the quality of each pair is specified?

**Understanding target:** Distinguish a joint product state from a correlated state with the same marginals. Understand why a measurement on independent spectators multiplies the retained state by a scalar, whereas correlations can change its conditional state.

**Dependencies and story role:** M03. Adds the statistical content of the tensor-product input promise.

**Conceptual connection:** Pair independence is separate from knowing, or imposing equalities among, the numerical fidelities.

**Source pointers:** Watrous [§2.1.2, product states, and §2.1.3][W2]; [model: what is fixed and what may vary](../science/model.md#what-is-fixed-and-what-may-vary) and [correlated-input example](../science/scope_and_examples.md#example-5-correlated-inputs-with-full-rank-isotropic-marginals).

<a id="m05"></a>
### M05 — The Bell target as a vectorized identity

**Phase:** Background/preliminaries.

**Central question:** Why does a maximally entangled vector turn two local operators into a matrix product with a transpose?

**Understanding target:** Connect $`|\Phi_d\rangle`$ with $`\mathrm{vec}(I_d)/\sqrt d`$ and track the identity relating $`A\otimes B`$ to $`AB^{\mathrm{T}}`$. Keep transpose, adjoint and complex conjugation distinct in the fixed target bases.

**Dependencies and story role:** M02–M03. Provides the bridge from bipartite state constraints to local matrix identities.

**Conceptual connection:** Target preservation will become a scalar-identity condition on every pair of local spectator slices.

**Source pointers:** Watrous [§1.1.2, Eq. (1.132)][W1]; [model's target convention](../science/model.md#states-and-operations) and [product-Kraus extraction](../science/product_branch_rigidity.md#product-kraus-extraction).

<a id="m06"></a>
### M06 — Isotropic noise and full support

**Phase:** Background/preliminaries.

**Central question:** Which features of the isotropic family matter even when its fidelity is very high?

**Understanding target:** Identify the target eigenvalue $`F`$ and the orthogonal eigenvalue $`(1-F)/(d^2-1)`$ of $`\omega(F)`$. Understand full rank for interior fidelities and the rank change at $`F=1`$.

**Dependencies and story role:** M01, M04–M05. Connects the target to the particular input family used throughout the argument.

**Conceptual connection:** An arbitrarily small amount of isotropic noise still occupies every orthogonal direction.

**Source pointers:** Watrous [§6.1.1, Example 6.10, Eq. (6.45)][W6]; [model: states and operations](../science/model.md#states-and-operations).

<a id="m07"></a>
### M07 — A fixed target and a linear fidelity numerator

**Phase:** Background/preliminaries.

**Central question:** What exactly does the project's fidelity measure?

**Understanding target:** Interpret $`F(\rho)=\mathrm{Tr}(P\rho)`$ as the overlap with the known pure target. Relate it to the square of Watrous's root-fidelity convention and recognize its linearity in an unnormalized output.

**Dependencies and story role:** M01, M05–M06. Fixes the score before operations and conditioning are combined.

**Conceptual connection:** A linear target numerator lets positive errors from distinct accepted records be compared without changing the target between inputs.

**Source pointers:** Watrous [§3.2, Definition 3.11, and §3.2.1, Propositions 3.12–3.13][W3]; [model](../science/model.md#states-and-operations) and [success accounting](../science/scope_and_examples.md#success-probability-and-accepted-fidelity).

<a id="m08"></a>
### M08 — Completely positive maps and Kraus operators

**Phase:** Background/preliminaries.

**Central question:** How does one mathematical operation describe processing a state while preserving physical positivity?

**Understanding target:** Understand complete positivity, a Kraus representation, and why adjoining an untouched system matters. Connect the Kraus and Choi descriptions of a finite-dimensional map without assuming the operation always succeeds.

**Dependencies and story role:** M01–M03. Introduces the dynamical object on which the classification acts.

**Conceptual connection:** An input-dependent probability can arise from one fixed linear map; it does not require choosing a different operation for each input.

**Source pointers:** Watrous [§2.2.2, Theorem 2.22][W2]; [model: states and operations](../science/model.md#states-and-operations).

<a id="m09"></a>
### M09 — Heralding, subnormalized outputs and accepted mixtures

**Phase:** Background/preliminaries.

**Central question:** How are success probability and the quality of a successful output kept separate?

**Understanding target:** Distinguish the positive output $`\widetilde\sigma`$, its trace $`p`$, its target numerator $`N`$, and conditional fidelity $`N/p`$. Understand that coarse-grained successful records are weighted by their probabilities.

**Dependencies and story role:** M07–M08. Combines state quality with the measurement and acceptance process.

**Conceptual connection:** The conditional state is nonlinear in its input, while the unnormalized accepted operation remains linear.

**Source pointers:** Watrous [§2.3.2, nondestructive measurements and instruments, Eqs. (2.258)–(2.260)][W2]; [success accounting](../science/scope_and_examples.md#success-probability-and-accepted-fidelity).

<a id="m10"></a>
### M10 — Local operations and the separable-map relaxation

**Phase:** Background/preliminaries.

**Central question:** How does separation between the two laboratories constrain an accepted operation?

**Understanding target:** Interpret product Kraus operators $`A_r\otimes B_r`$, distinguish separable maps from separable states, and understand why an impossibility for SEP also constrains LOCC. A general SEP map need not be implementable by LOCC.

**Dependencies and story role:** M03, M08–M09. Adds the physical restriction that will make the Bell-vector constraint rigid.

**Conceptual connection:** Classical communication permits coordination while preserving product structure within a fully resolved local branch.

**Source pointers:** Watrous [§6.1.2, Propositions 6.18 and 6.26][W6]; [model's operation class](../science/model.md#states-and-operations).

<a id="m11"></a>
### M11 — A finite effective map can include elaborate protocols

**Phase:** Background/preliminaries.

**Central question:** Why is a finite product-Kraus representation compatible with ancillas, adaptive records and limits of local protocols?

**Understanding target:** Relate finite input/output dimensions to finite separable Choi decompositions, using the laboratory output-plus-reference partition. Distinguish this effective representation from a finite-round restriction; the closed separable cone also contains the relevant limits.

**Dependencies and story role:** M08–M10. Connects the mathematical operation class to the complete accepted physical process.

**Conceptual connection:** Fixed local resources can be absorbed into the map; supplied shared entanglement changes the resource model.

**Source pointers:** Watrous [§2.2.2][W2]; [§6.1.1, Corollary 6.7 and Proposition 6.8, and §6.1.2, Proposition 6.22][W6]; [model](../science/model.md#states-and-operations). Watrous's finite-LOCC definition and the project's closure argument have distinct roles here.

<a id="m12"></a>
### M12 — Background synthesis: the exact universal-purification task

**Phase:** Background/preliminaries.

**Central question:** What must one fixed finite protocol guarantee when the fidelities are unknown?

**Understanding target:** Assemble the independent isotropic inputs, known target, threshold, SEP success map and resource promise into a pointwise best-input comparison. Distinguish a supplied best-pair label from exact numerical fidelities, identical-input preparation or an average-source benchmark.

**Dependencies and story role:** M01–M11. Integrates the preliminary objects into one operational question.

**Conceptual connection:** The allowed information determines which input family a single operation must handle, and the universal quantifier will constrain its individual Kraus operators.

**Source pointers:** Watrous [§2.3.2][W2] and [§6.1.2][W6] for operations and conditioning; [model](../science/model.md) for the project's guarantee and information assumptions.

## Phase II — Narrative and innovation

<a id="m13"></a>
### M13 — Approaching one perfect pair with noisy spectators

**Phase:** Narrative/innovation.

**Central question:** What constraint follows when only the promised best input approaches perfection?

**Understanding target:** Explain why fixing interior spectator fidelities leaves an allowed path with $`F_1\uparrow1`$. Understand the limiting condition through $`N\geq F_1p`$, including a boundary at which $`p`$ vanishes.

**Dependencies and story role:** M06, M09, M12. Starts the proof with a local limit inside the ordered promise.

**Conceptual connection:** Exact performance arbitrarily close to a pure state constrains an unnormalized output without requiring a defined conditional boundary state.

**Source pointers:** Watrous [§§2.2.2 and 2.3.2][W2]; [Theorem 1 proof, Eq. (15)](../science/ordered_purification.md#proof-of-theorem-1) and [boundary-success example](../science/scope_and_examples.md#example-2-allowed-postselection-with-zero-all-perfect-success).

<a id="m14"></a>
### M14 — Positive errors cannot cancel between branches

**Phase:** Narrative/innovation.

**Central question:** How does a constraint on the sum of accepted outputs reach every product Kraus operator?

**Understanding target:** Connect zero total Bell-error leakage to zero leakage in each positive summand. Use the invertibility of the spectator state to understand why every branch maps the entire perfect-pair support into the Bell line, or kills it.

**Dependencies and story role:** M01–M02, M08, M13. Converts a condition on a mixed output into a branchwise support condition.

**Conceptual connection:** Full rank extends a statement about one mixed spectator state to every vector in its support.

**Source pointers:** Watrous [§1.1.3][W1] and [§2.2.2][W2]; [Theorem 1 proof, Eqs. (15)–(16)](../science/ordered_purification.md#proof-of-theorem-1).

<a id="m15"></a>
### M15 — Local slices turn support into scalar identities

**Phase:** Narrative/innovation.

**Central question:** What does the Bell-line image condition require of local spectator slices?

**Understanding target:** Interpret the square matrices $`A_u,B_v`$ obtained by fixing local spectator basis vectors. Understand why every pair of slices obeys $`A_uB_v^{\mathrm{T}}=\lambda_{uv}I_d`$, rather than only one all-perfect input vector being constrained.

**Dependencies and story role:** M03, M05, M10, M14. Expresses the physical locality condition as a family of local matrix equations.

**Conceptual connection:** Vectorization makes the spatial restriction visible at the level of ordinary matrix multiplication.

**Source pointers:** Watrous [§1.1.2, Eq. (1.132)][W1]; [Lemma 2, slice construction and Eq. (6)](../science/product_branch_rigidity.md#product-kraus-extraction).

<a id="m16"></a>
### M16 — One invertible slice fixes the whole extraction branch

**Phase:** Narrative/innovation.

**Central question:** Why does one nonzero scalar identity force all spectator slices to factor?

**Understanding target:** Understand how an invertible slice pair forces proportionality of every other slice, producing local spectator bras and reciprocal filters. Distinguish this extraction case from a nonzero operator that annihilates the whole perfect-pair support.

**Dependencies and story role:** M02, M15. Completes the first branch ingredient and separates the two cases that the remaining argument must handle.

**Conceptual connection:** Equal input/output local dimensions allow slice inversion and turn many local constraints into one tensor-product structure.

**Source pointers:** Watrous [§§1.1.2–1.1.3][W1]; [Lemma 2](../science/product_branch_rigidity.md#product-kraus-extraction).

<a id="m17"></a>
### M17 — Reciprocal filters preserve the Bell vector on both sides

**Phase:** Narrative/innovation.

**Central question:** Why is preserving the target vector alone insufficient to determine the noisy output's target weight?

**Understanding target:** Track both $`L|\Phi_d\rangle=\lambda|\Phi_d\rangle`$ and the corresponding adjoint identity for a reciprocal product filter. Understand why the adjoint identity eliminates the orthogonal-isotropic contribution to the Bell numerator.

**Dependencies and story role:** M05, M16. Establishes the numerator accounting for extraction branches.

**Conceptual connection:** A state transformation and the backward action on a target measurement involve different operator identities; reciprocity supplies both.

**Source pointers:** Watrous [§1.1.2, adjoints and vectorization][W1]; [Lemma 3, Eqs. (7)–(8)](../science/product_branch_rigidity.md#reciprocal-local-filters).

<a id="m18"></a>
### M18 — Relative error acceptance singles out unitaries

**Phase:** Narrative/innovation.

**Central question:** Can a reciprocal filter accept the isotropic error component less readily than the target?

**Understanding target:** Relate the success denominator to the filter's singular values. Understand why its conditional fidelity cannot exceed the input fidelity and why equality for an interior input forces conjugate local unitaries up to scalar factors.

**Dependencies and story role:** M02, M06–M07, M09, M17. Completes the extraction-branch inequality and its equality condition.

**Conceptual connection:** The balance of target and error acceptance, rather than perfect-state preservation alone, determines the quality after postselection.

**Source pointers:** Watrous [§1.1.1, Cauchy–Schwarz, and §1.1.3][W1]; [Lemma 3](../science/product_branch_rigidity.md#reciprocal-local-filters) and [reciprocal qubit filter](../science/scope_and_examples.md#example-1-a-reciprocal-qubit-filter).

<a id="m19"></a>
### M19 — Annihilating branches still see a positive spectator contribution

**Phase:** Narrative/innovation.

**Central question:** What constrains a branch that never succeeds when pair 1 is perfect?

**Understanding target:** Understand why such a branch can act nontrivially on the noisy component and may output entanglement from spectators. Relate full-rank spectator support to the positive-operator lower bound by a nonzero multiple of $`KK^\dagger`$.

**Dependencies and story role:** M01, M06, M14, M16. Begins the second branch analysis without imposing separability on its output.

**Conceptual connection:** A vanishing boundary probability removes one input sector, but does not remove positivity constraints on the surviving sector.

**Source pointers:** Watrous [§1.1.2, positive operator order][W1] and [§2.2.2][W2]; [Lemma 4, Eq. (12)](../science/product_branch_rigidity.md#strict-leakage-from-an-annihilating-branch).

<a id="m20"></a>
### M20 — A positive product contribution forces strict Bell-error leakage

**Phase:** Narrative/innovation.

**Central question:** Why must a nonzero annihilating branch leave some output outside the target?

**Understanding target:** Connect the Bell overlap bound for a positive product operator to the lower bound from M19. Understand why this establishes strictly positive leakage even when the complete branch output is entangled.

**Dependencies and story role:** M05, M10, M19. Completes the annihilating-branch ingredient.

**Conceptual connection:** A positive product component with imperfect Bell overlap suffices; the full output need not be separable.

**Source pointers:** Watrous [§1.1.2][W1] and [§6.1.1, separable operators][W6]; [Lemma 4, Eqs. (13)–(14)](../science/product_branch_rigidity.md#strict-leakage-from-an-annihilating-branch).

<a id="m21"></a>
### M21 — Four coefficients describe the complete accepted map

**Phase:** Narrative/innovation.

**Central question:** How can the two branch classes be combined without imposing a stronger branch-by-branch performance promise?

**Understanding target:** Interpret $`g,h`$ as extraction target and error coefficients, and $`c,z`$ as annihilator target and total coefficients. Understand why the full numerator and success probability are affine in the distinguished fidelity.

**Dependencies and story role:** M09, M18, M20. Passes from individual branch mechanisms to the entire accepted operation.

**Conceptual connection:** Linear unnormalized accounting keeps the actual success-weighted guarantee intact while allowing all accepted records to contribute.

**Source pointers:** Watrous [§2.3.2, instruments][W2]; [Theorem 1 proof, Eq. (17)](../science/ordered_purification.md#proof-of-theorem-1).

<a id="m22"></a>
### M22 — Universal nondegradation forces every inequality to saturate

**Phase:** Narrative/innovation.

**Central question:** Can one type of successful branch compensate for the other's fidelity loss?

**Understanding target:** Understand why the boundary condition requires a sum of two nonpositive terms to be nonnegative. Connect this to exclusion of every nonzero annihilating branch and equality in each extraction filter, using positive spectator weights.

**Dependencies and story role:** M13, M21. Combines the local ingredients into the decisive global equality argument.

**Conceptual connection:** The common sign of the two error contributions turns a performance guarantee into a structural classification.

**Source pointers:** Watrous [§1.1.3][W1] and [§2.3.2][W2] for the underlying norm and conditioning tools; [Theorem 1 proof, Eqs. (18)–(19)](../science/ordered_purification.md#proof-of-theorem-1) and [two sources of error](../science/interpretation.md#two-possible-sources-of-error-both-with-the-same-sign).

<a id="m23"></a>
### M23 — The accepted transformation preserves the independent retained pair's fidelity

**Phase:** Narrative/innovation.

**Central question:** What physical freedom remains after the Kraus operators are classified?

**Understanding target:** Explain the spectator-dependent mixture of conjugate local unitaries and why acceptance is independent of the retained pair's state. Distinguish preservation of Bell fidelity for an arbitrary independent state from preservation of the entire isotropic state.

**Dependencies and story role:** M04–M05, M16, M22. Translates the equality argument into the operation's observable behavior.

**Conceptual connection:** The target's symmetry preserves the score, while independence makes spectator conditioning a scalar weight.

**Source pointers:** Watrous [§1.1.2][W1] and [§§2.1.2 and 2.3.2][W2]; [Theorem 1, Eqs. (2)–(4) and (20)](../science/ordered_purification.md#ordered-fidelity-rigidity-theorem).

<a id="m24"></a>
### M24 — The classification is sufficient and respects complete ordering

**Phase:** Narrative/innovation.

**Central question:** Does the surviving structure describe every universally safe operation when the best pair is identified?

**Understanding target:** Understand the converse for nonzero trace-nonincreasing maps of the classified form. Explain why complete ordering information leaves the same proof available, and how spectator postselection can remain nontrivial while preserving fidelity.

**Dependencies and story role:** M12, M23. Completes the known-best statement as an exact classification.

**Conceptual connection:** Order information permits safe retention, but its remaining successful freedom acts through the spectators and target-preserving unitaries.

**Source pointers:** Watrous [§2.3.2][W2] and [§6.1.2][W6]; [Theorem 1 and its converse](../science/ordered_purification.md#ordered-fidelity-rigidity-theorem) and [spectator-postselection example](../science/scope_and_examples.md#example-2-allowed-postselection-with-zero-all-perfect-success).

<a id="m25"></a>
### M25 — Unknown ordering turns rigidity into impossibility

**Phase:** Narrative/innovation.

**Central question:** Why does a classification obtained where pair 1 is best rule out a guarantee over every ordering?

**Understanding target:** Explain why the fixed map's Kraus structure holds outside the ordering sector used to establish it. Combine fidelity preservation of pair 1 with an allowed tuple having a better pair 2 and positive interior success.

**Dependencies and story role:** M24. Converts the structural theorem into the universal-purification obstruction.

**Conceptual connection:** An operator identity inferred from one input sector constrains the same operation on all inputs.

**Source pointers:** Watrous [§§2.2.2 and 2.3.2][W2] and [§6.1.2][W6]; [Corollary 5](../science/ordered_purification.md#unknown-order-impossibility).

<a id="m26"></a>
### M26 — Identical-input recurrence and the stronger heterogeneous guarantee

**Phase:** Narrative/innovation.

**Central question:** How can ordinary recurrence purification improve identical inputs while the universal best-input guarantee fails?

**Understanding target:** Connect the recurrence example's success and fidelity accounting to the diagonal identical-input family. Understand why this family omits the independent pure-face limit and why the same circuit can degrade the better of unequal inputs.

**Dependencies and story role:** M06, M09, M25. Connects the impossibility to a familiar successful purification operation.

**Conceptual connection:** A change in the family over which a guarantee is quantified can change its truth without changing the circuit.

**Source pointers:** Watrous [§6.2.2, distillable entanglement and entanglement cost][W6] for the distillation context; [ordinary recurrence example](../science/scope_and_examples.md#example-3-ordinary-recurrence-on-identical-isotropic-inputs), with its primary formula attribution.

<a id="m27"></a>
### M27 — Restricted noise removes the full-support obstruction

**Phase:** Narrative/innovation.

**Central question:** Why can a parity-check recurrence universally improve the better input under rank-two bit-flip noise?

**Understanding target:** Interpret the accepted equal-error cases and the resulting best-input improvement. Identify which missing noise directions prevent the full spectator-slice condition used for isotropic inputs.

**Dependencies and story role:** M06, M15, M26. Isolates the role of the noise family's support.

**Conceptual connection:** A high fidelity and a known restricted error family provide different kinds of source information.

**Source pointers:** Watrous [§6.1.1, Example 6.10, and §6.1.2][W6] for isotropic states and local operations; [rank-two recurrence example](../science/scope_and_examples.md#example-4-recurrence-for-rank-two-bit-flip-noise), including the primary restricted-family result.

<a id="m28"></a>
### M28 — Correlations can turn spectator selection into fidelity improvement

**Phase:** Narrative/innovation.

**Central question:** Why is independence still essential when every marginal and the joint state are full rank?

**Understanding target:** Explain how spectator outcomes reweight the components of the correlated-mixture example. Separate allowed correlations among spectators in the structural consequence from correlations between the retained pair and those spectators.

**Dependencies and story role:** M04, M09, M23. Identifies the statistical boundary of the fidelity-preservation consequence.

**Conceptual connection:** Conditioning can reveal information about an unmeasured system through correlations, even though the local operation never acts on that system.

**Source pointers:** Watrous [§§2.1.2–2.1.3 and 2.3.2][W2]; [correlated-input example](../science/scope_and_examples.md#example-5-correlated-inputs-with-full-rank-isotropic-marginals) and [Theorem 1's independent-input consequence](../science/ordered_purification.md#ordered-fidelity-rigidity-theorem).

<a id="m29"></a>
### M29 — Information, resources and the precise relation to earlier results

**Phase:** Narrative/innovation.

**Central question:** Which scientific question is resolved, and which changed assumptions define another question?

**Understanding target:** Distinguish the inherited universality benchmark and boundary method from the arbitrary-SEP branch classification. Locate the finite-input, equal-dimension, known-target, exact-guarantee and unassisted assumptions; keep the earlier catalytic Clifford result separate.

**Dependencies and story role:** M11, M24–M28. Places the theorem and its exceptions within one consistent operational and scholarly scope.

**Conceptual connection:** Strengthening the operation class does not automatically extend a result to new resources, output dimensions or performance comparators.

**Source pointers:** Watrous [§§6.1.2 and 6.2.2][W6] for operation and distillation frameworks; [scope boundaries](../science/scope_and_examples.md#boundaries-of-the-statement), [attribution](../science/ordered_purification.md#attribution-and-interpretation) and [primary-source comparison](../references/RELATED_WORK.md).

<a id="m30"></a>
### M30 — Narrative synthesis: exact universality as a structural constraint

**Phase:** Narrative/innovation.

**Central question:** How do the proof mechanism, the operational conclusion and the examples form one scientific account?

**Understanding target:** Connect the independently approachable pure face to branch support, local factorization, the two error inequalities and their forced equality. Explain how that chain yields fidelity-preserving retention with order information and impossibility without it, while accounting for the explicit exceptions.

**Dependencies and story role:** M12, M22–M29. Integrates the complete narrative from local operators to the global information constraint.

**Conceptual connection:** The result classifies what an exact universal performance promise permits an operation to do; the examples identify the assumptions carrying that classification.

**Source pointers:** Watrous [§1.1.2][W1], [§2.3.2][W2] and [§6.1.2][W6] for the connected foundations; [ordered theorem and corollary](../science/ordered_purification.md), [interpretation](../science/interpretation.md) and [worked examples](../science/scope_and_examples.md).

[W1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[W6]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf
