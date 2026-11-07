# Related work and attribution

The result concerns a state-independent readout that preserves a constant fraction of every regular local SLD-Fisher direction at rank two, together with an obstruction for every fixed finite eigenbasis-blind block at rank three. The [two-copy construction](../science/two-copy-readout.md) gives $`I_{\rm pair}\succeq J_{\rm pair}/12`$ using SWAP and finite projective 3-design readout in both branches. The [converse](../science/finite-block-obstruction.md) specifies the outcome spaces, spectral information available to the apparatus, and order of limits. The comparisons below distinguish local information from global reconstruction loss and coherent block size from working-memory size.

## Matched comparison

| Prior result | State family and objective | Measurement resource and dependence | Relation to the present result |
|---|---|---|---|
| [ZH18](#zh18), Theorems 2–4 | Exact universal Fisher symmetry for pure states and for qubits of every spectrum | Two-copy coherent POVMs with symmetric and Slater-determinant effects | Establishes the architecture and qubit advantage. The present extension is uniform over unknown rank-two supports in arbitrary dimension; the converse addresses every finite block and constant-factor efficiency. |
| [ZC26](#zc26), Definition 3 and Theorems 1–3 | Constant-factor SLD-Fisher recovery for pure states and a well-conditioned informative support | State-independent, single-copy projective 3-design | Supplies the randomized-readout framework. The present rank-two theorem removes the spectral conditioning; the rank-three converse covers all POVMs, beyond their selected single-copy counterexamples. |
| [PSW25](#psw25), Theorem 1.10 / Theorem 8.1 | Locally unbiased multiparameter estimation with smallest positive eigenvalue $`\alpha_r`$ | State-independent Keyl measurement; locally state-dependent estimator | The bound $`V_n\preceq(1+\delta)2J^{-1}/n`$ uses a sufficient collective size of order $`r/(\delta\alpha_r)`$. The present rank-two construction needs two copies independently of that spectral scale. |
| [NZ26](#nz26), Theorems 1.1–1.2 and Proposition 4.2 | Minimax trace-norm tomography of rank-at-most-$`r`$ states | At most $`t`$ jointly measured copies per round; nonadaptive upper and adaptive lower bounds | Optimal sample complexity $`\Theta[(dr/\varepsilon^2)\max\{1,r/\sqrt t\}]`$ is compatible with a failure of uniform local Fisher recovery. Their Fisher lower-bound family has uniform spectrum and moving support. |
| [ZWY07](#zwy07), Sec. III; [OW15](#ow15), Proposition 6.1 | Semi-unambiguous rank certification and optimal one-sided rank testing | Schur sectors with more rows than the null rank | Supplies the rank-certificate structure. The present converse reduces arbitrary-POVM singular Fisher information to these sectors. |
| [GardnerEtAl26](#gardneretal26), Proposition 2 and Table I | Weak incoherent-signal testing with unknown low-rank background | Global Schur sampling or persistent coherent memory | A related sensing motivation. Small working memory does not imply a bounded coherent block. |

## What is inherited

### Collective symmetry readout

Zhu and Hayashi classify coherent two-copy POVMs whose effects are symmetric pure tensor powers or antisymmetric Slater determinants [ZH18](#zh18). Their qubit collective SIC is universally Fisher symmetric across the Bloch ball. Their Eq. (13) reads $`I^{(2)}=J`$, where $`J`$ is the **single-copy** QFI, so it retains one half of $`J_{\rm pair}=2J`$.

An unknown rank-two support in a larger Hilbert space has additional tangent directions: either occupied eigenvector can move into the kernel. The positive proof controls these directions together with spectral changes and rotations within the support. The known fixed-Hilbert-space qubit theorem does not directly supply that uniform control.

### Projective 3-designs

Zhou and Chen formulate near-optimality as $`I\succeq cJ`$ with a state-independent constant [ZC26](#zc26). The present proof uses third-moment control after the SWAP outcome is retained. Its contribution is the uniform rank-two analysis of the complete measurement, rather than a design construction. Their Sec. VII.2 establishes failure for specified single-copy Haar and Pauli readouts, whereas the converse here covers arbitrary fixed finite-copy POVMs.

For qubit registers, exact Clifford 3-designs are due independently to Webb and Zhu [Webb16](#webb16), [Zhu17](#zhu17). Clifford orbits of pure states provide projective 3-designs. Koenig and Smolin give exact uniform Clifford selection in $`O(n^3)`$ classical operations [KS14](#ks14), Sec. II.2; their Sec. I.1 describes the relation to polynomial circuit synthesis. Circuit-resource statements additionally use the implementation assumptions in the construction.

### Schur rank certificates

Zhang, Wang, and Ying give a semi-unambiguous rank measurement by Young-diagram row count [ZWY07](#zwy07), Eq. (17). O'Donnell and Wright prove optimality of rejecting diagrams with more than $`r`$ rows for one-sided rank-$`r`$ testing [OW15](#ow15), Proposition 6.1. In their Sec. 2.6, Proposition 2.23 gives the Schur probability formula and Remark 2.24 identifies it with the RSK shape of an iid eigenvalue-label word. Their Theorem 2.14 identifies the row count with the longest strictly decreasing subsequence. These are the source facts behind the exact coefficient calculation here.

The additional converse step shows that sectors already populated at the rank-two boundary contribute no leading $`1/p`$ Fisher information after averaging over the eigenbasis. Uniformity over trace-normalized positive effects covers continuous outcomes and nominal-spectrum-dependent designs. The surviving three-row contribution requires both weak eigenvalue directions. The rank-testing result alone does not establish this all-POVM Fisher reduction.

## Why the objectives and limits matter

**Local information and reconstruction error.** Trace distance gives a small absolute cost to a sufficiently small eigenvalue error, whereas the local SLD information for a rare population grows as $`1/p`$. Thus the bounded-block trace-norm rate of [NZ26](#nz26) does not imply the uniform Fisher guarantee studied here.

**Fixed and growing blocks.** The guarantee of [PSW25](#psw25) allows the block to grow as a spectral scale vanishes. The converse here uses iterated local limits at fixed block size; its asymptotic coefficient is not a matched finite-$`p`$ complexity theorem.

**Block size and working memory.** The two-copy working memory in [GardnerEtAl26](#gardneretal26) can retain a coherent target through many interactions. Its size does not bound how many copies contribute coherently to the final measurement. Adaptive basis learning likewise changes the calibration available to the apparatus.

## Contribution and priority boundary

The contribution is the rank-two/rank-three boundary for uniform local information recovery under the stated architecture. The symmetry measurements, designs, and rank certificates are inherited. The claim is neither exact Fisher symmetry nor optimality of the numerical constant. The matched comparisons support this specific addition; they are not an exhaustive certification of publication priority.

## References

The labels below match the keys in [references.bib](references.bib). The specified preprint versions fix the theorem and equation numbering used above.

### ZH18

Huangjun Zhu and Masahito Hayashi, **Universally Fisher-Symmetric Informationally Complete Measurements**, *Physical Review Letters* **120**, 030404 (2018). [Published article](https://doi.org/10.1103/PhysRevLett.120.030404); [arXiv:1709.06112v2](https://arxiv.org/abs/1709.06112v2); [full text](https://arxiv.org/html/1709.06112v2). Relevant: Theorems 2–4, Eqs. (9)–(14), and the supplemental discussion of limited collective measurements.

### ZC26

Sisi Zhou and Senrui Chen, **Randomized Measurements for Multiparameter Quantum Metrology**, *PRX Quantum* **7**, 010314 (2026). [Published article](https://doi.org/10.1103/s27y-gbrp); [arXiv:2502.03536v3](https://arxiv.org/abs/2502.03536v3); [full text](https://arxiv.org/html/2502.03536v3). Relevant: Definition 1, Definition 3, Theorems 1–3, and Sec. VII.2.

### PSW25

Angelos Pelecanos, Jack Spilecki, and John Wright, **The debiased Keyl's algorithm: a new unbiased estimator for full state tomography**, arXiv:2510.07788v1 (2025). [Preprint](https://arxiv.org/abs/2510.07788v1); [full text](https://arxiv.org/html/2510.07788v1). Relevant: Theorem 1.10, restated as Theorem 8.1; Sec. 1.6 distinguishes the metrological statement from the tomography applications.

### NZ26

Ashwin Nayak and Xingyu Zhou, **Optimal Low-Rank Quantum State Tomography with Bounded-Sample Joint Measurements**, arXiv:2609.10514v2 (2026). [Preprint](https://arxiv.org/abs/2609.10514v2); [full text](https://arxiv.org/html/2609.10514v2). Relevant: Theorems 1.1–1.2, Proposition 4.2, and the adaptive protocol model.

### OW15

Ryan O'Donnell and John Wright, **Quantum Spectrum Testing**, in *Proceedings of the 47th Annual ACM Symposium on Theory of Computing*, pp. 529–538 (2015). [Published article](https://doi.org/10.1145/2746539.2746582); [arXiv:1501.05028v1](https://arxiv.org/abs/1501.05028v1); [full preprint](https://arxiv.org/html/1501.05028v1). Relevant preprint numbering: Theorem 2.14, Lemma 2.22, Proposition 2.23, Remark 2.24, and Proposition 6.1.

### ZWY07

Chi Zhang, Guoming Wang, and Mingsheng Ying, **Discrimination between pure states and mixed states**, *Physical Review A* **75**, 062306 (2007). [Published article](https://doi.org/10.1103/PhysRevA.75.062306); [arXiv:quant-ph/0611122v2](https://arxiv.org/abs/quant-ph/0611122v2); [full text](https://arxiv.org/html/quant-ph/0611122v2). Relevant: Sec. III, Eq. (17).

### Webb16

Zak Webb, **The Clifford group forms a unitary 3-design**, *Quantum Information and Computation* **16**(15–16), 1379–1400 (2016). [Published article](https://doi.org/10.26421/QIC16.15-16-8); [arXiv:1510.02769v3](https://arxiv.org/abs/1510.02769v3).

### Zhu17

Huangjun Zhu, **Multiqubit Clifford groups are unitary 3-designs**, *Physical Review A* **96**, 062336 (2017). [Published article](https://doi.org/10.1103/PhysRevA.96.062336); [arXiv:1510.02619v2](https://arxiv.org/abs/1510.02619v2). The cited preprint revision is dated January 2018; the journal publication is from December 2017.

### KS14

Robert Koenig and John A. Smolin, **How to efficiently select an arbitrary Clifford group element**, *Journal of Mathematical Physics* **55**, 122202 (2014). [Published article](https://doi.org/10.1063/1.4903507); [arXiv:1406.2170v1](https://arxiv.org/abs/1406.2170v1); [full text](https://arxiv.org/html/1406.2170v1). Relevant: Sec. I.1 for the representation and compilation connection; Sec. II.2 for efficient exact sampling.

### GardnerEtAl26

James W. Gardner, Federico Belliardo, Gideon Lee, Tuvia Gefen, and Liang Jiang, **Quantum superresolution and noise spectroscopy with quantum computing**, arXiv:2602.17862v1 (2026). [Preprint](https://arxiv.org/abs/2602.17862v1); [full text](https://arxiv.org/html/2602.17862v1). Relevant: Proposition 2, Table I, and the discussions of rank testing and constant working memory.
