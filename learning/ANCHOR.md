# From estimation bounds to fixed quantum readout

The organizing experiment is simple: a source emits copies of one unknown state, a fixed apparatus turns each coherent block into a classical record, and every input copy is counted. The questions are which local state changes survive that measurement, how the answer depends on rank, and what changes when a learned basis is replaced by a two-copy apparatus.

## The selected anchor

The single educational anchor is **DDG20**: Rafał Demkowicz-Dobrzański, Wojciech Górecki, and Mădălin Guţă, *Multi-parameter estimation beyond quantum Fisher information*, J. Phys. A **53**, 363001 (2020), [DOI](https://doi.org/10.1088/1751-8121/ab8ef3).

Use **arXiv:2001.11742v2, 1 September 2020**: [version record](https://arxiv.org/abs/2001.11742v2), [HTML](https://arxiv.org/html/2001.11742v2), [PDF](https://arxiv.org/pdf/2001.11742v2). All section references below identify this version. The review supplies the estimation framework; the linked scientific pages supply the rank-specific measurement constructions and proofs.

| DDG20 v2 section | Foundation used here | Project connection |
|---|---|---|
| [1.2](https://arxiv.org/html/2001.11742v2#S1.SS2) | States, probabilities, estimators and local models | Fixed apparatus and exact-rank conventions |
| [2.1](https://arxiv.org/html/2001.11742v2#S2.SS1) | Scores, Fisher matrices and classical covariance bounds | Complete branch and adaptive records |
| [2.2](https://arxiv.org/html/2001.11742v2#S2.SS2) | SLD information and the measurement bound | Single-copy metric and its tensor-product normalization |
| [2.7](https://arxiv.org/html/2001.11742v2#S2.SS7) | Estimation with nuisance parameters | Full-model comparison when the eigenbasis is unknown |
| [2.10–2.11](https://arxiv.org/html/2001.11742v2#S2.SS10) | Multiple copies and saturability | Coherent blocks, information retention and estimator scope |
| [3.1](https://arxiv.org/html/2001.11742v2#S3.SS1) | Concrete qubit estimation models | Why an unknown moving rank-two support adds directions |
| [4.5](https://arxiv.org/html/2001.11742v2#S4.SS5) | Localization, asymptotic strategies and applicability | Supplied calibration versus a paid pilot |
| [4.6.3](https://arxiv.org/html/2001.11742v2#S4.SS6.SSS3) | The full-rank scope of the general QLAN treatment | A boundary on what can be imported into this rank-deficient problem |

The [30-milestone map](MILESTONES.md) connects these foundations to the finite-design theorem, the rank-three obstruction and the exact Haar comparison. The allocation and sequence follow the scientific argument rather than the review's table of contents.

## Notation translation

| DDG20 | This repository | Meaning |
|---|---|---|
| $`F`$ | $`I_M`$ or $`I`$ | Classical Fisher information of the measured record |
| $`F_Q`$ | $`J`$ | Single-copy SLD quantum Fisher information |
| $`M_m`$ | $`E_x`$ | A POVM effect |
| $`L_i`$ | $`L_i`$ or $`L_A`$ | Coordinate or directional SLD |
| $`C`$ | $`W`$ | Quadratic loss weight |
| $`\Sigma`$ | $`\mathrm{Cov}(\widehat\theta)`$ | Covariance, with the stated bias convention retained |

The review also uses $`J`$ for a parameter-transformation Jacobian and $`r`$ for a qubit Bloch radius. Here $`J`$ denotes QFI and rank is an integer. A density-matrix tangent $`A`$ is different from an operator tuple in the Holevo bound. The rare eigenvalue $`p`$ in the rank-three model is distinct from an observed outcome probability.

## A local path and its classical information

At an operating point, a state path supplies $`\rho`$ and $`A=\partial_t\rho_t|_{t=0}`$. A selected measurement is held fixed while the state varies. It produces

```math
q_t(x)=\mathrm{Tr}(E_x\rho_t),
\qquad
\dot q_x=\mathrm{Tr}(E_xA),
\qquad
I_M(\rho;A)=\int_{q_0\gt0}\frac{\dot q_x^2}{q_0(x)}\,dx.
```

The integral includes discrete sums as a special case. The denominator makes a small change in a rare outcome statistically different from the same absolute change in a common outcome. Zero-probability outcomes follow the ordinary pointwise convention in the [model](../science/model.md); no direction-dependent limit is inserted into one common matrix.

For a regular rank-two qutrit path, $`A`$ can change the occupied populations, create occupied coherences, or rotate either occupied eigenvector into the empty level. These are seven real directions. Keeping only the three directions of a qubit with known fixed support would change the problem.

The SLD satisfies $`2A=\rho L_A+L_A\rho`$. In an eigenbasis this gives

```math
J_\rho(A)=2\sum_{i,j:\lambda_i+\lambda_j\gt0}
\frac{|A_{ij}|^2}{\lambda_i+\lambda_j}.
```

The [positive proof](../science/two-copy-readout.md) and [Haar comparison](../science/haar-pair-readout.md) evaluate the same metric. It remains the rank-two metric for each positive weak eigenvalue, even while that eigenvalue tends to zero.

## One apparatus and the copy budget

For $`k`$ independent input copies, the SLDs add and their mean-zero cross terms vanish. Hence $`J_k=kJ`$. A measurement retaining the fraction $`c`$ obeys $`I_M\succeq ckJ`$ on the entire allowed tangent space.

If a pair apparatus is repeated $`N/2`$ times, its total information is $`(N/2)I_{\rm pair}`$ and its input information is $`NJ`$. Its normalized fraction is therefore $`I_{\rm pair}/(2J)`$. A conditional antisymmetric outcome still consumes two copies; its information must be multiplied by its occurrence probability.

This matrix criterion protects every real combination of parameters. A larger target-coordinate diagonal does not establish a larger nuisance-adjusted experiment. For a parameter of interest and unknown eigenvector coordinates, form the appropriate Schur complement of the full Fisher matrix. DDG20 Section 2.7 supplies the statistical principle; the project supplies the complete moving-support tangent and its information matrices.

## Worked example: what the parity flag knows

Consider a rank-two state with eigenvalues $`1-t,t`$. A SWAP-parity measurement has antisymmetric probability $`q=t(1-t)`$. At fixed eigenbasis its flag information is

```math
I_{\rm flag}(t)
=\frac{(1-2t)^2}{t(1-t)[1-t(1-t)]},
\qquad
J_2(t)=\frac2{t(1-t)}.
```

At $`t=1/2`$, the flag has zero ordinary local information although $`J_2=8`$. The conditional measurements are therefore necessary for an all-direction theorem. As $`t\downarrow0`$, the flag fraction tends to $`1/2`$. This concerns the spectral direction; it says nothing by itself about support motion.

The normalized antisymmetric rank-two state is the pure wedge $`|1\wedge2\rangle`$. Rotating either occupied vector moves this wedge and encodes support information. The symmetric branch covers the remaining directions. A projective 3-design readout in both branches yields the [uniform finite-design bound](../science/two-copy-readout.md)

```math
I_{\rm pair}\succeq\frac1{12}J_2.
```

The bound is conservative. The [continuous-Haar calculation](../science/haar-pair-readout.md) evaluates a specified different implementation exactly, rather than treating $`1/12`$ as its measured information.

## Why the complete record matters

For branch probabilities $`w_b`$ and normalized conditional laws $`r_b`$, the record is $`q(b,x)=w_br_b(x)`$. The conditional score has mean zero, so

```math
I_{\rm full}
=\sum_b\frac{(w_b')^2}{w_b}+\sum_bw_bI_b.
```

Both the branch frequency and its conditional outcome matter. With a pilot record $`Y`$ selecting a later apparatus $`M_Y`$ on $`N-m`$ fresh copies, the same score argument gives the matrix identity

```math
I_{\rm total}=I_Y+(N-m)\mathbb E_Y[I_{M_Y}].
```

The apparatus is fixed conditional on the observed pilot. The derivative does not act on the estimator's output. The [sister calibration account](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/92a59ee026610f9a0e3c347630bd399421172337/science/paid-calibration.md) develops the strong/weak error distinction and an exact binomial pilot. Averaging the resulting information is different from substituting a calibration mean squared error into a nonlinear formula.

The inherited single-copy support-information budget applies separately to each conditional apparatus. After summing the transcript information, the full-model worst-direction fraction is at most $`1/4`$ for every classically adaptive one-copy protocol. The exact [Haar pair proof](../science/haar-pair-readout.md) shows a fraction strictly above $`1/4`$ for sufficiently small positive weak eigenvalue, tending to $`1/4`$. This is a local FI separation; it is not a finite-sample risk ordering or a universal crossover law.

## A rank-three example and the limit order

For a rank-three qutrit with eigenvalues $`1-\eta-p,\eta,p`$, the fully antisymmetric three-copy outcome has probability $`w_3=(1-\eta-p)\eta p`$. At fixed $`\eta\gt0`$ its binary information is $`\eta(1-\eta)/p+O(1)`$, while the three-copy QFI is $`3/p+O(1)`$. Thus its limiting fraction is $`\eta(1-\eta)/3`$.

The rare outcome retains a divergent information term, but its coefficient contains the second weak population. For arbitrary fixed blocks, the [Schur-sector calculation](../science/singular-information.md) gives the exact coefficient $`\beta_k(\eta)`$. The [all-POVM converse](../science/finite-block-obstruction.md) proves that the other sectors cannot supply a leading term uniformly over unknown bases and measurement effects. Fixed $`k,\eta`$ come first, then $`p\downarrow0`$, then $`\eta\downarrow0`$. No finite-$`p`$ uniform remainder is inferred when those quantities change together.

## Where the anchor ends and the project begins

DDG20 supplies scores, SLD bounds, nuisance handling, multiple-copy comparisons and a careful account of asymptotic applicability. Its Section 4.6.3 treats general finite-dimensional QLAN under full-rank assumptions; it does not establish a moving-support rank-deficient pilot result or uniformity as an occupied eigenvalue shrinks.

The project supplies the exact-rank conventions, finite-design bound, rank-two wedge mechanism, arbitrary-POVM rank-three obstruction, exact singular coefficient and continuous-Haar pair comparison. Primary research attribution is in [Related work](../references/RELATED_WORK.md). The [milestones](MILESTONES.md) organize these steps without identifying FI preservation with estimator attainability.
