# What the rank boundary says about a readout apparatus

The two-copy construction and the finite-block converse concern an apparatus used before the unknown state's eigenbasis has been learned. They compare its classical outcome information with the SLD quantum Fisher information of all input copies. The [model](model.md) fixes this experiment and its quantifiers.

## Rank two separates weight from support

Write a rank-two state as

```math
\rho=\lambda_1|u_1\rangle\langle u_1|
+\lambda_2|u_2\rangle\langle u_2|,
\qquad \lambda_1+\lambda_2=1.
```

The antisymmetric part of two copies is

```math
P_-\rho^{\otimes2}P_-
=\lambda_1\lambda_2
|u_1\wedge u_2\rangle\langle u_1\wedge u_2|.
```

Its probability carries spectral information. Its normalized state is pure and records the occupied two-dimensional subspace. Randomized pure-state readout can therefore recover local changes of that subspace with a constant efficiency.

The success probability becomes small when one eigenvalue does. This does not by itself destroy the information guarantee. The conditional support derivative becomes correspondingly sensitive to the weak eigenvector. Multiplying its Fisher information by the actual success probability leaves the scale required by the original SLD metric. The symmetric branch supplies the remaining radial and support-internal directions. The [proof](two-copy-readout.md) performs this comparison for the full record, including the flag and both branches.

This explains why a known qubit result is insufficient as a substitute. A qubit has a fixed two-dimensional physical Hilbert space. A rank-two state in a larger space has additional directions in which either occupied eigenvector moves into the kernel. Those directions must be measured without being given the support.

## Rank three introduces a second weak direction

For the qutrit family

```math
\rho_{\eta,p,U}
=U\mathrm{diag}(1-\eta-p,\eta,p)U^\dagger,
\qquad 0\lt p\ll\eta,
```

an eigenbasis measurement would observe the rare third component directly. Its information about $`p`$ is of order $`1/p`$. A universal apparatus cannot align to that component in advance.

At the rank-two boundary $`p=0`$, every regular Schur sector has positive probability for almost every rotated positive measurement effect. Such outcomes contribute no leading $`1/p`$ term. The singular contribution comes from sectors that are absent at rank two and appear when a third occupied direction is present.

A three-row sector requires all three eigenvector labels to occur among the copies. To first order in $`p`$, the rare third label occurs once; another weak label must also be present in the right permutation structure. This coincidence limits the information coefficient. The [exact coefficient](singular-information.md) is

```math
\beta_k(\eta)
=\sum_{m=0}^{k-1}
\left[1-\sum_{j=0}^m(1-\eta)^j\eta^{m-j}\right].
```

For example, $`\beta_3=\eta(1-\eta)`$ and $`\beta_4=3\eta(1-\eta)`$. Dividing by $`k`$ gives the optimum worst-eigenbasis fraction of the leading singular information. The attaining binary Schur-sector test is independent of the eigenbasis.

For fixed $`k`$, this fraction vanishes as $`\eta`$ tends to zero. For fixed $`\eta\gt 0`$, larger blocks can recover an increasing fraction of this particular leading spectral information. These statements refer to the coefficient after taking $`p\downarrow0`$. They do not give a uniform sample requirement at finite $`p`$.

## The coherent block is the constrained resource

The positive protocol consumes two fresh input copies in every run. It uses one SWAP-test control ancilla and a random Clifford readout of the two registers. The number of retained classical bits includes the random setting, parity bit and measurement result. A rare branch is not treated as a free prepared input.

The converse permits every POVM on a fixed block: additional ancillas, randomized settings and adaptation inside the block cannot evade it. A finite schedule of different state-independent block measurements is likewise represented by a recorded randomized apparatus.

Two resources lie outside this premise. First, previous blocks may be used to learn the eigenbasis and calibrate later measurements. The later detector then depends on information about the unknown basis. Second, a small quantum memory may remain coherent while interacting with many successive copies. Its final measurement can depend coherently on more than a fixed block of inputs. A bound on memory qubits is therefore not a bound on coherent block size. The relevant sensing comparison is discussed in [related work](../references/RELATED_WORK.md#why-the-objectives-and-limits-matter).

No QRAM or classical-data amplitude loading is used in the positive construction. The source must supply actual copies of the state, and the specified coherent gates are ideal. Noise robustness is a separate question.

## Local sensitivity and statistical estimation

For independent repetitions of a fixed block measurement, classical Fisher information adds. Thus the rank-two matrix bound persists under repetition. It controls every regular local parameter direction and every positive semidefinite weighting of the inverse information on an identifiable tangent space.

This information statement does not by itself give a finite-sample globally valid estimator. Local unbiasedness, identifiability, the parameter domain, estimator construction and computational access to its likelihood still matter. A polynomial physical circuit does not imply polynomial classical inference for an arbitrary many-body model.

The distinction is especially visible for a rare eigenvalue. For two nearby values $`p`$ and $`p+\delta p`$ in the same eigenbasis, the half-trace distance is $`|\delta p|`$. The local SLD squared length contains $`(\delta p)^2/p`$. Absolute reconstruction error and uniform relative local information therefore weight the rare component differently. Optimal bounded-block trace-norm tomography can coexist with the present obstruction; the corresponding result is compared explicitly in [NZ26](../references/RELATED_WORK.md#nz26).

## What is established

The positive result gives one finite, state-independent apparatus for all regular rank-two models, including an unknown support and arbitrary positive eigenvalue ratio. The negative result shows that no fixed finite block retains a positive fraction uniformly over rank-three qutrit spectra and eigenbases. Its exact singular coefficient is attained, so the mechanism is more specific than failure of a chosen randomized measurement.

The rank promise and the fixed-apparatus premise remain part of this conclusion. Rank-changing boundary parametrizations, approximate-rank inputs, globally adaptive calibration, and finite-sample estimation require their own models. The classification identifies where bounded coherent processing alone can remove spectral conditioning from universal local readout.
