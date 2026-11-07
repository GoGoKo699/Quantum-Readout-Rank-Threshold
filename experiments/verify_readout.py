"""Reproduce finite checks for the universal two-copy readout proof.

Requires Python 3 and NumPy. Run from any working directory. The JSON output is
written next to this script under results/readout.json.

Executed scopes:
* direct tensor derivatives and the analytical FI certificate for rank-two
  states in dimensions 2, 3, 4, and 7;
* all first three moments of the 60-state two-qubit stabilizer design;
* actual finite-design FI for the complete pair measurement on qubit inputs;
* actual finite-design FI for pure-state tangents in dimension four.

This is a numerical diagnostic of the proof, not a proof by sampling. It does
not evaluate the full measurement FI for higher-dimensional input states,
enumerate larger Clifford groups, or test noisy implementations or estimators.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np


SEED = 20261107
RNG = np.random.default_rng(SEED)
TENSOR_TOL = 1e-8
DESIGN_TOL = 1e-12
BOUND_TOL = 1e-10
ZERO_PROB_TOL = 1e-14


def random_unitary(d: int) -> np.ndarray:
    z = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    phases = phases / np.abs(phases)
    return q @ np.diag(phases)


def swap_projectors(d: int) -> tuple[np.ndarray, np.ndarray]:
    swap = np.zeros((d * d, d * d), dtype=complex)
    for i, j in itertools.product(range(d), repeat=2):
        swap[j * d + i, i * d + j] = 1
    identity = np.eye(d * d)
    return (identity + swap) / 2, (identity - swap) / 2


def wedge(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    return (np.kron(u, v) - np.kron(v, u)) / np.sqrt(2)


def projector(v: np.ndarray) -> np.ndarray:
    return np.outer(v, v.conj())


def hs_squared(a: np.ndarray) -> float:
    return float(np.vdot(a, a).real)


def relative_error(actual: float, expected: float) -> float:
    return abs(actual - expected) / max(1.0, abs(expected))


def sld_qfi(rho: np.ndarray, tangent: np.ndarray) -> float:
    eigenvalues, eigenvectors = np.linalg.eigh(rho)
    tangent_eigenbasis = eigenvectors.conj().T @ tangent @ eigenvectors
    denominators = eigenvalues[:, None] + eigenvalues[None, :]
    # The tested positive eigenvalues are at least 1e-6. This cutoff only
    # removes floating-point approximations to the exact kernel.
    active = denominators > 1e-11
    return float(2 * np.sum(np.abs(tangent_eigenbasis[active]) ** 2 / denominators[active]))


def tangent_examples(d: int) -> dict[str, np.ndarray]:
    radial = np.zeros((d, d), dtype=complex)
    radial[0, 0], radial[1, 1] = 1, -1
    internal = np.zeros_like(radial)
    internal[0, 1] = 0.6 + 0.8j
    internal[1, 0] = internal[0, 1].conjugate()
    result = {"radial": radial, "internal": internal}
    if d > 2:
        for i in (0, 1):
            external = np.zeros_like(radial)
            external[i, 2] = 0.6 + 0.8j
            external[2, i] = external[i, 2].conjugate()
            result[f"external_{i + 1}"] = external
    mixed = RNG.normal() * radial
    mixed[0, 1] = RNG.normal() + 1j * RNG.normal()
    mixed[1, 0] = mixed[0, 1].conjugate()
    if d > 2:
        mixed[:2, 2:] = RNG.normal(size=(2, d - 2)) + 1j * RNG.normal(size=(2, d - 2))
        mixed[2:, :2] = mixed[:2, 2:].conj().T
    result["mixed"] = mixed
    return result


def tensor_checks() -> dict:
    maximum_errors = {
        "branch_probability_absolute": 0.0,
        "branch_derivative_absolute": 0.0,
        "antisymmetric_state_relative": 0.0,
        "antisymmetric_derivative_relative": 0.0,
        "nonzero_wedge_qfi_relative": 0.0,
        "symmetric_hs_relative": 0.0,
        "single_copy_qfi_relative": 0.0,
        "certificate_relative": 0.0,
    }
    cases = 0
    nonzero_wedge_cases = 0
    minimum_fraction = math.inf
    worst_case = None
    for d in (2, 3, 4, 7):
        p_plus, p_minus = swap_projectors(d)
        for lambda2 in (0.5, 0.2, 0.01, 1e-6):
            lambda1 = 1 - lambda2
            q, s = lambda1 * lambda2, 1 - lambda1 * lambda2
            u = random_unitary(d)
            rho = u @ np.diag([lambda1, lambda2] + [0] * (d - 2)) @ u.conj().T
            sigma_plus = p_plus @ np.kron(rho, rho) @ p_plus
            sigma_minus = p_minus @ np.kron(rho, rho) @ p_minus
            w = wedge(u[:, 0], u[:, 1])
            w_projector = projector(w)
            for name, a0 in tangent_examples(d).items():
                a = u @ a0 @ u.conj().T
                pair_derivative = np.kron(a, rho) + np.kron(rho, a)
                derivative_plus = p_plus @ pair_derivative @ p_plus
                derivative_minus = p_minus @ pair_derivative @ p_minus
                radial = float(a0[0, 0].real)
                internal = float(abs(a0[0, 1]) ** 2)
                external1 = float(np.sum(np.abs(a0[0, 2:]) ** 2))
                external2 = float(np.sum(np.abs(a0[1, 2:]) ** 2))
                q_prime = (lambda2 - lambda1) * radial
                j_single = radial**2 / q + 4 * internal + 4 * external1 / lambda1 + 4 * external2 / lambda2
                expected_wedge_qfi = 4 * (external1 / lambda1**2 + external2 / lambda2**2)

                v1 = u[:, 2:] @ a0[2:, 0] / lambda1
                v2 = u[:, 2:] @ a0[2:, 1] / lambda2
                w_prime = wedge(v1, u[:, 1]) + wedge(u[:, 0], v2)
                w_derivative = np.outer(w_prime, w.conj()) + np.outer(w, w_prime.conj())
                expected_minus_derivative = q_prime * w_projector + q * w_derivative

                y = derivative_plus / s + q_prime * sigma_plus / s**2
                direct_hs = hs_squared(y)
                expected_hs = (
                    2 * radial**2
                    + 4 * (1 - 2 * q) * internal
                    + (4 * lambda1**2 + 2 * lambda2**2) * external1
                    + (4 * lambda2**2 + 2 * lambda1**2) * external2
                ) / s**2

                if expected_wedge_qfi > 0:
                    normalized_minus = sigma_minus / q
                    direct_w_derivative = derivative_minus / q - (q_prime / q) * normalized_minus
                    direct_wedge_qfi = 2 * hs_squared(direct_w_derivative)
                    nonzero_wedge_cases += 1
                    maximum_errors["nonzero_wedge_qfi_relative"] = max(
                        maximum_errors["nonzero_wedge_qfi_relative"],
                        relative_error(direct_wedge_qfi, expected_wedge_qfi),
                    )
                else:
                    # An exactly zero wedge tangent is checked by the raw
                    # derivative identity below, before division by small q.
                    direct_wedge_qfi = 0.0

                direct_certificate = q_prime**2 / (q * s) + s * direct_hs / 3 + q * direct_wedge_qfi / 4
                expected_certificate = q_prime**2 / (q * s) + s * expected_hs / 3 + q * expected_wedge_qfi / 4
                errors = {
                    "branch_probability_absolute": abs(float(np.trace(sigma_minus).real) - q),
                    "branch_derivative_absolute": abs(float(np.trace(derivative_minus).real) - q_prime),
                    "antisymmetric_state_relative": float(np.linalg.norm(sigma_minus - q * w_projector)) / q,
                    "antisymmetric_derivative_relative": float(np.linalg.norm(derivative_minus - expected_minus_derivative)) / max(1.0, float(np.linalg.norm(expected_minus_derivative))),
                    "symmetric_hs_relative": relative_error(direct_hs, expected_hs),
                    "single_copy_qfi_relative": relative_error(sld_qfi(rho, a), j_single),
                    "certificate_relative": relative_error(direct_certificate, expected_certificate),
                }
                for key, value in errors.items():
                    maximum_errors[key] = max(maximum_errors[key], value)
                fraction = direct_certificate / (2 * j_single)
                if fraction < minimum_fraction:
                    minimum_fraction = fraction
                    worst_case = {"dimension": d, "lambda2": lambda2, "tangent": name}
                if fraction < 1 / 12 - BOUND_TOL:
                    raise AssertionError(f"Tensor certificate failed: d={d}, lambda2={lambda2}, {name}")
                cases += 1
    if max(maximum_errors.values()) > TENSOR_TOL:
        raise AssertionError(f"Tensor identity residual exceeded tolerance: {maximum_errors}")
    return {
        "cases": cases,
        "nonzero_wedge_qfi_cases": nonzero_wedge_cases,
        "input_dimensions": [2, 3, 4, 7],
        "smaller_eigenvalues": [0.5, 0.2, 0.01, 1e-6],
        "maximum_errors": maximum_errors,
        "minimum_certified_pair_qfi_fraction": minimum_fraction,
        "required_fraction": 1 / 12,
        "minimum_case": worst_case,
        "zero_wedge_note": "Exactly zero wedge tangents are checked through the unnormalized derivative identity before division by the branch probability.",
    }


def two_qubit_stabilizer_projectors() -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    paulis = [np.kron(a, b) for a, b in itertools.product((identity, x, y, z), repeat=2)][1:]
    i4 = np.eye(4, dtype=complex)
    unique = {}
    for a, b in itertools.combinations(paulis, 2):
        if np.linalg.norm(a @ b - b @ a) > DESIGN_TOL:
            continue
        for sign_a, sign_b in itertools.product((-1, 1), repeat=2):
            p = (i4 + sign_a * a) @ (i4 + sign_b * b) / 4
            if abs(np.trace(p) - 1) > DESIGN_TOL or np.linalg.norm(p @ p - p) > DESIGN_TOL:
                raise AssertionError("Invalid stabilizer projector")
            key = tuple(np.round(np.stack((p.real, p.imag)), 12).ravel())
            unique[key] = p
    projectors = np.stack(list(unique.values()))
    if len(projectors) != 60:
        raise AssertionError(f"Expected 60 stabilizer states, found {len(projectors)}")
    return projectors


def tensor_power(a: np.ndarray, order: int) -> np.ndarray:
    result = np.ones((1, 1), dtype=complex)
    for _ in range(order):
        result = np.kron(result, a)
    return result


def haar_projector_moment(d: int, order: int) -> np.ndarray:
    tuples = list(itertools.product(range(d), repeat=order))
    index = {value: i for i, value in enumerate(tuples)}
    symmetric_projector = np.zeros((d**order, d**order), dtype=complex)
    for permutation in itertools.permutations(range(order)):
        for column, value in enumerate(tuples):
            row = index[tuple(value[i] for i in permutation)]
            symmetric_projector[row, column] += 1 / math.factorial(order)
    return symmetric_projector / math.comb(d + order - 1, order)


def design_moment_checks(projectors: np.ndarray) -> dict:
    residuals = {}
    for order in (1, 2, 3):
        actual = sum(tensor_power(p, order) for p in projectors) / len(projectors)
        expected = haar_projector_moment(4, order)
        residuals[str(order)] = float(np.linalg.norm(actual - expected))
    if max(residuals.values()) > DESIGN_TOL:
        raise AssertionError(f"Design moments failed: {residuals}")
    return {"dimension": 4, "projectors": len(projectors), "moment_frobenius_residuals": residuals}


def finite_design_fi(projectors: np.ndarray, sigma: np.ndarray, derivative: np.ndarray) -> tuple[float, int]:
    # sigma can be subnormalized, so summing this over the two branches
    # includes the flag information automatically.
    probabilities = np.einsum("aij,ji->a", projectors, sigma).real
    derivatives = np.einsum("aij,ji->a", projectors, derivative).real
    if float(np.min(probabilities)) < -DESIGN_TOL:
        raise AssertionError("Negative outcome probability")
    active = probabilities > ZERO_PROB_TOL
    if np.any(np.abs(derivatives[~active]) > 2e-10):
        raise AssertionError("A discarded zero-probability outcome has a nonzero derivative")
    value = sigma.shape[0] / len(projectors) * np.sum(derivatives[active] ** 2 / probabilities[active])
    return float(value), int(np.sum(~active))


def finite_pair_checks(projectors: np.ndarray) -> dict:
    p_plus, p_minus = swap_projectors(2)
    rank_two_fractions = []
    pure_fractions = []
    zero_outcomes = 0
    for lambda2 in (0.5, 0.2, 0.01, 1e-6, 0.0):
        for u in (np.eye(2, dtype=complex), random_unitary(2)):
            rho = u @ np.diag([1 - lambda2, lambda2]) @ u.conj().T
            examples = tangent_examples(2)
            if lambda2 == 0:
                examples = {"internal": examples["internal"]}
            for a0 in examples.values():
                a = u @ a0 @ u.conj().T
                pair = np.kron(rho, rho)
                derivative = np.kron(a, rho) + np.kron(rho, a)
                information = 0.0
                for p in (p_plus, p_minus):
                    value, zeros = finite_design_fi(projectors, p @ pair @ p, p @ derivative @ p)
                    information += value
                    zero_outcomes += zeros
                fraction = information / (2 * sld_qfi(rho, a))
                if lambda2 == 0:
                    pure_fractions.append(fraction)
                    required = 1 / 4
                else:
                    rank_two_fractions.append(fraction)
                    required = 1 / 12
                if fraction < required - BOUND_TOL:
                    raise AssertionError(f"Finite pair FI failed: lambda2={lambda2}, fraction={fraction}")
    return {
        "input_dimension": 2,
        "pair_design_dimension": 4,
        "rank_two_cases": len(rank_two_fractions),
        "pure_tangent_cases": len(pure_fractions),
        "minimum_rank_two_pair_qfi_fraction": min(rank_two_fractions),
        "required_rank_two_fraction": 1 / 12,
        "minimum_pure_pair_qfi_fraction": min(pure_fractions),
        "required_pure_fraction": 1 / 4,
        "zero_probability_outcomes_checked": zero_outcomes,
    }


def finite_pure_design_checks(projectors: np.ndarray) -> dict:
    fractions = []
    for case in range(8):
        if case < 2:
            phi = np.array([1, 0, 0, 0], dtype=complex)
            v = np.array([0, 1, 0, 0], dtype=complex) if case == 0 else np.array([0, 1, 1j, 0], dtype=complex) / np.sqrt(2)
        else:
            u = random_unitary(4)
            phi, v = u[:, 0], u[:, 1]
        sigma = projector(phi)
        derivative = np.outer(v, phi.conj()) + np.outer(phi, v.conj())
        information, _ = finite_design_fi(projectors, sigma, derivative)
        fraction = information / (4 * float(np.vdot(v, v).real))
        if fraction < 1 / 4 - BOUND_TOL:
            raise AssertionError(f"Pure design FI failed: {fraction}")
        fractions.append(fraction)
    return {"dimension": 4, "cases": len(fractions), "minimum_qfi_fraction": min(fractions), "required_fraction": 1 / 4}


def main() -> None:
    tensor = tensor_checks()
    projectors = two_qubit_stabilizer_projectors()
    moments = design_moment_checks(projectors)
    pairs = finite_pair_checks(projectors)
    pure = finite_pure_design_checks(projectors)
    result = {
        "status": "pass",
        "seed": SEED,
        "numpy_version": np.__version__,
        "scope": "Direct tensor checks in dimensions 2,3,4,7; exact-design moments and actual finite-design FI in dimension four, including complete pair readout for qubit inputs.",
        "limitations": "No full finite-design pair-FI calculation for input dimension greater than two, no numerical proof of the universal theorem, no large Clifford-group enumeration, and no noise or estimator tests.",
        "tolerances": {"tensor_identity": TENSOR_TOL, "design_moment": DESIGN_TOL, "bound": BOUND_TOL, "zero_probability": ZERO_PROB_TOL},
        "tensor_checks": tensor,
        "finite_design_moments": moments,
        "finite_pair_fi": pairs,
        "finite_pure_design_fi": pure,
    }
    destination = Path(__file__).resolve().parent / "results" / "readout.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
