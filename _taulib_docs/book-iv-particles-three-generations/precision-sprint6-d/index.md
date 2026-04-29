---
{
  "projection_kind": "taulib_declaration",
  "title": "PrecisionSprint6D",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/precision-sprint6-d/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::PrecisionSprint6D",
  "declaration_slug": "precision-sprint6-d",
  "kind": "structure",
  "name": "PrecisionSprint6D",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1596,
  "source_line_end": 1603,
  "registry_ids": [
    "IV.R410"
  ],
  "related_registry_items": [
    {
      "id": "IV.R410",
      "title": "m_μ NNLO + p-n NLO Precision Status after Sprint 6D",
      "url": "/registry/object/IV.R410/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1596-L1603",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1596-L1603",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1596-L1603)
- Source range: L1596-L1603
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R410` — m_μ NNLO + p-n NLO Precision Status after Sprint 6D

## Immediate Comment / Docstring

```lean
/-- [IV.R410] Precision status after Sprint 6D structure (formalized). -/
```

## Source Excerpt

```lean
structure PrecisionSprint6D where
  /-- m_μ/m_e best ppm. -/
  muon_ppm : Nat := 43
  /-- p-n mass best ppm. -/
  pn_ppm : Nat := 5
  /-- Number of Window–nucleon connections established. -/
  n_window_nucleon : Nat := 2
  deriving Repr
```
