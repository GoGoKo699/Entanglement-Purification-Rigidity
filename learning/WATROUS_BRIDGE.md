# From Watrous to entanglement-purification rigidity

John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018), is the educational anchor for this project. The [author's manuscript page][watrous] supplies the book and individual chapters. The source route below refers to its standard-layout manuscript.

The bridge connects the book's operator, channel and entanglement language to one question: what can a fixed successful local protocol do if its output must always be at least as faithful to a known Bell target as the best input? The authoritative model and proofs remain in [model](../science/model.md), [product-branch rigidity](../science/product_branch_rigidity.md) and [ordered purification](../science/ordered_purification.md). The [30-milestone map](MILESTONES.md) expands the dependencies; this page follows the causal argument through them.

## A focused route through the source

| Needed concept | Verified location in Watrous | Project connection |
| --- | --- | --- |
| Positive operators, adjoints, tensor products, vectorization and singular values | [Chapter 1][w1], Sections 1.1.2–1.1.3; vectorization identity (1.132) | [M01–M05](MILESTONES.md#m01): support, equality conditions and the Bell-vector matrix identity. |
| Product states and reduced states | [Chapter 2][w2], Section 2.1.2, “Product states,” Eq. (2.18); Section 2.1.3 | [M04](MILESTONES.md#m04): independence is a property of the joint state, stronger than knowledge of its marginals. |
| Completely positive maps and Kraus representations | [Chapter 2][w2], Sections 2.2.1–2.2.2, especially Theorem 2.22 | [M08](MILESTONES.md#m08): the accepted operation has an operator-sum representation. |
| Outcome probabilities and conditional output states | [Chapter 2][w2], Section 2.3.2, “Nondestructive measurements and instruments,” Eqs. (2.258)–(2.260) | [M09](MILESTONES.md#m09): success probabilities remain part of the calculation until normalization. |
| Fidelity convention | [Chapter 3][w3], Section 3.2, Definition 3.11; Section 3.2.1, Propositions 3.12–3.13 | [M07](MILESTONES.md#m07): convert the book's root fidelity to the project's Bell overlap. |
| Isotropic states | [Chapter 6][w6], Section 6.1.1, Example 6.10, especially Eq. (6.45) | [M06](MILESTONES.md#m06): the test family has a known pure target and full support at every interior fidelity. |
| Separable maps, product Kraus operators and LOCC | [Chapter 6][w6], Section 6.1.2, Definition 6.17 and Propositions 6.18, 6.22 and 6.26 | [M10–M11](MILESTONES.md#m10): product structure across laboratories, the correct Choi partition and the inclusion of LOCC in SEP. |
| Finite decompositions and limits | [Chapter 6][w6], Section 6.1.1, Corollary 6.7 and Proposition 6.8 | [M11](MILESTONES.md#m11): finite-dimensional separable Choi operators admit finite decompositions and form a closed cone. |

There is a scope distinction in the last two rows. Watrous's Definition 6.25 defines LOCC through finitely many communication stages; the accompanying footnote on printed page 330 states this restriction. Proposition 6.26 supplies that LOCC-to-SEP inclusion. The project's inclusion of limits is a further finite-dimensional argument: regrouped Choi operators remain in the closed separable cone, and their finite product decompositions recover product Kraus operators. This extension is explained in the [model](../science/model.md#states-and-operations).

## Notation and conventions

| In Watrous | In this project | Meaning |
| --- | --- | --- |
| $`A^*`$ | $`A^\dagger`$ | Adjoint, including complex conjugation and transpose. |
| $`A^{\mathrm{T}}`$, $`\overline A`$ | $`A^{\mathrm{T}}`$, $`\overline A`$ | Transpose and entrywise conjugation in the fixed local bases. |
| $`\mathbb{1}`$ | $`I`$ | Identity operator on the indicated space. |
| $`\mathrm{vec}(X)`$ | $`\lvert X\rangle\!\rangle`$ | The vector $`\sum_{jk}X_{jk}\lvert j\rangle\lvert k\rangle`$; its normalization depends on $`X`$. |
| $`\mathrm D(\mathcal X)`$ | A normalized state $`\rho`$ | A positive operator with trace one. An accepted output before division by its trace need not have trace one. |
| $`F(X,Y)`$ | $`F_{\rm W}(X,Y)`$ on this page | Watrous's fidelity, distinguished from the project's score. |
| A separable CP map on $`\mathcal X\otimes\mathcal Y`$ | $`\mathcal E`$ on all Alice and Bob inputs | Here $`\mathcal X=\bigotimes_i\mathcal H_{A_i}`$ and $`\mathcal Y=\bigotimes_i\mathcal H_{B_i}`$; each output space has dimension $`d`$. |

The product in a product Kraus operator means a product **between laboratories**. Alice's factor can act jointly on all of her input systems. It need not factor between pairs. In the Choi description, the separability partition groups Alice's output with her input reference, and Bob's output with his input reference.

Keeping the accepted records of a local protocol keeps the corresponding product Kraus terms. The resulting map remains separable and becomes trace-nonincreasing. A Kraus index need not itself be an observed classical outcome: the proof may refine a separable decomposition mathematically. Its premise applies to the whole accepted output, including the mixture over every accepted record.

### The fidelity conversion

Watrous's Definition 3.11 uses

```math
F_{\rm W}(X,Y)=\|\sqrt X\sqrt Y\|_1.
```

For the project's fixed pure target $`P=|\Phi_d\rangle\langle\Phi_d|`$, this gives

```math
F_{\rm Bell}(\rho)
=\mathrm{Tr}(P\rho)
=F_{\rm W}(P,\rho)^2.
```

The science pages call this overlap $`F(\rho)`$. The input parameter $`F_i`$ is likewise an overlap. In particular, a guarantee written in Watrous's convention would compare $`F_{\rm W}(P,\rho_{\rm out})`$ with $`\sqrt{F_i}`$.

For an unnormalized accepted output $`Y=\mathcal E(\Omega)`$, define $`p=\mathrm{Tr}Y`$ and $`N=\mathrm{Tr}(PY)`$. Then

```math
F_{\rm W}(P,Y)=\sqrt N,
\qquad
F_{\rm W}(P,Y/p)=\sqrt{N/p},
\qquad
F_{\rm Bell}(Y/p)=N/p.
```

These formulas follow directly because $`P\sqrt Y`$ has at most one nonzero singular value, whose square is $`\langle\Phi_d|Y|\Phi_d\rangle`$. They are the pure-target case of Watrous's Proposition 3.13 and agree with the square-root scaling in Proposition 3.12. The proof uses $`N-F_1p`$ because this expression remains defined when a limiting success probability vanishes.

## The model that activates the argument

The [model synthesis, M12](MILESTONES.md#m12), fixes finite $`n,d\ge2`$, a known maximally entangled target, and

```math
P=|\Phi_d\rangle\langle\Phi_d|,
\qquad
|\Phi_d\rangle=d^{-1/2}\sum_j|jj\rangle,
\qquad
R=\frac{I-P}{d^2-1},
\qquad
\omega(F)=FP+(1-F)R.
```

The input is the product $`\bigotimes_i\omega(F_i)`$, with each fidelity separately variable in $`(f_\star,1)`$ for a fixed $`1/d\le f_\star<1`$. In the ordered problem, pair 1 is promised to have the largest fidelity. One nonzero separable CP trace-nonincreasing map must obey the conditional guarantee throughout that region. No additional shared entangled resource is supplied.

The map can include adaptive local measurements, classical communication, local ancillas, shared randomness and postselection. “Fixed” means that these rules define one operation on the finite batch; its definition cannot change with numerical fidelities supplied from outside the model.

Every interior isotropic state has eigenvalues $`F`$ and $`(1-F)/(d^2-1)`$, all positive. Thus a nonzero CP map has positive success probability on every interior input. This statement supplies no uniform success floor, and it does not require success at a boundary input.

## From a perfect possible input to a rigid operation

The perfect-input boundary method and the universality benchmark are inherited from the work credited in the [related-work account](../references/RELATED_WORK.md#relation-to-the-2025-universal-purification-no-go). Watrous supplies the underlying operator language. The extraction and strict-leakage arguments below are project steps whose complete proofs appear in [Lemmas 2–4](../science/product_branch_rigidity.md).

### 1. Positivity turns a boundary statement into a support constraint

This is the passage from [M13](MILESTONES.md#m13) to [M14](MILESTONES.md#m14).

Fix noisy interior spectators $`\tau=\bigotimes_{i>1}\omega(F_i)>0`$ and let only $`F_1`$ approach one. The ordered promise remains valid along the final part of this path. Taking the limit in the homogeneous guarantee $`N(F_1)\ge F_1p(F_1)`$ gives

```math
\mathrm{Tr}\!\left[(I-P)\mathcal E(P\otimes\tau)\right]=0.
```

For a Kraus sum, that leakage is a sum of squared Hilbert–Schmidt norms:

```math
\sum_r\left\|(I-P)K_r(P\otimes\tau^{1/2})\right\|_2^2=0.
```

Each term therefore vanishes. Because $`\tau^{1/2}`$ is invertible, it ranges over the whole spectator space. Each $`K_r`$ consequently sends

```math
\mathcal S_1
=\mathrm{span}\{|\Phi_d\rangle_1\}\otimes\mathcal H_{\rm rest}
```

into the output Bell ray, possibly sending all of $`\mathcal S_1`$ to zero.

Two assumptions have separate jobs here. Positivity prevents different Kraus terms from canceling leakage. Full spectator rank turns a condition on the occupied input support into a condition on every spectator direction. No normalized boundary state was used.

### 2. Spatial factorization forces extraction

[M15](MILESTONES.md#m15) and [M16](MILESTONES.md#m16) explain why a support constraint has an operational consequence.

For $`K=A\otimes B`$, insert local spectator basis vectors to obtain square matrices $`A_u,B_v`$ acting on pair 1. Watrous's vectorization identity becomes

```math
(A_u\otimes B_v)|\Phi_d\rangle
=d^{-1/2}|A_uB_v^{\mathrm{T}}\rangle\!\rangle.
```

The support constraint is thus $`A_uB_v^{\mathrm{T}}=\lambda_{uv}I_d`$ for every $`u,v`$. If one coefficient is nonzero, its two matrices are invertible. Holding one of those matrices fixed forces every slice on the opposite side to be proportional to its active slice. The local maps therefore extract pair 1 and evaluate local spectator bras:

```math
A=M\otimes\langle a|,
\qquad
B=N\otimes\langle b|,
\qquad
MN^{\mathrm{T}}=\lambda I_d.
```

If every coefficient vanishes, the branch annihilates $`\mathcal S_1`$. These are the two classes in [Lemma 2](../science/product_branch_rigidity.md#product-kraus-extraction). The equal input and output dimensions matter: the active slices are square, so a nonzero scalar identity gives invertibility.

### 3. Reciprocal filters cannot improve isotropic noise

[M17](MILESTONES.md#m17) and [M18](MILESTONES.md#m18) examine the extracted pair.

The relation $`MN^{\mathrm{T}}=\lambda I`$ makes the two local filters reciprocal. For $`L=M\otimes N`$, it implies both

```math
L|\Phi_d\rangle=\lambda|\Phi_d\rangle,
\qquad
L^\dagger|\Phi_d\rangle=\overline\lambda|\Phi_d\rangle.
```

The second identity rules out a target contribution from $`LRL^\dagger`$. If $`x_j>0`$ are the squared singular values of $`M`$, the total accepted noise weight is constrained by

```math
\left(\sum_jx_j\right)\left(\sum_jx_j^{-1}\right)\ge d^2.
```

Equality requires every $`x_j`$ to be equal. [Lemma 3](../science/product_branch_rigidity.md#reciprocal-local-filters) turns this elementary inequality into the fidelity statement: an extraction branch accepts at least as much isotropic error per unit input weight as target per unit input weight. For an interior isotropic input, equality between accepted and input fidelity requires $`M=sU`$ and $`N=t\overline U`$.

The conjugate on Bob's unitary is essential. It ensures $`U(\overline U)^{\mathrm{T}}=UU^\dagger=I`$, so $`U\otimes\overline U`$ fixes the Bell target.

### 4. An annihilating branch still produces strictly positive leakage

[M19](MILESTONES.md#m19) and [M20](MILESTONES.md#m20) close the zero-boundary-success loophole.

A nonzero branch may satisfy $`K(P\otimes I)=0`$. It then receives weight only from the first pair's noise component. It may also transfer entanglement from the spectators, so its output cannot be assumed separable.

The useful comparison is an operator lower bound. Since $`\tau>0`$, there is $`\mu>0`$ with $`\tau\ge\mu I`$, and

```math
K(R\otimes\tau)K^\dagger
\ge \frac{\mu}{d^2-1}KK^\dagger.
```

The operator on the right is a nonzero product positive operator because $`KK^\dagger=AA^\dagger\otimes BB^\dagger`$. Its Bell overlap is at most $`1/d`$ of its trace. Therefore the left side has strictly positive population orthogonal to the Bell target. This is [Lemma 4](../science/product_branch_rigidity.md#strict-leakage-from-an-annihilating-branch).

The lower bound uses the smallest spectator eigenvalue only to obtain strict positivity for the fixed interior tuple. It supplies no bound uniform over all tuples near the boundary.

### 5. The accepted mixture forces every inequality to saturate

[M21](MILESTONES.md#m21) and [M22](MILESTONES.md#m22) restore the whole success map.

For the fixed spectators, let $`g`$ and $`h`$ denote the summed target and noise acceptance coefficients of extraction branches. The reciprocal-filter inequality gives $`h\ge g`$. Let $`c`$ and $`z`$ be the summed Bell overlap and total trace produced by annihilating branches on $`R\otimes\tau`$. Strict leakage gives $`z>c`$ whenever such a branch is present.

The [ordered proof](../science/ordered_purification.md#proof-of-theorem-1) shows that the exact guarantee arbitrarily close to $`F_1=1`$ requires

```math
(g-h)+(c-z)\ge0.
```

Both terms are nonpositive. Thus there can be no nonzero annihilating branch, and every extraction branch must saturate the filter inequality. Full-rank spectators assign every nonzero extraction bra a positive weight, so no exceptional extraction branch can disappear from this equality.

This is why the theorem can classify every product Kraus operator without having assumed a separate guarantee for individual heralding records.

### 6. Ordered rigidity determines the unknown-order outcome

The structural conclusion is [M23–M24](MILESTONES.md#m23) and [Theorem 1](../science/ordered_purification.md#ordered-fidelity-rigidity-theorem):

```math
A_r=s_rU_r\otimes\langle a_r|,
\qquad
B_r=t_r\overline{U_r}\otimes\langle b_r|.
```

For any input $`\rho_1\otimes\tau`$, with pair 1 independent of the spectators, the accepted operation is a positive mixture of $`U_r\otimes\overline{U_r}`$ acting on pair 1. Its weights depend only on $`\tau`$. Its success probability therefore depends only on the spectators, and its conditional Bell overlap equals $`\mathrm{Tr}(P\rho_1)`$ whenever success occurs. The spectators may be internally correlated or entangled between the laboratories. Independence of pair 1 from them is still needed.

Knowing the full fidelity ordering gives the same conclusion: strictly ordered fixed spectators still allow $`F_1\uparrow1`$. For an isotropic retained state, every surviving unitary leaves the entire normalized state unchanged.

Now impose the unknown-order guarantee. It includes the region where pair 1 is best, so the same fixed map must have this structure. That structure also fixes its action on tuples where pair 2 is better. An interior choice with $`F_2>F_1`$ then gives positive success and output fidelity exactly $`F_1`$, contradicting the required comparison with $`F_2`$. This is [M25](MILESTONES.md#m25) and [Corollary 5](../science/ordered_purification.md#unknown-order-impossibility).

## A complete two-pair example

Take $`d=2`$ and two independent isotropic pairs. Keep pair 1. Measure pair 2 locally in the computational basis and accept only outcomes $`(0,1)`$. Apply

```math
U=\begin{pmatrix}1&0\\0&i\end{pmatrix}
\quad\text{on Alice's retained qubit},\qquad
\overline U=\begin{pmatrix}1&0\\0&-i\end{pmatrix}
\quad\text{on Bob's.}
```

The accepted product Kraus operator has local factors

```math
A=U\otimes\langle0|,
\qquad B=\overline U\otimes\langle1|.
```

After regrouping by pairs, $`K^\dagger K=I_1\otimes|01\rangle\langle01|_2\le I`$. Thus this defines a valid CP trace-nonincreasing success map. The conjugate unitaries fix both $`|00\rangle`$ and $`|11\rangle`$, and hence $`|\Phi_2\rangle`$. By comparison, $`U\otimes U`$ would send $`|\Phi_2\rangle`$ to $`(|00\rangle-|11\rangle)/\sqrt2`$.

The spectator outcome has probability

```math
q(F_2)=\langle01|\omega(F_2)|01\rangle=\frac{1-F_2}{3},
```

because $`|01\rangle`$ is orthogonal to the target. Independence gives

```math
\mathcal E\bigl(\rho_1\otimes\omega(F_2)\bigr)
=q(F_2)(U\otimes\overline U)\rho_1(U\otimes\overline U)^\dagger.
```

For $`\rho_1=\omega(F_1)`$, the unitary leaves the state unchanged. At $`F_1=4/5`$ and $`F_2=7/10`$,

```math
\widetilde\sigma=\frac1{10}\omega(4/5),
\qquad
p=\frac1{10},
\qquad
N=\frac2{25},
\qquad
F_{\rm Bell}(\widetilde\sigma/p)=\frac45.
```

Watrous's corresponding fidelities are $`F_{\rm W}(P,\widetilde\sigma)=\sqrt2/5`$ before normalization and $`F_{\rm W}(P,\widetilde\sigma/p)=2/\sqrt5`$ afterward.

The same map succeeds with probability $`1/30`$ at $`F_1=4/5`$, $`F_2=9/10`$, but still outputs overlap $`4/5`$. It is universally safe when pair 1 is promised best and fails the unknown-order benchmark. At $`F_2=1`$, success vanishes altogether; this is permitted by the theorem. Vanishing on the all-perfect input is different from annihilating the entire support $`\mathcal S_1`$ with arbitrary spectators.

The example instantiates the classified family. The proof is needed to show that every universally safe separable map belongs to that family.

## What the bridge establishes, and where the scope changes

The conclusion combines three different ingredients: independently variable high-fidelity inputs supply a path to the perfect-input boundary; full spectator support and spatial factorization force extraction or annihilation; same-sign leakage rules out every form except conjugate unitaries on the identified best pair.

The [remaining milestones, M26–M30](MILESTONES.md#m26), connect this mechanism to the [worked examples and scope](../science/scope_and_examples.md). Identical-input recurrence can improve fidelity because its promised family does not allow one fidelity to approach one while the others stay fixed. Rank-two noise omits the full-support premise. Correlations between the retained pair and its spectators can change the retained conditional state under spectator postselection. Each changes a specific step of the argument.

The theorem concerns exact conditional nondegradation throughout the specified input family. It does not establish a quantitative approximation bound or an optimal fidelity–success tradeoff. The [interpretation](../science/interpretation.md) gives the operational consequence, and the [verification guide](../verification/README.md) identifies the limited role of finite numerical checks alongside the analytical proof.

[watrous]: https://cs.uwaterloo.ca/~watrous/TQI/
[w1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[w2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[w3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[w6]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf
