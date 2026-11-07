# Why no fixed block works uniformly at rank three

A finite collective measurement can have vanishing efficiency for a small eigenvalue even when it knows the nominal spectrum. The missing information comes from the unknown eigenbasis. This page proves the all-POVM obstruction, including continuous outcome spaces. [The singular-information calculation](singular-information.md) identifies the exact surviving coefficient.

The [model](model.md) defines single-copy SLD quantum Fisher information $`J`$ and block classical Fisher information $`I_{\mathcal M}`$. For a $`k`$-copy experiment, the corresponding quantum information is $`kJ`$.

## Statement and measurement dependence

Fix a finite positive integer $`k`$. For $`0<\eta\le 1/4`$ and $`0<p<\eta`$, consider

```math
\sigma_p=\mathrm{diag}(1-\eta-p,\eta,p),
\qquad
\rho_{p,U}=U\sigma_pU^\dagger,
\qquad U\in U(3).
```

The tangent varies $`p`$ while keeping $`\eta`$ and $`U`$ fixed. Every state used in the argument has full rank. Its single-copy information is

```math
J(p)=\frac1p+\frac1{1-\eta-p}.
```

A POVM $`\mathcal M_p`$ may depend on $`k`$, $`\eta`$, and the nominal value $`p`$, but not on $`U`$. Its local derivative does not differentiate the apparatus. More explicitly, if $`q_{\mathcal M_p}(t,U;x)`$ is the outcome density obtained by measuring $`\rho_{t,U}^{\otimes k}`$ with that chosen POVM, then

```math
I_{\mathcal M_p}(p,U)
=
\int
\frac{
\left[
\left.\partial_t q_{\mathcal M_p}(t,U;x)\right|_{t=p}
\right]^2
}{
q_{\mathcal M_p}(p,U;x)
}\,d\mu_p(x).
```

This is the usual local design convention. Allowing the nominal spectrum only strengthens the negative result.

**Finite-block obstruction.** Uniformly over all such POVMs,

```math
\limsup_{p\downarrow0}
\sup_{\mathcal M_p}
\frac{\mathbb E_U I_{\mathcal M_p}(p,U)}{kJ(p)}
\le
1-(1-\eta)^{k-1}
\le (k-1)\eta,
```

where the expectation uses Haar measure. Hence no positive constant $`c`$ satisfies $`I_{\mathcal M}\ge ckJ`$ for every full-rank qutrit state and every tangent when $`k`$ is fixed. For any proposed $`c`$, first choose $`\eta`$ sufficiently small and then choose $`p`$ sufficiently small. Some eigenbasis has efficiency no larger than the Haar average.

The proof below gives a sharper upper coefficient $`\beta_k(\eta)/k`$. The [next page](singular-information.md) computes it and shows that it is the exact limiting minimax efficiency for this particular spectral tangent.

Ancillas, recorded random settings, and adaptive operations within the block are included because they define a POVM on the $`k`$ inputs. Calibration learned from an increasing number of previous blocks is not included in the eigenbasis-blind premise.

## 1. Separate sectors present at the rank-two boundary

Schur–Weyl decomposition gives

```math
(\mathbb C^3)^{\otimes k}
=
\bigoplus_{\lambda\vdash k,\ \ell(\lambda)\le3}
\mathcal Q_\lambda\otimes\mathcal P_\lambda.
```

Here $`\mathcal Q_\lambda`$ carries an irreducible representation of $`U(3)`$, $`\mathcal P_\lambda`$ is the permutation multiplicity space, and $`\ell(\lambda)`$ is the number of rows. Let $`\Pi_\lambda`$ be the corresponding isotypic projector. Both the state and its derivative are block diagonal in these projectors.

Refining a measurement outcome by $`\lambda`$ cannot decrease its Fisher information. Indeed, for nonnegative outcome densities,

```math
\frac{\left(\sum_\lambda q_\lambda'\right)^2}
{\sum_\lambda q_\lambda}
\le
\sum_\lambda\frac{(q_\lambda')^2}{q_\lambda}.
```

Thus it suffices to study the refined effects $`\Pi_\lambda M(dx)\Pi_\lambda`$.

Define the regular and singular subspaces by

```math
\mathcal R_k
=
\bigoplus_{\ell(\lambda)\le2}
\mathcal Q_\lambda\otimes\mathcal P_\lambda,
\qquad
\mathcal K_k
=
\bigoplus_{\ell(\lambda)=3}
\mathcal Q_\lambda\otimes\mathcal P_\lambda.
```

Write $`\Pi_{\mathcal K_k}`$ for the singular projector. It is zero for $`k=1,2`$.

