---
{
  "projection_kind": "taulib_declaration",
  "title": "NNLOCrossCheck",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/nnlocross-check/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::NNLOCrossCheck",
  "declaration_slug": "nnlocross-check",
  "kind": "structure",
  "name": "NNLOCrossCheck",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1056,
  "source_line_end": 1063,
  "registry_ids": [
    "IV.R401"
  ],
  "related_registry_items": [
    {
      "id": "IV.R401",
      "title": "Cross-Check: 1/21 in p-n Mass Difference = 1/(4·W₃(4)+1); n=7 Higgs at +8 ppm",
      "url": "/registry/object/IV.R401/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1056-L1063",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1056-L1063",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1056-L1063)
- Source range: L1056-L1063
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R401` — Cross-Check: 1/21 in p-n Mass Difference = 1/(4·W₃(4)+1); n=7 Higgs at +8 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.R401] NNLO cross-check structure (formalized). -/
```

## Source Excerpt

```lean
structure NNLOCrossCheck where
  /-- p-n mass coefficient: 4·W₃(4)+1 = 21. -/
  pn_coefficient : Nat := 21
  /-- Higgs structural exponent n. -/
  higgs_n : Nat := 7
  /-- Number of Window-universal cross-checks. -/
  n_cross_checks : Nat := 3
  deriving Repr
```
