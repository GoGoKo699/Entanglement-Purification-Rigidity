# Scope and worked examples

The [model](model.md) fixes the target $`P`$, isotropic state $`\omega(F)`$, product input $`\Omega(\boldsymbol F)`$, and threshold $`f_\star`$. The exact theorem and proof are in [ordered purification](ordered_purification.md). This page gives success accounting, physical examples, and the assumptions that distinguish these conclusions from other purification tasks.

## Success probability and accepted fidelity

For an accepted operation $`\mathcal E`$, write

```math
\widetilde\sigma=\mathcal E(\Omega(\boldsymbol F)),
\qquad p=\operatorname{Tr}\widetilde\sigma,
\qquad N=\operatorname{Tr}(P\widetilde\sigma).
```

The normalized accepted state is $`\widetilde\sigma/p`$ and its target fidelity is $`F_{\rm out}=N/p`$. For several accepted heralding records,

```math
p=\sum_r p_r,
\qquad N=\sum_r N_r,
\qquad F_{\rm out}=\sum_{r:p_r>0}\frac{p_r}{p}F_r.
```

The guarantee concerns this mixture, weighted by success probabilities; it does not impose a separate fidelity guarantee on each accepted record.

A nonzero fixed completely positive map succeeds with positive probability on every full-rank interior input. Its success may approach zero at a boundary. The proof therefore takes limits in $`N\geq F_1p`$ without dividing by boundary success. It explicitly retains, and subsequently excludes, product branches annihilating the entire best-pair pure face; see [the positive-leakage argument](product_branch_rigidity.md). Zero success at the all-perfect input is allowed, as Example 2 demonstrates.

## Example 1: a reciprocal qubit filter

For $`d=2`$, consider the local contractions

```math
M_A=\begin{pmatrix}1&0\\0&r^{-1}\end{pmatrix},
\qquad
M_B=\begin{pmatrix}r^{-1}&0\\0&1\end{pmatrix},
\qquad r\geq1.
```

The successful product filter is $`L=M_A\otimes M_B`$. It satisfies

```math
M_AM_B^T=r^{-1}I_2,
\qquad L|\Phi_2\rangle=r^{-1}|\Phi_2\rangle.
```

A perfect Bell input remains perfect when this filter succeeds. For an isotropic input, however, direct evaluation gives

```math
p(F)=\frac{F}{r^2}
+\frac{1-F}{3}\left(1+r^{-2}+r^{-4}\right),
\qquad N(F)=\frac{F}{r^2},
```

and therefore

```math
F_{\rm out}
=\frac{F}{F+(1-F)(r^2+1+r^{-2})/3}.
```

For $`r>1`$ and $`0<F<1`$, this is strictly smaller than $`F`$. At $`r=2`$ and $`F=9/10`$,

```math
p=\frac{43}{160},
\qquad N=\frac9{40},
\qquad F_{\rm out}=\frac{36}{43}\approx0.8372<0.9.
```

Preservation of the perfect state alone is therefore insufficient. The relative acceptance of its isotropic orthogonal component determines whether a noisy input degrades.

## Example 2: allowed postselection with zero all-perfect success

Take two qubit pairs. Keep pair 1, measure pair 2 locally in the computational basis, and accept only Alice's outcome 0 and Bob's outcome 1. The successful Kraus operators are

```math
K_A=I_{A_1}\otimes\langle0|_{A_2},
\qquad
K_B=I_{B_1}\otimes\langle1|_{B_2}.
```

For independent isotropic inputs,

```math
\mathcal E\bigl(\omega(F_1)\otimes\omega(F_2)\bigr)
=\frac{1-F_2}{3}\omega(F_1).
```

Thus

```math
p=\frac{1-F_2}{3},
\qquad N=\frac{F_1(1-F_2)}{3},
\qquad F_{\rm out}=F_1.
```

The operation succeeds with positive probability for every interior tuple and has zero success whenever pair 2 is perfect, including the all-perfect input. It meets the guarantee when pair 1 is promised best. When $`F_2>F_1`$, it falls short of the best input.

This example also explains the use of independence in the structural conclusion: the scalar spectator probability factors out of the entire state of pair 1. Correlations between pair 1 and the measured spectators can change its conditional state after the same measurement.

## Example 3: ordinary recurrence on identical isotropic inputs

For two qubit pairs, apply a controlled-NOT locally on each side, using pair 1 as control and pair 2 as target. Measure pair 2 in the computational basis and accept equal Alice/Bob outcomes. A final isotropic twirl can be added without changing the target fidelity. This is the usual recurrence step, with target Bell-state conventions adjusted to $`\Phi^+`$. Its identical-input fidelity formula is Eq. (7) of Bennett et al. [2].

