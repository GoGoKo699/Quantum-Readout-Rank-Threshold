# Learning the rank threshold

The learning material uses **Sidhu and Kok, *A Geometric Perspective on Quantum Parameter Estimation* (2020)** as its single educational anchor. The [conceptual bridge](ANCHOR.md) identifies the exact sections of arXiv:1907.06628v2, translates the notation, and develops the connection to this repository's fixed-readout problem. Research precedents and technical dependencies are collected separately in [Related work](../references/RELATED_WORK.md).

The organizing question is how a measurement turns a path of quantum states into a path of classical probabilities. The quantum Fisher information measures the local sensitivity present in the states; the classical Fisher information measures the sensitivity retained in the complete outcome record. The rank threshold concerns one apparatus that preserves a uniform fraction without first learning the unknown eigenbasis.

## Three connected routes

| Route | Reading sequence | Main connection |
|---|---|---|
| Statistical foundations | [Anchor sections and notation](ANCHOR.md#the-selected-anchor), [local probability paths](ANCHOR.md#a-local-path-and-its-classical-information), [state tangents](ANCHOR.md#from-a-state-tangent-to-an-observed-distribution), then [model](../science/model.md) | Move from a score and a probability metric to the SLD metric and a precise experiment. |
| Positive construction | [Copy budget](ANCHOR.md#one-apparatus-and-the-copy-budget), [rank-two symmetry](ANCHOR.md#why-rank-two-has-a-useful-symmetry-branch), [complete branch record](ANCHOR.md#why-the-complete-branch-record-matters), then [two-copy proof](../science/two-copy-readout.md) | Understand how the branch flag and both conditional readouts cover spectral and support motion. |
| Converse and its scope | [Three-copy example](ANCHOR.md#worked-example-the-three-copy-rank-certificate), [finite-block obstruction](ANCHOR.md#from-the-example-to-the-finite-block-obstruction), then [all-POVM proof](../science/finite-block-obstruction.md) and [exact coefficient](../science/singular-information.md) | Separate an achieved rare-event coefficient from the proof that no apparatus has a better limiting worst-basis coefficient. |

The [30 milestones](MILESTONES.md) give a common sequence across these routes: foundational concepts first, then the repository's model, construction, converse and resource interpretation. They describe the mathematical connections underlying the result.

## Keep the experiment attached to the formulas

Every repetition of the positive apparatus consumes two fresh copies and records its SWAP flag, random setting and readout result. Its guarantee is

```math
I_{\rm pair}\succeq\frac1{12}J_{\rm pair},
\qquad
J_{\rm pair}=2J.
```

The converse fixes a finite coherent block and an unknown eigenbasis. Its exact coefficient concerns a particular spectral tangent, with the rare eigenvalue taken to zero before the second weak eigenvalue. These conventions distinguish the result from a state-dependent optimal measurement, a protocol that learns a basis across blocks, or a global reconstruction guarantee.

The [model](../science/model.md) fixes the theorem statements and boundary conventions. The [resource interpretation](../science/interpretation.md) connects them to calibration, persistent memory and statistical estimation. The [verification guide](../verification/README.md) explains which finite identities are checked computationally and which general conclusions rely on the analytical proofs.
