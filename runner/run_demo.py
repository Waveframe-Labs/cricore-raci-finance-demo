"""
---
title: "CRI-CORE RACI Finance Demo Runner"
filetype: "operational"
type: "non-normative"
domain: "case-study"
version: "0.3.2"
doi: "TBD-0.3.2"
status: "Active"
created: "2026-03-02"
updated: "2026-03-02"

author:
  name: "Shawn C. Wright"
  email: "swright@waveframelabs.org"
  orcid: "https://orcid.org/0009-0006-6043-9295"

maintainer:
  name: "Waveframe Labs"
  url: "https://waveframelabs.org"

license: "Apache-2.0"

copyright:
  holder: "Waveframe Labs"
  year: "2026"

ai_assisted: "partial"

dependencies:
  - "../scenarios/budget_reallocation/policy.yaml"
  - "../scenarios/budget_reallocation/proposal.json"

anchors:
  - "CRI-CORE-RACI-Finance-Runner-v0.3.2"
---
"""

from __future__ import annotations

import json
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping

from cricore.enforcement.execution import run_enforcement_pipeline
from cricore.integrity.finalize import finalize_run_integrity


# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
SCENARIO_ROOT = ROOT / "scenarios" / "budget_reallocation"
OUTPUTS_ROOT = ROOT / "outputs" / "runs"

