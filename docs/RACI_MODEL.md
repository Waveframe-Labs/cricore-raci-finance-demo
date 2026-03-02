---
title: "CRI-CORE RACI Finance Demo — RACI Structural Model"
filetype: "documentation"
type: "normative"
domain: "case-study"
version: "0.1.0"
doi: "TBD-0.1.0"
status: "Active"
created: "2026-03-01"
updated: "2026-03-01"

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

dependencies: []

anchors:
  - "CRI-CORE-RACIModel-v0.1.0"
---

# RACI Structural Enforcement Model

This document defines how traditional **RACI (Responsible, Accountable, Consulted, Informed)** 
is operationalized structurally within the CRI-CORE enforcement kernel.

The objective is not to redefine RACI conceptually, but to convert it into 
an enforceable structural contract surface.

---

## 1. Traditional RACI Assumptions

Traditional RACI frameworks assume:

- Linear workflow
- Static human roles
- Manual approval checkpoints
- Clear and stable ownership boundaries

In an agentic environment, these assumptions degrade because:

- Proposals may originate from AI systems
- Work is continuous rather than checkpoint-based
- Roles may be dynamically assigned
- Responsibility may blur across human and system actors

This demo translates RACI into a structural enforcement model.

---

## 2. Structural RACI Mapping

In this demo, RACI roles are expressed as structural identities within the 
`run_context.identities` surface expected by CRI-CORE.

Example mapping:

{
  "identities": {
    "required_roles": [
      "Responsible",
      "Accountable"
    ],
    "actors": [
      { "id": "ai-agent-001", "type": "service", "role": "Responsible" },
      { "id": "finance-manager-017", "type": "human", "role": "Accountable" }
    ]
  }
}

### Enforcement Rules

When `required_roles` are declared:

1. Each required role must be satisfied by exactly one actor.
2. A single identity may not satisfy multiple required roles.
3. Structural equality (id, type) defines identity.
4. No semantic interpretation of authority is performed.
5. CRI-CORE does not validate business meaning — only structural conformance.

---

## 3. What This Achieves

This converts RACI from documentation into enforcement:

- AI cannot self-approve if Accountable role is required.
- Budget mutation cannot occur unless Accountable role is structurally present.
- Separation-of-duties violations are mechanically rejected.
- Governance becomes executable.

---

## 4. Non-Goals

This demo does not:

- Define HR authority policies
- Validate budget thresholds
- Interpret financial compliance regulations
- Replace enterprise governance systems

It only enforces structural admissibility at the mutation boundary.

---

## 5. Why This Matters

RACI traditionally describes responsibility.

CRI-CORE enforces responsibility before state mutation occurs.

This demonstrates how agentic systems can operate inside 
enterprise governance boundaries without dissolving accountability.
