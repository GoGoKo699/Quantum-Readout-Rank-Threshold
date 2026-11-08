# Exact Haar pair readout near a shrinking occupied eigenvalue

The [finite-design construction](two-copy-readout.md) retains at least $`1/12`$ of the two-copy SLD information in every rank-two tangent. That constant is a certificate, rather than the exact information of the apparatus. This page computes a particular continuous apparatus exactly enough to compare it with fully counted adaptive single-copy measurements.

For a rank-two qutrit approaching a pure state, parity followed by Haar readout has a worst-direction fraction strictly greater than $`1/4`$ for all sufficiently small positive second eigenvalues. It approaches $`1/4`$ from above. Every protocol measuring fresh copies separately, with arbitrary classical adaptation and all calibration records counted, has full-model fraction at most $`1/4`$. The comparison concerns local Fisher information. It neither orders finite-sample risks nor determines a universal calibration crossover.

The sister repository [Calibrated Quantum Readout](https://github.com/GoGoKo699/Calibrated-Quantum-Readout) owns the calibrated $`1/4`$ optimum and the [paid-calibration account](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/main/science/paid-calibration.md): complete pilot records, strong and weak eigenvector errors, and the scope of geometric calibration costs. The exact Haar calculation has its authoritative home here. The parity and design primitives, support-information budget and adaptive Fisher chain rule are inherited ingredients; see [related work](../references/RELATED_WORK.md#calibration-and-the-exact-haar-comparison).

## State, tangent and counted fraction

Fix

```math
\rho_b=\mathrm{diag}(a,b,0),
\qquad a=1-b,\qquad 0\lt b\lt 1/2,
\qquad q=ab.
```

Write a general regular rank-two tangent as

```math
A=\begin{pmatrix}
-v&z&u\\
\overline z&v&w\\
\overline u&\overline w&0
\end{pmatrix},
\qquad v\in\mathbb R,\quad z,u,w\in\mathbb C.
```

These seven real coordinates change the occupied probabilities, create occupied coherences, and move either occupied vector into the empty level. The one-copy SLD information is

```math
J_{\rho_b}(A)
=\frac{v^2}{ab}+4|z|^2+\frac{4|u|^2}{a}
+\frac{4|w|^2}{b}.
```

The pair information is $`J_2=2J`$. For even total input budget $`N`$, $`N/2`$ independent pair records have

```math
I_{\rm total}=\frac N2 I_{\rm pair},
\qquad
c_H(b)=\lambda_{\min}\!\left[(2J)^{-1/2}
I_{\rm pair}(2J)^{-1/2}\right].
```

Thus $`c_H`$ is already a fraction of all consumed copies' QFI. Every pair is measured, including both parity outcomes. All statements take the limit through $`b\gt0`$ on the rank-two tangent stratum, not on the different rank-one tangent space at $`b=0`$.

## The continuous apparatus and its branch information

Measure $`P_\pm=(\mathbb I\pm S)/2`$, where $`S`$ swaps the inputs. In either branch, measure the continuous rank-one Haar POVM on the full pair space of dimension $`D=9`$:

```math
E(d\psi)=D|\psi\rangle\langle\psi|\,d\mu_H(\psi).
```

Here $`\mu_H`$ is normalized Haar measure. The complete outcome includes the parity sign and the Haar outcome. This is an exact projective 3-design, so it is a valid instance of the general measurement model. It is a distinct implementation from a finite Clifford ensemble. No efficient finite circuit or sharp finite-design constant follows from this calculation.

For a subnormalized branch state $`\sigma`$ and its derivative $`B`$, which need not be traceless, the full contribution from that branch is

```math
F_H(\sigma;B)
=D\mathbb E_H\frac{\langle\psi|B|\psi\rangle^2}
{\langle\psi|\sigma|\psi\rangle}
=\mathbb E\frac{(Z^\dagger BZ)^2}{Z^\dagger\sigma Z}.
```

The entries of $`Z`$ are independent standard complex Gaussians. To obtain the equality, write $`Z=R\psi`$: its direction is Haar and independent of $`R`$, while $`\mathbb E R^2=D`$. The quotient is homogeneous of degree two in $`Z`$. Its diagonal part includes any branch-probability derivative, so no separate parity term should be added after summing these subnormalized contributions.

Let $`X_i=|Z_i|^2`$, independent exponentials of mean one. Phase averaging gives $`2|B_{ij}|^2\mathbb E[X_iX_j/(\sum_\ell p_\ell X_\ell)]`$ for an off-diagonal derivative between occupied eigenvalues $`p_i,p_j`$. If $`j`$ lies in the kernel of $`\sigma`$, independence removes $`X_j`$ from this expectation. Cross terms between distinct unordered matrix entries vanish. A diagonal derivative instead contributes the expectation of its entire squared diagonal linear form, including its cross terms.

## Four exact tangent-class fractions

In the symmetric branch the nonzero eigenvalues are $`a^2,ab,b^2`$ on $`|11\rangle,|12;+\rangle,|22\rangle`$. Define

```math
P=a^2X_1+abX_2+b^2X_3,
\qquad
g_i=\mathbb E\frac{X_i}{P},
\qquad
h_{ij}=\mathbb E\frac{X_iX_j}{P}.
```

The antisymmetric branch is $`ab|1\wedge2\rangle\langle1\wedge2|`$. For a normalized pure state with vector derivative perpendicular to its state vector, Haar FI is exactly half its SLD information. This follows from the same Gaussian identity: the off-diagonal derivative is weighted by $`2\mathbb E X_j=2`$, while pure-state QFI is four times the squared derivative norm.

**Weak occupied-null motion.** For $`A_{23}=w`$, the antisymmetric contribution is $`2(a/b)|w|^2`$. In the symmetric branch, the derivative connects $`|12;+\rangle`$ to $`|13;+\rangle`$ with entry $`aw`$ and $`|22\rangle`$ to $`|23;+\rangle`$ with entry $`\sqrt2bw`$. Therefore

```math
I_-=\frac{2a}{b}|w|^2,
\qquad I_+=2a^2|w|^2g_2+4b^2|w|^2g_3,
\qquad
r_w=\frac a4+\frac{ba^2}{4}g_2+\frac{b^3}{2}g_3.
```

The large conditional support sensitivity has already been multiplied by the rare antisymmetric probability $`ab`$. There is no successful-shot normalization.

**Strong occupied-null motion.** For $`A_{13}=u`$, the antisymmetric term is $`2(b/a)|u|^2`$, and the symmetric entries give

```math
I_+=4a^2|u|^2g_1+2b^2|u|^2g_2,
\qquad
r_u=\frac a8\left(\frac{2b}{a}+4a^2g_1+2b^2g_2\right).
```

**Occupied coherence.** For $`A_{12}=z`$, the antisymmetric state and its probability do not change. The symmetric entries are $`\sqrt2az`$ and $`\sqrt2bz`$ between the three occupied branch eigenvectors. Consequently

```math
I_+=4a^2|z|^2h_{12}+4b^2|z|^2h_{23},
\qquad
r_z=\frac{a^2h_{12}+b^2h_{23}}2.
```

**Occupied probabilities.** For $`A=\mathrm{diag}(-v,v,0)`$, the antisymmetric probability derivative is $`(a-b)v`$. The symmetric diagonal derivative is $`v(-2a,a-b,2b)`$. Put

```math
K=\mathbb E\frac{[-2aX_1+(a-b)X_2+2bX_3]^2}{P}.
```

Then

```math
I_-=\frac{(a-b)^2v^2}{ab},
\qquad I_+=v^2K,
\qquad r_v=\frac{(a-b)^2+abK}{2}.
```

Both subnormalized branches are included. In particular, $`I_-`$ alone is not the information of a free conditional antisymmetric input.

## Limits of the full seven-dimensional matrix

The apparatus is covariant under $`U\otimes U`$. At the diagonal state, its invariance under diagonal phase unitaries separates the real population direction and the three distinct complex tangent spaces $`12,13,23`$. Each complex space rotates with a different phase character. Hence FI has no cross terms between the four classes and is scalar within each real two-dimensional coherence class. The full normalized eigenvalues are $`r_v,r_z,r_z,r_u,r_u,r_w,r_w`$.

The limits can be justified without interchanging a divergent integral and a limit. First, $`X_1/P\le1/a^2`$, so dominated convergence gives $`g_1\to1`$. Dropping $`b^2X_3`$ from the denominator yields

```math
g_2\le \frac1{a^2}f(b/a),
\qquad
f(r)=\frac{r-1-\log r}{(r-1)^2},
\qquad
g_3\le\frac{\log(a/b)}{a(a-b)}.
```

These elementary two-exponential integrals show $`g_2,g_3=O(\log(1/b))`$. Also, $`X_1X_2/P\le X_2/a^2`$ gives $`h_{12}\to1`$, and $`h_{23}\le1/(ab)`$. Thus $`r_u,r_z\to1/2`$ and $`r_w\to1/4`$.

For the radial class, the three-square inequality bounds $`K`$ by three diagonal expectations. The $`X_1^2/P`$ term is bounded by $`X_1/a^2`$. The $`X_2^2/P`$ term is $`O(\log(1/b))`$ after dropping $`b^2X_3`$ and integrating $`X_1`$; the resulting logarithm is integrable against $`X_2^2e^{-X_2}`$. Similarly, independence and the two-exponential inverse-denominator integral bound $`\mathbb E[X_3^2/P]=O(\log(1/b))`$. Therefore $`K=O(\log(1/b))`$ and $`r_v\to1/2`$.

| Tangent class | Fraction of pair QFI as $`b\downarrow0`$ |
|---|---:|
| Occupied probabilities | $`1/2`$ |
| Occupied coherence, both quadratures | $`1/2`$ |
| Strong occupied-null motion, both quadratures | $`1/2`$ |
| Weak occupied-null motion, both quadratures | $`1/4`$ |

It follows that $`c_H(b)\to1/4`$. This limit is for the full tangent matrix, rather than one favorable diagonal FI entry.

## Strict comparison with adaptive single-copy readout

The weak coefficient satisfies the exact identity

```math
r_w-\frac14
=\frac b4\left(a^2g_2+2b^2g_3-1\right).
```

As $`b\downarrow0`$, the nonnegative integrand $`X_2/P`$ tends almost surely to $`X_2/X_1`$. Its limiting mean is infinite, since the independent exponential $`X_1`$ has infinite inverse mean. Fatou's lemma therefore gives $`g_2\to\infty`$. The parenthesis is positive for every sufficiently small positive $`b`$. The other three class fractions tend to $`1/2`$, so there exists $`b_0\gt0`$ such that

```math
\boxed{c_H(b)\gt\frac14\quad\text{for every }0\lt b\lt b_0,
\qquad \lim_{b\downarrow0}c_H(b)=\frac14.}
```

The opposing single-copy ceiling applies to the complete adaptive record. At a fixed true state, let $`\mathcal C`$ be the four-dimensional support-null tangent subspace. Every one-copy POVM obeys the inherited [support-information budget](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/main/science/optimality.md#information-budget-for-support-rotations), $`\mathrm{tr}(J_{\mathcal C}^{-1}I_{\mathcal C})\le1`$. Positivity gives its integrand directly: for an effect density $`E`$ and probability $`p=aE_{11}+bE_{22}`$,

```math
\frac{a|E_{13}|^2+b|E_{23}|^2}{p}\le E_{33}.
```

Completeness integrates $`E_{33}`$ to one. At $`p=0`$ the numerator also vanishes under the ordinary score convention. Now condition on each complete classical history: the next apparatus is a fixed one-copy POVM. The [adaptive Fisher chain rule](../references/RELATED_WORK.md#nz26) gives

```math
\mathrm{tr}\left(J_{\mathcal C}^{-1}I_{{\rm total},\mathcal C}\right)
\le N,
\qquad
I_{\rm total}\succeq cNJ\ \Longrightarrow\ 4cN\le N.
```

Thus every classically adaptive single-copy protocol, including all pilot copies, has $`c\le1/4`$. No coherent memory may join different copies in this comparison. For every even $`N`$, repeated Haar pairs have fraction $`c_H(b)`$ and strictly exceed that ceiling for $`0\lt b\lt b_0`$. The claim holds even against a single-copy experiment supplied the nominal basis; it does not depend on proving an optimal basis-learning cost.

The [paid-calibration analysis](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/main/science/paid-calibration.md) makes the complementary point: strong and weak basis errors differ, and an exact pilot must be charged through $`I_Y+(N-m)\mathbb E I_{M_Y}`$. A calibration MSE, the ideal $`1/4`$ optimum, and the conservative finite-design $`1/12`$ certificate do not determine an actual crossover.

## Reproduction and limits

[verify_haar_pair.py](../verification/verify_haar_pair.py) evaluates these exact expectations through deterministic 35-digit Laplace integrals. It checks the symmetric equal-spectrum case, all four tangent classes and near-boundary limits. The [verification guide](../verification/README.md#exact-continuous-haar-comparison) records dependencies and numerical scope. The eventual strict inequality is proved by Fatou's lemma and the other class limits, not by sampled numerical minima.

No quantitative value of $`b_0`$, all-spectrum dominance, finite-Clifford $`1/4`$ guarantee or optimal pair constant is claimed. The apparatus here has continuous Haar outcomes. The separate finite-design theorem and circuit implementation remain valid at their stated $`1/12`$ guarantee. Neither local matrix comparison by itself provides a uniform estimator, finite-sample risk ordering, efficient classical inference or robustness to physical gate and calibration errors.
