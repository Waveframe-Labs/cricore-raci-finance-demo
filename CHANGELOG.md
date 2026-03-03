---
title: "CRI-CORE RACI Finance Demo Changelog"
filetype: "documentation"
type: "release-history"
domain: "case-study"
version: "0.3.4"
doi: "TBD-0.3.4"
status: "Active"
created: "2026-03-03"
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
  - "RACI-DEMO-CHANGELOG-v0.3.4"
---

# Changelog

All notable changes to the **CRI-CORE RACI Finance Demo** are documented here.

This project follows **semantic versioning (0.x pre-stable)**.

---

## [0.3.4] – 2026-03-03

### Added

- `CHANGELOG.md` for explicit release history tracking
- `CITATION.cff` enabling GitHub citation metadata

### Documentation

- Clarified repository citation metadata for research and governance use

---

## [0.3.3] – 2026-03-03

### Added

- Initial public release of the **CRI-CORE RACI Finance Demo**

### Demonstration Scope

- Deterministic commit gating in a financial RACI responsibility model
- Structural enforcement of separation-of-duties constraints
- Example scenarios demonstrating:

  - valid responsibility separation (`commit_allowed = True`)
  - structural role violation (`commit_allowed = False`)

### Dependencies

- Requires **CRI-CORE ≥ 0.6.0** from PyPI