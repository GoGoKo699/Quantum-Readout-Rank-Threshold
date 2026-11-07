# Thirty milestones for the rank boundary in quantum readout

A source supplies copies of an unknown quantum state. A fixed apparatus processes a bounded number of copies at a time and produces a classical record. This project asks how much of the state's local statistical sensitivity that record can preserve without first learning the state's eigenbasis.

The map has two phases. **M01–M12 are background/preliminaries:** they connect states, parameter changes, information metrics, copy accounting and symmetry into the precise readout question. **M13–M30 are narrative/innovation:** they connect the two-copy mechanism, the arbitrary-POVM obstruction and the exact singular coefficient into the rank classification and its scope.

The allocation gives twelve milestones to the language shared by both proofs and eighteen to the scientific argument. The construction uses conditional pure-state geometry and design moments; the converse uses support at a rank boundary and uniformity over all measurements. Both mechanisms need to remain visible before they can be compared. The final milestone of each phase integrates the preceding objects and claims.

The single educational anchor is Jasminder S. Sidhu and Pieter Kok, [*A Geometric Perspective on Quantum Parameter Estimation*][sk], *AVS Quantum Science* **2**, 014701 (2020). Section and equation numbers below refer to **arXiv:1907.06628v2**. The anchor supplies the geometric and statistical framework. The linked science pages supply the project-specific design bounds, exterior-square mechanism, Schur-sector arguments and limit statements. Those research ingredients are not presented as results of the anchor.

