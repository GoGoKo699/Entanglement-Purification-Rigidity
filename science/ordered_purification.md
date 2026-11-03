# Ordered purification and the unknown-order obstruction

Use the [model and notation](model.md): $`P`$ is the fixed maximally entangled target, $`R=(I-P)/(d^2-1)`$, $`\omega(F)=FP+(1-F)R`$, and $`\Omega(\boldsymbol F)=\bigotimes_i\omega(F_i)`$. The threshold satisfies $`1/d\le f_\star<1`$. All maps below are nonzero separable completely positive trace-nonincreasing maps from a fixed finite $`n\ge2`$ pairs to one pair, with common local dimension $`d\ge2`$ and no additional shared entanglement.

The result concerns exact nondegradation on the whole promised region, not a typical-source or identical-input guarantee. Its three algebraic ingredients are [Lemmas 2–4](product_branch_rigidity.md).

## Ordered-fidelity rigidity theorem


**Theorem 1.** Suppose that, for every $`F_i\in(f_\star,1)`$ satisfying

```math
F_1\ge \max_{i>1}F_i,
```

the fixed separable success map satisfies

```math
\operatorname{Tr}\!\left[P\mathcal E(\Omega(\boldsymbol F))\right]
\ge F_1\operatorname{Tr}\mathcal E(\Omega(\boldsymbol F)).
\tag{1}
```

Then every nonzero product Kraus operator in any finite separable decomposition of $`\mathcal E`$ has the form

```math
A_r=s_rU_r\otimes\langle a_r|,
\qquad
B_r=t_r\overline{U_r}\otimes\langle b_r|,
\tag{2}
```

where $`U_r`$ is unitary on the first local input system, $`s_r,t_r\ne0`$, and the bras act on the local spectator systems $`2,\ldots,n`$.

Consequently, for every state $`\rho`$ of pair 1 and every spectator state $`\tau`$ independent of that pair,

```math
\mathcal E(\rho\otimes\tau)
=\sum_r q_r(\tau)V_r\rho V_r^\dagger,
\qquad
V_r=U_r\otimes\overline{U_r},
\tag{3}
```

with

```math
q_r(\tau)=|s_rt_r|^2
\langle a_r b_r|\tau|a_r b_r\rangle\ge0.
\tag{4}
```

Whenever $`\sum_rq_r(\tau)>0`$, the accepted output has Bell fidelity exactly $`F(\rho)`$. The acceptance probability depends only on the spectators. Conversely, every nonzero trace-nonincreasing map of the form (2) satisfies (1).

The same conclusion holds if the promise supplies the complete ordering $`F_1\ge F_2\ge\cdots\ge F_n`$, rather than only the identity of a best pair.

## Proof of Theorem 1


Fix one spectator tuple with every fidelity strictly inside $`(f_\star,1)`$, and let

```math
\tau=\bigotimes_{i=2}^n\omega(F_i)>0.
```

All first-pair fidelities sufficiently close to one satisfy the ordering promise. Taking $`F_1\uparrow1`$ in the homogeneous inequality (1) yields

```math
\operatorname{Tr}\!\left[(I-P)\mathcal E(P\otimes\tau)\right]=0.
\tag{15}
```

Each summand in the product-Kraus decomposition is nonnegative. Equivalently,

```math
\left\|(I-P)K_r(P\otimes\tau^{1/2})\right\|_2^2=0
\quad\text{for every }r.
\tag{16}
```

