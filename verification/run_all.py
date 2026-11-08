"""Run the repository's scientific reproduction checks."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    for relative in ("experiments/verify_readout.py", "experiments/check_schur.py", "verification/verify_haar_pair.py"):
        result = subprocess.run(
            [sys.executable, str(ROOT / relative)],
            cwd=ROOT, capture_output=True, text=True,
        )
        if result.returncode:
            sys.stdout.write(result.stdout)
            sys.stderr.write(result.stderr)
            raise SystemExit(result.returncode)
        print(f"PASS: {relative}")
    readout = json.loads((ROOT / "experiments/results/readout.json").read_text())
    schur = json.loads((ROOT / "experiments/results/schur.json").read_text())
    haar = json.loads((ROOT / "experiments/results/haar_pair.json").read_text())
    print(json.dumps({
        "haar_status": haar["status"],
        "haar_integral_cases": len(haar["cases"]),
        "readout_status": readout["status"],
        "tensor_checks": readout["tensor_checks"],
        "finite_design_moments": readout["finite_design_moments"],
        "finite_pair_fi": readout["finite_pair_fi"],
        "exact_schur_cases": schur["schur_case_count"],
        "exact_character_projector_cases": schur["projector_case_count"],
        "schur_all_passed": schur["all_passed"],
    }, indent=2))


if __name__ == "__main__":
    main()