For independent isotropic fidelities $`F_1,F_2`$, put $`q_i=(1-F_i)/3`$. Counting accepted Bell-error patterns gives

```math
p=F_1F_2+F_1q_2+q_1F_2+5q_1q_2,
\qquad
N=F_1F_2+q_1q_2.
```

For identical inputs $`F_1=F_2=F`$, $`q=(1-F)/3`$, these reduce to

```math
p=F^2+2Fq+5q^2,
\qquad
F_{\rm out}=\frac{F^2+q^2}{F^2+2Fq+5q^2}.
```

In particular,

```math
F_{\rm out}-F
=\frac{(1-F)(4F-1)(2F-1)}{9p}>0
\qquad\text{for }\frac12<F<1.
```

This familiar improvement is compatible with rigidity. The identical-input promise confines the allowed fidelity vectors to a diagonal. One cannot take one input to perfection while keeping its spectators fixed and noisy within that promise.

The same recurrence step fails the best-input guarantee when the fidelities vary separately. At fixed $`F_2<1`$,

```math
\lim_{F_1\to1}F_{\rm out}
=\frac{F_2}{F_2+q_2}
=\frac{3F_2}{1+2F_2}<1.
```

Consequently it degrades a sufficiently good first pair when compared with that pair's own fidelity, even if the second pair is itself highly faithful.

## Example 4: recurrence for rank-two bit-flip noise

A restricted noise promise changes the conclusion. Let

```math
\rho_X(F)=F|\Phi^+\rangle\langle\Phi^+|
+(1-F)|\Psi^+\rangle\langle\Psi^+|,
```

with $`1/2<F<1`$. These states have rank two. Zang et al. explicitly establish the universality of the bilateral controlled-NOT step for this family in Proposition 37 [1]. The probability and fidelity can also be read directly from its four error cases.

Write $`b=0`$ for $`\Phi^+`$ and $`b=1`$ for $`\Psi^+`$. The bilateral controlled-NOT sends

```math
(b_1,b_2)\longmapsto(b_1,b_1\oplus b_2).
```

Equal measurement outcomes on the target occur exactly when $`b_1=b_2`$. Thus:

| Initial errors | Probability | Accepted? | Kept state |
| --- | --- | --- | --- |
| $`0,0`$ | $`F_1F_2`$ | Yes | $`\Phi^+`$ |
| $`0,1`$ | $`F_1(1-F_2)`$ | No | — |
| $`1,0`$ | $`(1-F_1)F_2`$ | No | — |
| $`1,1`$ | $`(1-F_1)(1-F_2)`$ | Yes | $`\Psi^+`$ |

The exact accounting is

```math
p=F_1F_2+(1-F_1)(1-F_2),
\qquad N=F_1F_2,
\qquad
F_{\rm out}=\frac{F_1F_2}{F_1F_2+(1-F_1)(1-F_2)}.
```

If $`F_1\geq F_2>1/2`$,

```math
F_{\rm out}-F_1
=\frac{F_1(1-F_1)(2F_2-1)}{p}>0.
```

The symmetric statement holds when $`F_2\geq F_1>1/2`$. Hence this fixed protocol strictly beats the better input throughout the interior of the rank-two family. For example, $`F_1=9/10`$ and $`F_2=3/5`$ give

```math
p=\frac{29}{50},
\qquad N=\frac{27}{50},
\qquad F_{\rm out}=\frac{27}{29}>\frac9{10}.
```

The missing noise directions are decisive. A rank-two spectator has only a proper support subspace. Vanishing leakage on that support does not impose the full spectator-slice identities used in the isotropic rigidity proof. The protocol is therefore a genuine example of universal purification under a different noise promise, consistent with the theorem's isotropic hypothesis.

## Example 5: correlated inputs with full-rank isotropic marginals

Consider the two-pair state

```math
\Theta=\frac12\omega(9/10)\otimes\omega(9/10)
+\frac12\omega(3/5)\otimes\omega(3/5).
```

Both marginals are $`\omega(3/4)`$, and the joint state is full rank. The pairs are correlated through their shared mixture label.

Keep pair 1 and accept outcome $`(0,0)`$ when pair 2 is measured locally in the computational basis. For an isotropic spectator the probability of this outcome is

```math
q(F)=\langle00|\omega(F)|00\rangle
=\frac{1+2F}{6}.
```

Linearity gives the unnormalized kept state

```math
\widetilde\sigma
=\frac12q(9/10)\omega(9/10)
+\frac12q(3/5)\omega(3/5),
```

