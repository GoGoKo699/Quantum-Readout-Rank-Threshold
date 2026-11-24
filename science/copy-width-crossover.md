# The coherent copy-width crossover at rank three

A fixed finite block can lose essentially all information about the smallest eigenvalue of a qutrit with two weakly occupied levels. Allowing the block to grow gives a sharp recovery curve. The relevant block width is set by the larger weak eigenvalue, even though the parameter being estimated is the smaller one.

## Model and statement

Consider the same local scalar experiment as in the [fixed-block theorem](singular-information.md). The source supplies independent copies of

```math
\rho_{\eta,p,U}=U\,\mathrm{diag}(1-\eta-p,\eta,p)\,U^\dagger,
\qquad 0\lt p\lt\eta\le\tfrac14,
```

with a common unknown $`U\in U(3)`$. The derivative is with respect to $`p`$ at fixed $`\eta,U`$. An apparatus acts jointly on $`k\ge1`$ copies and keeps its complete outcome record. It may depend on the nominal $`\eta,p`$ and is held fixed during differentiation. For a POVM $`\mathcal M`$, let $`I_\mathcal M(p,U)`$ be the classical Fisher information in that record. Define

```math
J(p)=\frac1p+\frac1{1-\eta-p},
\qquad
R_k(\eta,p)=\sup_{\mathcal M}\inf_{U\in U(3)}
              \frac{I_\mathcal M(p,U)}{kJ(p)}.
```

The supremum covers arbitrary POVMs, including continuous outcomes. The denominator charges all $`k`$ copies against their single-copy SLD information. For any sequence with $`\eta\downarrow0`$, $`p/\eta\to0`$, and $`k\eta\to a\in[0,\infty]`$,

```math
\boxed{\displaystyle
R_k(\eta,p)\longrightarrow g(a),
\qquad
 g(a)=1-\frac{1-e^{-a}}{a}\quad(0\lt a\lt\infty),
\qquad g(0)=0,\quad g(\infty)=1.}
```

At finite positive $`a`$, one bit from weak Schur sampling attains the limit. In the large-width regime, the readout can attain the endpoint using separate Schur measurements on subblocks. Every copy used by the subblock measurements counts toward the denominator.

The curve is strictly increasing on the positive half-line. For a target fraction $`c\in(0,1)`$, the transition occurs at $`k\eta=g^{-1}(c)`$. For example, $`g^{-1}(1/2)\simeq1.5936`$. Near the endpoints, $`g(a)=a/2+O(a^2)`$ as $`a\downarrow0`$ and $`1-g(a)\sim1/a`$ as $`a\to\infty`$. These statements concern the limiting scalar information fraction. Finite-sample risk and simultaneous protection of the full rank-three tangent require separate analyses.

## 1. Achievability at finite positive width

