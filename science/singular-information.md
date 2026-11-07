# Exact information carried by the new Schur sectors

For the qutrit family

```math
\rho_{p,U}
=
U\mathrm{diag}(1-\eta-p,\eta,p)U^\dagger,
\qquad
J(p)=\frac1p+\frac1{1-\eta-p},
```

the [finite-block proof](finite-block-obstruction.md) shows that only the three-row Schur sectors retain a leading $`1/p`$ contribution after an unknown eigenbasis is taken into account. This page computes that contribution exactly.

Keep $`k`$ and $`0\lt \eta\le1/4`$ fixed while $`p\downarrow0`$. Write

```math
a=1-\eta,\qquad b=\eta,\qquad q=ab.
```

The symbols $`a,b`$ below describe the boundary spectrum. At positive $`p`$, the first eigenvalue is $`a-p`$.

## The exact limiting minimax value

Let

```math
R_k(\eta,p)
=
\sup_{\mathcal M}\inf_{U\in U(3)}
\frac{I_{\mathcal M}(p,U)}{kJ(p)}.
```

The supremum allows arbitrary POVMs on $`k`$ copies, including continuous outcomes. A measurement may use $`k,\eta,p`$, but it cannot use $`U`$. It is held fixed when the local derivative is taken, as specified in the [model](model.md) and the [converse](finite-block-obstruction.md).

Define the complete homogeneous polynomial in two variables by

```math
h_m(a,b)=\sum_{j=0}^{m}a^j b^{m-j},
\qquad m\ge0.
```

Then the exact limit is

```math
\boxed{
\lim_{p\downarrow0}R_k(\eta,p)
=
\frac{\beta_k(\eta)}{k},
\qquad
\beta_k(\eta)
=
\sum_{m=0}^{k-1}\bigl[1-h_m(a,b)\bigr].
}
```

In particular, $`\beta_1=\beta_2=0`$. For $`k\ge3`$, an equivalent positive expression is

```math
\beta_k(\eta)
=
q\sum_{j=0}^{k-3}(k-2-j)h_j(a,b).
```

The optimum here concerns the displayed spectral tangent. It is not the optimum of the full multiparameter rank-three problem.

## 1. From a Schur sector to a word event

Let $`\Pi_{\mathcal K_k}`$ project onto the sectors with three rows and set

```math
w_k(p)
=
\mathrm{Tr}
\!\left(
\Pi_{\mathcal K_k}
\mathrm{diag}(a-p,b,p)^{\otimes k}
\right).
```

The Schur probability formula is

```math
\Pr(\lambda)
=
f^\lambda s_\lambda(a-p,b,p),
```

