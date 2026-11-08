# Thirty milestones for quantum readout, rank and calibration

The map follows one scientific question: how much local state sensitivity can a complete measurement record preserve when the eigenbasis is unknown? It covers the rank classification and the precise comparison between learned single-copy calibration and a fixed two-copy apparatus.

**M01–M10 are background/preliminaries.** They connect individual states, tangents, records and information metrics into the complete experiment. **M11–M30 are narrative/innovation.** They connect the rank-two construction, rank-three obstruction and exact Haar comparison into their physical and statistical scope. Ten foundational milestones suffice for the shared language; twenty narrative milestones retain the different proof mechanisms and their eventual synthesis. The allocation is determined by this project, not by a learner's prior knowledge.

The single educational anchor is **DDG20**, Demkowicz-Dobrzański, Górecki and Guţă, [*Multi-parameter estimation beyond quantum Fisher information*, arXiv:2001.11742v2](https://arxiv.org/html/2001.11742v2). Section references identify that version. The [anchor bridge](ANCHOR.md) maps its notation and explains the additional project-specific arguments. DDG20 supplies statistical foundations; the scientific pages supply design, wedge, Schur and exact-Haar proofs with their research attribution.

## Phase I: Background/preliminaries, M01–M10

### M01: States, spectrum and occupied support

**Central question.** What does rank reveal about an unknown source, and what does it leave unknown?

**Understanding target.** A density matrix is positive with trace one. Its positive eigenvalues weight occupied orthogonal directions, and their span is its support. A rank-two promise does not provide the support orientation. A rank-two state in a qutrit therefore carries more local directions than a qubit whose entire Hilbert space is supplied.

**Dependencies and story role.** No previous milestone is required. This introduces the source before its measurement or statistical objective.

**Conceptual connection.** The distinction between weights and orientation becomes the separation between spectral information and support information in the SWAP branches.

**Source pointers.** DDG20 Section 1.2; [model](../science/model.md).

### M02: Physical paths within a rank stratum

**Central question.** Which state changes belong to the local model?

**Understanding target.** A differentiable, trace-preserving state path has a Hermitian traceless tangent. On the exact-rank manifold its kernel-to-kernel block vanishes, while occupied eigenvalues and support orientation may vary. A limit through positive eigenvalues is distinct from substituting the lower-rank tangent space at its endpoint.

**Dependencies and story role.** Uses M01. It specifies allowed changes before assigning them an information metric.

**Conceptual connection.** The rank-two positive result and the strictly positive rank-three obstruction approach boundaries in different ways.

**Source pointers.** DDG20 Sections 1.2 and 2.2; [model](../science/model.md).

### M03: A fixed apparatus defines a probability model

**Central question.** How does a quantum measurement turn a state path into a complete classical record?

**Understanding target.** A POVM has positive effects summing or integrating to the identity. Tracing an effect against the state gives its outcome probability. Recorded settings and branch flags are parts of that outcome; ancillas and adaptation inside one coherent block can be included in one block POVM.

**Dependencies and story role.** Uses M01–M02. It connects the physical source to the classical experiment.

**Conceptual connection.** The constructive protocol specifies one such record; the converse permits every POVM, including continuous outcomes.

**Source pointers.** DDG20 Sections 1.2 and 2.1; [model](../science/model.md).

### M04: Scores and rare outcomes

**Central question.** What makes a small probability change statistically visible?

**Understanding target.** The score is the local derivative of log probability. Its mean square is Fisher information, equivalently a sum of squared probability derivatives divided by probabilities. A rare outcome can carry substantial local information, but an unweighted conditional information is not its contribution per input attempt.

**Dependencies and story role.** Uses M02–M03. It introduces the measured information before the quantum benchmark.

**Conceptual connection.** The rare antisymmetric branch and the rare third-eigenvalue sectors must be probability weighted throughout the proofs.

**Source pointers.** DDG20 Section 2.1; [complete-record bridge](ANCHOR.md#why-the-complete-record-matters).

### M05: The SLD quantum benchmark

**Central question.** How is local sensitivity defined before choosing the readout?

**Understanding target.** The SLD solves $`2A=\rho L+L\rho`$ and gives $`J_\rho(A)=\mathrm{Tr}(\rho L^2)`$. The spectral formula weights each tangent matrix element by its occupied eigenvalue sum. A measurement cannot exceed this scalar information for one specified direction, but an attaining measurement may depend on that direction and state.

**Dependencies and story role.** Uses M01–M04. It gives the denominator in every retained-information fraction.

**Conceptual connection.** The weak support direction has a different quantum scale from strong support motion, so raw FI eigenvalues are not directly comparable.

**Source pointers.** DDG20 Section 2.2; [state-to-record bridge](ANCHOR.md#a-local-path-and-its-classical-information).

### M06: Matrices, worst directions and nuisance coordinates

**Central question.** Why must an unknown-basis comparison use a full Fisher matrix?

**Understanding target.** A directional inequality for every real parameter combination is a matrix inequality. The smallest QFI-normalized eigenvalue measures simultaneous protection. If eigenvectors are nuisance parameters, effective target information comes from a Schur complement of the full matrix; a target diagonal treats those nuisance coordinates as known.

**Dependencies and story role.** Uses M04–M05. It identifies the statistical objective and prevents scalar-coordinate comparisons from replacing it.

**Conceptual connection.** The exact Haar comparison later reduces seven tangent directions to four symmetry classes while retaining all nuisance couplings.

**Source pointers.** DDG20 Sections 2.1, 2.2 and 2.7; [model](../science/model.md); [Haar comparison](../science/haar-pair-readout.md).

### M07: Independent copies and coherent blocks

**Central question.** What is the correct information denominator for a joint readout?

**Understanding target.** Independent-copy SLD information is additive: a coherent block of $`k`$ inputs has quantum information $`kJ`$. Repeating a pair apparatus $`N/2`$ times yields total information $`(N/2)I_{\rm pair}`$ from $`N`$ copies. Ancillas, unsuccessful branches and a pilot do not create free input specimens.

**Dependencies and story role.** Uses M03–M06. It fixes the charged resource before comparing one-copy and joint apparatuses.

**Conceptual connection.** Pair information must be normalized by $`2J`$, and a paid adaptive experiment by $`NJ`$.

**Source pointers.** DDG20 Section 2.10; [copy-budget bridge](ANCHOR.md#one-apparatus-and-the-copy-budget).

### M08: Conditional records and the Fisher chain rule

**Central question.** How do branch frequencies and conditional measurements combine?

**Understanding target.** The joint score splits into a branch score and a conditional score of mean zero. Its FI is the flag information plus the probability-weighted conditional FI. The matrix identity extends to adaptive histories because conditional cross terms vanish, provided the selected apparatus is fixed when differentiating at each history.

**Dependencies and story role.** Uses M04 and M07. It unifies parity records with pilot-selected readout.

**Conceptual connection.** Both the positive two-copy proof and the paid single-copy comparison use this same accounting, with different physical resources.

**Source pointers.** DDG20 Section 2.1; [record bridge](ANCHOR.md#why-the-complete-record-matters); [two-copy proof](../science/two-copy-readout.md).

### M09: Fixed apparatus, calibration and asymptotic scope

**Central question.** Which information may the apparatus use before the unknown state is measured?

**Understanding target.** A fixed universal readout lacks the eigenbasis; a calibrated readout is supplied it; an adaptive strategy learns from charged earlier copies. These are different experiments. Fixed-state localization arguments do not automatically supply uniform finite-sample calibration as an occupied eigenvalue shrinks.

**Dependencies and story role.** Uses M01–M08. It fixes the order of access and the central uniformity quantifier.

**Conceptual connection.** The same small eigenvalue can control measurement sensitivity and the cost of learning a useful basis, without defining one universal crossover.

**Source pointers.** DDG20 Sections 4.5 and 4.6.3; [interpretation](../science/interpretation.md).

### M10: The full fixed-readout question

**Central question.** How do the state family, apparatus and statistical objective form one problem?

**Understanding target.** The background phase combines the rank promise, regular tangents, complete record, coherent-block budget and full-matrix SLD fraction. The task is one apparatus protecting all permitted directions uniformly over unknown spectra and supports. It is distinct from optimizing a scalar direction or proving a reconstruction risk bound.

**Dependencies and story role.** Uses M01–M09. This closes the background phase by stating the complete experiment and its comparison criteria.

**Conceptual connection.** The narrative phase can now ask why rank two succeeds, rank three fails, and coherent pairs compare differently with learned one-copy calibration.

**Source pointers.** DDG20 Sections 2.7, 2.10–2.11; [model](../science/model.md).

## Phase II: Narrative/innovation, M11–M30

### M11: The pure-state baseline

**Central question.** Why can randomized one-copy readout preserve pure-state sensitivity?

**Understanding target.** For pure-state manifold tangents, projective 3-design moments give a constant fraction of SLD information. The statement concerns tangents within the pure-state manifold, not a path creating an additional eigenvalue. This inherited result sets the first row of the rank classification.

**Dependencies and story role.** Uses M05 and M10. It starts the narrative with the simpler boundary family.

**Conceptual connection.** The same conditional pure-state geometry will reappear inside the antisymmetric branch of a mixed rank-two input.

**Source pointers.** DDG20 Sections 2.2 and 3.1; [two-copy design bound](../science/two-copy-readout.md); [attribution](../references/RELATED_WORK.md).

### M12: Resolving SWAP parity

**Central question.** What does exchange symmetry reveal without an eigenbasis?

**Understanding target.** The exchange projectors separate a pair into symmetric and antisymmetric sectors. For occupied weights $`1-t,t`$, the antisymmetric probability is $`t(1-t)`$. Its flag alone loses first-order spectral sensitivity at equal weights, so the conditional measurements remain necessary.

**Dependencies and story role.** Uses M03, M07–M08 and M11. It introduces the state-independent physical primitive.

**Conceptual connection.** The flag supplies some spectral information while preparing a conditional state with useful support geometry.

**Source pointers.** DDG20 Sections 2.1 and 2.10; [worked parity example](ANCHOR.md#worked-example-what-the-parity-flag-knows).

### M13: The pure wedge encodes support motion

**Central question.** Why is the rank-two antisymmetric branch especially useful?

**Understanding target.** The normalized branch is the pure wedge of the two occupied eigenvectors. Its orientation describes the two-dimensional occupied subspace. Differentiating the wedge detects each occupied-to-kernel motion, including motion of a weakly occupied direction; internal occupied rotations do not change that support.

**Dependencies and story role.** Uses M02, M05 and M12. It connects the physical branch to the positive proof mechanism.

**Conceptual connection.** A rare branch can retain weak-support sensitivity because its conditional derivative grows in precisely the compensating quantum scale.

**Source pointers.** DDG20 Section 2.2 for pure-state information; [rank-two geometry](../science/two-copy-readout.md).

### M14: Three design moments become an information bound

**Central question.** How does a fixed randomized measurement control an unknown conditional state?

**Understanding target.** A projective 3-design matches the first three Haar projector moments. Cauchy–Schwarz converts second and third moment identities into a lower bound on the measured FI. The pure conditional wedge admits a stronger bound than a general mixed branch. The design itself requires no state-dependent calibration.

**Dependencies and story role.** Uses M04–M05 and M13. It supplies the measurement ingredient before combining the tangent classes.

**Conceptual connection.** Finite 3-design moments provide a conservative universal certificate; a complete Haar distribution later permits exact information integrals.

**Source pointers.** DDG20 Sections 2.1–2.2; [design lemma and attribution](../science/two-copy-readout.md).

### M15: Every rank-two tangent component is covered

**Central question.** How do the flag and both branches protect the whole model?

**Understanding target.** The proof separates eigenvalue changes, occupied coherences and each occupied-to-kernel motion. The flag, symmetric derivative norm and probability-weighted pure wedge information jointly bound every term of the SLD quadratic form. This establishes at least $`1/12`$ of pair QFI in arbitrary ambient dimension.

**Dependencies and story role.** Uses M06–M08 and M12–M14. It integrates the positive mechanism into a full-matrix theorem.

**Conceptual connection.** The weak eigenvalue may approach zero without destroying the certificate because the antisymmetric contribution covers weak support motion.

**Source pointers.** DDG20 Sections 2.2 and 2.10; [uniform fraction proof](../science/two-copy-readout.md).

### M16: Finite implementation and its boundaries

**Central question.** What physical resources realize the finite-design theorem?

**Understanding target.** On qubit registers, a nondestructive SWAP test followed by random Clifford readout implements the required finite design. Each branch is measured and retained. Polynomial physical control does not imply efficient likelihood evaluation or an estimator for every statistical model. The exact Haar companion is a different continuous implementation.

**Dependencies and story role.** Uses M07, M14–M15. It attaches the positive theorem to an explicit apparatus without adding an unproved computational claim.

**Conceptual connection.** The finite certificate remains valid while sharper continuous-Haar constants are analyzed separately.

**Source pointers.** DDG20 Sections 2.10–2.11; [implementation](../science/two-copy-readout.md); [verification](../verification/README.md).

### M17: A third occupied eigenvalue changes the task

**Central question.** Why can rank-three qutrits defeat a fixed block?

**Understanding target.** The hard family has eigenvalues $`1-\eta-p,\eta,p`$ in an unknown basis. The rare eigenvalue has SLD information diverging as $`1/p`$. The converse asks which outcomes of any finite-block apparatus can retain a leading term with a coefficient uniform in the second weak eigenvalue.

**Dependencies and story role.** Uses M04–M05, M09–M10 and M15. It opens the converse with the tangent and singular scale that must be controlled.

**Conceptual connection.** Rank-three failure is not a failure of the displayed rank-two apparatus; it quantifies over every fixed finite-block POVM.

**Source pointers.** DDG20 Section 2.2; [converse model](../science/finite-block-obstruction.md).

### M18: Schur sectors detect genuinely new support

**Central question.** Which symmetry sectors can carry leading rare-eigenvalue information?

**Understanding target.** Sectors with at least three rows vanish on rank-two states and appear when a third occupied direction is present. They can therefore produce probabilities linear in the rare eigenvalue. Regular sectors already present at rank two require a separate upper-bound argument; identifying the singular sectors alone is not the converse.

**Dependencies and story role.** Uses M12 and M17. It identifies the representation-theoretic mechanism before proving optimality.

**Conceptual connection.** The three-copy fully antisymmetric event is a small worked instance of a general rank certificate.

**Source pointers.** DDG20 Section 2.10 for multiple-copy context; [finite-block reduction](../science/finite-block-obstruction.md); [coefficient](../science/singular-information.md).

### M19: Uniformity over all measurement effects

**Central question.** What turns a symmetry observation into an arbitrary-POVM converse?

**Understanding target.** The regular-sector contribution must be shown negligible at the leading singular scale uniformly over normalized positive effects after averaging the unknown basis. This controls arbitrary outcome spaces and nominal-spectrum-dependent choices of apparatus. A proof for one randomized measurement would not establish impossibility for all measurements.

**Dependencies and story role.** Uses M03, M09 and M18. It supplies the load-bearing quantifier in the negative theorem.

**Conceptual connection.** The lower and upper constructions use different arguments but meet on the same singular coefficient.

**Source pointers.** DDG20 Sections 2.1–2.2 for the information framework; [uniform all-effect proof](../science/finite-block-obstruction.md).

### M20: Computing and attaining the exact singular coefficient

**Central question.** How much leading information survives in a fixed block?

**Understanding target.** A word representation of Schur probabilities converts the derivative of the three-row event into a finite sum over suffixes. The result is $`\beta_k(\eta)=\sum_{m=0}^{k-1}[1-h_m(1-\eta,\eta)]`$. A binary measurement of those sectors attains this leading coefficient, with both outcomes and all $`k`$ inputs counted.

**Dependencies and story role.** Uses M04, M08 and M18–M19. It joins the constructive rank certificate with its matching upper bound.

**Conceptual connection.** The coefficient describes a specific spectral tangent, rather than the full rank-three multiparameter optimum.

**Source pointers.** DDG20 Sections 2.1 and 2.10; [exact coefficient and small blocks](../science/singular-information.md).

### M21: The rank classification and its iterated limits

**Central question.** Which uniform statements follow from the positive and negative arguments?

**Understanding target.** Pure-state tangents need one copy; arbitrary rank-two moving-support models admit a two-copy constant; all rank-three qutrit spectra admit no fixed finite-block constant. The exact converse fixes block size and the second eigenvalue, sends the rare eigenvalue to zero, then shrinks the second eigenvalue. It supplies no simultaneous-limit finite remainder.

**Dependencies and story role.** Uses M11–M20. It integrates the first two mechanisms into the original classification.

**Conceptual connection.** The ensuing calibration comparison changes the supplied information and adaptation resources while retaining precise local FI normalization.

**Source pointers.** DDG20 Sections 2.10–2.11; [model classification](../science/model.md); [interpretation](../science/interpretation.md).

### M22: Calibrated and adaptive single-copy ceilings

**Central question.** What survives of a calibrated one-copy optimum after classical adaptation?

**Understanding target.** At a rank-two qutrit the inherited support-information budget is one across four real support-rotation directions. It gives the calibrated full-model fraction ceiling $`1/4`$. Applying that same budget conditionally along an adaptive transcript and summing all copies preserves the ceiling, including charged calibration attempts.

**Dependencies and story role.** Uses M06–M09 and M21. It establishes the comparator for the exact pair calculation.

**Conceptual connection.** This is an adaptive corollary of an inherited budget, not a second discovery of the calibrated theorem.

**Source pointers.** DDG20 Sections 2.1, 2.7 and 2.10; [Haar comparison](../science/haar-pair-readout.md); [sister calibrated theorem](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/main/science/optimality.md).

### M23: The paid pilot is part of the experiment

**Central question.** How should a basis-learning pilot be included in total information?

**Understanding target.** The total matrix is $`I_Y+(N-m)\mathbb E_Y[I_{M_Y}]`$ for a retained $`m`$-copy pilot record. Conditional derivatives hold the selected apparatus fixed. Expected FI, high-probability conditional FI, expected inverse information and estimator risk are distinct quantities; one cannot exchange them inside a nonlinear comparison.

**Dependencies and story role.** Uses M06–M09 and M22. It puts calibration and readout on the same charged-record footing.

**Conceptual connection.** An exact discrete pilot law can matter more than a nominal mean squared angular error near a rare outcome.

**Source pointers.** DDG20 Sections 2.1, 2.7 and 4.5; [complete-record bridge](ANCHOR.md#why-the-complete-record-matters); [sister paid-calibration account](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/main/science/paid-calibration.md).

### M24: Strong leakage and weak-vector error differ

**Central question.** Why is one basis-error norm insufficient near a small occupied eigenvalue?

**Understanding target.** A strong occupied vector mixed with the empty level adds strong population to outcomes intended to be rare and can suppress weak-direction information. Small weak-vector-only misalignment lacks that leakage and retains a nonzero full-matrix fraction as the weak eigenvalue shrinks. Its two quadratures can still differ, and arbitrary large misalignment is not safe.

**Dependencies and story role.** Uses M01–M02, M06 and M23. It identifies the geometry hidden by a single calibration-error summary.

**Conceptual connection.** Full-matrix nuisance coupling strengthens the strong-error warning and prevents scalar retention from certifying simultaneous protection.

**Source pointers.** DDG20 Section 2.7; [sister error calculation](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/main/science/paid-calibration.md); [comparison scope](../science/interpretation.md).

### M25: Geometric calibration is not an FI threshold

**Central question.** What does a calibration-consistency lower bound actually prove?

**Understanding target.** Two-point fidelity bounds require $`mb\to\infty`$, where $`b`$ is the smaller occupied eigenvalue, for the specified uniform strong-angle accuracy or weak-angle consistency tasks. They do not prove a threshold for constant total-record FI. The exact binomial pilot also has lattice atoms, so a Gaussian approximation needs its own regime and cannot define a universal crossover.

**Dependencies and story role.** Uses M09 and M23–M24. It separates a genuine resource obstruction from a stronger unsupported inference.

**Conceptual connection.** A state-independent pair apparatus can preserve local information without first outputting a consistent eigenbasis estimate.

**Source pointers.** DDG20 Sections 4.5 and 4.6.3; [sister paid pilot and geometric lower bound](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/blob/main/science/paid-calibration.md).

### M26: Haar readout as an exact comparator

**Central question.** How can one evaluate a specified two-copy apparatus beyond a moment certificate?

**Understanding target.** After SWAP parity, continuous Haar rank-one readout permits an exact Gaussian-coordinate expression for each subnormalized branch FI. Radial independence converts Haar expectations to exponential-coordinate integrals. Including trace-changing branch derivatives automatically retains parity probability information.

**Dependencies and story role.** Uses M08, M12–M16 and M22. It replaces a lower certificate by the exact FI of one declared apparatus.

**Conceptual connection.** The apparatus is a valid continuous projective design, but its sharp constants are not assigned to the finite Clifford implementation.

**Source pointers.** DDG20 Sections 2.1 and 2.10; [exact Haar derivation](../science/haar-pair-readout.md).

### M27: Four symmetry classes cover seven directions

**Central question.** Why do four scalar calculations suffice for a full-model Haar comparison?

**Understanding target.** Diagonal phase covariance removes cross terms between the spectral line and the three complex tangent spaces, and makes each complex block isotropic. The pair-QFI fractions tend to $`1/2`$ for spectral, occupied-coherence and strong-null classes, and $`1/4`$ for the weak-null class. The weak coefficient includes probability-weighted wedge and symmetric contributions.

**Dependencies and story role.** Uses M06, M13 and M26. It recovers the full matrix rather than inferring it from convenient coordinate diagonals.

**Conceptual connection.** The weak-null class controls the limiting worst-direction fraction even though the other directions approach larger fractions.

**Source pointers.** DDG20 Section 2.7 for full-model interpretation; [four-class proof](../science/haar-pair-readout.md).

### M28: Strict pair advantage near the boundary

**Central question.** Why is the limiting equality not the entire comparison?

**Understanding target.** The exact weak-class fraction exceeds $`1/4`$ for sufficiently small positive weak eigenvalue because a nonnegative exponential integral diverges by Fatou’s lemma. The other class fractions approach $`1/2`$. Together with covariance and the adaptive single-copy ceiling, this proves a strict full-model local FI separation before the rank boundary is reached.

**Dependencies and story role.** Uses M22 and M26–M27. It integrates exact information and the inherited support budget into the comparison theorem.

**Conceptual connection.** The result needs no crossover law, but it leaves the explicit boundary threshold and sharp finite-design performance unquantified.

**Source pointers.** DDG20 Sections 2.10–2.11 for interpretation; [strict Haar separation](../science/haar-pair-readout.md).

### M29: What the operational conclusion permits

**Central question.** How far can an information separation be turned into an estimation claim?

**Understanding target.** The comparison counts all inputs and the full seven-dimensional local tangent. It proves neither finite-sample risk dominance nor a universally optimal two-copy constant. Classical estimation complexity, finite control errors, compound basis errors and global loss require further models. The rank-three converse still concerns fixed apparatuses and its specified iterated limit.

**Dependencies and story role.** Uses M06–M10, M21 and M23–M28. It relates the proved results to the statistical tasks that motivate them.

**Conceptual connection.** Keeping local information, geometric calibration and attainable risk distinct preserves the useful consequence without inventing a stronger one.

**Source pointers.** DDG20 Sections 2.7, 2.11, 4.5 and 4.6.3; [interpretation](../science/interpretation.md); [verification](../verification/README.md).

### M30: The complete readout story

**Central question.** How do rank, calibration and coherent processing jointly determine the supported result?

**Understanding target.** The full story combines a rank-two conditional-purity mechanism, a rank-three rare-sector obstruction, exact input accounting and a near-boundary Haar separation from adaptive one-copy readout. Each result retains its own state promise, apparatus, tangent space and limit order. The educational framework and inherited ingredients remain distinct from the project-supplied derivations.

**Dependencies and story role.** Uses the entire narrative phase. This final synthesis connects the local objects to the global scientific contribution.

**Conceptual connection.** One can now choose the correct theorem for a declared experiment and identify which missing resource or statistical premise blocks a stronger inference.

**Source pointers.** DDG20 Sections 2.10–2.11 and 4.5; [model](../science/model.md); [Haar proof](../science/haar-pair-readout.md); [related work](../references/RELATED_WORK.md).
