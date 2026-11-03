# Related work and precise scope

## Result studied here

Let

```math
P_d=|\Phi_d\rangle\langle\Phi_d|,\qquad
|\Phi_d\rangle=d^{-1/2}\sum_{a=0}^{d-1}|aa\rangle,\qquad
\omega_d(F)=F P_d+(1-F)\frac{I-P_d}{d^2-1}.
```

Fix finite integers $`d,n\geq2`$, a threshold $`f_*\in[1/d,1)`$, and a nonzero separable, completely positive, trace-nonincreasing success map from $`n`$ input pairs to one output pair, each with local dimension $`d`$. The map is fixed independently of the input fidelities, and no additional shared entangled resource is supplied.

The ordered-input rigidity statement assumes that, for every independent input $`\bigotimes_i\omega_d(F_i)`$ with $`F_i\in(f_*,1)`$ and $`F_1\geq\max_{i>1}F_i`$, the conditional output fidelity is at least $`F_1`$. It concludes that every nonzero product Kraus operator factors into local spectator bras and conjugate local unitaries on pair 1, up to a scalar. Consequently, for any input $`\rho_1\otimes\tau`$, the accepted output is a mixture of $`U\otimes\overline U`$ conjugations of $`\rho_1`$, with weights depending only on $`\tau`$. Its Bell fidelity equals that of $`\rho_1`$. The output state itself need not equal $`\rho_1`$.

Full ordering information gives the same conclusion. If no ordering information is supplied, universality over every fidelity tuple would imply this rigidity for pair 1 and then fail whenever another pair has strictly greater fidelity. Thus no nonzero SEP success map universally attains $`\max_iF_i`$, for any fixed finite $`n\geq2`$, even with an arbitrarily high fidelity floor. No lower bound on the success probability is assumed.

## Relation to the 2025 universal-purification no-go

The universality task and its ordered-fidelity variant originate with Zang et al. [1]. The relevant comparisons are:

| Prior result and source location | Established scope | Relation to the present result |
|---|---|---|
| Theorem 3; Supplemental Material §II.D | No universal LOCC protocol for all entangled two-qubit inputs; the proof excludes SEP already on all entangled isotropic inputs. | The present obstruction persists after excluding every input below any chosen $`f_*<1`$, and holds for all finite $`d`$. |
| Proposition 10; Supplemental Material §III.D, Proposition 39 | Given fidelity ordering, universal bilocal Clifford EPPs on complete Bell-diagonal state sets preserve the best input fidelity. | The present theorem proves a product-Kraus structural classification for arbitrary unassisted SEP maps on the high-fidelity isotropic family. |
| Theorem 11 and its preceding assistance model | The Clifford no-go and ordered triviality survive assistance by pure Bell pairs that must be returned unchanged. | The present theorem removes the Clifford restriction without supplied entanglement; it does not establish arbitrary-SEP catalytic rigidity. |
| Main-text Discussion, final research-directions paragraphs | Higher-threshold universal SEP/LOCC purification beyond bilocal Clifford circuits is left open. | The arbitrary-SEP high-fidelity no-go resolves this question for independent isotropic inputs. |

“Complete Bell-diagonal state set” is Definition 5 of [1]. Such sets need not contain an open isotropic interval. The present theorem therefore does not subsume every input-set extension in that paper.

The structural proof uses the limit in which the promised best pair becomes perfect while the spectators remain full rank. Positivity constrains each successful product Kraus operator separately. The argument then excludes both nonunitary reciprocal filters and branches whose success vanishes on that perfect-pair boundary. This addresses the possibility of very rare successful outcomes without imposing a success floor.

## The open question in the 2026 dissertation

Zang's dissertation [2], Chapter 5, **printed pages 56–57**, reiterates that the earlier results leave open universal LOCC purification at a higher minimum fidelity using operations beyond bilocal Clifford protocols. It specifically identifies the search for higher-threshold separable universal EPPs as a next step. The official deposit is dated **August 2026, version v1**. This is a direct statement of the gap addressed here, rather than an inference from the 2025 abstract alone.

## Guaranteed improvement with different comparators

Zang et al. [3] study the canonical two-to-one recurrence protocol with nonidentical Bell-diagonal inputs and memory decoherence. Their **§III.B and Appendix B.3, Proposition B.1**, compare Werner-input output fidelity with

```math
F_{\mathrm{baseline}}
=\lambda\max(F_1,F_2)+(1-\lambda)\min(F_1,F_2).
```

The average-input comparator has a guarantee throughout the entangled Werner regime. Larger weights on the better input are possible after imposing a higher fidelity floor; the nontrivial high-fidelity guarantees in Proposition B.1 have $`\lambda<2/3`$, whereas the best-input comparator would require $`\lambda=1`$. Their positive results for suitable rank-two Bell-diagonal families further illustrate the relevance of the input-state set. These statements concern useful, weaker performance guarantees and do not imply exact domination of the best input for arbitrary heterogeneous full-rank inputs.

## Shared randomness and accumulated inputs