EXPECTED_CONTRACT_VERSION = "0.3.0"
RUN_CLAIM_FILENAME = "claim.json"


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _new_run_id(prefix: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    micros = datetime.now(timezone.utc).strftime("%f")
    return f"{prefix}-{stamp}-{micros}"


def _write_json(path: Path, obj: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _copy_if_exists(src: Path, dst: Path) -> None:
    if src.exists():
        shutil.copy2(src, dst)


def _print_stage_results(results: List[Any]) -> None:
    for r in results:
        stage_id = getattr(r, "stage_id", "<unknown>")
        passed = bool(getattr(r, "passed", False))
        print(f"{stage_id}: {'OK' if passed else 'FAILED'}")
        if not passed:
            for msg in getattr(r, "messages", []) or []:
                print(f"  - {msg}")


def _list_run_dir(run_root: Path) -> None:
    print(f"\nRun directory: {run_root}")
    print("Artifacts:")
    for p in sorted(run_root.rglob("*")):
        if p.is_dir():
            continue
        rel = p.relative_to(run_root)
        print(f"  - {rel.as_posix()}")


def _print_replay_footer(run_root: Path) -> None:
    print("\nReplay This Run Independently:")
    print(f"  cd {run_root}")
    print("  python -c \"from cricore.enforcement.execution import run_enforcement_pipeline; "
          "results, commit_allowed = run_enforcement_pipeline('.', expected_contract_version='0.3.0'); "
          "print(commit_allowed)\"")


# -----------------------------------------------------------------------------
# Run materialization
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class Actors:
    proposer_ai: Dict[str, str]
    finance_manager: Dict[str, str]
    cfo: Dict[str, str]
    compliance: Dict[str, str]


def _actors_valid() -> Actors:
    return Actors(
        proposer_ai={"id": "agent-budget-optimizer", "type": "service", "role": "proposer"},
        finance_manager={"id": "finance-mgr-001", "type": "human", "role": "responsible"},
        cfo={"id": "cfo-001", "type": "human", "role": "accountable"},
        compliance={"id": "compliance-001", "type": "human", "role": "consulted"},
    )


def _run_context_valid(actors: Actors) -> Dict[str, Any]:
    return {
        "identities": {
            "actors": [
                actors.proposer_ai,
                actors.finance_manager,
                actors.cfo,
                actors.compliance,
            ],
            "required_roles": ["responsible", "accountable"],
            "conflict_flags": {},
        },
        "integrity": {
            "workflow_execution_ref": "demo://raci-finance/budget-reallocation",
            "run_payload_ref": "demo://raci-finance/payload",
            "attestation_ref": "demo://raci-finance/attestation",
        },
        "publication": {
            "repository_ref": "repo://cricore-raci-finance-demo",
            "commit_ref": "local",
        },
    }


def _run_context_violation_reused_identity(actors: Actors) -> Dict[str, Any]:
    reused = {"id": "finance-mgr-001", "type": "human"}
    return {
        "identities": {
            "actors": [
                actors.proposer_ai,
                {"id": reused["id"], "type": reused["type"], "role": "responsible"},
                {"id": reused["id"], "type": reused["type"], "role": "accountable"},
                actors.compliance,
            ],
            "required_roles": ["responsible", "accountable"],
            "conflict_flags": {},
        },
        "integrity": {
            "workflow_execution_ref": "demo://raci-finance/budget-reallocation",
            "run_payload_ref": "demo://raci-finance/payload",
            "attestation_ref": "demo://raci-finance/attestation",
        },
        "publication": {
            "repository_ref": "repo://cricore-raci-finance-demo",
            "commit_ref": "local",
        },
    }


def _materialize_run(run_root: Path, *, run_id: str, run_context: Dict[str, Any]) -> None:
    run_root.mkdir(parents=True, exist_ok=True)
    (run_root / "validation").mkdir(parents=True, exist_ok=True)

    _write_json(
        run_root / RUN_CLAIM_FILENAME,
        {
            "claim_id": f"claim::{run_id}",
            "scenario": "budget_reallocation",
            "amount_usd": 18_400_000,
            "created_utc": _utc_now_iso(),
        },
    )

    _write_json(
        run_root / "contract.json",
        {
            "contract_version": EXPECTED_CONTRACT_VERSION,
            "run_id": run_id,
            "created_utc": _utc_now_iso(),
            "claim_ref": RUN_CLAIM_FILENAME,
        },
    )

    _copy_if_exists(SCENARIO_ROOT / "policy.yaml", run_root / "policy.yaml")
    _copy_if_exists(SCENARIO_ROOT / "proposal.json", run_root / "proposal.json")

    _write_json(run_root / "randomness.json", {"run_id": run_id, "deterministic": True})
    _write_json(run_root / "approval.json", {"run_id": run_id})
    _write_json(run_root / "validation" / "invariant_results.json", {"run_id": run_id})
    _write_text(run_root / "report.md", f"# Finance Demo Run\n\nrun_id: {run_id}\n")
    _write_json(run_root / "run_context.json", run_context)


# -----------------------------------------------------------------------------
# Execution
# -----------------------------------------------------------------------------

def _execute(label: str, run_context: Dict[str, Any]) -> None:
    run_id = _new_run_id(label)
    run_root = OUTPUTS_ROOT / run_id

    _materialize_run(run_root, run_id=run_id, run_context=run_context)
    finalize_run_integrity(run_root)

    results, commit_allowed = run_enforcement_pipeline(
        str(run_root),
        expected_contract_version=EXPECTED_CONTRACT_VERSION,
        run_context=run_context,
    )

    print(f"\n== {label} ==")
    _print_stage_results(results)

    if label.startswith("VIOLATION"):
        print("\nStructural Difference From VALID:")
        print("  - finance-mgr-001 assigned to both 'responsible' and 'accountable'")
        print("  - Violates required role independence constraint")

    print(f"\nCOMMIT: {'allowed' if commit_allowed else 'blocked'}")
    _list_run_dir(run_root)
    _print_replay_footer(run_root)


# -----------------------------------------------------------------------------
# CLI Entry
# -----------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage:")
        print("  python runner/run_demo.py valid")
        print("  python runner/run_demo.py violation")
        return

    OUTPUTS_ROOT.mkdir(parents=True, exist_ok=True)
    actors = _actors_valid()

    choice = sys.argv[1].strip().lower()

    if choice == "valid":
        _execute("VALID", _run_context_valid(actors))
    elif choice == "violation":
        _execute("VIOLATION-REUSED-IDENTITY", _run_context_violation_reused_identity(actors))
    else:
        print("Invalid option. Use 'valid' or 'violation'.")


if __name__ == "__main__":
    main()
    