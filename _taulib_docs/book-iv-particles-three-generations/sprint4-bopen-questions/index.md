---
{
  "projection_kind": "taulib_declaration",
  "title": "Sprint4BOpenQuestions",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/sprint4-bopen-questions/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::Sprint4BOpenQuestions",
  "declaration_slug": "sprint4-bopen-questions",
  "kind": "structure",
  "name": "Sprint4BOpenQuestions",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 925,
  "source_line_end": 934,
  "registry_ids": [
    "IV.R400"
  ],
  "related_registry_items": [
    {
      "id": "IV.R400",
      "title": "PMNS CP Phase δ_CP from σ-Breaking; New OQ-C6/C7",
      "url": "/registry/object/IV.R400/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L925-L934",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L925-L934",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L925-L934)
- Source range: L925-L934
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R400` — PMNS CP Phase δ_CP from σ-Breaking; New OQ-C6/C7

## Immediate Comment / Docstring

```lean
/-- [IV.R400] Sprint 4B open questions structure (formalized). -/
```

## Source Excerpt

```lean
structure Sprint4BOpenQuestions where
  /-- Number of open questions. -/
  n_questions : Nat := 3
  /-- OQ-C6 (ρ̄) deviation from PDG in ppm. -/
  oq_c6_rho_ppm : Nat := 975
  /-- OQ-C7 (PMNS) deviation from PDG in ppm. -/
  oq_c7_pmns_ppm : Nat := 18213
  /-- OQ-C5a (muon) deviation from PDG in ppm. -/
  oq_c5a_muon_ppm : Nat := 307
  deriving Repr
```