where $`f^\lambda=\dim\mathcal P_\lambda`$ and $`s_\lambda`$ is a Schur polynomial. Weak Schur sampling has the same Young-diagram distribution as Robinson–Schensted–Knuth insertion applied to an independent word drawn from the eigenvalue probabilities. The number of rows is the longest strictly decreasing subsequence length. These are [OW15, Proposition 2.23, Remark 2.24, and Theorem 2.14](../references/RELATED_WORK.md#ow15).

The corresponding binary test of rank at most two is established rank-testing machinery [ZWY07](../references/RELATED_WORK.md#zwy07), [OW15, Proposition 6.1](../references/RELATED_WORK.md#ow15). Its leading Fisher coefficient is computed here.

At first order in $`p`$, a word contains exactly one letter $`3`$. Such a word has three rows precisely when a $`2`$ and then a $`1`$ occur after that $`3`$. Its prefix before the $`3`$ does not affect this event.

If the suffix has length $`m`$, it fails to contain the subsequence $`21`$ exactly when it has the form

```math
\underbrace{1\cdots1}_{j}
\underbrace{2\cdots2}_{m-j}
\qquad\text{for some }0\le j\le m.
```

The total probability of these monotone suffixes is $`h_m(a,b)`$. Summing over the $`k`$ possible positions of the single $`3`$ therefore gives

```math
w_k'(0)
=
\sum_{m=0}^{k-1}\bigl[1-h_m(a,b)\bigr]
=
\beta_k(\eta).
```

Terms with two or more occurrences of $`3`$ are $`O(p^2)`$. Terms with none never enter a three-row sector, including the derivative contributions from the changing first eigenvalue. This explains why the coefficient uses the boundary probabilities $`a,b`$ without an additional normalization factor.

## 2. A positive formula and small blocks

Because $`a+b=1`$, the homogeneous polynomials obey

```math
h_0=h_1=1,
\qquad
h_m=h_{m-1}-q h_{m-2}
\quad(m\ge2).
```

It follows that

```math
1-h_m
=
q\sum_{j=0}^{m-2}h_j
\quad(m\ge2).
```

Summing over $`m`$ gives the positive expression for $`\beta_k`$.

The first values are:

| Copies $`k`$ | Singular coefficient $`\beta_k(\eta)`$ | Limiting efficiency $`\beta_k(\eta)/k`$ |
|---|---|---|
| $`1`$ | $`0`$ | $`0`$ |
| $`2`$ | $`0`$ | $`0`$ |
| $`3`$ | $`q`$ | $`q/3`$ |
| $`4`$ | $`3q`$ | $`3q/4`$ |
| $`5`$ | $`6q-q^2`$ | $`(6q-q^2)/5`$ |
| $`6`$ | $`10q-4q^2`$ | $`(10q-4q^2)/6`$ |

For three copies, the only singular sector is the fully antisymmetric one. Its probability is

```math
w_3(p)=\det\sigma_p=(a-p)bp,
```

so its derivative is $`q`$. For four copies, the only three-row partition is $`(2,1,1)`$. Its multiplicity is three and

```math
s_{(2,1,1)}(x_1,x_2,x_3)
=
x_1x_2x_3(x_1+x_2+x_3).
```

Since the state has trace one, $`w_4(p)=3(a-p)bp`$, giving derivative $`3q`$.

These examples expose the additional rare coincidence. Resolving the third eigenvalue requires an event whose leading probability also contains the second eigenvalue. The coefficient is therefore small when both occupied weak directions are rare.

## 3. Why this coefficient is optimal

The converse established the uniform bound

```math
\limsup_{p\downarrow0}
\sup_{\mathcal M}
\mathbb E_U[pI_{\mathcal M}(p,U)]
\le\beta_k(\eta).
```

Uniformity over normalized effects is important: it permits the supremum over measurements to be taken before the limit. Since the worst eigenbasis is no better than the Haar average and $`pkJ(p)\to k`$, this gives

```math
\limsup_{p\downarrow0}R_k(\eta,p)
\le \frac{\beta_k(\eta)}{k}.
```

For the matching lower bound, use only the binary measurement

```math
\left\{
\Pi_{\mathcal K_k},
I-\Pi_{\mathcal K_k}
\right\}.
```

Its probabilities are independent of $`U`$. For $`k\ge3`$,

```math
w_k(p)=\beta_k(\eta)p+O(p^2),
\qquad
w_k'(p)=\beta_k(\eta)+O(p),
```

with $`\beta_k(\eta)\gt 0`$. Its Fisher information is therefore

```math
I_{\mathrm{binary}}(p)
=
\frac{[w_k'(p)]^2}{w_k(p)[1-w_k(p)]}
=
\frac{\beta_k(\eta)}{p}+O(1).
```

This single measurement works for every eigenbasis, so it supplies the matching lower limit. For $`k=1,2`$, the singular projector is zero and nonnegativity of Fisher information, together with the converse, gives the stated zero limit.

The binary rank certificate is consequently optimal for the leading singular coefficient. Other outcomes can still contribute finite or slower-diverging information; the statement does not say that the binary measurement is optimal at finite $`p`$.

## 4. Consequence for uniform rank-three readout

The probability interpretation gives $`0\lt h_j(a,b)\le1`$. Hence for $`k\ge3`$,

```math
0\lt \beta_k(\eta)
\le
q\,\frac{(k-1)(k-2)}2.
```

For every fixed $`k`$, $`h_j(1-\eta,\eta)\to1`$ as $`\eta\downarrow0`$, so

```math
\frac{\beta_k(\eta)}{\eta}
\longrightarrow
\frac{(k-1)(k-2)}2.
```

Combining this with the exact $`p\downarrow0`$ limit gives

```math
\lim_{\eta\downarrow0}
\lim_{p\downarrow0}
R_k(\eta,p)=0
\qquad
\text{for every fixed finite }k.
```

Growing the block at a fixed second eigenvalue gives a different limit. For fixed $`0\lt \eta\le1/4`$, the generating function implies

```math
\sum_{m=0}^{\infty}h_m(a,b)
=\frac1{(1-a)(1-b)}
=\frac1q.
```

Since $`\beta_k=k-\sum_{m=0}^{k-1}h_m`$, this yields

```math
\lim_{k\to\infty}\lim_{p\downarrow0}R_k(\eta,p)=1
\qquad\text{for every fixed }0\lt \eta\le1/4.
```

An increasing block can therefore recover the full leading singular coefficient at a fixed second eigenvalue. A fixed block loses its uniform fraction when that second eigenvalue also becomes small.

These are iterated-limit statements. They do not provide a remainder uniform in $`k`$ or $`\eta`$, and they are not a matched finite-$`p`$ copy-complexity law.

## 5. Exact finite checks

There is also a direct Schur-polynomial expression for the coefficient. At first order only partitions $`(u,v,1)`$ contribute: a last row of size at least two supplies at least two factors of $`p`$. Removing one three-box column gives

```math
\beta_k(\eta)
=
ab\!\!\sum_{\substack{u+v=k-1\\u\ge v\ge1}}
f^{(u,v,1)}s_{(u-1,v-1)}(a,b),
\qquad
f^{(u,v,1)}
=\frac{k!(u-v+1)(u+1)v}{(u+2)!(v+1)!}.
```

Here $`s_{(r,s)}(a,b)=\sum_{j=0}^{r-s}a^{r-j}b^{s+j}`$. This provides an algebraic comparison with the word-event derivation.

[check_schur.py](../experiments/check_schur.py) verifies the coefficient with exact rational arithmetic using independent descriptions:

- A Jacobi–Trudi determinant calculation of the full three-variable Schur probabilities and their derivative.
- The binary-suffix formula and its positive recurrence form.
- Explicit permutation-character projectors for the three- and four-copy examples.

The [recorded checks](../experiments/results/schur.json) cover 30 Schur cases with $`1\le k\le10`$ and $`\eta\in\{1/1000,1/10,1/4\}`$, plus 12 character-projector cases at the boundary and at positive $`p`$. All comparisons are exact rational identities. These checks test the representation multiplicities, derivatives, and normalization factors. They do not replace the uniform all-POVM proof or establish an unproved simultaneous limit.

