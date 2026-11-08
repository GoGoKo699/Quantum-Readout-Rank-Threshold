# Learning the rank threshold

The single educational anchor is **Demkowicz-Dobrzański, Górecki and Guţă, *Multi-parameter estimation beyond quantum Fisher information* (2020), arXiv:2001.11742v2**. The [source bridge](ANCHOR.md) identifies the relevant sections, translates notation and develops concrete examples. The [30-milestone map](MILESTONES.md) connects those foundations to the rank classification and the fully counted comparison with learned calibration.

The organizing question is how much local sensitivity one fixed readout preserves without knowing the eigenbasis. Rank two admits a useful two-copy symmetry decomposition. Rank three creates a rare-information obstruction for every fixed finite block. A separate exact Haar calculation compares two-copy readout against all classically adaptive single-copy strategies near a shrinking occupied eigenvalue.

## Connected reading routes

| Route | Reading sequence | Main connection |
|---|---|---|
| Foundations | [Source and notation](ANCHOR.md#the-selected-anchor), [probability paths](ANCHOR.md#a-local-path-and-its-classical-information), [copy budget](ANCHOR.md#one-apparatus-and-the-copy-budget), then [model](../science/model.md) | Connect scores, SLD information, nuisance parameters and the complete experiment. |
| Uniform rank-two construction | [Parity example](ANCHOR.md#worked-example-what-the-parity-flag-knows), [complete record](ANCHOR.md#why-the-complete-record-matters), then [two-copy proof](../science/two-copy-readout.md) | See how the flag, pure wedge and symmetric branch jointly cover the full tangent. |
| Rank-three obstruction | [Rank-three example](ANCHOR.md#a-rank-three-example-and-the-limit-order), [all-POVM converse](../science/finite-block-obstruction.md), then [exact coefficient](../science/singular-information.md) | Separate an achieved rare-event coefficient from its matching worst-basis upper bound. |
| Paid calibration comparison | [Transcript accounting](ANCHOR.md#why-the-complete-record-matters), [exact Haar proof](../science/haar-pair-readout.md), then [sister calibration account](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/main/science/paid-calibration.md) | Compare full-record information, distinct eigenvector errors and the adaptive single-copy ceiling on one model. |

The map assigns M01–M10 to background/preliminaries and M11–M30 to narrative/innovation. The first phase builds the complete measurement problem; the second integrates the positive construction, converse and sharp near-boundary comparison. The map is common scientific material, with no learner-specific assessment record.

## Keep the resource and statistical scopes visible

Every pair attempt consumes two copies and retains the parity flag, random setting and outcome. The finite projective 3-design apparatus guarantees at least $`1/12`$ of pair QFI. The exact continuous-Haar companion has a distinct implementation and a stronger sufficiently-near-boundary conclusion; it does not assign that sharp constant to a finite Clifford ensemble.

The rank-three exact coefficient concerns one spectral tangent in an iterated limit. The Haar comparison concerns the full rank-two tangent space at each positive weak eigenvalue. Neither statement alone constructs a finite-sample estimator attaining an inverse-information benchmark. The [model](../science/model.md), [interpretation](../science/interpretation.md) and [verification guide](../verification/README.md) retain these distinctions and the reproduction routes.
