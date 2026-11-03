# Model, question and reading route

Entanglement purification combines noisy shared pairs using operations performed in two separated laboratories. When the pairs have different and unknown qualities, a successful protocol can be less useful than simply retaining the best input. The question here is whether one fixed finite-input protocol can avoid that outcome on every possible input, even after every pair is promised to be arbitrarily close to perfect.

The answer is negative for unassisted separable operations. More precisely, if the best pair is identified in advance, the only operations that never degrade it throughout the promised family preserve its Bell fidelity exactly. This structural statement is the source of the impossibility when the best pair is unidentified.

## States and operations


Alice and Bob receive $`n\ge 2`$ independent pairs. Each local input space and each local output space has the same finite dimension $`d\ge 2`$. The target is fixed and known:

```math
|\Phi_d\rangle=\frac{1}{\sqrt d}\sum_{j=0}^{d-1}|j\rangle_A|j\rangle_B,
\qquad
P=|\Phi_d\rangle\langle\Phi_d|.
```

Transposes and entrywise complex conjugates refer to these bases. Define

```math
R=\frac{I-P}{d^2-1},
\qquad
\omega(F)=FP+(1-F)R.
```

The Bell fidelity of a normalized output state $`\rho`$ is $`F(\rho)=\mathrm{Tr}(P\rho)`$. Fix a threshold $`f_\star\in[1/d,1)`$. The theorem will assume a guarantee only for isotropic inputs with independently variable fidelities in $`(f_\star,1)`$. Every such input is positive definite. In particular, the argument does not need low-fidelity or separable inputs.

A fixed accepted branch is a nonzero completely positive, trace-nonincreasing map

```math
\mathcal E(X)=\sum_r K_rXK_r^\dagger,
\qquad
K_r=A_r\otimes B_r,
\qquad
\sum_r K_r^\dagger K_r\le I.
```

This finite product-Kraus representation defines the class of separable operations used here. Alice's map $`A_r`$ acts on all her input systems and outputs one $`d`$-dimensional system; Bob's map has the analogous meaning. Local ancillary systems, local discards, classical communication, and shared classical randomness can be included in this success map. No additional shared entangled resource is supplied. Every LOCC protocol induces such a separable map, so the conclusions apply to LOCC as well; see [Chitambar et al.][locc2014] for the relation between these operation classes.

For

```math
\Omega(\boldsymbol F)=\bigotimes_{i=1}^n\omega(F_i),
\qquad
p(\boldsymbol F)=\mathrm{Tr}\mathcal E(\Omega(\boldsymbol F)),
```

the conditional output is $`\mathcal E(\Omega)/p`$. Because $`\mathcal E\ne0`$ and $`\Omega>0`$, one has $`p(\boldsymbol F)>0`$ at every interior tuple. This imposes no lower bound on that probability and no requirement that it remain positive at a boundary tuple.

Throughout the proof, tensor factors are regrouped when necessary so that Alice's systems precede Bob's. Labels make the distinguished pair and its spectators unambiguous.


The finite product-Kraus form is not a finite-round restriction. For finite input and output dimensions, a Choi operator separable across Alice's output-plus-input-reference systems and Bob's output-plus-input-reference systems admits a finite decomposition into product positive operators; refining their spectral decompositions gives product Kraus operators. The cone is closed, so LOCC limits are included whenever they define the stipulated finite-dimensional success map. Local workspaces and classical transcripts have already been absorbed into that effective map. The theorem does not require every SEP map to be physically implementable by LOCC: proving impossibility in the larger class suffices.

The threshold convention includes any proposed minimum $`f_0<1`$: take $`f_\star=\max\{f_0,1/d\}`$. The proof uses only the entangled isotropic states in the resulting open interval, without evaluating a conditional state at $`F_i=1`$.

## What is fixed, and what may vary?

| Ingredient | Model |
|---|---|
| Input count and dimension | Arbitrary but fixed finite $`n\ge2`$ and $`d\ge2`$; one output pair of the same local dimension. |
| Source states | Independent pairs; each fidelity varies separately throughout $`(f_\star,1)`$. Identical copies are included but are not the whole promise. |
| Target and score | Known fixed $`P`$; the score is its overlap with the normalized accepted state, without a square root. |
| Protocol information | The map may depend on $`n,d,f_\star`$ and the promised ordering. It cannot change with the unknown numerical fidelity tuple. |
| Local processing | General local quantum operations, local ancillas, classical communication, classical randomness, local discarding and postselection. |
| Additional shared entanglement | None; the input pairs are the supplied entangled resource. |
| Success | Positive on every interior tuple because the map is nonzero and the input is full rank. No uniform lower bound or boundary-success condition. |
| Guarantee | Exact conditional fidelity at least that of the best input, for every allowed tuple. No averaging over source parameters. |

Calling the success map fixed permits arbitrary measurements and adaptive control inside the protocol. What is excluded is selecting a different map using numerical source parameters supplied from outside the stated input. Unbounded repeated attempts that consume an unbounded number of pairs are also outside a fixed finite batch.

## Two conclusions

**Ordered rigidity.** If pair 1 is promised to be best, universal nondegradation forces each product branch to extract pair 1 through a conjugate pair of local unitaries, while applying local bras to the spectators. For any state of pair 1 independent of its spectators, the accepted Bell fidelity is exactly its input value. Knowing the full ordering gives the same result.

**Unknown-order impossibility.** If every ordering is allowed, the same map would have to obey ordered rigidity on the region where pair 1 is best. That fixes its action even outside that region; choosing a better pair 2 then contradicts the guarantee. This holds for every fidelity floor below one and every fixed finite batch size.

The exact statements and their proofs have their authoritative home in [ordered purification](ordered_purification.md). A guarantee for all independent states above the fidelity floor is also impossible, since that larger family includes the isotropic test family used here.

## Connected reading route

1. This page fixes the information, operation and success model.
2. [Product-branch rigidity](product_branch_rigidity.md) proves the three algebraic facts: extraction from a perfect pair, reciprocal-filter fidelity loss, and strictly positive leakage from boundary-annihilating branches.
3. [Ordered purification](ordered_purification.md) combines them into the structural theorem and unknown-order corollary.
4. [Scope and examples](scope_and_examples.md) calculates physical examples and explains which changed assumptions escape the result.
5. [Interpretation](interpretation.md) explains the mechanism, operational consequence and relation to existing purification protocols.

The [related-work comparison](../references/RELATED_WORK.md) credits the universality benchmark and earlier no-go results. The [verification guide](../verification/README.md) separates finite algebra checks from the analytical proof.

[locc2014]: https://arxiv.org/abs/1210.4583v2
