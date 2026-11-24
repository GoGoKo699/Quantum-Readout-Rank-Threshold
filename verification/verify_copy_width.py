"""Check finite identities and examples for the scalar copy-width crossover."""

from __future__ import annotations

from bisect import bisect_right
from collections import Counter
from fractions import Fraction
from itertools import product
import json
import math


def three_row_probability(k: int, eta, p):
    """Track the prefix of 321 found so far, with p derivatives at fixed eta."""
    dominant = 1 - eta - p
    probabilities = [1, 0, 0, 0]
    derivatives = [0, 0, 0, 0]
    for _ in range(k):
        empty, third, second, accepted = probabilities
        d_empty, d_third, d_second, d_accepted = derivatives
        probabilities = [
            (1 - p) * empty,
            p * empty + (1 - eta) * third,
            eta * third + (eta + p) * second,
            dominant * second + accepted,
        ]
        derivatives = [
            (1 - p) * d_empty - empty,
            p * d_empty + empty + (1 - eta) * d_third,
            eta * d_third + (eta + p) * d_second + second,
            dominant * d_second - second + d_accepted,
        ]
    return probabilities[-1], derivatives[-1]


def rsk_row_count(word: tuple[int, ...]) -> int:
    rows: list[list[int]] = []
    for letter in word:
        for row in rows:
            column = bisect_right(row, letter)
            if column == len(row):
                row.append(letter)
                break
            row[column], letter = letter, row[column]
        else:
            rows.append([letter])
    return len(rows)


def weighted_word_counts(counts: Counter, eta: Fraction, p: Fraction):
    """Differentiate word weights by multiplicity, including at p=0."""
    dominant = 1 - eta - p
    probability = derivative = Fraction(0)
    for (first, second, third), count in counts.items():
        fixed = count * eta**second
        probability += fixed * dominant**first * p**third
        if third:
            derivative += fixed * dominant**first * third * p ** (third - 1)
        if first:
            derivative -= fixed * first * dominant ** (first - 1) * p**third
    return probability, derivative


def check_word_probabilities() -> int:
    cases = 0
    for k in range(1, 8):
        counts = Counter(
            tuple(word.count(letter) for letter in (1, 2, 3))
            for word in product((1, 2, 3), repeat=k)
            if rsk_row_count(word) == 3
        )
        for eta in (Fraction(1, 4), Fraction(1, 123)):
            boundary, beta = three_row_probability(k, eta, Fraction(0))
            assert boundary == 0
            assert beta == sum(
                1 - sum((1 - eta)**(m - j) * eta**j for j in range(m + 1))
                for m in range(k)
            )
            for p in (Fraction(0), eta / 7):
                expected = weighted_word_counts(counts, eta, p)
                probability, derivative = three_row_probability(k, eta, p)
                assert (probability, derivative) == expected, (k, eta, p)
                assert abs(probability - p * beta) <= 2 * k * (k - 1) * p**2
                assert abs(derivative - beta) <= 4 * k * (k - 1) * p
                cases += 1
    return cases


def check_weak_qubit_coefficients() -> int:
    """Count the part of the first-order mass outside the symmetric sector."""
    cases = 0
    for n in range(1, 9):
        # At Hamming weight j the symmetric projector has one diagonal
        # contribution of 1/choose(n,j) per computational-basis string.
        one_rare = [word for word in product((0, 1), repeat=n) if sum(word) == 1]
        coefficient = sum(1 - Fraction(1, math.comb(n, sum(word))) for word in one_rare)
        assert coefficient == n - 1
        for q in (Fraction(1, 100), Fraction(1, 100_000_000)):
            regular_mass = sum((1 - q)**(n - j) * q**j for j in range(n + 1))
            direct_mass = sum(
                (1 - q)**(n - sum(word)) * q**sum(word) / math.comb(n, sum(word))
                for word in product((0, 1), repeat=n)
            )
            assert regular_mass == direct_mass
            if q < Fraction(1, 1_000_000):
                assert abs((1 - regular_mass) / q - coefficient) < Fraction(1, 1_000_000)
            cases += 1

    # For one weak qubit, a recorded Haar rank-one readout has finite-q
    # information even though the nonsymmetric event never occurs.
    scaled_information = []
    for q in (1e-2, 1e-4, 1e-6, 1e-8):
        contrast = 1 - 2 * q
        information = 2 * (math.log((1 - q) / q) - 2 * contrast) / contrast**3
        scaled_information.append(q * information)
        assert 0 < information <= 1 / (q * (1 - q))
    assert scaled_information[-1] < 4e-7
    assert all(a > b for a, b in zip(scaled_information, scaled_information[1:]))
    return cases + len(scaled_information)


def check_flag_decomposition() -> int:
    cases = 0
    for k in (1, 3, 6, 12):
        for eta, p in ((Fraction(1, 4), Fraction(1, 80)), (Fraction(1, 81), Fraction(1, 10_001))):
            s = eta + p
            q = p / s
            q_derivative = (1 - q) / s
            count_weights = [math.comb(k, n) * s**n * (1 - s)**(k - n) for n in range(k + 1)]
            count_mean = sum(n * weight for n, weight in enumerate(count_weights))
            assert sum(count_weights) == 1
            assert count_mean == k * s
            coefficient = sum(max(n - 1, 0) * weight for n, weight in enumerate(count_weights))
            assert coefficient == k * s - 1 + (1 - s)**k
            flag_information = Fraction(k) / (s * (1 - s))
            block_information = k * (1 / p + 1 / (1 - s))
            assert flag_information / block_information == q / (1 - eta)
            assert flag_information + q_derivative**2 * count_mean / (q * (1 - q)) == block_information
            cases += 1
    return cases


def crossover(mean: float) -> float:
    if mean == 0:
        return 0.0
    if math.isinf(mean):
        return 1.0
    return 1 + math.expm1(-mean) / mean


def poisson_coefficient(mean: float) -> float:
    weight = math.exp(-mean)
    terms = []
    for n in range(1, math.ceil(mean + 14 * math.sqrt(mean) + 30)):
        weight *= mean / n
        terms.append((n - 1) * weight)
    return math.fsum(terms) / mean


def check_crossover_examples() -> list[dict]:
    table = []
    for mean in (0.01, 0.25, 1.0, 4.0, 100.0):
        target = crossover(mean)
        assert math.isclose(target, poisson_coefficient(mean), abs_tol=2e-13, rel_tol=0)
        for k in (1_000, 10_000):
            eta = mean / k
            p = eta / k**2
            probability, derivative = three_row_probability(k, eta, p)
            block_information = k * (1 / p + 1 / (1 - eta - p))
            efficiency = derivative**2 / (probability * (1 - probability) * block_information)
            assert abs(efficiency - target) < 3 / k, (mean, k, efficiency, target)
            table.append({
                "copies": k,
                "k_eta": mean,
                "p_over_eta": p / eta,
                "binary_fisher_fraction": efficiency,
                "limiting_fraction": target,
            })
    assert crossover(0) == 0 < table[0]["binary_fisher_fraction"] < 0.006
    assert 0.985 < table[-1]["binary_fisher_fraction"] < crossover(math.inf) == 1
    return table


def main() -> None:
    print(json.dumps({
        "status": "pass",
        "exact_word_cases": check_word_probabilities(),
        "weak_qubit_cases": check_weak_qubit_coefficients(),
        "exact_flag_cases": check_flag_decomposition(),
        "crossover_examples": check_crossover_examples(),
    }, indent=2))


if __name__ == "__main__":
    main()