Use the binary measurement that records whether the Young diagram has three rows. The [fixed-block calculation](singular-information.md#1-from-a-schur-sector-to-a-word-event) derives its probability $`w_k(p)`$ via the Robinson–Schensted–Knuth correspondence. For the independent eigenvalue-label word, three rows are equivalent to containing a strictly decreasing subsequence $`321`$ [OW15](../references/RELATED_WORK.md#ow15). The finite-block identities are

```math
 w_k(0)=0,
\qquad
 w_k'(0)=\beta_k(\eta)
 =\sum_{m=0}^{k-1}\left[1-h_m(1-\eta,\eta)\right],
\qquad
 h_m(b,c)=\sum_{j=0}^{m}b^j c^{m-j}.
```

A joint-limit remainder follows directly from the word distribution. Its one-letter law is $`D_p=(1-\eta-p,\eta,p)`$, with derivatives $`D_p'=(-1,0,1)`$ and $`D_p''=0`$. Throughout the interval from zero to the nominal $`p`$, the second derivative of $`D_p^{\otimes k}`$ has $`\ell^1`$ norm at most $`4k(k-1)`$, by the product rule. The same bound applies to the absolute second derivative of the event probability. Thus, uniformly in the stated model,

```math
\begin{aligned}
|w_k(p)-p\beta_k(\eta)|&\le 2k(k-1)p^2,\\
|w_k'(p)-\beta_k(\eta)|&\le 4k(k-1)p.
\end{aligned}
```

For every $`m`$, $`h_m(1-\eta,\eta)`$ differs from $`(1-\eta)^m`$ by a nonnegative quantity at most $`\eta/(1-\eta)`$. Consequently,

```math
\left|\frac{\beta_k(\eta)}{k}-
\left[1-\frac{1-(1-\eta)^k}{k\eta}\right]\right|
 \le \frac{\eta}{1-\eta}.
```

When $`k\eta\to a\in(0,\infty)`$, the term in brackets tends to $`g(a)>0`$, and $`kp\to0`$. It follows that $`w_k(p)=kp[g(a)+o(1)]`$ and $`w_k'(p)=k[g(a)+o(1)]`$. As $`pJ(p)\to1`$, the binary Fisher information satisfies

```math
\frac{[w_k'(p)]^2}{kJ(p)\,w_k(p)[1-w_k(p)]}
\longrightarrow g(a).
```

The binary probability is independent of $`U`$, so this yields the lower bound for the worst eigenbasis directly.

### Exact finite-block probability

A four-state word calculation obtains the binary probability and its derivative at any interior parameters. The states record progress through the subsequence $`321`$. The terminal state is absorbing. With row-vector convention, the transition matrix is

```math
T(p)=
\begin{pmatrix}
 1-p & p & 0 & 0\\
 0 & 1-\eta & \eta & 0\\
 0 & 0 & \eta+p & 1-\eta-p\\
 0 & 0 & 0 & 1
\end{pmatrix}.
```

Start with $`u_0=(1,0,0,0)`$ and $`d_0=(0,0,0,0)`$. Iterate $`u_{j+1}=u_jT(p)`$ and $`d_{j+1}=d_jT(p)+u_jT'(p)`$. The terminal entries of $`u_k,d_k`$ are $`w_k(p),w_k'(p)`$. The associated Fisher fraction is the displayed binary expression when $`k\ge3`$. For $`k=1,2`$ the bit is deterministically zero and has zero Fisher information. The word calculation evaluates the probabilities of the quantum Schur measurement. The original eigenbasis remains unknown to the apparatus.

## 2. A uniform bound for an uncalibrated weak qubit

The upper bound uses a separate fixed-size fact. On $`n`$ qubits, let $`I_\mathcal N(q,V)`$ be the Fisher information for $`q`$ in a POVM independent of $`V`$, applied to

```math
\sigma_{q,V}^{\otimes n},
\qquad
\sigma_{q,V}=V\,\mathrm{diag}(1-q,q)V^\dagger.
```

Let $`V`$ be Haar in $`U(2)`$ and define $`C_n(q)=\sup_\mathcal N\mathbb E_V[qI_\mathcal N(q,V)]`$. The supremum may use the nominal $`q`$, with the measurement held fixed under the local derivative. Then

```math
\lim_{q\downarrow0}C_n(q)=(n-1)_+,
\qquad 0\le C_n(q)\le \frac{n}{1-q}.
```

The last inequality is the scalar qubit QFI bound. At $`n=0`$ the record has no $`q`$ dependence. For $`n\ge1`$, write $`P_\parallel`$ for the symmetric-subspace projector and $`P_\perp=I-P_\parallel`$. Both commute with the product state for every $`q,V`$. Refining any POVM by retaining this sector label can only increase its information, since summing the two sector outcomes reproduces the original record. The eigenvalue at excitation count $`\ell`$ is

```math
\lambda_\ell(q)=q^\ell(1-q)^{n-\ell},\qquad 0\le\ell\le n.
```

The symmetric subspace contains one Dicke vector of each excitation count and the complementary subspace contains $`\binom n\ell-1`$. The vectors rotate with $`V^{\otimes n}`$.

For an effect with diagonal weights $`x_i\ge0`$ in any of these rotated eigenbases, the probability and its derivative are $`h=\sum_i\lambda_i x_i`$ and $`h'=\sum_i\lambda_i' x_i`$. Cauchy–Schwarz gives

```math
\frac{(h')^2}{h}\le\sum_i\frac{(\lambda_i')^2}{\lambda_i}x_i.
```

In the complementary sector, sum or integrate the inequality over outcomes. Completeness gives the bound $`\sum_\ell[\binom n\ell-1](\lambda_\ell')^2/\lambda_\ell`$. After multiplication by $`q`$, only $`\ell=1`$ has a nonzero limit, giving $`n-1`$. Projecting onto the complementary sector alone attains this coefficient when $`n\ge2`$: its probability is $`(n-1)q+O(q^2)`$ with derivative $`n-1+O(q)`$. For $`n=1`$ this sector is empty.

It remains to show that the symmetric sector contributes $`o(1)`$ to $`q I`$, uniformly over the POVM. On the symmetric subspace, dominate the POVM by its trace measure. Its Radon–Nikodym effect densities $`E`$ are positive with trace one, and the total trace measure is $`n+1`$. For such an $`E`$, let

```math
x_\ell(V;E)=\langle D_\ell(V)|E|D_\ell(V)\rangle,
\qquad
h(q,V;E)=\sum_{\ell=0}^{n}\lambda_\ell(q)x_\ell(V;E),
```

where $`D_\ell(V)`$ is the rotated Dicke vector at count $`\ell`$. The inequality above bounds $`q(h')^2/h`$ by a constant depending on $`n`$, uniformly in $`E,V`$ for sufficiently small $`q`$, because each $`q(\lambda_\ell')^2/\lambda_\ell`$ is bounded. For every sequence $`q_j\downarrow0`$ and $`E_j`$, a subsequence converges to a positive trace-one $`E_0`$. Along that subsequence, $`h(q_j,V;E_j)\to x_0(V;E_0)`$. This limit is positive for Haar-almost every $`V`$. Indeed, choose an eigenvector of $`E_0`$ with positive weight. Its overlap with the rotated pure tensor power $`D_0(V)`$ is real analytic and nonzero somewhere, since those tensor powers span the symmetric subspace. The squared overlap therefore vanishes only on a Haar-null set. The derivatives $`h'`$ stay bounded for fixed $`n`$. Dominated convergence gives

```math
\lim_{q\downarrow0}\ \sup_{E\succeq0,\ \mathrm{tr}E=1}
\mathbb E_V\!\left[q\frac{(\partial_q h(q,V;E))^2}{h(q,V;E)}\right]=0.
```

If this uniform limit failed, a sequence of near-maximizing effects and its convergent subsequence would contradict dominated convergence. Multiplication by the trace mass $`n+1`$ bounds the whole symmetric record. Together with the complementary-sector calculation, this proves the weak-qubit fact. In particular, the order of the measurement supremum and the small-$`q`$ limit is controlled even for spectrum-dependent choices of POVM.

## 3. The qutrit converse at finite positive width

Fix the dominant ray, and consider the subfamily with a Haar-random basis on the remaining weak plane. It suffices to upper-bound the average information there, since the worst basis is no better than this average. Enhance the apparatus with the dominant ray and the full string of flags that say which input registers lie in the weak plane. The projectors giving these flags commute with every state and tangent in the subfamily. As with the sector refinement above, forgetting the flags gives the original measurement statistics. This enhancement is used only to bound the information available to the original readout.

Write

```math
s=\eta+p,\qquad q=p/s,\qquad q'=\frac{dq}{dp}=\eta/s^2.
```

The flags are independent Bernoulli variables with parameter $`s`$, and their count $`N`$ has law $`\mathrm{Bin}(k,s)`$. Conditional on the positions of $`N=n`$ flags, the weak registers form precisely the uncalibrated $`n`$-qubit experiment from Section 2. The other registers are known pure states and may be absorbed into the conditional POVM. That POVM can depend on all flags, including their positions. The bound $`C_n(q)`$ holds for each such choice.

The Fisher chain rule adds the flag information $`k/[s(1-s)]`$ to the conditional information, with the latter multiplied by $`(q')^2`$ to express the derivative in $`p`$. In particular,

```math
\begin{aligned}
R_k(\eta,p)
&\le \frac{k/[s(1-s)]}{kJ(p)}
   +\frac{(q')^2}{qkJ(p)}\,\mathbb E\big[C_N(q)\big]\\
&=\frac{q}{1-\eta}
 +\frac{(1-q)^2(1-s)}{ks(1-\eta)}\,\mathbb E\big[C_N(q)\big].
\end{aligned}
```

For $`k\eta\to a\in(0,\infty)`$ and $`p/\eta\to0`$, we have $`ks\to a`$, $`q\to0`$, and $`N\Rightarrow Z\sim\mathrm{Poisson}(a)`$. To pass to the expectation, truncate first at a fixed count cutoff. On the tail use $`C_N(q)\le N/(1-q)`$ and the bounded binomial second moments. This yields

```math
\lim\mathbb E[C_N(q)]=\mathbb E[(Z-1)_+]=a-1+e^{-a}.
```

The flag fraction vanishes, and the conditional coefficient tends to $`1/a`$. Hence the limsup of the optimal fraction is $`g(a)`$, matching the lower bound.

The count argument explains the loss in the limit. A block has order-one weak-plane arrivals at $`k\eta=O(1)`$. Among $`n`$ such arrivals, unknown orientation costs one sample's leading information whenever $`n\ge1`$. The expected retained amount is therefore $`\mathbb E[(Z-1)_+]`$, rather than the calibrated value $`\mathbb E[Z]`$.

## 4. Narrow and wide block limits

For integers $`K\ge k\ge1`$, repeating an apparatus on $`\lfloor K/k\rfloor`$ disjoint subblocks and ignoring any remaining inputs gives

```math
R_K(\eta,p)\ge \frac{k\lfloor K/k\rfloor}{K}\,R_k(\eta,p).
```

This follows from conditional independence given the fixed $`U`$ and additivity of classical Fisher information. Ignored inputs still count in $`KJ(p)`$.

If $`k\eta\to0`$, compare to blocks $`K=\lceil a'/\eta\rceil`$ for any fixed $`a'>0`$. The subblocks fill a fraction tending to one, so $`\limsup R_k\le g(a')`$. Taking $`a'\downarrow0`$ and using nonnegativity proves the narrow-block endpoint.

If $`k\eta\to\infty`$, take subblocks of size $`m=\lceil a'/\eta\rceil`$ for fixed $`a'>0`$. They fill a fraction tending to one, and using the binary Schur apparatus on each gives $`\liminf R_k\ge g(a')`$. Taking $`a'\to\infty`$ and using $`R_k\le1`$ proves the wide-block endpoint. This argument allows $`kp`$ to be large on the original block. The Taylor estimate is used only within each subblock, where $`mp\to0`$.

## Relation to the fixed-block theorem and prior work

The [fixed-block theorem](singular-information.md) addresses a different limiting order and gives $`\beta_k(\eta)/k`$ when $`p\downarrow0`$ at fixed $`k,\eta`$. Its Schur identity provides the first derivative here. The uniform word estimate and the weak-plane converse establish the simultaneous growing-width result.

The rank certificate and its word representation are inherited [ZWY07](../references/RELATED_WORK.md#zwy07), [OW15](../references/RELATED_WORK.md#ow15). The optimality of weak Schur sampling for minimax unitarily invariant hypothesis tests [GardnerEtAl26](../references/RELATED_WORK.md#gardneretal26) addresses testing risk. In this local Fisher experiment, an apparatus can retain its randomized settings, so averaging the measurement and discarding that record need not preserve its Fisher information. The converse above allows those records. The covariance guarantee in [PSW25](../references/RELATED_WORK.md#psw25) uses a block size governed by the smallest occupied eigenvalue and addresses a multiparameter objective. The exact $`1/\eta`$ width here is for the specified scalar tangent, with the two weak eigenvalues separated by $`p/\eta\to0`$.
