---
{
  "projection_kind": "taulib_declaration",
  "title": "WindingTransitionMatrix",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/winding-transition-matrix/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::WindingTransitionMatrix",
  "declaration_slug": "winding-transition-matrix",
  "kind": "structure",
  "name": "WindingTransitionMatrix",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2626,
  "source_line_end": 2637,
  "registry_ids": [
    "IV.D378"
  ],
  "related_registry_items": [
    {
      "id": "IV.D378",
      "title": "Winding Transition Matrix on T² Primitive Modes",
      "url": "/registry/object/IV.D378/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2626-L2637",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2626-L2637",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2626-L2637)
- Source range: L2626-L2637
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D378` — Winding Transition Matrix on T² Primitive Modes

## Immediate Comment / Docstring

```lean
/-- [IV.D378] Winding transition matrix on T² primitive modes.
    3×3 symmetric matrix: diagonal = eigenvalues, off-diagonal = κ(C;n). -/
```

## Source Excerpt

```lean
structure WindingTransitionMatrix where
  /-- Matrix dimension. -/
  dim : Nat := 3
  /-- Trace contribution from eigenvalues (×1000). -/
  trace_eigenvalues_x1000 : Nat := 19170
  /-- κ(C;1) appears 4 times off-diagonal. -/
  kC1_count : Nat := 4
  /-- κ(C;2) appears 2 times off-diagonal. -/
  kC2_count : Nat := 2
  /-- Matrix is symmetric. -/
  symmetric : Bool := true
  deriving Repr
```
