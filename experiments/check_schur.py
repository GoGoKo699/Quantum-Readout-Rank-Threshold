"""Check the singular Schur coefficient using exact rational arithmetic.

Run from any working directory with Python 3. The default output is
experiments/results/schur.json. No third-party packages are needed.

The checks compare a three-variable Jacobi-Trudi derivative with the iid-word
formula, test normalization across all Schur sectors, and independently use
permutation-character projectors for k = 3 and k = 4. These finite identities
do not verify the all-POVM compactness argument or any simultaneous limit.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


Dual = tuple[Fraction, Fraction]
ZERO: Dual = (Fraction(0), Fraction(0))
ONE: Dual = (Fraction(1), Fraction(0))


def add(x: Dual, y: Dual) -> Dual:
    return x[0] + y[0], x[1] + y[1]


def multiply(x: Dual, y: Dual) -> Dual:
    return x[0] * y[0], x[1] * y[0] + x[0] * y[1]


def scale(x: Dual, coefficient: Fraction | int) -> Dual:
    return coefficient * x[0], coefficient * x[1]


def homogeneous_duals(variables: tuple[Dual, ...], degree: int) -> list[Dual]:
    """Coefficients of product_i (1 - x_i t)^(-1), to the given degree."""
    result = [ONE] + [ZERO] * degree
    for variable in variables:
        for j in range(1, degree + 1):
            result[j] = add(result[j], multiply(variable, result[j - 1]))
    return result


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def determinant(matrix: list[list[Dual]]) -> Dual:
    result = ZERO
    for permutation in itertools.permutations(range(len(matrix))):
        term = ONE
        for i, j in enumerate(permutation):
            term = multiply(term, matrix[i][j])
        result = add(result, scale(term, permutation_sign(permutation)))
    return result


def partitions(k: int) -> list[tuple[int, int, int]]:
    return [
        (first, second, k - first - second)
        for first in range(k, -1, -1)
        for second in range(min(first, k - first), -1, -1)
        if 0 <= k - first - second <= second
    ]


def specht_dimension(shape: tuple[int, int, int]) -> int:
    """Three-row form of the hook-length dimension formula."""
    numerator = math.factorial(sum(shape))
    for i in range(3):
        for j in range(i + 1, 3):
            numerator *= shape[i] - shape[j] + j - i
    denominator = math.prod(math.factorial(shape[i] + 2 - i) for i in range(3))
    dimension = Fraction(numerator, denominator)
    assert dimension.denominator == 1
    return dimension.numerator


def schur_dual(shape: tuple[int, int, int], h: list[Dual]) -> Dual:
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            degree = shape[i] - i + j
            row.append(h[degree] if degree >= 0 else ZERO)
        matrix.append(row)
    return determinant(matrix)


def schur_weights(k: int, eta: Fraction, p: Fraction = Fraction(0)) -> dict:
    """Weights and p derivatives, with eta held fixed."""
    variables = ((1 - eta - p, Fraction(-1)), (eta, Fraction(0)), (p, Fraction(1)))
    h = homogeneous_duals(variables, k + 2)
    return {
        shape: scale(schur_dual(shape, h), specht_dimension(shape))
        for shape in partitions(k)
    }


def binary_h(degree: int, a: Fraction, b: Fraction) -> Fraction:
    return sum((a**j * b ** (degree - j) for j in range(degree + 1)), Fraction(0))


def beta_suffix(k: int, eta: Fraction) -> Fraction:
    return sum((1 - binary_h(m, 1 - eta, eta) for m in range(k)), Fraction(0))


def beta_positive(k: int, eta: Fraction) -> Fraction:
    if k < 3:
        return Fraction(0)
    a, b = 1 - eta, eta
    return a * b * sum(
        ((k - 2 - j) * binary_h(j, a, b) for j in range(k - 2)), Fraction(0)
    )


def beta_two_variable_schur(k: int, eta: Fraction) -> Fraction:
    """The determinant factor leaves only shapes (u, v, 1) at first order."""
    a, b = 1 - eta, eta
    result = Fraction(0)
    for u in range(1, k):
        v = k - 1 - u
        if not 1 <= v <= u:
            continue
        r, s = u - 1, v - 1
        polynomial = sum((a ** (r - j) * b ** (s + j) for j in range(r - s + 1)), Fraction(0))
        result += a * b * specht_dimension((u, v, 1)) * polynomial
    return result


def cycle_lengths(permutation: tuple[int, ...]) -> list[int]:
    unseen = set(range(len(permutation)))
    lengths = []
    while unseen:
        first = min(unseen)
        current, length = first, 0
        while current in unseen:
            unseen.remove(current)
            length += 1
            current = permutation[current]
        lengths.append(length)
    return lengths


def power_trace(variables: tuple[Dual, ...], degree: int) -> Dual:
    value = sum((x**degree for x, _ in variables), Fraction(0))
    derivative = sum((degree * x ** (degree - 1) * dx for x, dx in variables), Fraction(0))
    return value, derivative


def projector_weight(k: int, eta: Fraction, p: Fraction = Fraction(0)) -> Dual:
    """Trace the explicit character projector for the sole three-row sector.

    For k=3 the representation is sign. For k=4 it is sign times the
    standard representation, whose character is number of fixed points - 1.
    The projector factor is dim(P_lambda) / k!, not dim(Q_lambda) / k!.
    """
    if k not in (3, 4):
        raise ValueError("This independent character check is defined for k=3,4.")
    variables = ((1 - eta - p, Fraction(-1)), (eta, Fraction(0)), (p, Fraction(1)))
    total = ZERO
    for permutation in itertools.permutations(range(k)):
        character = permutation_sign(permutation)
        if k == 4:
            character *= sum(i == j for i, j in enumerate(permutation)) - 1
        term = ONE
        for length in cycle_lengths(permutation):
            term = multiply(term, power_trace(variables, length))
        total = add(total, scale(term, character))
    multiplicity = 1 if k == 3 else 3
    return scale(total, Fraction(multiplicity, math.factorial(k)))


def rational(x: Fraction) -> str:
    return str(x)


def run_checks() -> dict:
    etas = (Fraction(1, 1000), Fraction(1, 10), Fraction(1, 4))
    schur_cases = []
    for eta in etas:
        for k in range(1, 11):
            weights = schur_weights(k, eta)
            total = ZERO
            singular = ZERO
            for shape, weight in weights.items():
                assert weight[0] >= 0
                total = add(total, weight)
                if shape[2] > 0:
                    assert weight[0] == 0
                    assert weight[1] >= 0
                    singular = add(singular, weight)
            assert total == ONE, (k, eta, "Schur normalization", total)
            coefficient = beta_suffix(k, eta)
            assert singular == (Fraction(0), coefficient)
            assert coefficient == beta_positive(k, eta)
            assert coefficient == beta_two_variable_schur(k, eta)
            if k >= 3:
                assert 0 < coefficient <= eta * (1 - eta) * (k - 1) * (k - 2) / 2
            else:
                assert coefficient == 0
            q = eta * (1 - eta)
            small_formulas = {3: q, 4: 3 * q, 5: 6 * q - q**2, 6: 10 * q - 4 * q**2}
            if k in small_formulas:
                assert coefficient == small_formulas[k]
            schur_cases.append({
                "k": k,
                "eta": rational(eta),
                "beta": rational(coefficient),
                "beta_over_k": rational(coefficient / k),
                "schur_sectors": len(weights),
                "three_row_sectors": sum(shape[2] > 0 for shape in weights),
                "all_exact_comparisons_passed": True,
            })

    projector_cases = []
    for eta in etas:
        for k in (3, 4):
            for p in (Fraction(0), eta / 3):
                direct = projector_weight(k, eta, p)
                multiplicity = 1 if k == 3 else 3
                expected = (
                    multiplicity * (1 - eta - p) * eta * p,
                    multiplicity * eta * (1 - eta - 2 * p),
                )
                assert direct == expected, (k, eta, p, direct, expected)
                schur = ZERO
                for shape, weight in schur_weights(k, eta, p).items():
                    if shape[2] > 0:
                        schur = add(schur, weight)
                assert direct == schur
                projector_cases.append({
                    "k": k,
                    "eta": rational(eta),
                    "p": rational(p),
                    "probability": rational(direct[0]),
                    "p_derivative": rational(direct[1]),
                    "permutations_summed": math.factorial(k),
                    "character_and_schur_agree": True,
                })

    return {
        "all_passed": True,
        "arithmetic": "Exact fractions; no floating-point tolerance.",
        "schur_case_count": len(schur_cases),
        "projector_case_count": len(projector_cases),
        "checks": [
            "Full three-variable Jacobi-Trudi weights sum to one and derivatives sum to zero.",
            "All three-row weights vanish at p=0; their derivative equals the suffix formula.",
            "The positive homogeneous-polynomial formula and determinant-factor formula agree.",
            "The stated k=3,4,5,6 polynomials and the positive coefficient bound hold.",
            "Explicit k=3,4 permutation-character projectors agree at boundary and positive p.",
        ],
        "scope": "Finite coefficient and normalization checks only; not a numerical proof of the all-POVM bound or a simultaneous-limit rate.",
        "schur_cases": schur_cases,
        "projector_cases": projector_cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "results" / "schur.json",
    )
    args = parser.parse_args()
    results = run_checks()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(
        f"Passed {results['schur_case_count']} exact Schur cases and "
        f"{results['projector_case_count']} character-projector cases; output: {args.output}"
    )


if __name__ == "__main__":
    main()