The norm in (16) is the Hilbert–Schmidt norm. Since $`\tau`$ is positive definite, every $`K_r`$ maps $`\mathcal S_1`$ into the output Bell ray. [Lemma 2](product_branch_rigidity.md#product-kraus-extraction) divides the nonzero branches into two classes: extraction branches of the form (5), and branches annihilating $`\mathcal S_1`$.

For an extraction branch, write $`L_r=M_r\otimes N_r`$ for its reciprocal filter and let

```math
w_r=\langle a_rb_r|\tau|a_rb_r\rangle>0,
\qquad
g_r=w_r|\lambda_r|^2,
\qquad
h_r=w_r\operatorname{Tr}(L_rRL_r^\dagger).
```

Its contribution to the accepted Bell numerator on $`\omega(F)\otimes\tau`$ is $`Fg_r`$, and its contribution to the success probability is $`Fg_r+(1-F)h_r`$. Lemma 3 gives $`h_r\ge g_r`$.

For an annihilating branch, put

```math
\sigma_r=K_r(R\otimes\tau)K_r^\dagger,
\qquad
c_r=\operatorname{Tr}(P\sigma_r),
\qquad
z_r=\operatorname{Tr}(\sigma_r).
```

Its Bell numerator and success probability are $`(1-F)c_r`$ and $`(1-F)z_r`$, respectively. Lemma 4 gives $`z_r>c_r`$.

Sum the extraction coefficients to obtain $`g=\sum g_r`$, $`h=\sum h_r`$, and the annihilating coefficients to obtain $`c=\sum c_r`$, $`z=\sum z_r`$. The total numerator and success probability are

```math
N(F)=Fg+(1-F)c,
\qquad
p(F)=Fg+(1-F)(h+z).
\tag{17}
```

For $`F<1`$, the requirement $`N(F)\ge Fp(F)`$ is equivalent to

```math
c+F(g-h-z)\ge0.
\tag{18}
```

Letting $`F\uparrow1`$ gives

```math
(g-h)+(c-z)\ge0.
\tag{19}
```

Both terms on the left are nonpositive. The second is strictly negative if any nonzero annihilating branch is present. Hence no such branch exists, and $`h=g`$. Every extraction weight $`w_r`$ is strictly positive, so each individual extraction branch must attain equality in Lemma 3. This gives exactly the unitary form (2).

For any independent input $`\rho\otimes\tau`$, that form gives (3)–(4). Every $`V_r=U_r\otimes\overline{U_r}`$ fixes $`|\Phi_d\rangle`$, so

```math
\operatorname{Tr}\!\left[P\mathcal E(\rho\otimes\tau)\right]
=F(\rho)\sum_rq_r(\tau),
\qquad
\operatorname{Tr}\mathcal E(\rho\otimes\tau)=\sum_rq_r(\tau).
\tag{20}
```

This proves exact fidelity preservation whenever the protocol succeeds, as well as the converse. For a promise of complete ordering, choose the fixed spectator fidelities strictly ordered. The same limit $`F_1\uparrow1`$ stays within that promise and proves the same Kraus classification. $`\square`$

## Unknown-order impossibility

**Corollary 5.** For every finite $`n,d\ge2`$ and every $`f_\star\in[1/d,1)`$, no nonzero separable success map can satisfy

```math
F\!\left(\frac{\mathcal E(\Omega(\boldsymbol F))}{p(\boldsymbol F)}\right)
\ge\max_iF_i
\tag{21}
```

for every independently variable tuple $`F_i\in(f_\star,1)`$.

**Proof.** Such a map would satisfy Theorem 1 on the subfamily where pair 1 is best. Its Kraus structure would therefore preserve the first pair's fidelity for every independent isotropic tuple, including tuples outside that ordering region. Choose $`F_2>F_1`$. The input is positive definite, so the nonzero map succeeds with positive probability, but its conditional fidelity is $`F_1\lt F_2`$. This contradicts (21). $`\square`$

Since the promised isotropic family is a subset of the full set of high-fidelity states, the impossibility also applies to a guarantee over all independent states above the same fidelity threshold.


## Attribution and interpretation

The universality benchmark, fidelity-ordering variant and perfect-input boundary method come from [Zang et al. (2025)](../references/RELATED_WORK.md#relation-to-the-2025-universal-purification-no-go). The added step is the arbitrary-SEP product-branch classification, including branches that annihilate the perfect-input support. The [scope examples](scope_and_examples.md) show why boundary success, independence and full-rank noise must be handled explicitly. The [interpretation](interpretation.md) connects the proof to the operational question.
