# Model and rank classification

A source emits independent copies of an unknown finite-dimensional quantum state. Each run sends a fixed number of copies through the same measurement apparatus. The apparatus can couple the copies and use recorded classical randomness, but it is not calibrated to the unknown state. The question is whether its outcome record preserves a constant fraction of the local quantum Fisher information in every parameter direction.

The relevant boundary is the number of occupied eigenstates. One copy is enough for pure-state families. Two copies suffice uniformly for rank-two families, including an unknown support in a large Hilbert space. Already for rank-three qutrits, every fixed finite block loses an arbitrarily large fraction of the available local information on some spectra.

## 1. States, tangents and the information convention

Let $`\rho_\theta`$ be a differentiable statistical model on $`\mathbb C^d`$. At a parameter point and a real direction $`u`$, write

```math
\rho=\rho_\theta,\qquad
A=\sum_j u_j\partial_j\rho_\theta.
```

The positive results concern smooth fixed-rank models. Thus $`A`$ is Hermitian and traceless, and its kernel-to-kernel block is zero. Directions may change the positive eigenvalues, rotate eigenvectors within the occupied support, and move that support into its orthogonal complement. The derivative is defined for a two-sided physical path. The rank promise does not mean that the support is supplied to the apparatus.

The symmetric logarithmic derivative $`L`$ solves $`2A=\rho L+L\rho`$. Its value on the kernel is irrelevant. The single-copy SLD quantum Fisher information is

```math
J_\rho(A)=\operatorname{Tr}(\rho L^2)
=\sum_{i,j:\lambda_i+\lambda_j>0}
\frac{2|A_{ij}|^2}{\lambda_i+\lambda_j},
```

where $`\lambda_i`$ are the eigenvalues of $`\rho`$. The associated multiparameter matrix is denoted by $`J`$. This is the ordinary pointwise SLD quantity. No continuous extension through a rank-changing singularity is part of the definition.

For a block of $`k`$ independent copies,

```math
A^{(k)}
=\sum_{j=1}^k
\rho^{\otimes(j-1)}\otimes A\otimes
\rho^{\otimes(k-j)},\qquad
J_{\rho^{\otimes k}}(A^{(k)})=kJ_\rho(A).
```

Every efficiency fraction below is normalized by the information of all copies consumed in the block. In particular, $`J_2=2J`$.

## 2. What a fixed apparatus may do

A block apparatus is a POVM $`M`$ on $`(\mathbb C^d)^{\otimes k}`$. Its outcomes may be finite, countable or continuous. Ancillas prepared independently of the unknown state, coherent controls, intermediate measurements, and adaptation within the block are allowed. They induce one POVM on the input copies.

The apparatus retains its classical random settings, success flags and readout outcomes. All input copies are charged, including attempts with an uninformative outcome. The apparatus is reset between blocks; a coherent memory that carries information from indefinitely many inputs is a different resource model.

For a general outcome space, use the finite trace measure $`\nu(B)=\operatorname{Tr}M(B)`$. The density $`E_x=dM/d\nu`$ is positive with trace one almost everywhere. With

```math
q_\rho(x)=\operatorname{Tr}(E_x\rho^{\otimes k}),\qquad
\dot q_\rho(x)=\operatorname{Tr}(E_x A^{(k)}),
```

the classical Fisher information of the full record is

```math
I_M(\rho;A)
=\int_{\{q_\rho>0\}}
\frac{\dot q_\rho(x)^2}{q_\rho(x)}\,d\nu(x).
```

At a zero-probability outcome, a regular two-sided physical tangent has zero first derivative. The positive proof uses the corresponding zero contribution convention. The negative theorem is evaluated at strictly positive qutrit states before taking a limit.

A universal fraction means

```math
I_M(\rho;A)\ge c\,kJ_\rho(A)
```

for all states and regular tangents in the stated class, where $`c>0`$ does not depend on the unknown spectrum, eigenbasis or tangent. A directional inequality for every real $`u`$ is equivalent to the matrix inequality $`I_M\succeq ckJ`$. This simultaneous matrix comparison is stronger than optimizing a measurement separately for one specified parameter direction.

The constructive apparatus depends only on the known Hilbert-space dimension. The converse allows more: its POVM may be chosen using the exact nominal spectrum. That choice is held fixed when the local statistical derivative is taken. Differentiating the apparatus itself would describe a different experiment.

## 3. The rank-two construction

**Theorem 1.** For every finite $`d`$, a fixed finite-outcome measurement on two copies satisfies

```math
I_M(\rho;A)\ge\frac{1}{12}J_{\rho^{\otimes2}}(A^{(2)})
```

for every smooth rank-two model and every tangent. The constant is uniform over the two positive eigenvalues and the unknown support. At a pure state, for pure-state manifold tangents, the same measurement satisfies $`I_M\ge J_2/4`$.