The notation follows the [model](../science/model.md): $`\rho`$ is a state, $`A`$ is a local state derivative, $`M`$ is a measurement, $`I_M`$ is its classical Fisher information, and $`J_\rho(A)`$ is the single-copy SLD quantum Fisher information in direction $`A`$. A block contains $`k`$ independent copies, so its quantum information is $`kJ_\rho(A)`$. The [notation bridge](ANCHOR.md#notation-translation) translates the anchor's symbols into these conventions.

## Phase I: Background/preliminaries, M01–M12

### M01: States and occupied support

**Central question.** What information about a source is specified by its state, its spectrum and its rank?

**Understanding target.** A density matrix is a positive operator of trace one. Its positive eigenvalues are the weights of occupied orthogonal directions; their span is its support. Rank counts occupied directions, while the ambient dimension counts all available directions. Knowing that the rank is two does not identify the support or provide a measurement basis.

**Dependencies and story role.** This is the starting object for the background phase. It establishes the distinction between a physical qubit and an unknown two-dimensional support inside a larger system.

**Conceptual connection.** Spectral weights and support orientation will become different kinds of statistical motion, and the two-copy apparatus will record them through different parts of its outcome.

**Source pointers.** Anchor context: [SK, Sec. IV.A][sk]. Project definitions: [Model, “States, tangents and the information convention”](../science/model.md#1-states-tangents-and-the-information-convention); physical distinction: [Interpretation, “Rank two separates weight from support”](../science/interpretation.md#rank-two-separates-weight-from-support).

### M02: Physical parameter changes and rank strata

**Central question.** Which infinitesimal changes belong to the statistical model being measured?

**Understanding target.** For a differentiable physical path $`\rho_t`$, the tangent $`A=\partial_t\rho_t|_{t=0}`$ is Hermitian and traceless. Along a smooth fixed-rank path its kernel-to-kernel block vanishes, while its support can move. A tangent within the pure-state manifold and a path that creates a new eigenvalue at a boundary require different information statements.

**Dependencies and story role.** Uses M01. It makes the allowed local motions precise before a metric is assigned to them.

**Conceptual connection.** The positive theorem concerns regular tangents within a rank stratum. The converse studies strictly positive states approaching a boundary. Keeping those roles distinct prevents a boundary limit from silently changing the model.

**Source pointers.** Anchor context: [SK, Sec. II.A and Sec. IV.D, discussion following Eq. (88)][sk]. Project convention: [Model, “States, tangents and the information convention”](../science/model.md#1-states-tangents-and-the-information-convention); endpoint distinction: [Two-copy readout, “Degenerate spectra and pure-state tangents”](../science/two-copy-readout.md#degenerate-spectra-and-pure-state-tangents).

### M03: A measurement becomes a probability model

**Central question.** How does a quantum apparatus turn state changes into an observable record?

**Understanding target.** A positive-operator-valued measurement, or POVM, assigns positive effects to outcomes, with total effect equal to the identity. Outcome probabilities are traces of effects against the state. Ancillas and adaptation within a block can be included in this description. A random setting or branch flag that is retained is part of the outcome, so it belongs in the probability model.

**Dependencies and story role.** Uses M01–M02. It connects the physical source to the classical distributions whose sensitivity will be measured.

**Conceptual connection.** The construction specifies one complete record. The converse permits every POVM, including continuous outcome spaces, so an implementation detail cannot evade its measurement model.

**Source pointers.** Anchor: [SK, Sec. IV.A][sk]. Project apparatus and outcome convention: [Model, “What a fixed apparatus may do”](../science/model.md#2-what-a-fixed-apparatus-may-do).

### M04: Classical Fisher information as local sensitivity

**Central question.** What makes a small change in a probability distribution statistically visible?

**Understanding target.** The score is the derivative of the log probability, and classical Fisher information is its mean square. Equivalently, it sums or integrates the squared probability derivative divided by the probability. This defines a local quadratic measure of distinguishability. It is different from an absolute reconstruction error or a finite-sample guarantee for an estimator.

**Dependencies and story role.** Uses M02–M03. It supplies the classical quantity that every later measurement comparison uses.

**Conceptual connection.** The probability in the denominator gives rare outcomes a distinctive role. The rank-three argument will ask whether an unknown-basis apparatus can produce outcomes carrying the rare eigenvalue's leading information.

**Source pointers.** Anchor: [SK, Sec. II.D, Eq. (24), and Sec. III.B, Eqs. (39)–(43)][sk]. Project definition: [Model, “What a fixed apparatus may do”](../science/model.md#2-what-a-fixed-apparatus-may-do); interpretation: [“Local sensitivity and statistical estimation”](../science/interpretation.md#local-sensitivity-and-statistical-estimation).

### M05: The SLD metric before a readout is chosen

**Central question.** How is the available local information defined at the quantum-state level?

**Understanding target.** The symmetric logarithmic derivative, or SLD, is an operator $`L`$ satisfying

```math
2A=\rho L+L\rho,
\qquad
J_\rho(A)=\mathrm{Tr}(\rho L^2).
```

Its kernel values do not affect the information. A measurement's classical Fisher information is bounded above by this quantum quantity. The bound identifies a local metric; a measurement attaining it may depend on the state and parameter direction.

**Dependencies and story role.** Uses M01–M04. It establishes the benchmark against which the fixed apparatus is judged.

**Conceptual connection.** Optimizing a measurement at one specified state is a different quantifier from requiring one apparatus to preserve a fraction for every state and tangent.

**Source pointers.** Anchor: [SK, Sec. IV.D, Eqs. (83), (86)–(88) and (93)][sk]. Project normalization: [Model, “States, tangents and the information convention”](../science/model.md#1-states-tangents-and-the-information-convention).

### M06: Pure-state geometry and irrelevant phase

**Central question.** Which part of a pure vector's motion changes its physical state?

**Understanding target.** A pure state is a ray, so a phase change alone has no observable effect. After removing the phase direction, its local motion is represented by a vector orthogonal to the state vector. The pure-state QFI is four times that orthogonal vector's squared norm. This simple geometry permits a uniform information comparison for randomized pure-state readout.

**Dependencies and story role.** Uses M02 and M05. It isolates the geometric ingredient that makes the rank-two antisymmetric branch useful.

**Conceptual connection.** Two mixed-state copies can produce a pure conditional state. Its purity concerns the normalized branch state, while the branch's occurrence probability must still be counted.

**Source pointers.** Anchor: [SK, Sec. IV.C, Eq. (77)][sk]. Project pure-state calculation: [Two-copy readout, “A projective 3-design information bound”](../science/two-copy-readout.md#a-projective-3-design-information-bound).

### M07: Mixed-state geometry and weak directions

**Central question.** Why can a small eigenvalue make an information guarantee difficult?

**Understanding target.** In an eigenbasis, the SLD metric weights a matrix element of the tangent by the reciprocal of the corresponding sum of eigenvalues. Diagonal changes describe spectral motion; off-diagonal changes describe motion within the support or into its orthogonal complement. A small positive eigenvalue can make a weakly occupied direction carry large local QFI.

**Dependencies and story role.** Uses M01–M02 and M05–M06. It connects state geometry to the spectral conditioning that the project seeks to remove.

**Conceptual connection.** An ordinary matrix norm treats tangent entries more evenly than the SLD metric does. The positive proof must recover the stronger weights of support motion, while the converse exploits the weight of a rare eigenvalue.

**Source pointers.** Anchor: [SK, Sec. IV.D, Eqs. (86)–(88)][sk]. Project decomposition: [Two-copy readout, “Rank-two geometry of the two sectors”](../science/two-copy-readout.md#rank-two-geometry-of-the-two-sectors); rare-eigenvalue interpretation: [“Rank three introduces a second weak direction”](../science/interpretation.md#rank-three-introduces-a-second-weak-direction).

### M08: Copy accounting and complete conditional records

**Central question.** How do input copies and recorded branches enter an information comparison?

**Understanding target.** QFI adds for independent copies, so a two-copy experiment is compared with twice the single-copy QFI. A record consisting of a branch label and a conditional result has information equal to the label's information plus the probability-weighted conditional information. If branch probabilities change with the parameter, the label contributes its own term. Every attempted block is charged.

**Dependencies and story role.** Uses M03–M05. It joins statistical accounting to the physical resources consumed by an apparatus.

**Conceptual connection.** A rare successful branch can be informative, but its conditional sensitivity must be multiplied by its actual probability. Retaining the other branch and the flag can preserve information that postselection would omit.

**Source pointers.** Anchor for product additivity: [SK, Sec. IV.B, Eq. (63)][sk]. Full flag decomposition: [Two-copy readout, “Proof of the uniform fraction”](../science/two-copy-readout.md#proof-of-the-uniform-fraction). Copy convention: [Model, “States, tangents and the information convention”](../science/model.md#1-states-tangents-and-the-information-convention).

### M09: Simultaneous parameter directions

**Central question.** What does it mean to preserve information about every local parameter direction at once?

**Understanding target.** A multiparameter Fisher matrix is a quadratic form: choosing a real direction in parameter space produces a scalar Fisher information. An inequality for every direction is equivalent to a positive-semidefinite matrix inequality. Such a retained-information bound does not assert simultaneous saturation of the SLD Cramér–Rao bound by an estimator.

**Dependencies and story role.** Uses M02, M04 and M05. It turns scalar calculations into the simultaneous statement required of a universal readout.

**Conceptual connection.** Measurement incompatibility motivates care with attainability claims. The project's positive theorem proves a uniform matrix fraction, while the negative theorem can refute that possibility using one carefully chosen direction.

**Source pointers.** Anchor: [SK, Secs. V.A–V.C, especially Eqs. (127)–(129)][sk]. Project comparison: [Model, “What a fixed apparatus may do”](../science/model.md#2-what-a-fixed-apparatus-may-do); estimation scope: [Interpretation, “Local sensitivity and statistical estimation”](../science/interpretation.md#local-sensitivity-and-statistical-estimation).

### M10: Copy permutations and basis-independent sectors

**Central question.** Which collective properties can be measured without knowing the state's eigenvectors?

**Understanding target.** Exchanging identical input registers is defined independently of their unknown basis. For two copies it separates symmetric and antisymmetric sectors. With more copies, permutation symmetry organizes the tensor power into Schur sectors. The number of occupied one-particle directions restricts which sectors can occur.

**Dependencies and story role.** Uses M01, M03 and M08. It introduces the common symmetry language behind both the constructive measurement and the converse.

**Conceptual connection.** A sector can reveal rank or support structure without revealing an eigenbasis. The same principle produces the rank-two wedge state and identifies sectors that are absent at a rank-two boundary.

**Source pointers.** Anchor context for composite states: [SK, Sec. IV.B][sk]. Project symmetry definitions: [Two-copy readout, “Measurement and theorem”](../science/two-copy-readout.md#measurement-and-theorem); general sectors: [Converse, “Separate sectors present at the rank-two boundary”](../science/finite-block-obstruction.md#1-separate-sectors-present-at-the-rank-two-boundary).

### M11: Randomized readout and moment matching

**Central question.** How can a finite measurement retain the useful averages of an isotropic random readout?

**Understanding target.** Haar averaging supplies a basis-independent reference ensemble. A finite projective 3-design has first three projector moments equal to those Haar moments. Those moments can control an information inequality without requiring a continuously sampled measurement. The chosen setting remains part of the observed record.

**Dependencies and story role.** Uses M03–M06 and M08. It supplies the randomized measurement ingredient and explains why a finite physical apparatus can realize the needed symmetry.

**Conceptual connection.** The positive theorem needs only a few ensemble moments. Its universality comes from their exact identities, together with the structure created by the exchange measurement.

**Source pointers.** Anchor context for measurement choice: [SK, Secs. IV.A and IV.I][sk]. Project definition and moment argument: [Two-copy readout, “A projective 3-design information bound”](../science/two-copy-readout.md#a-projective-3-design-information-bound); finite realization: [“Implementation and resource accounting”](../science/two-copy-readout.md#implementation-and-resource-accounting).

### M12: The universal readout question

**Central question.** What must one fixed apparatus accomplish for a rank promise to be operationally useful?

**Understanding target.** Combine the state class, regular tangents, complete outcome record and copy budget into the requirement

```math
I_M(\rho;A)\ge c\,kJ_\rho(A).
```

Here $`c\gt0`$ is uniform over the unknown spectrum, eigenbasis and tangent. The constructive apparatus may use the known dimension. Its rank promise does not supply the support, and its coherent block is reset between runs.

**Dependencies and story role.** Integrates M01–M11. It closes the background phase with the exact problem that the two proofs address.

**Conceptual connection.** Local quantum geometry, symmetry and physical copy costs now meet in one comparison. The central issue is whether bounded coherent processing can remove spectral conditioning before basis calibration.

**Source pointers.** Anchor context: [SK, Sec. IV.I and Secs. V.A–V.C][sk]. Project quantifiers: [Model, “What a fixed apparatus may do”](../science/model.md#2-what-a-fixed-apparatus-may-do); resource model: [Interpretation, “The coherent block is the constrained resource”](../science/interpretation.md#the-coherent-block-is-the-constrained-resource).

## Phase II: Narrative/innovation, M13–M30

### M13: The complete two-copy apparatus

**Central question.** What physical record does the proposed universal rank-two measurement produce?

**Understanding target.** The apparatus receives two fresh copies, measures exchange parity, and performs the same projective 3-design readout on the full pair register in either branch. Its output contains the parity, the design setting and the final result. The measurement depends on the dimension but does not select a basis using the unknown state or tangent.

**Dependencies and story role.** Uses M08 and M10–M12. It begins the narrative with the concrete operation whose information will be analyzed.

**Conceptual connection.** This combines a collective operation that reorganizes the state with a fixed readout that extracts information from the resulting branches. Both branches belong to one experiment and one two-copy budget.

**Source pointers.** Anchor context: [SK, Sec. IV.A][sk]. Project protocol: [Two-copy readout, “Measurement and theorem”](../science/two-copy-readout.md#measurement-and-theorem); theorem overview: [Model, “The rank-two construction”](../science/model.md#3-the-rank-two-construction).

### M14: The antisymmetric branch separates weight and support

**Central question.** Why does the antisymmetric part of two rank-two copies have a pure normalized state?

**Understanding target.** For occupied orthonormal eigenvectors $`|u_1\rangle,|u_2\rangle`$ with positive weights $`\lambda_1,\lambda_2`$, their normalized antisymmetric combination is $`|u_1\wedge u_2\rangle`$. The branch has the form

```math
P_-\rho^{\otimes2}P_-
=q\,|u_1\wedge u_2\rangle\langle u_1\wedge u_2|,
\qquad q=\lambda_1\lambda_2.
```

The probability carries spectral weight. The pure state represents the occupied plane, with internal basis changes affecting only an irrelevant phase.

**Dependencies and story role.** Uses M01, M06, M10 and M13. It identifies the mechanism that makes the rank-two construction work.

**Conceptual connection.** An unknown mixed-state support becomes accessible through pure-state geometry without assuming that the branch can be prepared for free.

**Source pointers.** Anchor for pure-state geometry: [SK, Sec. IV.C, Eq. (77)][sk]. Project identity and derivative: [Two-copy readout, “Antisymmetric branch”](../science/two-copy-readout.md#antisymmetric-branch); meaning: [Interpretation, “Rank two separates weight from support”](../science/interpretation.md#rank-two-separates-weight-from-support).

### M15: The symmetric branch retains complementary motion

**Central question.** What information remains outside the pure antisymmetric branch?

**Understanding target.** The symmetric branch has probability $`s=1-q`$ and normalized state $`\tau_+`$. Its three occupied pair states carry eigenvalue changes, rotations inside the original support, and support motion. The normalized derivative $`Y=\partial_t\tau_+`$ includes the derivative of the branch normalization. Its squared Hilbert–Schmidt norm separates into the original tangent components without cross terms.

**Dependencies and story role.** Uses M02, M07 and M13–M14. It supplies the complementary branch needed for a statement about every tangent direction.

**Conceptual connection.** The symmetric conditional state can have rank three, but the proof only needs a matrix-norm information bound for this structured branch. The final benchmark remains the QFI of the rank-two inputs.

**Source pointers.** Anchor context for mixed-state tangents: [SK, Sec. IV.D, Eqs. (86)–(88)][sk]. Project calculation: [Two-copy readout, “Symmetric branch”](../science/two-copy-readout.md#symmetric-branch).

### M16: Third moments supply the conditional information bounds

**Central question.** Which quantitative guarantee does the design readout provide in each branch?

**Understanding target.** For a normalized conditional state $`\sigma`$ and regular tangent $`B`$, the first three design moments and Cauchy–Schwarz imply

```math
I_3(\sigma;B)\ge\frac13\mathrm{Tr}(B^2).
```

When $`\sigma`$ and $`B`$ belong to a pure-state path, the same argument gives $`I_3(\sigma;B)\ge J_\sigma(B)/4`$. The general matrix-norm bound and the stronger pure-state bound serve different branches.

**Dependencies and story role.** Uses M05–M07, M11 and M14–M15. It connects the measurement's finite moment identities to the branch quantities computed from the state.

**Conceptual connection.** The proof uses a lower bound from a concrete readout, in addition to the general quantum upper benchmark. It needs no knowledge of the conditional state's eigenbasis.

**Source pointers.** Anchor for the measurement/QFI comparison: [SK, Sec. IV.D, Eq. (93)][sk]. Project lower bounds and their moment derivation: [Two-copy readout, “A projective 3-design information bound”](../science/two-copy-readout.md#a-projective-3-design-information-bound).

### M17: The full record compensates for a rare branch

**Central question.** How can a branch with small probability still protect the required information fraction?

**Understanding target.** The complete Fisher information includes the binary flag and both probability-weighted conditional readouts. The antisymmetric support derivative contains inverse eigenvalue factors. Its increased conditional sensitivity can balance a small occurrence probability when compared with the corresponding single-copy SLD weight. The symmetric branch and the flag retain the remaining information.

**Dependencies and story role.** Uses M07–M08 and M14–M16. It combines the branch calculations into a physically charged information certificate.

**Conceptual connection.** The mechanism is visible only after probability and conditional sensitivity are combined. A success probability alone does not determine the information efficiency of a flagged measurement.

**Source pointers.** Anchor for copy normalization: [SK, Sec. IV.B, Eq. (63)][sk]. Full branch identity and certificate: [Two-copy readout, “Proof of the uniform fraction”](../science/two-copy-readout.md#proof-of-the-uniform-fraction); physical explanation: [Interpretation, “Rank two separates weight from support”](../science/interpretation.md#rank-two-separates-weight-from-support).

### M18: One constant covers every regular rank-two direction

**Central question.** Why does the branch certificate imply a uniform multiparameter guarantee?

**Understanding target.** Eigenvalue motion, motion within the occupied support, and motion of each occupied direction into the kernel account for the full rank-two tangent. Comparing their coefficients gives

```math
I_M(\rho;A)\ge\frac16J_\rho(A)=\frac1{12}J_2(\rho;A).
```

The bound remains valid at equal positive eigenvalues. For tangents within the pure-state manifold, the same apparatus has the separate bound $`I_M\ge J_2/4`$. The constant $`1/12`$ is a certified fraction, with no optimality claim.

**Dependencies and story role.** Uses M07, M09 and M14–M17. It completes the constructive proof by integrating all tangent components and endpoint conventions.

**Conceptual connection.** The scalar component comparison becomes a matrix inequality because it holds for every physical direction. Unknown support motion is included, so the result extends beyond a fixed physical qubit.

**Source pointers.** Anchor for the matrix viewpoint: [SK, Sec. V.A, Eqs. (127)–(129)][sk]. Project proof: [“Proof of the uniform fraction”](../science/two-copy-readout.md#proof-of-the-uniform-fraction); degeneracy and pure-state scope: [“Degenerate spectra and pure-state tangents”](../science/two-copy-readout.md#degenerate-spectra-and-pure-state-tangents).

### M19: The physical cost of the construction

**Central question.** Which resources make the abstract two-copy measurement an executable readout?

**Understanding target.** For an input encoded in $`n`$ qubits, the pair uses $`2n`$ data qubits and one SWAP-control ancilla. A controlled exchange followed by ancilla readout resolves parity without discarding the pair. Random Clifford readout supplies a finite 3-design with polynomial sampling and gate costs under the stated ideal encoded-register model. Two fresh copies and all classical settings are counted.

**Dependencies and story role.** Uses M03, M08, M11 and M13–M18. It connects the proved apparatus with its physical resources.

**Conceptual connection.** Efficient execution of the readout establishes a measurement resource statement. Classical likelihood evaluation, finite-sample inference and robustness to imperfect gates have additional requirements.

**Source pointers.** Anchor context for an estimation procedure: [SK, Secs. IV.A and IV.I][sk]. Project implementation assumptions: [Two-copy readout, “Implementation and resource accounting”](../science/two-copy-readout.md#implementation-and-resource-accounting); coherent-block model: [Interpretation, “The coherent block is the constrained resource”](../science/interpretation.md#the-coherent-block-is-the-constrained-resource).

### M20: A third occupied direction changes the question

**Central question.** Which local signal exposes the weakness of every fixed block at rank three?

**Understanding target.** The converse uses the full-rank qutrit family

```math
\rho_{\eta,p,U}
=U\,\mathrm{diag}(1-\eta-p,\eta,p)\,U^\dagger,
\qquad 0\lt p\lt\eta\le\frac14.
```

The varying parameter is $`p`$; $`\eta`$ and the eigenbasis $`U`$ are fixed. Its QFI is $`J_{\eta,p}=1/p+1/(1-\eta-p)`$. The apparatus may know the nominal spectrum, but it cannot use $`U`$ and is held fixed in the derivative.

**Dependencies and story role.** Uses M02, M05, M07 and M12. It introduces the concrete obstruction family after the positive theorem has been established.

**Conceptual connection.** The large local weight of a rare population is available to an aligned detector. The universal-apparatus question asks whether that weight remains accessible without the alignment.

**Source pointers.** Anchor for spectral SLD information and measurement choice: [SK, Sec. IV.D, Eqs. (86)–(88), and Sec. IV.I][sk]. Project family and derivative convention: [Converse, “Statement and measurement dependence”](../science/finite-block-obstruction.md#statement-and-measurement-dependence).

### M21: Schur refinement isolates the common kernel

**Central question.** How can a statement about arbitrary measurements be reduced to symmetry sectors?

**Understanding target.** The $`k`$-copy state and its derivative are block diagonal in Schur sectors. Recording a sector label refines the outcomes and cannot decrease classical Fisher information. At $`p=0`$, sectors with at most two rows are populated, while three-row sectors form a common kernel. Write $`\mathcal K_k`$ for that singular subspace and $`\Pi_{\mathcal K_k}`$ for its projector.

**Dependencies and story role.** Uses M04, M10 and M20. It converts the unknown measurement problem into regular and singular contributions with different boundary behavior.

**Conceptual connection.** A rank certificate identifies a sector absent for every rank-two eigenbasis. This common absence is stronger than an outcome being rare in one particular basis.

**Source pointers.** Anchor context for classical information and composite states: [SK, Sec. II.D and Sec. IV.B][sk]. Project refinement and support structure: [Converse, “Separate sectors present at the rank-two boundary”](../science/finite-block-obstruction.md#1-separate-sectors-present-at-the-rank-two-boundary).

### M22: Unknown eigenbases populate regular effects

**Central question.** Why does a nonzero regular-sector effect usually have positive probability at the boundary?

**Understanding target.** Haar averaging of the boundary state is strictly positive on each regular representation block. Irreducibility and the state's identity on the permutation multiplicity space give this statement for every nonzero positive effect, including effects within multiplicities. Real-analyticity then implies positive boundary probability for almost every eigenbasis.

**Dependencies and story role.** Uses M10–M11 and M21. It supplies the pointwise support fact needed for the regular-sector information limit.

**Conceptual connection.** Haar measure is a proof device for locating a poorly served eigenbasis; the result does not require a source that randomly redraws its basis. Averaging also exposes why a hidden multiplicity cannot furnish an extra rare-outcome channel.

**Source pointers.** Anchor context for the measurement model: [SK, Sec. IV.A][sk]. Project irreducibility, multiplicity and almost-everywhere argument: [Converse, “Separate sectors present at the rank-two boundary”](../science/finite-block-obstruction.md#1-separate-sectors-present-at-the-rank-two-boundary).

### M23: A common bound controls the singularity

**Central question.** What permits a boundary limit to pass through an average over eigenbases?

**Understanding target.** The effectwise SLD bound controls a measurement contribution by the positive operator $`p\rho_{\eta,p,U}^{\otimes k}L_{k,p,U}^2`$, where $`L_{k,p,U}`$ is the product-state SLD. For the stated family,

```math
0\preceq p\rho_{\eta,p,U}^{\otimes k}L_{k,p,U}^2
\preceq4k^2\mathbb I.
```

This supplies a common dominating constant for trace-one effects. Positive regular-sector boundary probability then makes the leading $`1/p`$ coefficient vanish for each fixed regular effect.

**Dependencies and story role.** Uses M05, M08 and M20–M22. It turns a support observation into a controlled information limit.

**Conceptual connection.** The conclusion concerns the leading singular coefficient. Regular-sector information may still be finite or diverge more slowly; the argument does not need to eliminate those contributions.

**Source pointers.** Anchor for the SLD information bound: [SK, Sec. IV.D, Eq. (93)][sk]. Project domination proof: [Converse, “Bound the effectwise singularity”](../science/finite-block-obstruction.md#2-bound-the-effectwise-singularity).

### M24: Uniformity covers every apparatus and outcome space

**Central question.** Why can the apparatus not avoid the limit by changing its effects with the nominal spectrum?

**Understanding target.** Trace-normalized positive effects form a compact set in a fixed finite-dimensional sector. A convergent subsequence, the boundary positivity from M22 and the domination from M23 upgrade fixed-effect convergence to uniform convergence over effects. The finite trace measure of a POVM then covers arbitrarily many or continuously many outcomes, even when the outcome space changes with nominal $`p`$.

**Dependencies and story role.** Uses M03 and M21–M23. It completes the decisive step from individual effects to the full arbitrary-POVM statement.

**Conceptual connection.** The proof needs uniformity before optimizing over measurements. Compactness is applied to normalized effects, without assuming a finite list of candidate apparatuses or a bounded number of outcomes.

**Source pointers.** Anchor context for measurement optimization: [SK, Sec. IV.I][sk]. Project uniformity: [Converse, “Uniform convergence over regular effects”](../science/finite-block-obstruction.md#3-uniform-convergence-over-regular-effects); arbitrary outcomes: [“Continuous and changing outcome spaces”](../science/finite-block-obstruction.md#continuous-and-changing-outcome-spaces).

### M25: The surviving information is a rank-certificate weight

**Central question.** Which part of the tensor power can still carry leading information about the rare third population?

**Understanding target.** Only the singular sectors can retain a leading $`1/p`$ contribution. Let $`w_k(p)`$ be the probability of $`\mathcal K_k`$ and define $`\beta_k(\eta)=w_k'(0)`$. The limiting operator counts strings containing exactly one third eigenvector. A contributing string must also contain the second eigenvector, giving

```math
\beta_k(\eta)\le
k\bigl[1-(1-\eta)^{k-1}\bigr].
```

Combined with M24, this bounds the leading information of every POVM.

**Dependencies and story role.** Uses M20–M24. It identifies the physical and mathematical source of the obstruction.

**Conceptual connection.** A universally recognizable third direction requires a coincidence with another occupied weak direction. The rank certificate's appearance probability therefore limits the available singular information.

**Source pointers.** Anchor context for spectral sensitivity: [SK, Sec. IV.D, Eqs. (86)–(88)][sk]. Project limiting operator and coefficient: [Converse, “Bound the surviving singular sectors”](../science/finite-block-obstruction.md#4-bound-the-surviving-singular-sectors).

### M26: The exact coefficient is a word event

**Central question.** How does the required coincidence produce an exact finite-block coefficient?

**Understanding target.** The Schur distribution equals the Young-diagram distribution of an independent eigenvalue-label word under Robinson–Schensted–Knuth insertion. Three rows require a strictly decreasing subsequence of length three. At first order in $`p`$, there is one letter 3; a 2 and then a 1 must follow it. With $`a=1-\eta`$, $`b=\eta`$ and $`h_m(a,b)=\sum_{j=0}^m a^j b^{m-j}`$,

```math
\beta_k(\eta)=\sum_{m=0}^{k-1}\bigl[1-h_m(a,b)\bigr].
```

This yields $`\beta_1=\beta_2=0`$, $`\beta_3=\eta(1-\eta)`$ and $`\beta_4=3\eta(1-\eta)`$.

**Dependencies and story role.** Uses M10, M21 and M25. It sharpens the coarse rare-coincidence bound into an exact coefficient.

**Conceptual connection.** The combinatorial event records the permutation structure as well as the presence of labels. It explains why counting every occurrence of the two weak directions would overestimate the surviving coefficient.

**Source pointers.** Anchor context for the information being quantified: [SK, Sec. IV.D][sk]. Project derivation: [Singular information, “From a Schur sector to a word event”](../science/singular-information.md#1-from-a-schur-sector-to-a-word-event) and [“A positive formula and small blocks”](../science/singular-information.md#2-a-positive-formula-and-small-blocks). Research dependency: [OW15, Proposition 2.23, Remark 2.24 and Theorem 2.14](../references/RELATED_WORK.md#ow15).

### M27: A binary measurement attains the leading minimax value

**Central question.** Is the singular coefficient only an upper bound, or can one apparatus attain it for every eigenbasis?

**Understanding target.** Define $`R_k(\eta,p)`$ as the best worst-eigenbasis fraction $`I_M/(kJ_{\eta,p})`$ over allowed POVMs. The uniform converse bounds its upper limit. The binary measurement $`\{\Pi_{\mathcal K_k},\mathbb I-\Pi_{\mathcal K_k}\}`$ has basis-independent probability $`w_k(p)=\beta_k(\eta)p+O(p^2)`$ and attains the matching leading Fisher coefficient. Thus

```math
\lim_{p\downarrow0}R_k(\eta,p)=\frac{\beta_k(\eta)}k.
```

This optimum concerns the displayed spectral tangent and its leading singular term.

**Dependencies and story role.** Uses M09, M24–M26. It closes the converse with a matching operational construction.

**Conceptual connection.** The same rank certificate both limits arbitrary readout and attains the surviving information. Optimality here does not extend to every multiparameter direction or every positive value of $`p`$.

**Source pointers.** Anchor context for measurement optimization and attainability: [SK, Sec. IV.I and Sec. V.C][sk]. Project quantifiers: [Singular information, “The exact limiting minimax value”](../science/singular-information.md#the-exact-limiting-minimax-value); matching bounds: [“Why this coefficient is optimal”](../science/singular-information.md#3-why-this-coefficient-is-optimal).

### M28: Two copies are necessary at rank two

**Central question.** What rules out a one-copy universal replacement for the successful two-copy apparatus?

**Understanding target.** For an unknown-basis qubit with eigenvalues $`1-p,p`$, the boundary is pure. Its unitary orbit spans the entire one-copy Hilbert space, so there is no common singular sector. The uniform effect argument makes the best basis-blind one-copy fraction vanish as $`p\downarrow0`$, even with nominal-spectrum information. Together with M18, this makes two the minimum fixed block for arbitrary rank-two models.

**Dependencies and story role.** Uses M06, M18 and M22–M24. It returns from the general obstruction machinery to the necessity half of the positive classification.

**Conceptual connection.** The rank-two advantage requires a collective sector that one copy does not possess. A rank promise alone does not provide the eigenbasis needed for a locally optimized single-copy detector.

**Source pointers.** Anchor for pure-state geometry and optimized readout: [SK, Sec. IV.C and Sec. IV.I][sk]. Project necessity proof: [Converse, “Why rank two needs two copies”](../science/finite-block-obstruction.md#5-why-rank-two-needs-two-copies).

### M29: The order of limits determines the resource claim

**Central question.** How do fixed blocks and growing blocks differ when two eigenvalues become rare?

**Understanding target.** At each fixed finite $`k`$, taking $`p\downarrow0`$ first and then $`\eta\downarrow0`$ makes the optimum fraction vanish. At fixed positive $`\eta`$, taking $`p\downarrow0`$ first and then $`k\to\infty`$ recovers the full leading coefficient:

```math
\lim_{\eta\downarrow0}\lim_{p\downarrow0}R_k(\eta,p)=0,
\qquad
\lim_{k\to\infty}\lim_{p\downarrow0}R_k(\eta,p)=1.
```

These statements provide no remainder uniform in all three quantities and no matched copy-complexity law at finite $`p`$.

**Dependencies and story role.** Uses M08, M20 and M25–M27. It integrates the exact coefficient with the fixed-resource premise before the final classification.

**Conceptual connection.** The obstruction says that each fixed apparatus size can be defeated by some spectrum. Growing coherent blocks and finite-sample estimation introduce separate scaling questions.

**Source pointers.** Anchor context for repeated data and statistical bounds: [SK, Secs. II.C–II.D and IV.E][sk]. Project limits: [Singular information, “Consequence for uniform rank-three readout”](../science/singular-information.md#4-consequence-for-uniform-rank-three-readout); boundary convention: [Converse, “Scope of the conclusion”](../science/finite-block-obstruction.md#scope-of-the-conclusion).

### M30: The rank boundary as one scientific account

**Central question.** What do the positive mechanism and the universal obstruction establish together?

**Understanding target.** Pure-state families admit a positive universal fraction with one copy. Arbitrary regular rank-two families require two copies, and the stated apparatus retains at least $`1/12`$ of pair QFI. Already among rank-three qutrits, no fixed finite coherent block retains a uniform positive fraction. This classification concerns local SLD information before eigenbasis calibration, with all input copies counted.

**Dependencies and story role.** Integrates M12, M18–M19 and M25–M29. It closes the narrative with the contribution, its mechanism and its operational scope.

**Conceptual connection.** Rank two separates spectral weight from a pure representation of support. Rank three introduces an additional weak-direction coincidence. The resulting information boundary coexists with different reconstruction losses, adaptive calibration and persistent-memory protocols because those change the objective or resource model. The symmetry and design tools are established ingredients; the stated classification depends on their complete rank-two analysis and the all-POVM converse.

**Source pointers.** Anchor context for geometric information, estimation and attainability: [SK, Secs. III.B, IV.E and V.C][sk]. Project synthesis: [Model, “Classification and provenance”](../science/model.md#5-classification-and-provenance); operational and statistical meaning: [Interpretation, “What is established”](../science/interpretation.md#what-is-established) and [“Local sensitivity and statistical estimation”](../science/interpretation.md#local-sensitivity-and-statistical-estimation); attribution: [Related work, “Contribution and priority boundary”](../references/RELATED_WORK.md#contribution-and-priority-boundary).

[sk]: https://arxiv.org/pdf/1907.06628v2
