# Reproduce the scientific checks

The analytical results are proved in the [two-copy readout](../science/two-copy-readout.md), [exact Haar comparison](../science/haar-pair-readout.md), [finite-block obstruction](../science/finite-block-obstruction.md), and [singular coefficient](../science/singular-information.md) accounts. The checks below target their tensor identities, normalization factors, design moments, branch integrals and finite coefficient calculations.

## Run

The numerical requirements pin NumPy 2.3.5 and mpmath 1.3.0. Python 3.10 or newer is supported; the original tensor/Schur reference run used Python 3.12.14. The Schur checks use only Python's standard library. From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The runner executes all three scripts and fails if any check fails. It rewrites their JSON result files deterministically in the recorded environment. Floating-point diagnostics can vary slightly between numerical-library implementations; the scripts record their tolerances and check the actual identities and bounds.

Each script can also be run independently:

```bash
python3 experiments/verify_readout.py
python3 experiments/check_schur.py
python3 verification/verify_haar_pair.py
```

## Two-copy readout

[verify_readout.py](../experiments/verify_readout.py) performs four related checks:

1. It constructs rank-two states and tangent matrices in dimensions 2, 3, 4 and 7. It directly projects the tensor derivative into both SWAP sectors and checks the conditional symmetric Hilbert–Schmidt norm, the pure wedge derivative, the single-copy SLD information, and the analytical certificate. Equal positive eigenvalues and a smaller eigenvalue of $`10^{-6}`$ are included.
2. It constructs all 60 two-qubit stabilizer projectors and compares their first three moments with the Haar moments.
3. It calculates the actual finite-POVM information of the complete pair apparatus for qubit inputs, including pure-state tangents.
4. It checks the standalone projective-design pure-state bound in dimension four.

The [recorded result](../experiments/results/readout.json) contains the random seed, NumPy version, tolerances, counts and residuals. The reference run has 72 tensor cases, 24 mixed-qubit pair cases, 2 pure-qubit pair cases, and 8 standalone pure-state design cases. The minimum sampled analytical pair fraction is about 0.10417; the proved lower bound is $`1/12`$. The minimum measured finite-design pair fraction in the mixed-qubit cases is about 0.24444.

The full finite-design pair measurement is evaluated only for qubit inputs. Higher-dimensional moving-support cases are checked through tensor derivatives and the analytical certificate. The script does not enumerate larger Clifford groups or infer a universal constant from sampled minima.

## Schur coefficient and normalization

[check_schur.py](../experiments/check_schur.py) uses exact rational arithmetic. It compares the three-variable Jacobi–Trudi Schur derivatives with the binary-word suffix formula, the positive homogeneous-polynomial formula, and the determinant-factor expression over partitions $`(u,v,1)`$. It checks total Schur probability and its derivative across all sectors.

A second calculation explicitly sums permutation characters for three and four copies. This independently checks the projectors and their multiplicity factors, both at the rank-two boundary and at positive rare-eigenvalue weight.

The [recorded result](../experiments/results/schur.json) contains 30 Schur cases with $`k=1,\ldots,10`$ and $`\eta\in\{1/1000,1/10,1/4\}`$, plus 12 character-projector cases. Every comparison is an exact rational identity.

## What the checks establish

These computations test formulas on which the analytical comparison depends. They do not prove compactness, almost-everywhere positivity, dominated convergence, or an assertion uniform over all POVMs. Those steps remain explicit in the written converse.

The checks do not establish noise robustness, classical estimation complexity, or a simultaneous finite-$`p`$ scaling law. The small-system finite-design information is a diagnostic of the stated apparatus, not a numerical claim of optimality.

## Exact continuous-Haar comparison

[verify_haar_pair.py](verify_haar_pair.py) computes the exact expectations in [the Haar account](../science/haar-pair-readout.md) through deterministic Laplace integrals with 35 decimal digits. For independent unit-mean exponentials, the transform is a product of factors $`(1+tp_i)^{-1}`$, with additional denominator factors for each moment. Diagonal second moments include the exponential factor two. The calculation checks $`\sum_i p_i g_i=1`$ and $`\sum_i p_i h_{ij}=1`$, in addition to the four tangent-class ratios. Its tolerance for these normalization identities is $`10^{-25}`$.

The [recorded result](../experiments/results/haar_pair.json) covers the equal-spectrum point and four shrinking eigenvalues. At $`b=1/2`$, all four class fractions are $`1/4`$. At $`b=0.1,0.01,0.001,10^{-5}`$, the sampled minima are approximately 0.2658944, 0.2566769, 0.2512297 and 0.2500238. The output identifies these as continuous-Haar fractions of the complete pair QFI, not finite Clifford information.

These values check moment factors and representative behavior. The written proof establishes the full seven-dimensional decomposition, the limit and the strict inequality for all sufficiently small positive $`b`$ using phase covariance and Fatou's lemma. No sampled minimum is used to prove a universal constant, to specify the threshold, or to infer finite-sample risk ordering.

## Hosted mathematical display

The [read-only workflow](../.github/workflows/hosted-math.yml) checks commit-pinned GitHub pages in an anonymous Chromium browser at widths 1440 and 760. The [collector](hosted/capture_hosted_math.cjs) reads the source from Git objects, compiles each formula with MathJax, and compares its symbols and structure against the actual hosted MathML. It includes inline formulas, displays and table cells. A source-bound content contract also protects the headline constants, the strict spectral domain and the exact limiting coefficient. The [text and relation checker](hosted/check_rendered_math.py) checks source identity, counts, relations and any supplied content contract.

To reproduce a complete capture with Node.js 18 or newer, Python 3.10 or newer, and Git, use an isolated dependency directory outside this repository:

```bash
npm install --prefix /tmp/readout-browser playwright@1.56.1 mathjax-full@3.2.1
/tmp/readout-browser/node_modules/.bin/playwright install chromium
export NODE_PATH=/tmp/readout-browser/node_modules
node verification/hosted/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Quantum-Readout-Rank-Threshold \
  --revision "$(git rev-parse HEAD)" \
  --output /tmp/readout-hosted-evidence \
  --contract verification/hosted/math-contract.json
```

The output directory must be new or empty. The default scope includes every tracked Markdown page at the supplied revision. The report records exact source hashes, page and expression counts, runtime versions, failures, screenshots and artifact hashes. A failed capture remains a failed capture; a source parser or successful numerical run cannot replace it.

Inspect the saved screenshots as well as the automated report. Structural comparison checks mathematical content within the supported parser and browser; visual review checks layout and legibility. Neither verifies the scientific proofs, all browser versions or future hosting behavior. GitHub Actions artifacts are temporary diagnostic records, not a permanent archive.