The measurement first resolves exchange parity,

```math
P_\pm=\frac{\mathbb 1\pm S}{2},
```

where $`S`$ swaps the two inputs. It then performs a projective 3-design readout on the full two-copy register in either branch. The parity bit, randomized setting and readout outcome are all kept.

For $`n`$-qubit inputs, a random Clifford followed by computational-basis readout supplies the design. A nondestructive SWAP test uses one additional control ancilla and $`n`$ controlled swaps. The physical readout has polynomial gate complexity in $`n`$. Evaluating the likelihood of an arbitrary statistical model is a separate classical task.

The [complete proof](two-copy-readout.md) derives the design moment inequality and compares every rank-two tangent component. It handles equal positive eigenvalues directly, without differentiating an arbitrary basis inside a degenerate eigenspace. The constant is a proved lower bound, not an optimality claim.

## 4. The finite-block obstruction

Fix $`0<\eta\le1/4`$ and $`0<p<\eta`$, and define

```math
\rho_{\eta,p,U}
=U\operatorname{diag}(1-\eta-p,\eta,p)U^\dagger,
\qquad U\in U(3).
```

The parameter of interest is $`p`$; $`\eta`$ and $`U`$ are fixed when taking its derivative. Its single-copy quantum Fisher information is

```math
J_{\eta,p}=\frac1p+\frac1{1-\eta-p}.
```

Let $`R_k(\eta,p)`$ be the largest worst-eigenbasis efficiency achievable by a POVM on $`k`$ copies, allowing nominal-spectrum dependence but no dependence on $`U`$:

```math
R_k(\eta,p)
=\sup_{M\ {\rm independent\ of}\ U}
\inf_{U\in U(3)}
\frac{I_M(\eta,p,U)}{kJ_{\eta,p}}.
```

Set $`a=1-\eta`$, $`b=\eta`$ and

```math
h_m(a,b)=\sum_{j=0}^m a^j b^{m-j},
\qquad
\beta_k(\eta)=\sum_{m=0}^{k-1}\bigl[1-h_m(a,b)\bigr].
```

**Theorem 2.** For each fixed finite $`k\ge1`$ and fixed $`\eta`$,

```math
\lim_{p\downarrow0}R_k(\eta,p)
=\frac{\beta_k(\eta)}{k}.
```

The upper bound holds for arbitrary POVM outcome spaces, with uniformity over nominal-spectrum-dependent choices. The binary measurement that distinguishes Schur sectors with at least three rows from the remaining sectors attains the displayed leading coefficient. In particular,

```math
0\le\frac{\beta_k(\eta)}k
\le 1-(1-\eta)^{k-1}
\le(k-1)\eta.
```

For any fixed $`k`$, choosing $`\eta`$ sufficiently small and then $`p`$ sufficiently small defeats every proposed uniform positive fraction. This already occurs in a fixed three-dimensional Hilbert space.

The [arbitrary-POVM proof](finite-block-obstruction.md) explains why regular Schur sectors cannot retain a leading $`1/p`$ contribution after averaging over the unknown eigenbasis. The [singular-information account](singular-information.md) derives the exact coefficient, its attaining measurement and its small-block examples. The order of limits is part of the result; it is not a uniform finite-$`p`$ estimate when the block size also changes.

## 5. Classification and provenance

| Promised family | Minimum fixed coherent block | Uniform local SLD-Fisher fraction |
|---|---:|---|
| Pure states, with pure-state tangents | 1 | Positive; projective 3-designs suffice |
| Rank at most two, with smooth tangents within each rank stratum | 2 | At least $`1/12`$ of pair QFI |
| All rank-three qutrit states | No finite block | The worst-case fraction can be arbitrarily small |

One-copy impossibility for rank-two models follows already from the unknown-basis qubit family approaching a pure state, as shown in the [converse account](finite-block-obstruction.md). Thus two is necessary as well as sufficient for the stated universal task. The pure-state 3-design result and exact collective qubit readout are established antecedents [ZC26, ZH18](../references/RELATED_WORK.md).

The new classification concerns unknown moving rank-two supports and arbitrary fixed blocks at rank three. SWAP sectors, Clifford designs and Schur rank certificates are standard ingredients. The [related-work account](../references/RELATED_WORK.md) states the inherited results and compares matching assumptions and losses.

## 6. Reading route

Read [two-copy readout](two-copy-readout.md) for the construction, [finite-block obstruction](finite-block-obstruction.md) for the converse, and [singular information](singular-information.md) for the exact coefficient and its meaning. The [resource interpretation](interpretation.md) connects these statements to calibration, repeated experiments and other estimation objectives. [Verification](../verification/README.md) gives the executed finite checks and their analytical limits.