Zang et al. [4] accumulate $`m`$ rounds from $`n`$ heterogeneous Werner sources and shuffle the pairs before grouping them for a fixed EPP. Their **Operational model, Eq. (1), p. 1**, uses a uniformly random source-label permutation as its non-accumulating baseline. **Theorem 4, p. 4**, guarantees nondecreasing success probability and success-weighted Bell fidelity $`p_{\mathrm{succ}}F_{\mathrm{succ}}`$ for any finite $`m\geq1`$, any fixed $`n`$-to-one biCEP, and visibilities $`0\leq w_i\leq1`$ (equivalently $`F_i\in[1/4,1]`$). Both quantities are monotone in $`m`$. **Proposition 3, p. 2**, additionally guarantees nondecreasing normalized fidelity for the two-source CNOT example with $`F_i\in[1/2,1]`$. The **Conclusion, p. 5**, excludes this stronger guarantee for general biCEPs.

These guarantees compare protocols against a source-symmetrized baseline and use repeated source outputs. They do not impose dominance over the best individual input. The rigidity theorem instead requires an exact best-input guarantee for independently variable fidelities in a fixed finite batch.

## Blind distributed purification

Zhao et al. [5] formulate a different universality problem. A fixed LOCC map receives identical copies of $`\mathcal N(\psi)`$, where the target pure state $`\psi`$ is unknown within a specified set. Their **Definition 1, Eq. (2), Theorems 1–2, and Corollary 3** establish two-to-one blind-purification obstructions under depolarizing noise for all pure two-qubit states and for Bell-state sets. They also construct targeted purification for a known pure state.

Here the target $`\Phi_d`$ is fixed and known, while the fidelities of different pairs are independently unknown. The present result permits arbitrary finite batch size and local dimension. The blind-purification obstruction therefore concerns different missing information and does not imply the ordered heterogeneous-input rigidity statement.

## Boundaries of the claim

The guarantee is exact and must hold throughout an open fidelity region extending arbitrarily close to one. The theorem makes no quantitative claim about approximate universality, average-case performance, a fidelity-versus-success tradeoff, or a number of copies that adapts to supplied exact source parameters. It does not prohibit purification of identical inputs or restricted rank-deficient noise families. Pair 1 must be independent of the spectators for the stated fidelity-preservation consequence: conditioning on correlated spectators can alter its marginal fidelity. No arbitrary entangled-catalyst extension is asserted.

The comparison above identifies a specific theorem-level strengthening and explicit open-question closure. It is not a claim that every form of universal purification, or every prior result bearing that name, has been classified.

## Primary references and versions

1. **Allen Zang, Xinan Chen, Eric Chitambar, Martin Suchara, and Tian Zhong**, *No-Go Theorems for Universal Entanglement Purification*, Physical Review Letters **134**, 190803 (2025). Published May 13, 2025. [Publisher and DOI](https://doi.org/10.1103/PhysRevLett.134.190803); [arXiv:2407.21760v2, May 6, 2025](https://arxiv.org/abs/2407.21760v2); [full text and supplement](https://arxiv.org/html/2407.21760v2).

2. **Yinxing Zang**, *Entanglement Purification Beyond Identical Input*, PhD dissertation, University of Chicago (August 2026), deposited version v1. [Official record](https://knowledge.uchicago.edu/records/9w5q8-knt65); [official PDF](https://knowledge.uchicago.edu/records/9w5q8-knt65/files/PhD_Dissertation_ZANG-2607.pdf?download=1). Location: Chapter 5, Outlook, printed pp. 56–57.

3. **Allen Zang, Xin-An Chen, Eric Chitambar, Martin Suchara, and Tian Zhong**, *Entanglement Purification in Quantum Networks: Guaranteed Improvement and Optimal Time*, [arXiv:2505.02286v1, May 4, 2025](https://arxiv.org/abs/2505.02286v1); [full text](https://arxiv.org/html/2505.02286v1). Locations: §III, especially §III.B; Appendix B.3, Proposition B.1. The source is cited here as the verified preprint version.

4. **Allen Zang, Bikun Li, Xinan Chen, Eric Chitambar, Liang Jiang, Martin Suchara, and Tian Zhong**, *Enhancing Entanglement Purification with Shared Randomness*, [arXiv:2607.21555v1, July 23, 2026](https://arxiv.org/abs/2607.21555v1); [versioned PDF](https://arxiv.org/pdf/2607.21555v1). Locations: Operational model and Eq. (1); Proposition 3; Theorem 4; Conclusion. The PDF's manuscript date is July 24, 2026; its arXiv version stamp is July 23. Comparison uses that original PDF.

5. **Benchi Zhao, Yu-Ao Chen, Xuanqiang Zhao, Chengkai Zhu, Giulio Chiribella, and Xin Wang**, *Power and Limitations of Distributed Quantum State Purification*, Physical Review Letters **136**, 090203 (2026). Published March 4, 2026. [Publisher and DOI](https://doi.org/10.1103/3bb1-pmtp); [arXiv:2509.08691v2, March 9, 2026](https://arxiv.org/abs/2509.08691v2); [full text](https://arxiv.org/html/2509.08691v2). Locations: Definition 1 and Eq. (2); Theorems 1–2; Corollary 3; the paragraph following Theorem 1 explicitly distinguishing two copies from arbitrary batch size.
