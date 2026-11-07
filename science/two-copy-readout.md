# Two-copy readout for an unknown rank-two state

A processor receives two identical copies of a state whose support and eigenvalues are unknown. It first measures whether the pair is symmetric or antisymmetric under exchange. In either branch it applies the same projective 3-design readout to the full two-copy register, recording the exchange flag, random setting, and final outcome. Every input pair produces a record, and every pair is charged to the copy cost.

This measurement preserves at least one twelfth of the two-copy SLD quantum Fisher information in every regular rank-two tangent direction. The fraction is independent of the ambient dimension and of the smaller positive eigenvalue. On qubit registers the measurement uses a SWAP test and random Clifford gates, with a gate count polynomial in the number of input qubits.

The symmetry sectors and randomized-measurement primitives are established tools. Two-copy Fisher-symmetric measurements and Slater-determinant effects are studied in [ZH18](../references/RELATED_WORK.md#zh18); the projective 3-design framework and third-moment method are developed for multiparameter metrology in [ZC26](../references/RELATED_WORK.md#zc26). The statement proved here controls all tangent directions of an unknown, possibly ill-conditioned, two-dimensional support in an arbitrary ambient space. The [related-work comparison](../references/RELATED_WORK.md) specifies that distinction and the associated attribution.

## Statistical model and information convention

Let $`\rho`$ be a density matrix on $`\mathbb C^d`$. A regular rank-two tangent is a Hermitian derivative $`A=\partial_t\rho_t|_{t=0}`$ along a differentiable path whose rank is two in a neighborhood of zero. In particular,

```math
\mathrm{Tr}A=0,\qquad
P_{\ker\rho}A P_{\ker\rho}=0.
```

The support may move with the parameter. We impose no lower bound on either positive eigenvalue.

For a POVM with outcome probability density $`p_t(y)`$, the classical Fisher information in the direction $`A`$ is

```math
I_{\mathcal M}(\rho;A)
=\int_{p_0(y)\gt 0}\frac{[\partial_t p_t(y)|_{t=0}]^2}{p_0(y)}\,dy.
```

The notation also covers discrete outcomes, for which the integral is a sum. A zero-probability outcome with zero first derivative contributes zero. This is the ordinary local Fisher information at the specified state, rather than a limit taken through a rank-changing model.

For $`\rho=\sum_i\lambda_i|i\rangle\langle i|`$, the SLD quantum Fisher information is

```math
J_\rho(A)=
2\sum_{i,j:\lambda_i+\lambda_j\gt 0}
\frac{|A_{ij}|^2}{\lambda_i+\lambda_j}.
```

The derivative of the two-copy state is $`A\otimes\rho+\rho\otimes A`$, and its QFI is additive:

```math
J_2(\rho;A)=2J_\rho(A).
```

For a multiparameter model, the scalar expressions are evaluated on every real linear combination of its parameter derivatives. A scalar inequality holding for every such tangent is equivalent to the corresponding positive-semidefinite matrix inequality.

## Measurement and theorem

Let $`S`$ exchange the two copies and set $`P_\pm=(\mathbb I\pm S)/2`$. Fix a finite projective 3-design on a Hilbert space containing the two-copy register. A projective 3-design is an ensemble of unit vectors whose first three projector moments equal the Haar moments. Its associated rank-one POVM is defined in the next section.

The measurement $`\mathcal M_d`$ has two steps:

1. Measure $`\{P_+,P_-\}`$ and retain the sign.
2. Apply the fixed projective 3-design POVM to the resulting state, in both sign branches. Retain the complete design setting and outcome.

There is no conditioning of the input copy budget on the sign. In particular, a symmetric outcome is measured and retained, rather than discarded.

**Theorem 1.** For every finite $`d`$, the measurement above can be chosen independently of $`\rho`$ and $`A`$ so that every regular rank-two tangent satisfies

```math
I_{\mathcal M_d}(\rho^{\otimes2};A)
\ge\frac1{12}J_2(\rho;A).
```

Consequently, for every regular multiparameter rank-two model,

```math
I_{\mathcal M_d}\succeq\frac1{12}J_2.
```

For pure-state manifold tangents, the same apparatus satisfies the stronger inequality $`I_{\mathcal M_d}\ge J_2/4`$.

The proof has three parts. A third-moment bound controls the design readout of a general conditional state and of a pure conditional state. The rank-two antisymmetric state is pure, while its symmetric partner has rank three. A direct tangent calculation then shows that their retained records cover every term of the original SLD metric with a uniform coefficient.

## A projective 3-design information bound

Let $`\nu`$ be a projective 3-design probability distribution in dimension $`D`$. Its associated POVM is

```math
E(d\psi)=D|\psi\rangle\langle\psi|\,d\nu(\psi).
```

The first-moment identity makes these effects sum to the identity. For a normalized state $`\sigma`$ and a traceless Hermitian regular tangent $`B`$, write

```math
r(\psi)=\langle\psi|\sigma|\psi\rangle,
\qquad z(\psi)=\langle\psi|B|\psi\rangle.
```

The resulting FI is $`I_3(\sigma;B)=D\mathbb E_\nu[z^2/r]`$, with the zero-probability convention stated above. If $`r=0`$, regularity implies $`z=0`$.

**Lemma 2.** For every such state and tangent,

```math
I_3(\sigma;B)
\ge \frac{D+2}{D+1}
\frac{(\mathrm{Tr}B^2)^2}
{\mathrm{Tr}B^2+2\mathrm{Tr}(\sigma B^2)}
\ge\frac13\mathrm{Tr}B^2.
```

If $`\sigma`$ is pure and $`B`$ is a pure-state tangent, then

```math
I_3(\sigma;B)\ge\frac14J_\sigma(B).
```

**Proof.** If $`B=0`$, the statements are immediate. Otherwise Cauchy–Schwarz gives

```math
\mathbb E_\nu\frac{z^2}{r}
\ge\frac{(\mathbb E_\nu z^2)^2}{\mathbb E_\nu(z^2r)}.
```

The second and third design moments, together with $`\mathrm{Tr}B=0`$ and $`\mathrm{Tr}\sigma=1`$, are

```math
\mathbb E_\nu z^2=\frac{\mathrm{Tr}B^2}{D(D+1)},
\qquad
\mathbb E_\nu(z^2r)=
\frac{\mathrm{Tr}B^2+2\mathrm{Tr}(\sigma B^2)}
{D(D+1)(D+2)}.
```

Substitution proves the first bound. Since $`0\preceq\sigma\preceq\mathbb I`$, the denominator is at most $`3\mathrm{Tr}B^2`$, proving the second.

For a pure state, choose a phase convention in which

```math
\sigma=|\phi\rangle\langle\phi|,\qquad
B=|v\rangle\langle\phi|+|\phi\rangle\langle v|,
\qquad \langle\phi|v\rangle=0.
```

Then $`\mathrm{Tr}B^2=2\|v\|^2`$, $`\mathrm{Tr}(\sigma B^2)=\|v\|^2`$, and $`J_\sigma(B)=4\|v\|^2`$. In fact the moment calculation gives

```math
I_3(\sigma;B)
\ge\frac{D+2}{4(D+1)}J_\sigma(B)
\ge\frac14J_\sigma(B).
```

These moment identities require no knowledge of the support or spectrum of $`\sigma`$. They are the design ingredient used below. See [ZC26](../references/RELATED_WORK.md#zc26) for the broader randomized-metrology framework.

## Rank-two geometry of the two sectors

Diagonalize the state only for the proof:

```math
\rho=\lambda_1|1\rangle\langle1|
+\lambda_2|2\rangle\langle2|,
\qquad \lambda_1,\lambda_2\gt 0,\quad\lambda_1+\lambda_2=1.
```

Set

```math
q=\lambda_1\lambda_2,\qquad s=1-q,
\qquad
A_{11}=a,\quad A_{22}=-a,\quad
v=|A_{12}|^2,\quad
t_i=\sum_{k\gt 2}|A_{ik}|^2.
```

The letters $`q`$ and $`s`$ denote the antisymmetric and symmetric probabilities. The one-copy information becomes

```math
J_\rho(A)=\frac{a^2}{q}+4v
+\frac{4t_1}{\lambda_1}+\frac{4t_2}{\lambda_2}.
```

Thus the proof must control eigenvalue changes, changes within the occupied support, and motion of each occupied direction into the kernel.

### Antisymmetric branch

For orthonormal vectors, write $`|i\wedge j\rangle=(|ij\rangle-|ji\rangle)/\sqrt2`$. The unnormalized antisymmetric state is

```math
\sigma_-=P_-\rho^{\otimes2}P_-
=q|1\wedge2\rangle\langle1\wedge2|.
```

Its probability derivative is

```math
q'=(\lambda_2-\lambda_1)a.
```

The normalized conditional state $`W=\sigma_-/q`$ is pure. The component of its vector derivative orthogonal to $`|1\wedge2\rangle`$ is

```math
|\dot w\rangle_\perp=
\sum_{k\gt 2}\frac{A_{k1}}{\lambda_1}|k\wedge2\rangle
+\sum_{k\gt 2}\frac{A_{k2}}{\lambda_2}|1\wedge k\rangle.
```

These wedge vectors are mutually orthogonal. It follows that

```math
J_W(\partial W)=
4\left(\frac{t_1}{\lambda_1^2}+\frac{t_2}{\lambda_2^2}\right).
```

This identity can also be obtained by differentiating $`P_-\rho^{\otimes2}P_-`$ directly and removing its trace derivative. It does not require a differentiable choice of eigenvectors inside a degenerate support. Internal rotations affect a two-dimensional support's one-dimensional exterior square only by an irrelevant phase.

### Symmetric branch

Write $`|ij;+\rangle=(|ij\rangle+|ji\rangle)/\sqrt2`$ for $`i\ne j`$. The unnormalized symmetric state is

```math
\sigma_+=\lambda_1^2|11\rangle\langle11|
+\lambda_2^2|22\rangle\langle22|
+q|12;+\rangle\langle12;+|.
```

Its trace is $`s`$, its normalized state is $`\tau_+=\sigma_+/s`$, and its normalized derivative is

```math
Y=\partial\tau_+
=\frac{P_+(A\otimes\rho+\rho\otimes A)P_+}{s}
+\frac{q'}{s^2}\sigma_+.
```

A direct calculation yields

```math
\mathrm{Tr}Y^2=
\frac{1}{s^2}\left[
2a^2+4(1-2q)v
+(4\lambda_1^2+2\lambda_2^2)t_1
+(4\lambda_2^2+2\lambda_1^2)t_2
\right].
```

For completeness, the matrix entries responsible for this expression are as follows. The radial derivative is diagonal on $`|11\rangle,|22\rangle,|12;+\rangle`$, with entries

```math
\frac{a}{s^2}
\bigl(\lambda_1(1+\lambda_2),
-\lambda_2(1+\lambda_1),
\lambda_2-\lambda_1\bigr).
```

Their squared sum is $`2a^2/s^2`$. The internal derivative connects $`|12;+\rangle`$ to $`|11\rangle`$ and $`|22\rangle`$ with magnitudes $`\sqrt2\lambda_1|A_{12}|/s`$ and $`\sqrt2\lambda_2|A_{12}|/s`$. For each $`k\gt 2`$, the $`A_{1k}`$ derivative connects $`|11\rangle`$ to $`|1k;+\rangle`$ and $`|12;+\rangle`$ to $`|2k;+\rangle`$ with magnitudes $`\sqrt2\lambda_1|A_{1k}|/s`$ and $`\lambda_2|A_{1k}|/s`$. Interchanging 1 and 2 gives the remaining entries. Each off-diagonal entry and its adjoint contribute twice its squared magnitude. These matrix positions are distinct, so the Hilbert–Schmidt norm has no cross terms between the listed components.

## Proof of the uniform fraction

Retaining the SWAP flag gives the exact classical decomposition

```math
I_{\mathcal M_d}
=\frac{(q')^2}{qs}
+s I_3(\tau_+;Y)
+q I_3(W;\partial W).
```

The first term is the information in the binary flag. The other terms weight each conditional measurement by its actual occurrence probability. Lemma 2 therefore implies

```math
I_{\mathcal M_d}
\ge \frac{(q')^2}{qs}
+\frac{s}{3}\mathrm{Tr}Y^2
+\frac{q}{4}J_W(\partial W).
```

Compare this quadratic form with the four components of $`J_\rho(A)`$.

For the eigenvalue derivative, the coefficient ratio is

```math
R_a(q)=\frac{1-4q+2q/3}{1-q}
=\frac{1-10q/3}{1-q}\ge\frac29,
\qquad 0\lt q\le\frac14.
```

Indeed, $`R_a(q)-2/9=7(1-4q)/[9(1-q)]`$. For the internal direction, the ratio is

```math
R_v(q)=\frac{1-2q}{3(1-q)}\ge\frac29,
```

with difference $`(1-4q)/[9(1-q)]`$.

For an external component belonging to eigenvalue $`\lambda`$, the other eigenvalue is $`1-\lambda`$. Its ratio to the corresponding term $`4t/\lambda`$ in the one-copy QFI is

```math
R_{\mathrm{ext}}(\lambda)
=\frac{\lambda[4\lambda^2+2(1-\lambda)^2]}
{12(\lambda^2-\lambda+1)}+\frac{1-\lambda}{4}
=\frac{3\lambda^3+2\lambda^2-4\lambda+3}
{12(\lambda^2-\lambda+1)}.
```

The last summand in the first expression is the probability-weighted information supplied by the pure antisymmetric branch. It prevents the information fraction from vanishing when either occupied eigenvalue becomes small. Explicitly,

```math
R_{\mathrm{ext}}(\lambda)-\frac16
=\frac{(\lambda+1)(3\lambda^2-3\lambda+1)}
{12(\lambda^2-\lambda+1)}\gt 0,
\qquad 0\lt \lambda\lt 1.
```

Every component is therefore at least one sixth of its one-copy QFI. Since the components have no cross terms,

```math
I_{\mathcal M_d}\ge\frac16J_\rho(A)
=\frac1{12}J_2(\rho;A).
```

This proves Theorem 1 and its multiparameter version. The constant is a conservative certificate; no optimality of $`1/12`$ is claimed.

## Degenerate spectra and pure-state tangents

At $`\lambda_1=\lambda_2=1/2`$, every expression above is finite. The proof decomposes the physical derivative matrix $`A`$ in any orthonormal basis of the support. It never divides by $`\lambda_1-\lambda_2`$, so degeneracy introduces no missing tangent directions. Both changes of the eigenvalues and arbitrary off-diagonal support derivatives are included.

For a pure-state path $`\rho_t=|\phi_t\rangle\langle\phi_t|`$, the pair is always symmetric and pure. The antisymmetric branch has zero probability and zero first derivative. Lemma 2 applied directly to the symmetric pair gives

```math
I_{\mathcal M_d}(\rho^{\otimes2};A)\ge\frac14J_2(\rho;A).
```

This assertion concerns tangents within the pure-state manifold. A parameterization that creates a new eigenvalue at a boundary can have nonregular classical or quantum information limits; such a model is not silently included in this theorem.

## Implementation and resource accounting

For an $`n`$-qubit input, the pair occupies $`2n`$ qubits. Prepare one ancilla in $`|+\rangle`$, apply a controlled exchange of the two registers, and measure the ancilla in the $`X`$ basis. This realizes the projectors $`P_\pm`$ while retaining the pair. The controlled exchange consists of $`n`$ controlled-SWAP gates, each with a constant-size decomposition in a standard universal gate set.

After either flag, sample a Clifford operator on all $`2n`$ data qubits, apply it, and measure in the computational basis. Record the Clifford setting as part of the outcome. The multiqubit Clifford group is an exact unitary 3-design [Webb16](../references/RELATED_WORK.md#webb16), [Zhu17](../references/RELATED_WORK.md#zhu17), so the resulting state ensemble gives the required projective 3-design. Uniform Clifford sampling and synthesis use polynomial classical work and a polynomial number of gates in $`n`$ under the usual ideal circuit model; [KS14](../references/RELATED_WORK.md#ks14) gives an explicit uniform-sampling algorithm and discusses polynomial synthesis. This is a finite ensemble, even though its full list is not enumerated by the processor.

For a general $`d`$-dimensional input, choose a fixed isometric encoding into $`n=\lceil\log_2d\rceil`$ qubits. The theorem is unaffected by the unused dimensions. The polynomial gate statement assumes this encoded register is available; it does not claim that an arbitrary physical encoding of a $`d`$-level system can be implemented at no cost.

The measurement consumes two fresh copies per record and uses no knowledge of their eigenbasis, no spectral calibration, and no state-dependent choice of setting. All symmetric and antisymmetric outcomes count. The theorem establishes the retained local information of this measurement. It does not assert a polynomial-time estimator, a finite-sample global reconstruction guarantee, or robustness to imperfect SWAP and Clifford operations.

## Reproducible numerical checks and their scope

The proof above is analytical. The companion [verification script](../experiments/verify_readout.py) checks the tensor derivatives and information certificate directly, then evaluates finite-design Fisher information in small systems. Its recorded output is [readout.json](../experiments/results/readout.json).

Run from the repository root:

```bash
python experiments/verify_readout.py
```

The script checks rank-two states in dimensions 2, 3, 4, and 7, including equal eigenvalues and a smaller eigenvalue of $`10^{-6}`$. It uses isolated radial, internal, and external tangents as well as mixed tangents in random bases. It compares the direct symmetric derivative's Hilbert–Schmidt norm with the formula above, the direct antisymmetric derivative with the wedge formula, and the resulting certificate with $`J_2/12`$. For an exactly zero wedge tangent it checks the unnormalized identity, avoiding cancellation from division by a small branch probability.

Separately, it constructs all 60 two-qubit stabilizer states and verifies their first three projector moments. It then computes the actual finite-POVM FI for the full pair measurement on qubit states, including pure-state tangents, and checks the standalone pure-state design bound in dimension four. The full pair FI calculation in this diagnostic is restricted to qubit inputs; higher-dimensional moving-support examples are checked at the tensor-derivative and analytical-certificate level. The script does not enumerate larger Clifford groups or replace the proof with a numerical optimization.

The recorded run uses NumPy 2.3.5 and random seed 20261107. It passed all checks:

| Executed check | Result |
|---|---|
| Rank-two tensor cases | 72, including 36 nonzero wedge tangents |
| Largest symmetric derivative norm relative residual | $`1.78\times10^{-15}`$ |
| Largest nonzero wedge QFI relative residual | $`5.80\times10^{-11}`$ |
| Smallest sampled analytical certificate divided by pair QFI | 0.1041667, above $`1/12`$ |
| Stabilizer design moment residuals, orders 1 and 2 | Zero at the recorded precision |
| Stabilizer design third-moment Frobenius residual | $`1.39\times10^{-17}`$ |
| Actual finite-design pair FI on 24 rank-two qubit cases | Minimum pair-QFI fraction 0.2444444 |
| Actual finite-design pair FI on 2 pure qubit tangents | Minimum pair-QFI fraction $`1/3`$ |
| Standalone pure-state design FI on 8 dimension-four cases | Minimum QFI fraction $`1/3`$ |

The sampled minima are diagnostics, not estimates of the optimal universal constants. The JSON output also records every tolerance and the larger residuals arising from small-eigenvalue numerical conditioning.