At $`p=0`$, the state has rank two. Its tensor power vanishes on $`\mathcal K_k`$, while its representation block is nonzero in every sector of $`\mathcal R_k`$. This is the established support structure behind Schur rank tests; see [OW15, Lemma 2.22 and Proposition 6.1](../references/RELATED_WORK.md#ow15).

For a nonzero positive effect $`E`$ in a regular sector, put

```math
q_0(E,U)=\mathrm{Tr}\!\left(E\rho_{0,U}^{\otimes k}\right).
```

This function is positive for Haar-almost every $`U`$. To see why, the state block has the form $`R_\lambda(\sigma_0)\otimes I_{\mathcal P_\lambda}`$, with $`R_\lambda(\sigma_0)\ne0`$. Irreducibility gives

```math
\int
U^{\otimes k}\Pi_\lambda\sigma_0^{\otimes k}
\Pi_\lambda(U^\dagger)^{\otimes k}\,dU
=
\frac{\mathrm{Tr}R_\lambda(\sigma_0)}
{\dim\mathcal Q_\lambda}\,I_{\mathcal Q_\lambda\otimes\mathcal P_\lambda}.
```

The coefficient is strictly positive, so $`q_0(E,U)`$ is not identically zero. It is a nonnegative real-analytic function on the connected group $`U(3)`$; its zero set therefore has Haar measure zero.

The identity on the multiplicity space is essential here. An effect supported in a permutation multiplicity does not create an additional invisible sector. Equivalently, its partial trace over $`\mathcal P_\lambda`$ remains a nonzero positive effect on $`\mathcal Q_\lambda`$.

## 2. Bound the effectwise singularity

Set $`a=1-\eta-p`$. In the eigenbasis of $`\rho_{p,U}`$, the single-copy SLD and the product-state SLD are

```math
L_p=\mathrm{diag}(-1/a,0,1/p),
\qquad
L_{k,p}=\sum_{i=1}^k L_p^{(i)}.
```

Conjugation by $`U^{\otimes k}`$ is understood when the eigenbasis is not fixed. The state commutes with this SLD. For every positive effect $`E`$, the quantum Cauchy–Schwarz inequality gives

```math
p\,\frac{(q_p'(E,U))^2}{q_p(E,U)}
\le
\mathrm{Tr}
\!\left(E\,p\rho_{p,U}^{\otimes k}L_{k,p,U}^2\right).
```

A uniform operator bound controls the right-hand side. On a basis string with occupation counts $`n_a,n_\eta,n_p`$, the eigenvalue of $`p\sigma_p^{\otimes k}L_{k,p}^2`$ is

```math
p\,a^{n_a}\eta^{n_\eta}p^{n_p}
\left(\frac{n_p}{p}-\frac{n_a}{a}\right)^2.
```

Using $`(u-v)^2\le2u^2+2v^2`$ bounds this by the sum

```math
2n_p^2a^{n_a}\eta^{n_\eta}p^{n_p-1}
+
2n_a^2a^{n_a-2}\eta^{n_\eta}p^{n_p+1}.
```

The first term is absent if $`n_p=0`$ and otherwise is at most $`2k^2`$. The second is absent if $`n_a=0`$; otherwise $`a\ge1/2`$ and $`p\le1/4`$ bound it by $`8k^2p\le2k^2`$. Consequently,

```math
0\le p\rho_{p,U}^{\otimes k}L_{k,p,U}^2
\le 4k^2 I.
```

In particular, an effect with trace one has a common integrable bound $`4k^2`$. No bound on the number of outcomes is used.

## 3. Uniform convergence over regular effects

In one regular sector, normalize positive effects to $`\mathrm{Tr}E=1`$ and define

```math
F_p(E)=
\int
p\,\frac{(q_p'(E,U))^2}{q_p(E,U)}\,dU.
```

Then

```math
\lim_{p\downarrow0}
\sup_{E\ge0,\ \mathrm{Tr}E=1}F_p(E)=0.
```

For a fixed effect this follows from the almost-everywhere positivity of $`q_0(E,U)`$ and dominated convergence. Uniformity also follows, and it is what permits spectrum-dependent apparatus designs.

Suppose uniform convergence failed. There would be $`p_j\downarrow0`$ and normalized positive effects $`E_j`$ for which $`F_{p_j}(E_j)`$ stays above a positive constant. The normalized positive cone is compact in finite dimension, so a subsequence converges to an effect $`E_*`$ with trace one.

For Haar-almost every $`U`$,

```math
q_{p_j}(E_j,U)\longrightarrow q_0(E_*,U)>0.
```

The derivative remains bounded in operator norm: $`\|\partial_p\rho_{p,U}^{\otimes k}\|\le k`$, so $`|q_p'(E,U)|\le k`$ for normalized effects. The integrand therefore tends to zero almost everywhere. The preceding bound $`4k^2`$ applies to the entire subsequence. Dominated convergence gives $`F_{p_j}(E_j)\to0`$, a contradiction.

This argument does not require the optimizing effects to converge without passing to a subsequence. It establishes a uniform bound over all of them.

### Continuous and changing outcome spaces

For a POVM $`M`$ on a finite-dimensional regular sector, define its trace measure

```math
\mu(A)=\mathrm{Tr}M(A).
```

The operator-valued Radon–Nikodym density $`E_x=dM/d\mu`$ is positive and has trace one almost everywhere. Its trace measure has total mass equal to the sector dimension. Hence

```math
\mathbb E_U[pI_M]
=
\int F_p(E_x)\,d\mu(x)
\le
\dim(\mathcal Q_\lambda\otimes\mathcal P_\lambda)
\sup_E F_p(E).
```

This tends to zero. The bound depends only on the sector, not on the POVM's outcome space or its dependence on the nominal spectrum. Summing over the finitely many regular sectors proves that their contribution to $`pI`$ vanishes uniformly over all POVMs.

## 4. Bound the surviving singular sectors

On $`\mathcal K_k`$, completeness and the effectwise information bound imply

```math
pI_{\mathcal K_k}
\le
\mathrm{Tr}
\!\left(
\Pi_{\mathcal K_k}\,
p\rho_{p,U}^{\otimes k}L_{k,p,U}^2
\right).
```

Only strings containing exactly one third eigenvector survive in the limit. In the diagonal basis, the limiting operator is

```math
A_{\eta,k}
=
\sum_{i=1}^k
\bigl(|3\rangle\langle3|\bigr)_i
\otimes
\sigma_0^{\otimes(k-1)}_{\{1,\ldots,k\}\setminus\{i\}}.
```

Convergence is in operator norm because the space is finite dimensional. Since the projector commutes with $`U^{\otimes k}`$, the trace of the limit is independent of $`U`$. Define

```math
w_k(p)=\mathrm{Tr}
\!\left(\Pi_{\mathcal K_k}\sigma_p^{\otimes k}\right),
\qquad
\beta_k(\eta)=w_k'(0)
=\mathrm{Tr}(\Pi_{\mathcal K_k}A_{\eta,k}).
```

The derivative identity follows because the other derivative terms replace one factor by $`-|1\rangle\langle1|`$. Those terms remain inside a two-dimensional one-particle support and are annihilated by $`\Pi_{\mathcal K_k}`$.

A contributing string needs both the third eigenvector and at least one second eigenvector. Dropping the projector can only increase its weight, so

```math
\beta_k(\eta)
\le
k\left[1-(1-\eta)^{k-1}\right].
```

Combining this with the uniform regular-sector estimate yields

```math
\limsup_{p\downarrow0}
\sup_{\mathcal M}
\mathbb E_U[pI_{\mathcal M}(p,U)]
\le \beta_k(\eta).
```

Finally, $`pkJ(p)\to k`$. This proves the announced obstruction and the stronger bound with coefficient $`\beta_k(\eta)/k`$.

## 5. Why rank two needs two copies

A single-copy analogue already rules out uniform efficiency on all mixed qubits. Take

```math
\widetilde\rho_{p,U}
=
U\mathrm{diag}(1-p,p)U^\dagger,
\qquad
\widetilde J(p)=\frac1p+\frac1{1-p}.
```

At $`p=0`$, the orbit of the pure boundary state spans the entire qubit Hilbert space. Every nonzero positive effect therefore has positive boundary probability for Haar-almost every $`U`$. There is no common singular subspace on one copy.

The same compact-effect argument applies. Its dominating operator is particularly simple:

```math
p\,\widetilde\rho_{p,U}\widetilde L_{p,U}^2
=
U\mathrm{diag}\!\left(\frac{p}{1-p},1\right)U^\dagger
\le I,
\qquad 0<p\le\frac12.
```

Thus

```math
\lim_{p\downarrow0}
\sup_{\mathcal M}
\frac{\mathbb E_U I_{\mathcal M}(p,U)}
{\widetilde J(p)}
=0.
```

No one-copy apparatus has a uniform positive fraction over arbitrary rank-two states, even with continuous outcomes and nominal-spectrum dependence. Together with the [two-copy construction](two-copy-readout.md), this makes two copies the minimum fixed block size for that guarantee. One copy suffices for pure-state tangents through projective 3-design readout [ZC26, Theorem 1](../references/RELATED_WORK.md#zc26).

The qubit and qutrit counterexamples also apply in larger ambient spaces: restrict any proposed POVM to the tensor powers of a known two- or three-dimensional subspace. A known embedding supplies no escape from the corresponding lower bound.

## Scope of the conclusion

The argument concerns local SLD information at positive $`p`$. It uses no Cramér–Rao inference at the singular boundary $`p=0`$. It excludes a uniform constant for every fixed finite $`k`$, rather than deriving a joint-limit rate in $`k`$, $`\eta`$, and $`p`$.

The [exact coefficient](singular-information.md) describes what survives for the displayed eigenvalue tangent. The [interpretation](interpretation.md) distinguishes this local criterion from trace-norm reconstruction, adaptive calibration, and persistent quantum-memory protocols.

