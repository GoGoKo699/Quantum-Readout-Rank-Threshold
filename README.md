# Quantum Readout Rank Threshold

**How many copies must a fixed quantum readout process jointly to preserve local sensitivity without knowing the state's eigenbasis?**

A source emits identical copies of an unknown state. Each run uses the same apparatus on a fixed coherent block and keeps its complete classical record. The guarantee is a constant fraction of the SLD quantum Fisher information in every regular parameter direction, uniformly over the unknown spectrum and support.

| State family | Fixed coherent block | Uniform information guarantee |
|---|---:|---|
| Pure states | One copy suffices | Established projective 3-design result |
| Rank-two states in any dimension | Two copies are necessary and sufficient | At least $`1/12`$ of the pair QFI |
| Rank-three qutrit states | No fixed finite block suffices | The worst-case fraction can approach zero |

The pure-state baseline is prior work [ZC26](references/RELATED_WORK.md#zc26). Two-copy universal qubit readout is also established [ZH18](references/RELATED_WORK.md#zh18). The rank-two theorem here includes an unknown moving support in an arbitrary ambient dimension and no lower bound on the smaller eigenvalue.

## Two copies preserve rank-two sensitivity

The apparatus measures SWAP parity and then performs a projective 3-design readout on the full pair register in both branches. It retains the parity bit, random setting and final outcome. For every smooth rank-two model,

```math
I_{\mathrm{readout}}\succeq\frac1{12}J_2,
\qquad J_2=2J.
```

The antisymmetric branch is a pure state encoding the occupied support. Its probability supplies spectral information, while the symmetric branch covers the remaining tangent directions. Every attempt consumes two copies; all branch probabilities and outcomes enter the bound.

On qubit registers, the protocol uses a SWAP-test ancilla and random Clifford gates. This is an efficient physical readout under the stated circuit model. General classical estimation complexity is separate.

## Paid calibration and an exact two-copy comparison

The sister project [Calibrated Quantum Readout](https://github.com/GoGoKo699/Calibrated-Quantum-Readout) determines the sharp calibrated single-copy fraction. Its [paid-calibration analysis](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/92a59ee026610f9a0e3c347630bd399421172337/science/paid-calibration.md) counts the entire pilot record and separates strong- from weak-eigenvector errors near a small occupied eigenvalue. This repository supplies the exact [continuous-Haar pair comparison](science/haar-pair-readout.md).

For a rank-two qutrit $`\rho_b=\operatorname{diag}(1-b,b,0)`$, parity followed by continuous Haar readout has full-model fraction $`c_H(b)\gt1/4`$ for every sufficiently small $`b\gt0`$, tending to $`1/4`$ as $`b\downarrow0`$. Every protocol measuring fresh copies separately, with classical adaptation and calibration records counted, has fraction at most $`1/4`$. Thus this continuous pair apparatus strictly exceeds the adaptive single-copy ceiling near the boundary. The proof uses exact branch information and all seven tangent directions.

The Haar apparatus is distinct from the finite Clifford implementation above. The result does not assign the finite design a sharp constant, order finite-sample estimation risks, or assume a crossover law in calibration budget.

## Rank three defeats every fixed block

For the unknown-basis qutrit family

```math
\rho_{\eta,p,U}
=U\mathrm{diag}(1-\eta-p,\eta,p)U^\dagger,
\qquad 0\lt p\lt \eta\le1/4,
```

consider information about the rare eigenvalue $`p`$. The converse permits every POVM on a fixed finite block of $`k`$ copies, including continuous outcomes and knowledge of the nominal spectrum.

Only Schur sectors with three rows can retain the leading $`1/p`$ information. Their coefficient is explicit:

```math
\beta_k(\eta)
=\sum_{m=0}^{k-1}\left[
1-\sum_{j=0}^m(1-\eta)^j\eta^{m-j}
\right].
```

The optimum worst-eigenbasis fraction tends to $`\beta_k(\eta)/k`$ as $`p\downarrow0`$ with $`k,\eta`$ fixed. A binary Schur-sector measurement attains this coefficient. For every fixed $`k`$, the fraction then tends to zero as $`\eta\downarrow0`$. This exact optimum concerns the displayed spectral tangent and the stated iterated limit.

## Read the science

| Question | Authoritative account |
|---|---|
| What is the experiment and exact classification? | [Model and claims](science/model.md) |
| How does the two-copy measurement work? | [Construction and complete proof](science/two-copy-readout.md) |
| What does exact pair information say near a shrinking occupied eigenvalue? | [Haar pair readout and adaptive single-copy comparison](science/haar-pair-readout.md) |
| Why does the converse cover every finite-block POVM? | [Finite-block obstruction](science/finite-block-obstruction.md) |
| What information survives, and which measurement attains it? | [Exact singular coefficient](science/singular-information.md) |
| What do block size, calibration and sensitivity mean operationally? | [Resource interpretation](science/interpretation.md) |
| Which results and primitives are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| How are the finite identities reproduced? | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps questions to these sources.

## Learn the argument

The learning route uses Demkowicz-Dobrzański, Górecki and Guţă's [*Multi-parameter estimation beyond Quantum Fisher Information*](https://arxiv.org/abs/2001.11742v2) as its single educational anchor, shared with Calibrated Quantum Readout. Begin with the [source-to-project bridge](learning/ANCHOR.md), then follow the [30-milestone map](learning/MILESTONES.md): 10 background milestones and 20 narrative milestones. The [learning entrypoint](learning/README.md) gives focused routes through the construction, converse and fully counted comparison.

## Reproduce the checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The checks validate tensor derivatives, finite design moments and small-system measurement information, exact Schur coefficients through independent algebraic and permutation formulas, and continuous-Haar information through 35-digit Laplace integrals. The universal converse and eventual strict Haar comparison are established by the proofs, not finite enumeration.

## Scope

The positive result concerns regular fixed-rank tangents and counts the full pair record. The converse constrains a fixed apparatus on independent coherent blocks. Learned calibration across blocks, persistent quantum memory, and global trace-distance reconstruction have different resources or losses. No uniform finite-$`p`$ remainder is claimed when the block size or the second eigenvalue changes.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
