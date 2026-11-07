# From Fisher geometry to a rank threshold

This bridge develops the statistical language needed to read the repository's rank classification. It follows one educational anchor for the foundations, then uses the repository's model and proofs for the fixed-readout question. The central comparison is between the local information present in the input states and the information preserved in one apparatus's complete classical record.

## The selected anchor

Jasminder S. Sidhu and Pieter Kok, **A Geometric Perspective on Quantum Parameter Estimation**, *AVS Quantum Science* **2**, 014701 (2020). [Published article](https://doi.org/10.1116/1.5119961); [arXiv:1907.06628v2](https://arxiv.org/abs/1907.06628v2); [primary PDF](https://arxiv.org/pdf/1907.06628v2).

The section and equation numbers below refer to the preprint revision of 19 September 2019. Page numbers are the printed PDF pages.

| Foundation | Exact source location |
|---|---|
| Statistical models, covariance and classical Fisher information | II.A–D, pp. 3–5; Eqs. (24), (27) |
| Probability geometry | III.A–B, pp. 6–7; Eqs. (39), (41)–(43) |
| Measurement probabilities | IV.A, p. 8; Eq. (53) |
| Product-state information | IV.B, p. 9; Eq. (63) |
| Pure-state and Bures geometry | IV.C, p. 10; Eqs. (77)–(78) |
| SLD, spectral formula and measurement bound | IV.D, pp. 10–11; Eqs. (83), (87)–(88), (93) |
| Matrix information and attainability | V.A–C, pp. 16–19; Eqs. (128), (156), (161) |

## Notation translation

| Quantity | Anchor | Repository |
|---|---|---|
| Outcome law | $`{\rm Pr}(x\mid\theta)`$ | $`q_\theta(x)`$ |
| POVM | $`\Pi(x)\,dx`$ | $`M(dx)=E_x\,d\nu(x)`$ |
| Classical information | $`I(\theta)`$ | $`I_M`$ |
| SLD quantum information | $`I_Q(\theta)`$ | $`J`$ or $`J_\rho(A)`$ |
| State derivative | $`\partial_\theta\rho`$ | $`A`$ |
| SLD | $`L_\theta`$ | $`L`$ |
| Eigenvalues | $`p_j`$ | $`\lambda_j`$ |

The anchor also uses $`J`$ for a parameter-transformation Jacobian. In this repository $`J`$ denotes QFI. The rare eigenvalue $`p`$ in the converse is a state parameter, while $`q_\theta(x)`$ describes an observed outcome.

The derivations below use the conventions in [Model and claims](../science/model.md), including its treatment of zero probabilities and fixed-rank tangents.

## A local path and its classical information

Consider a differentiable path of outcome probabilities $`q_t(x)`$ near $`t=0`$. Write $`q_x=q_0(x)`$ and $`\dot q_x=\partial_tq_t(x)|_{t=0}`$. Normalization gives $`\sum_x\dot q_x=0`$. At positive-probability outcomes the score is

```math
s_x=\frac{\dot q_x}{q_x},
\qquad
\sum_x q_xs_x=0,
\qquad
I=\sum_xq_xs_x^2
=\sum_x\frac{\dot q_x^2}{q_x}.
```

Thus information depends on both the probability distribution and its direction of change. The same distribution can be sensitive to one parameter direction and insensitive to another.

The associated squared local length is

```math
d\ell_C^2=\sum_x\frac{(dq_x)^2}{q_x}=I\,dt^2.
```

The denominator matters. A change of size $`dq_x`$ in a rare outcome contributes more than the same absolute change in a common outcome. This is the feature of Fisher geometry that makes small eigenvalues central to the repository's question.

For several parameters, choose a real direction $`u`$ and a path $`\theta(t)=\theta_0+tu`$. Then $`\dot q_x=\sum_j u_j\partial_jq_\theta(x)`$, and the directional information is $`u^{\mathsf T}Iu`$. An inequality for every such direction is a positive-semidefinite matrix inequality. It controls combinations of parameters as well as individual coordinate axes.

All of these formulas extend to continuous outcomes by replacing sums with integrals against a fixed dominating measure. The [model](../science/model.md#2-what-a-fixed-apparatus-may-do) uses the trace measure of the POVM to make that convention explicit.

## From a state tangent to an observed distribution

A quantum model supplies a state and a tangent,

```math
\rho=\rho_{\theta_0},
\qquad
A=\sum_j u_j\partial_j\rho_{\theta_0}.
```

For the regular fixed-rank paths used here, $`A`$ is Hermitian and traceless, and its kernel-to-kernel block vanishes. This permits changes of the positive eigenvalues and motion of the occupied support. A rank promise supplies the number of occupied directions; it does not supply their orientation.

The SLD solves

```math
2A=\rho L+L\rho.
```

In an eigenbasis of $`\rho`$, this equation gives $`L_{ij}=2A_{ij}/(\lambda_i+\lambda_j)`$ whenever the denominator is positive. Substitution yields

```math
J_\rho(A)
=\mathrm{Tr}(\rho L^2)
=2\sum_{i,j:\lambda_i+\lambda_j\gt0}
\frac{|A_{ij}|^2}{\lambda_i+\lambda_j}.
```

The value assigned to $`L`$ on the kernel does not affect this quantity. A model that creates a new eigenvalue at a boundary requires separate care; the positive theorem concerns two-sided paths within a fixed-rank stratum.

A fixed POVM converts this state path into an ordinary probability path:

```math
q_t(x)=\mathrm{Tr}(E_x\rho_t),
\qquad
\dot q_x=\mathrm{Tr}(E_xA).
```

Consequently, $`J_\rho(A)`$ describes the local state geometry, while $`I_M(\rho;A)`$ describes the geometry after the measurement. Their ratio quantifies how much of that directional information reaches the record. The measurement bound is $`I_M\le J_\rho(A)`$ for one copy.

For a pure state, write a tangent as

```math
\rho=|\psi\rangle\langle\psi|,
\qquad
A=|v\rangle\langle\psi|+|\psi\rangle\langle v|,
\qquad
\langle\psi|v\rangle=0.
```

The same SLD convention gives $`J_\rho(A)=4\langle v|v\rangle`$. This pure-state expression becomes useful after the rank-two antisymmetric branch has been isolated. The [two-copy proof](../science/two-copy-readout.md#a-projective-3-design-information-bound) supplies the randomized-readout bound needed there.

## One apparatus and the copy budget

For a block of $`k`$ independent copies, the state is $`\rho^{\otimes k}`$ and its tangent is

```math
A^{(k)}
=\sum_{i=1}^k
\rho^{\otimes(i-1)}\otimes A\otimes
\rho^{\otimes(k-i)}.
```

Its SLD is the sum of the single-copy SLDs acting on the separate registers. Since $`\mathrm{Tr}(\rho L)=0`$, the cross terms in the square have zero expectation:

```math
L^{(k)}=\sum_{i=1}^kL^{(i)},
\qquad
J_{\rho^{\otimes k}}(A^{(k)})=kJ_\rho(A).
```

A joint measurement can preserve information that a fixed one-copy measurement loses, even though the copies supplied by the source are independent. The benchmark already counts the information in all $`k`$ inputs.

The positive task asks for one apparatus, chosen before the unknown spectrum and support are revealed, such that

```math
I_M(\rho;A)\ge c\,kJ_\rho(A)
```

for every permitted state and tangent. Choosing a different optimal measurement for each state and direction has different quantifiers. The constructive theorem uses a measurement depending only on the Hilbert-space dimension.

After $`N`$ independent repetitions, the full record has information $`NI_M`$ and has consumed $`Nk`$ input copies. The efficiency fraction remains $`I_M/(kJ)`$. Additional copies used for unsuccessful branches or prior calibration cannot be omitted from an account of the experiment.

The converse even allows the apparatus to know the nominal spectrum. When evaluating its local Fisher information, that chosen apparatus is held fixed as the true parameter is varied. Its dependence on the nominal design point is not differentiated.

## Why rank two has a useful symmetry branch

Write the state in an eigenbasis for analysis:

```math
\rho=\lambda_1|1\rangle\langle1|
+\lambda_2|2\rangle\langle2|,
\qquad
\lambda_1+\lambda_2=1.
```

The experiment does not use this basis. It measures the exchange projectors $`P_\pm=(\mathbb 1\pm S)/2`$, where $`S`$ swaps the two registers. Set $`q=\lambda_1\lambda_2`$. The two branch probabilities are

```math
\mathrm{Pr}(-)=q,
\qquad
\mathrm{Pr}(+)=1-q.
```

The antisymmetric branch has the especially simple form

```math
P_-\rho^{\otimes2}P_-
=q\,|1\wedge2\rangle\langle1\wedge2|,
\qquad
|1\wedge2\rangle
=\frac{|12\rangle-|21\rangle}{\sqrt2}.
```

Its normalized state is pure and describes the occupied two-dimensional subspace. That connects a mixed input to the pure-state tangent formula above.

Each attempt starts with two input copies and measures SWAP parity. The subsequent readout and retained record are the same in both branches:

| SWAP-parity branch | Readout on the full pair register | Retained record |
|---|---|---|
| Symmetric | Projective 3-design | Parity flag, setting and outcome |
| Antisymmetric | Projective 3-design | Parity flag, setting and outcome |

There are several kinds of information to retain. With $`A_{11}=a`$, $`A_{22}=-a`$, the one-copy metric separates as

```math
J_\rho(A)
=\frac{a^2}{\lambda_1\lambda_2}
+4|A_{12}|^2
+4\sum_{j\gt2}\left(
\frac{|A_{1j}|^2}{\lambda_1}
+\frac{|A_{2j}|^2}{\lambda_2}
\right).
```

The first term changes the spectrum, the second changes the state within its occupied support, and the last terms move the support into the kernel. Those last directions are why a rank-two state in a large space requires more analysis than a qubit in a known two-dimensional space.

The full [construction](../science/two-copy-readout.md#proof-of-the-uniform-fraction) combines the branch flag with a projective 3-design measurement in both branches. Such a design matches the first three projector moments of uniformly distributed pure states. The moment bound and the component comparison together give

```math
I_M\ge\frac16J_\rho(A)=\frac1{12}J_2,
\qquad J_2=2J_\rho(A).
```

This bridge explains the roles of the ingredients; the linked proof establishes the uniform constant. The smaller eigenvalue may approach zero, and the support remains unknown.

## Why the complete branch record matters

Let $`B`$ be a retained branch flag. At a point with positive branch probabilities $`w_b(t)`$, let $`r_b(x\mid t)`$ be the normalized conditional outcome law. The full law is

```math
q_t(b,x)=w_b(t)r_b(x\mid t).
```

Its score is the sum $`\partial_t\log w_b+\partial_t\log r_b`$. For each branch, $`\sum_x\partial_tr_b(x\mid t)=0`$, so the cross term vanishes when computing the score's second moment. Hence

```math
I_{\rm full}
=\sum_b\frac{(w_b')^2}{w_b}
+\sum_bw_bI_b.
```

For the two SWAP branches this becomes

```math
I_{\rm full}
=\frac{(q')^2}{q(1-q)}
+(1-q)I_+
+qI_-.
```

The first term is information in how often each branch occurs. The other terms weight conditional information by the probability of obtaining the relevant branch. The identity is also the accounting used in the [positive proof](../science/two-copy-readout.md#proof-of-the-uniform-fraction).

In the randomized readout, $`x`$ includes both the sampled setting and the final result. A setting drawn independently of the parameter supplies no information by itself, but retaining it specifies which conditional experiment produced the result.

As a simple check on the flag term, take eigenvalues $`1-t,t`$ with a fixed eigenbasis. Then $`q=t(1-t)`$ and $`q'=1-2t`$. At $`t=1/2`$, the flag has zero local Fisher information, while the pair QFI is $`8`$. This explains why the flag alone cannot establish the theorem. At that point the conditional symmetric record is essential.

## Worked example: the three-copy rank certificate

Consider the converse family with an unknown eigenbasis,

```math
\rho_{\eta,p,U}
=U\,\mathrm{diag}(1-\eta-p,\eta,p)\,U^\dagger,
\qquad
0\lt p\lt\eta\le\frac14.
```

Hold $`\eta`$ and $`U`$ fixed while differentiating $`p`$. The single-copy QFI is

```math
J(p)=\frac1p+\frac1{1-\eta-p}.
```

Use three copies and the binary measurement $`\{P_{\wedge^3},\mathbb 1-P_{\wedge^3}\}`$. In three dimensions the fully antisymmetric subspace is one-dimensional. It is invariant under a simultaneous change of basis, so the outcome law is independent of $`U`$. Its two probabilities are

```math
w(p)=(1-\eta-p)\eta p,
\qquad 1-w(p).
```

This determinant identity is the $`k=3`$ case in [Exact singular coefficient](../science/singular-information.md#2-a-positive-formula-and-small-blocks).

Differentiation and the binary Fisher formula give

```math
w'(p)=\eta(1-\eta-2p),
\qquad
I_{\rm binary}(p)
=\frac{[w'(p)]^2}{w(p)}
+\frac{[w'(p)]^2}{1-w(p)}
=\frac{[w'(p)]^2}{w(p)[1-w(p)]}.
```

Both outcomes are included. Let $`q=\eta(1-\eta)`$. At fixed positive $`\eta`$,

```math
w(p)=qp-\eta p^2,
\qquad
I_{\rm binary}(p)=\frac{q}{p}+O(1),
\qquad
3J(p)=\frac3p+O(1).
```

Therefore

```math
\lim_{p\downarrow0}
\frac{I_{\rm binary}(p)}{3J(p)}
=\frac{\eta(1-\eta)}3.
```

Each record consumes three input copies, including the much more common complementary outcome. After $`N`$ records the cost is $`3N`$ copies, and both informations are multiplied by $`N`$. Conditioning the copy count on obtaining the antisymmetric outcome would change the resource accounting.

The rare outcome does retain a $`1/p`$ divergence. Its coefficient also contains the second weak population $`\eta`$. For example, the limiting fraction is $`0.03`$ at $`\eta=0.1`$ and $`0.0033`$ at $`\eta=0.01`$. These are limits as $`p\downarrow0`$ at the stated fixed $`\eta`$ values.

The [converse and matching bound](../science/singular-information.md#3-why-this-coefficient-is-optimal) establish that this is the optimum worst-eigenbasis leading coefficient for three copies and this spectral tangent. The calculation alone demonstrates what the binary measurement achieves.

## From the example to the finite-block obstruction

For a general fixed block, Schur sectors separate components already present at rank two from components that require a third occupied direction. The three-row components supply the leading rare-eigenvalue information. The technical step in the [all-POVM proof](../science/finite-block-obstruction.md#3-uniform-convergence-over-regular-effects) shows that the other components contribute no leading $`1/p`$ term after averaging over the unknown eigenbasis, uniformly over all measurement effects. That uniformity is needed to cover continuous outcomes and spectrum-dependent choices of apparatus.

For $`a=1-\eta`$ and $`b=\eta`$, the exact surviving coefficient is

```math
\beta_k(\eta)
=\sum_{m=0}^{k-1}
\left[1-\sum_{j=0}^m a^j b^{m-j}\right].
```

The [exact minimax statement](../science/singular-information.md#the-exact-limiting-minimax-value) says

```math
\lim_{p\downarrow0}
\sup_{M\ {\rm independent\ of}\ U}
\inf_U
\frac{I_M(\eta,p,U)}{kJ(p)}
=\frac{\beta_k(\eta)}k.
```

For each fixed finite $`k`$, this fraction tends to zero when $`\eta\downarrow0`$. The order is fixed $`k,\eta`$, then $`p\downarrow0`$, then $`\eta\downarrow0`$. The result does not provide a uniform finite-$`p`$ error term when the block size or second eigenvalue changes.

This obstruction concerns an apparatus that lacks the eigenbasis. Learning that basis from earlier blocks changes the information available to the later apparatus. A small coherent memory maintained through many input copies also changes the coherent-block resource. Both distinctions are developed in [Resource interpretation](../science/interpretation.md#the-coherent-block-is-the-constrained-resource).

## What the information guarantee does and does not imply

On an identifiable tangent space, the matrix comparison $`c\,kJ\preceq I_M\preceq kJ`$ implies

```math
(kJ)^{-1}\preceq I_M^{-1}
\preceq c^{-1}(kJ)^{-1}.
```

This compares the local inverse-information benchmarks. A Cramér–Rao inequality is a lower bound on an estimator's covariance under its stated regularity and unbiasedness conditions. The information comparison alone does not construct an estimator with a matching finite-sample covariance upper bound. Multiparameter attainability also requires care; preserving a fraction of the SLD matrix is not a claim of simultaneous exact saturation.

The loss function matters as well. For the displayed diagonal family, changing $`p`$ by $`\delta p`$ has half-trace distance $`|\delta p|`$, while the local SLD squared length includes $`(\delta p)^2/p`$. A small absolute reconstruction error can therefore coexist with poor relative local information in a rare component. The [interpretation](../science/interpretation.md#local-sensitivity-and-statistical-estimation) and [research comparisons](../references/RELATED_WORK.md) make that distinction explicit.

## Where the anchor ends and the project begins

The anchor supplies the estimation geometry. The repository supplies the fixed-apparatus quantifiers, regular rank-stratum conventions, finite projective-design bound, unknown-support two-copy analysis, arbitrary-POVM Schur-sector reduction, and exact singular coefficient. Those are separate arguments with research attribution in [Related work](../references/RELATED_WORK.md).

The [30 milestones](MILESTONES.md) organize these foundations and project-specific steps. The [learning routes](README.md) connect them to the authoritative theorem and proof pages.
