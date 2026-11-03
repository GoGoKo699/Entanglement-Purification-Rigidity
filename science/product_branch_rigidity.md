# Product-branch rigidity

The [ordered-fidelity theorem](ordered_purification.md) follows from three facts about a single product Kraus operator. The first converts a perfect-pair image constraint into factorization. The second determines the fidelity cost of the resulting filters. The third handles product branches that vanish on the perfect-pair input support, including branches with entangled outputs.

Throughout, use the [model's fixed bases and normalized noise state](model.md): $`P=|\Phi_d\rangle\langle\Phi_d|`$ and $`R=(I-P)/(d^2-1)`$. A local operator maps all local inputs to one $`d`$-dimensional output. Spectator tensor factors are regrouped into Alice's and Bob's laboratories as needed.

## Product-Kraus extraction


**Lemma 2.** Let $`K=A\otimes B`$ be a product operator from the input laboratories to the two output systems. Write

```math
\mathcal S_1=\mathrm{span}\{|\Phi_d\rangle_1\}\otimes\mathcal H_{\rm rest}.
```

If $`K\mathcal S_1\subseteq\mathrm{span}\{|\Phi_d\rangle_{\rm out}\}`$, then either $`K\mathcal S_1=\{0\}`$, or

```math
A=M\otimes\langle a|,
\qquad
B=N\otimes\langle b|,
\qquad
MN^{\mathrm{T}}=\lambda I_d,
\qquad\text{(5)}
```

for invertible $`M,N`$ and a scalar $`\lambda\ne0`$.

**Proof.** For local spectator basis vectors $`u,v`$, define the square slices

```math
A_u=A(I_{A_1}\otimes|u\rangle),
\qquad
B_v=B(I_{B_1}\otimes|v\rangle).
```

Use vectorization $`|X\rangle\!\rangle=\sum_{jk}X_{jk}|j\rangle|k\rangle`$. Then

```math
(A_u\otimes B_v)|\Phi_d\rangle
=\frac{1}{\sqrt d}|A_uB_v^{\mathrm{T}}\rangle\!\rangle.
```

The assumed image condition is therefore equivalent to

```math
A_uB_v^{\mathrm{T}}=\lambda_{uv}I_d
\quad\text{for all }u,v.
\qquad\text{(6)}
```

If every $`\lambda_{uv}`$ is zero, $`K`$ annihilates $`\mathcal S_1`$, because spectator product vectors span its spectator factor. Otherwise choose $`u_0,v_0`$ with $`\lambda_{u_0v_0}\ne0`$. Both $`A_{u_0}`$ and $`B_{v_0}`$ are invertible. Holding $`v_0`$ fixed in (6) makes every $`A_u`$ proportional to $`A_{u_0}`$; holding $`u_0`$ fixed makes every $`B_v`$ proportional to $`B_{v_0}`$. The proportionality coefficients define the two spectator bras, giving (5). $`\square`$

## Reciprocal local filters

**Lemma 3.** Suppose $`MN^{\mathrm{T}}=\lambda I_d`$, with $`\lambda\ne0`$, and let $`L=M\otimes N`$. Then

```math
L|\Phi_d\rangle=\lambda|\Phi_d\rangle,
\qquad
L^\dagger|\Phi_d\rangle=\overline\lambda|\Phi_d\rangle.
\qquad\text{(7)}
```

Furthermore,

```math
\mathrm{Tr}(PLRL^\dagger)=0,
```

```math
\mathrm{Tr}(LRL^\dagger)
=\frac{\mathrm{Tr}(M^\dagger M)\mathrm{Tr}(N^\dagger N)-|\lambda|^2}{d^2-1}
\ge |\lambda|^2.
\qquad\text{(8)}
```

Equality in the last inequality holds precisely when $`M=sU`$ and $`N=t\overline U`$ for a unitary $`U`$ and nonzero scalars $`s,t`$.

**Proof.** The first identity in (7) follows by vectorization. Since $`N=\lambda M^{-\mathrm{T}}`$, one also has $`M^\dagger\overline N=\overline\lambda I`$, which proves the second identity. This second identity is necessary: preserving the Bell vector on the right alone would not, for a general operator, determine the Bell numerator of the noise component. Here it gives

```math
\langle\Phi_d|LRL^\dagger|\Phi_d\rangle
=|\lambda|^2\langle\Phi_d|R|\Phi_d\rangle=0.
```

The trace formula follows from $`R=(I-P)/(d^2-1)`$. If $`x_1,\ldots,x_d>0`$ are the squared singular values of $`M`$, then

```math
\mathrm{Tr}(M^\dagger M)\mathrm{Tr}(N^\dagger N)
=|\lambda|^2\left(\sum_jx_j\right)\left(\sum_jx_j^{-1}\right)
\ge d^2|\lambda|^2.
\qquad\text{(9)}
```

Cauchy–Schwarz is an equality exactly when all $`x_j`$ are equal. This means $`M=sU`$, and (5) then implies $`N=t\overline U`$. $`\square`$

For reference, the conditional fidelity produced by this filter on an isotropic input is

```math
\frac{F}{F+(1-F)(\chi-1)/(d^2-1)}\le F,
```

```math
\chi=\frac{\mathrm{Tr}(M^\dagger M)\mathrm{Tr}(N^\dagger N)}{|\lambda|^2}\ge d^2.
\qquad\text{(10)}
```

Thus a reciprocal filter that preserves the perfect target cannot improve the isotropic input fidelity.

## Strict leakage from an annihilating branch

**Lemma 4.** Let $`\tau>0`$ be any spectator state, possibly entangled between the laboratories. If a nonzero product operator $`K=A\otimes B`$ annihilates $`\mathcal S_1`$, then

```math
\mathrm{Tr}\!\left[(I-P)K(R\otimes\tau)K^\dagger\right]>0.
\qquad\text{(11)}
```

**Proof.** Choose $`\mu>0`$ such that $`\tau\ge\mu I`$. Annihilation of $`\mathcal S_1`$ means $`K(P\otimes I)=0`$. Positivity therefore gives

```math
K(R\otimes\tau)K^\dagger
\ge\frac{\mu}{d^2-1}K[(I-P)\otimes I]K^\dagger
=\frac{\mu}{d^2-1}KK^\dagger.
\qquad\text{(12)}
```

For positive $`X,Y`$ on the two output systems,

```math
\mathrm{Tr}[P(X\otimes Y)]
=\frac{1}{d}\mathrm{Tr}(XY^{\mathrm{T}})
\le\frac{1}{d}\mathrm{Tr}(X)\mathrm{Tr}(Y).
\qquad\text{(13)}
```

Apply this to $`KK^\dagger=AA^\dagger\otimes BB^\dagger`$. Equations (12)–(13) imply the explicit strict bound

```math
\mathrm{Tr}\!\left[(I-P)K(R\otimes\tau)K^\dagger\right]
\ge\frac{\mu}{d^2-1}\left(1-\frac1d\right)\mathrm{Tr}(KK^\dagger)>0.
\qquad\text{(14)}
```

The final inequality uses $`d\ge2`$ and $`K\ne0`$. The argument does not assume that the spectators or the branch output are separable. $`\square`$


These are branchwise identities and inequalities. They do not assume that the protocol succeeds at a perfect boundary input, or that an annihilating branch has a separable output. The [ordered proof](ordered_purification.md#proof-of-theorem-1) supplies the positivity argument that makes them apply to every branch of a universally nondegrading success map.
