---
{
  "projection_kind": "taulib_declaration",
  "title": "NormalOrdering",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/normal-ordering/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::NormalOrdering",
  "declaration_slug": "normal-ordering",
  "kind": "structure",
  "name": "NormalOrdering",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 390,
  "source_line_end": 397,
  "registry_ids": [
    "IV.R117"
  ],
  "related_registry_items": [
    {
      "id": "IV.R117",
      "title": "Normal ordering predicted",
      "url": "/registry/object/IV.R117/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L390-L397",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L390-L397",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L390-L397)
- Source range: L390-L397
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R117` — Normal ordering predicted

## Immediate Comment / Docstring

```lean
/-- [IV.R117] The tau-framework predicts normal neutrino mass ordering:
    lightest = Gen 1 (crossing-point), heaviest = Gen 3 (full-lemniscate).
    Testable by JUNO, DUNE, Hyper-Kamiokande. -/
```

## Source Excerpt

```lean
structure NormalOrdering where
  /-- Predicted ordering. -/
  ordering : String := "normal"
  /-- Testable. -/
  testable : Bool := true
  /-- Scope. -/
  scope : String := "tau-effective"
  deriving Repr
```