so that

```math
p=\frac5{12},
\qquad N=\frac8{25},
\qquad F_{\rm out}=\frac{96}{125}>\frac34.
```

The accepted spectator outcome favors the higher-fidelity component and thereby changes the fidelity of the unmeasured pair. Full-rank isotropic marginals alone do not ensure the fidelity-preservation consequence of ordered rigidity; independence from the spectators is required.

## Exact values for implementation checks

These values include the probability of the complete accepted event. Example 2 accepts only spectator outcome $`(0,1)`$, and Example 5 accepts only $`(0,0)`$. Both equal target outcomes are accepted in the recurrence examples.

| Operation and input | Success $`p`$ | Target numerator $`N`$ | Accepted fidelity $`N/p`$ |
| --- | --- | --- | --- |
| Reciprocal filter: $`r=2`$, $`F=9/10`$ | $`43/160`$ | $`9/40`$ | $`36/43`$ |
| Spectator postselection: $`F_1=9/10`$, $`F_2=3/5`$ | $`2/15`$ | $`3/25`$ | $`9/10`$ |
| Isotropic recurrence: $`F_1=F_2=9/10`$ | $`197/225`$ | $`73/90`$ | $`365/394`$ |
| Isotropic recurrence: $`F_1=99/100`$, $`F_2=9/10`$ | $`2087/2250`$ | $`401/450`$ | $`2005/2087`$ |
| Bit-flip recurrence: $`F_1=9/10`$, $`F_2=3/5`$ | $`29/50`$ | $`27/50`$ | $`27/29`$ |
| Correlated mixture: state $`\Theta`$, spectator outcome $`(0,0)`$ | $`5/12`$ | $`8/25`$ | $`96/125`$ |

## Boundaries of the statement

**Independent states and separately variable fidelities.** The input is a product of the $`n`$ pair states, and the promise permits the fidelities to vary independently as coordinates of the allowed set. These are distinct requirements. Identically prepared independent pairs satisfy the first but have an additional equality constraint on the second. Correlated states with isotropic marginals do not satisfy the product-state hypothesis. Knowledge of the marginals alone does not justify applying the theorem to their joint state.

**Exact, pointwise comparison.** The required comparison is $`F_{\rm out}\geq\max_iF_i`$ for every permitted vector, or $`F_{\rm out}\geq F_1`$ throughout a best-index sector. Averaging fidelity over a distribution of source parameters defines a different benchmark. The theorem does not give a numerical lower bound on the size of a violation for a protocol that fails universality.

**Finite quantum input.** The result holds for every fixed finite $`n`$, however large. It places no restriction to Clifford gates or a particular circuit architecture. Procedures drawing an unbounded number of fresh input pairs do not define the same fixed-$`n`$ task.

**Known target and equal output dimension.** All fidelities refer to the specified maximally entangled target in known local bases. Outcome-dependent corrections to that target are included in $`\mathcal E`$. The output has the same local dimension $`d`$ as each input pair; the proof uses this equality when it inverts an active $`d\times d`$ slice.

**Available side information and adaptivity.** The protocol may be designed for a known threshold $`f_\star`$, known best-input index, or known complete ordering. Inside that promise it remains one fixed operation. Later gates and acceptance decisions may depend on measurement records, including estimates made using the supplied finite batch. Exact numerical fidelities supplied from outside the protocol would define a different information model.

**Ancillary resources.** Fixed local or shared separable ancillas can be absorbed into the separable success map, as can discarded local outputs and accepted classical records. A supplied entangled catalyst or other extra shared entangled state is outside the assumptions. The theorem concerns operations separable across Alice and Bob's laboratories; quantum communication that implements a nonseparable operation is outside that class.

## References

[1] Allen Zang, Xinan Chen, Eric Chitambar, Martin Suchara, and Tian Zhong, *No-Go Theorems for Universal Entanglement Purification*, Physical Review Letters **134**, 190803 (2025). [Published article](https://doi.org/10.1103/PhysRevLett.134.190803); [full primary text, including Proposition 37 and the ordered-fidelity results](https://arxiv.org/html/2407.21760v2).

[2] Charles H. Bennett, Gilles Brassard, Sandu Popescu, Benjamin Schumacher, John A. Smolin, and William K. Wootters, *Purification of Noisy Entanglement and Faithful Teleportation via Noisy Channels*, Physical Review Letters **76**, 722–725 (1996). [Published article](https://doi.org/10.1103/PhysRevLett.76.722); [primary preprint, Eq. (7) and the bilateral-XOR error table](https://arxiv.org/pdf/quant-ph/9511027).
