---
{
  "projection_kind": "taulib_declaration",
  "title": "WindowUniversalityNNLO",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/window-universality-nnlo-l1004/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::WindowUniversalityNNLO",
  "declaration_slug": "window-universality-nnlo-l1004",
  "kind": "structure",
  "name": "WindowUniversalityNNLO",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1004,
  "source_line_end": 1011,
  "registry_ids": [
    "IV.P191"
  ],
  "related_registry_items": [
    {
      "id": "IV.P191",
      "title": "Window RG Period: W₃(4)^k Governs k-th Perturbative Order",
      "url": "/registry/object/IV.P191/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1004-L1011",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1004-L1011",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1004-L1011)
- Source range: L1004-L1011
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P191` — Window RG Period: W₃(4)^k Governs k-th Perturbative Order

## Immediate Comment / Docstring

```lean
/-- [IV.P191] Window universality NNLO structure. -/
```

## Source Excerpt

```lean
structure WindowUniversalityNNLO where
  /-- NLO window: W₃(4) = 5. -/
  nlo_window : Nat := 5
  /-- NNLO window: W₃(4)² = 25. -/
  nnlo_window : Nat := 25
  /-- Cross-check: 4·W₃(4)+1 = 21 (p-n bonus). -/
  cross_check : Nat := 21
  deriving Repr
```
