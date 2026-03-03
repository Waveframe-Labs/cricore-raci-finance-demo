---
title: "CRI-CORE RACI Finance Demo — Executable Accountability in an Agentic Environment"
filetype: "documentation"
type: "non-normative"
domain: "case-study"
version: "0.3.4"
doi: "TBD-0.3.4"
status: "Active"
created: "2026-02-27"
updated: "2026-03-03"

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
  - "cricore>=0.6.0"  

anchors:
  - "CRI-CORE-RACI-Finance-Demo-v0.3.4"
---

# CRI-CORE RACI Finance Demo

**Deterministic Commit Gating in an Agentic Finance Workflow**

This repository demonstrates how **CRI-CORE** enforces structural responsibility
at the mutation boundary in an AI-assisted finance workflow.

The focus is not policy semantics or lifecycle orchestration.

The focus is this:

> A governed state mutation may only occur if structural responsibility
> constraints pass deterministic validation.

---

## Business Scenario

An AI system proposes a budget reallocation between cost centers.

Declared roles:

- **Proposer** — AI system generating the recommendation  
- **Responsible** — Finance Manager validating feasibility  
- **Accountable** — CFO authorizing financial impact  
- **Consulted** — Compliance review  

CRI-CORE enforces:

- Required roles must be declared
- Each required role must be satisfied
- No identity may satisfy multiple required roles
- Structural independence is mechanically validated
- Commit authorization is atomic and centralized

If structural validation fails:

    commit_allowed = False

---

## What This Demonstrates

This is **not**:

- Lifecycle governance
- AI ethics policy
- Semantic evaluation
- Financial correctness validation

This is deterministic structural enforcement.

The kernel:

- Validates separation of duties
- Enforces contract version compliance
- Materializes cryptographic integrity artifacts
- Seals the run state
- Gates commit authorization

The kernel does not interpret intent.

It enforces structure.

---

## Scenarios Included

### 1. Valid Separation of Duties

Distinct Responsible and Accountable identities.

Result:

    commit_allowed = True

### 2. Reused Identity (Violation)

The same identity attempts to satisfy both:

- Responsible
- Accountable

Result:

    commit_allowed = False

The violation is structural, not semantic.

---

## Installation

This demo depends on the public **CRI-CORE** enforcement kernel.

Install the dependency:

    pip install cricore>=0.6.0

Clone this repository and run the demo from the project root.

---

## How to Run

Run the valid scenario:

    python runner/run_demo.py valid

Run the violation scenario:

    python runner/run_demo.py violation

Each run:

- Materializes a local run directory under `outputs/runs/`
- Generates:
  - `claim.json`
  - `contract.json`
  - `binding.json`
  - `payload.tar.gz`
  - `SHA256SUMS.txt`
  - `SEAL.json`
- Executes the full CRI-CORE enforcement pipeline
- Prints replay instructions for independent verification

---

## Replayability

Every run prints instructions to independently recompute enforcement:

    run_enforcement_pipeline('.', expected_contract_version='0.3.0')

No runner logic is required to verify the decision.

This demonstrates deterministic, replayable enforcement.

---

## Architectural Positioning

This demo frames CRI-CORE as:

> Executable separation-of-duties enforcement for agentic systems.

Instead of asking:

"Who owns this decision?"

We ask:

"Can this mutation occur unless ownership is structurally validated?"

That is the mutation boundary.

---

## Intended Audience

- Enterprise Governance Leaders  
- Finance Transformation Teams  
- AI Risk & Compliance Officers  
- Separation-of-Duties Architects  
- Agentic Orchestration Designers  

---

## License

Apache 2.0

---

<div align="center">
  <sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity • Governed under the Aurora Research Initiative (ARI)</sub>
</div>
