---
{
  "projection_kind": "taulib_declaration",
  "title": "OQCKM1Sprint6B",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/oqckm1-sprint6-b/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::OQCKM1Sprint6B",
  "declaration_slug": "oqckm1-sprint6-b",
  "kind": "structure",
  "name": "OQCKM1Sprint6B",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1518,
  "source_line_end": 1523,
  "registry_ids": [
    "IV.R409"
  ],
  "related_registry_items": [
    {
      "id": "IV.R409",
      "title": "OQ-CKM1 Status after Sprint 6B: All Four Wolfenstein τ-Effective",
      "url": "/registry/object/IV.R409/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1518-L1523",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1518-L1523",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1518-L1523)
- Source range: L1518-L1523
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R409` — OQ-CKM1 Status after Sprint 6B: All Four Wolfenstein τ-Effective

## Immediate Comment / Docstring

```lean
/-- [IV.R409] OQ-CKM1 status after Sprint 6B structure (formalized). -/
```

## Source Excerpt

```lean
structure OQCKM1Sprint6B where
  /-- Number of τ-effective Wolfenstein parameters (all 4). -/
  n_tau_effective : Nat := 4
  /-- Number of open exponent derivations. -/
  n_open_derivations : Nat := 1
  deriving Repr
```
